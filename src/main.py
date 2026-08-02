"""Orchestrator: collect → filter → score → AI → render pipeline."""

import argparse
import os
import sys
import yaml
from datetime import datetime
from pathlib import Path

from src.collectors.base import EventRecord
from src.collectors.real_search import RealSearchCollector
from src.filters.dedup import Deduplicator
from src.filters.quality import QualityFilter
from src.filters.scorer import Scorer
from src.render.markdown_weekly import MarkdownRenderer

ROOT = Path(__file__).resolve().parent.parent


def load_config() -> dict:
    """Load all YAML config files and merge into one dict."""
    config: dict = {}
    for filename in ["sources.yml", "keywords.yml", "quality.yml"]:
        path = ROOT / "config" / filename
        if path.exists():
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
            config.update(data)
    return config


# ── Obsidian 插件生态 domain keyword → category mapping (12 categories) ──
OBSIDIAN_CATEGORY_KEYWORDS: dict[str, list[str]] = {
    "#core_plugin": [
        "Dataview", "Templater", "Tasks", "QuickAdd", "Omnisearch",
        "Calendar", "BRAT", "Linter", "core plugin", "plugin update",
        "插件更新", "Tasks plugin", "Dataview plugin", "Templater update",
    ],
    "#ai_plugin": [
        "Smart Connections", "Copilot", "Claudian", "Khoj", "Codian",
        "AI plugin", "AI agent", "RAG", "LLM", "embedding",
        "semantic search", "local model", "Ollama", "Text Generator",
        "AI 插件", "大模型", "本地模型", "Smart Composer",
    ],
    "#visual_tool": [
        "Excalidraw", "Kanban", "Min3D", "Mermaid", "Canvas",
        "mind map", "diagram", "flowchart", "graph view", "timeline",
        "白板", "看板", "思维导图", "画布", "Excalidraw plugin",
    ],
    "#pkm_workflow": [
        "Zettelkasten", "PARA", "Second Brain", "Breadcrumbs",
        "Note Refactor", "workflow", "PKM", "tagging", "frontmatter",
        "backlink", "双链", "知识管理", "笔记方法", "第二大脑",
        "Breadcrumbs plugin", "Periodic Notes",
    ],
    "#writing_tool": [
        "Pandoc", "Better Word Count", "cMenu", "Typewriter", "Outliner",
        "writing", "markdown editor", "editor", "export",
        "写作", "导出", "Markdown 编辑器", "Pandoc plugin",
    ],
    "#sync_backup": [
        "Remotely Save", "Obsidian Sync", "backup", "WebDAV",
        "encryption", "sync", "同步", "备份", "Remotely Save plugin",
        "Git plugin", "Obsidian Git",
    ],
    "#theme_ui": [
        "theme", "Style Settings", "CSS snippet", "AnuPpuccin",
        "Minimal theme", "UI", "主题", "界面", "Theme",
        "Style Settings plugin", "CSS 片段",
    ],
    "#security": [
        "malware", "RAT", "PHANTOMPULSE", "Remote Disable",
        "Safety Scorecard", "Access Disclosure", "security",
        "vulnerability", "malicious plugin", "安全", "漏洞", "恶意",
        "malicious", "security review",
    ],
    "#dev_api": [
        "MCP", "obsidian-skills", "mcp-obsidian", "obsidian-mcp-server",
        "Obsidian API", "plugin SDK", "Obsidian CLI", "developer",
        "TypeScript", "obsidian-releases", "manifest", "开发者",
        "Model Context Protocol", "MCP server", "plugin API",
    ],
    "#official_news": [
        "Obsidian Community", "Obsidian 1.12", "Obsidian 1.13", "Bases",
        "Obsidian Reader", "Web Clipper", "Roadmap", "Changelog",
        "官方", "official", "Obsidian update", "Obsidian release",
        "Obsidian changelog",
    ],
    "#chinese_community": [
        "Pkmer", "少数派", "汉化", "中文教程", "中文社区",
        "小红书", "什么值得买", "sspai", "中文插件", "Pkmer 周报",
        "中文",
    ],
    "#plugin_release": [
        "new plugin", "plugin release", "community plugin",
        "first release", "plugin list", "plugin spotlight", "release",
        "新插件", "插件推荐", "插件发布", "新版本",
    ],
}


def _auto_categorize(record: EventRecord, config: dict) -> list[str]:
    """Obsidian-domain keyword classification."""
    text = f"{record.title} {record.description}".lower()
    matched: list[str] = []
    for cat_id, keywords in OBSIDIAN_CATEGORY_KEYWORDS.items():
        if any(kw.lower() in text for kw in keywords):
            matched.append(cat_id)
    return matched[:3]  # max 3 categories per event


def _merge_records(records: list[EventRecord]) -> list[EventRecord]:
    """Merge records with same event_id, combining citation chains."""
    merged: dict[str, EventRecord] = {}
    for r in records:
        if r.event_id in merged:
            existing = merged[r.event_id]
            existing_keys = {c.source_key for c in existing.citations}
            for c in r.citations:
                if c.source_key not in existing_keys:
                    existing.citations.append(c)
            # Take the longer description
            if r.description and len(r.description) > len(existing.description or ""):
                existing.description = r.description
        else:
            merged[r.event_id] = r
    return list(merged.values())


def _generate_cn_titles(records: list[EventRecord]) -> None:
    """Generate Chinese titles for ALL event records via LLM batch translation.

    Strategy: LLM translates all events in batches (15 per call).
    Falls back to keyword pre-processing only if no LLM key is available.
    """
    import re

    # ── Preprocessing: longest-match-first keyword substitution ──
    # Sort DESCENDING by length so "Smart Connections" matches before "Connections"
    _PREPROCESS: list[tuple[str, str]] = sorted([
        # Multi-word plugin names FIRST (keep as proper nouns in CN context)
        ("Smart Connections", "Smart Connections"),
        ("Smart Composer", "Smart Composer"),
        ("Text Generator", "Text Generator"),
        ("Remotely Save", "Remotely Save"),
        ("Style Settings", "Style Settings"),
        ("Advanced Tables", "Advanced Tables"),
        ("Periodic Notes", "Periodic Notes"),
        ("Better Word Count", "Better Word Count"),
        ("Model Context Protocol", "MCP"),
        ("Obsidian Community", "Obsidian 社区"),
        ("Obsidian Reader", "Obsidian Reader"),
        ("Web Clipper", "Web Clipper"),
        ("community plugin", "社区插件"),
        ("new plugin", "新插件"),
        ("first release", "首次发布"),
        ("plugin release", "插件发布"),
        ("Obsidian Sync", "Obsidian 同步"),
        ("semantic search", "语义搜索"),
        ("local model", "本地模型"),
        ("local models", "本地模型"),
        ("security review", "安全审查"),
        ("Safety Scorecard", "安全评分卡"),
        ("Access Disclosure", "权限披露"),
        ("Remote Disable", "远程禁用"),
        ("Obsidian CLI", "Obsidian CLI"),
        ("plugin API", "插件 API"),
        ("plugin SDK", "插件 SDK"),
        ("obsidian-releases", "obsidian-releases"),
        ("obsidian-skills", "obsidian-skills"),
        ("obsidian-mcp-server", "obsidian-mcp-server"),
        ("mcp-obsidian", "mcp-obsidian"),
        ("Second Brain", "第二大脑"),
        ("artificial intelligence", "AI"),
        ("note-taking", "笔记"),
        ("data center", "数据中心"),
        # Single-word plugins / products (keep proper nouns)
        ("Dataview", "Dataview"), ("Templater", "Templater"),
        ("Excalidraw", "Excalidraw"), ("QuickAdd", "QuickAdd"),
        ("Omnisearch", "Omnisearch"), ("Claudian", "Claudian"),
        ("Khoj", "Khoj"), ("Codian", "Codian"),
        ("Breadcrumbs", "Breadcrumbs"), ("Outliner", "Outliner"),
        ("Zettelkasten", "卡片盒笔记法"),
        ("Obsidian", "Obsidian"), ("Notion", "Notion"),
        ("Dynalist", "Dynalist"), ("Logseq", "Logseq"),
        # Companies / platforms
        ("GitHub", "GitHub"), ("Reddit", "Reddit"),
        ("Discord", "Discord"), ("Product Hunt", "Product Hunt"),
        ("Pkmer", "Pkmer"), ("YouTube", "YouTube"),
        ("Google", "谷歌"), ("Microsoft", "微软"),
        ("OpenAI", "OpenAI"), ("Anthropic", "Anthropic"),
        ("Claude", "Claude"), ("ChatGPT", "ChatGPT"),
        ("Apple", "苹果"), ("Meta", "Meta"),
        # AI / technical terms
        ("MCP", "MCP"), ("RAG", "RAG"), ("LLM", "大模型"),
        ("AI agent", "AI Agent"), ("AI agents", "AI Agent"),
        ("AI plugin", "AI 插件"), ("AI plugins", "AI 插件"),
        ("embedding", "向量嵌入"), ("embeddings", "向量嵌入"),
        ("Ollama", "Ollama"), ("vault", "笔记库"),
        ("backlink", "反向链接"), ("backlinks", "反向链接"),
        ("frontmatter", "frontmatter"), ("TypeScript", "TypeScript"),
        ("changelog", "更新日志"), ("roadmap", "路线图"),
        ("milestone", "里程碑"), ("release", "发布"),
        ("released", "发布"), ("releases", "发布"),
        ("update", "更新"), ("updated", "更新"),
        ("updates", "更新"), ("announced", "宣布"),
        ("launched", "推出"), ("introduced", "推出"),
        ("published", "发布"),
        ("theme", "主题"), ("themes", "主题"),
        ("plugin", "插件"), ("plugins", "插件"),
        ("workflow", "工作流"), ("workspace", "工作区"),
        ("database", "数据库"), ("query", "查询"),
        ("sync", "同步"), ("backup", "备份"),
        ("encryption", "加密"), ("security", "安全"),
        ("vulnerability", "漏洞"), ("malware", "恶意软件"),
        ("malicious", "恶意"),
        ("downloads", "下载量"), ("download", "下载"),
        ("community", "社区"), ("official", "官方"),
        ("developer", "开发者"), ("developers", "开发者"),
        ("notes", "笔记"), ("note", "笔记"),
        # Geography / generic
        ("China", "中国"), ("Chinese", "中国"),
        ("U.S.", "美国"), ("United States", "美国"),
        ("Japan", "日本"), ("Korea", "韩国"),
        ("Europe", "欧洲"), ("European", "欧洲"),
        ("new", "新"), ("New", "新"),
        ("first", "首个"), ("First", "首个"),
        ("best", "最佳"), ("Best", "最佳"),
        ("largest", "最大"), ("Largest", "最大"),
        ("global", "全球"), ("Global", "全球"),
        ("world", "全球"), ("World", "全球"),
        ("AI", "AI"), ("API", "API"), ("SDK", "SDK"),
        ("CLI", "CLI"), ("iOS", "iOS"), ("Android", "Android"),
        ("web", "Web"), ("mobile", "移动端"),
        ("desktop", "桌面端"), ("Windows", "Windows"),
        ("macOS", "macOS"), ("Linux", "Linux"),
    ], key=lambda x: -len(x[0]))

    for r in records:
        en = r.title.strip()
        cn = en
        for term, cn_term in _PREPROCESS:
            idx = 0
            while True:
                idx = cn.find(term, idx)
                if idx == -1:
                    break
                before_ok = idx == 0 or not cn[idx - 1].isalnum() and cn[idx - 1] != "'"
                after_ok = (idx + len(term) == len(cn)
                            or not cn[idx + len(term)].isalnum() and cn[idx + len(term)] != "'")
                if before_ok and after_ok:
                    cn = cn[:idx] + cn_term + cn[idx + len(term):]
                    idx += len(cn_term)
                else:
                    idx += 1
        cn = re.sub(r'\s{2,}', ' ', cn).strip()
        r.title_cn = cn if cn != en else ""

    # ── LLM batch translation for ALL events ──
    try:
        from src.ai.llm_client import LLMClient
        client = LLMClient()
    except Exception:
        print("  [CN translate] No LLM key found — using keyword-only fallback")
        return

    BATCH_SIZE = 15  # smaller batches = fewer 429s
    id_to_cn: dict[str, str] = {}
    all_records = [r for r in records if r.title.strip()]

    for batch_start in range(0, len(all_records), BATCH_SIZE):
        batch = all_records[batch_start:batch_start + BATCH_SIZE]
        lines = [f"{j+1}. {r.title}" for j, r in enumerate(batch)]
        prompt = (
            "Translate these Obsidian plugin ecosystem headlines into concise, fluent Chinese.\n"
            "Rules: keep plugin names and technical acronyms (Dataview/Templater/MCP/RAG/LLM) as-is.\n"
            "Return one line per number, format: N. 中文翻译\n\n"
            + "\n".join(lines)
        )
        for attempt in range(3):
            try:
                import time
                if attempt > 0:
                    time.sleep(60)  # wait for rate-limit window to reset
                result = client.chat(
                    "You are an Obsidian plugin ecosystem translator. Translate English headlines "
                    "into fluent, concise Chinese. Preserve plugin names and technical acronyms. "
                    "Output format: N. Chinese translation — one numbered line per headline, no extra text.",
                    prompt, temperature=0.1,
                )
                for line in result.strip().split("\n"):
                    line = line.strip()
                    parts = line.split(". ", 1)
                    if len(parts) == 2 and parts[0].isdigit():
                        idx = int(parts[0]) - 1
                        if 0 <= idx < len(batch):
                            id_to_cn[batch[idx].event_id] = parts[1].strip()
                break
            except Exception as e:
                print(f"  [CN translate] Batch {batch_start // BATCH_SIZE + 1} attempt {attempt + 1} failed: {str(e)[:80]}")
                if attempt == 2:
                    print(f"  [CN translate] Batch {batch_start // BATCH_SIZE + 1} exhausted retries, using keyword preprocess")
        import time
        time.sleep(2)  # rate limiting guard

    for r in records:
        if r.event_id in id_to_cn and id_to_cn[r.event_id]:
            r.title_cn = id_to_cn[r.event_id]

    print(f"  [CN translate] LLM translated {len(id_to_cn)}/{len(all_records)} titles")


def run_weekly(config: dict):
    """Full weekly pipeline: collect from all Tier 1 + Tier 2 sources."""
    print(f"[Weekly] Starting pipeline — {datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC")
    records: list[EventRecord] = []

    sources_cfg = config.get("sources", {})
    enabled_sources = {k: v for k, v in sources_cfg.items() if v.get("enabled", True)}

    print(f"[Weekly] Collecting from {len(enabled_sources)} sources...")

    for source_key, source_cfg in enabled_sources.items():
        try:
            collector = RealSearchCollector(config, source_key)
            collector.gh_token = os.environ.get("GH_TOKEN", "")
            items = collector.collect()
            for item in items:
                item.categories = _auto_categorize(item, config)
            records.extend(items)
            if items:
                print(f"  [{source_key}] {len(items)} items — {source_cfg.get('name', source_key)}")
        except Exception as e:
            print(f"  [{source_key}] FAILED: {e}")

    if not records:
        print("[Weekly] No records collected — check source configuration.")
        return

    # Merge + dedup
    merged = _merge_records(records)
    print(f"[Weekly] Merged: {len(merged)} unique events (from {len(records)} raw)")

    dedup = Deduplicator(str(ROOT / "data" / "state.json"))
    new_records, seen = dedup.deduplicate(merged)
    print(f"[Weekly] Dedup: {len(new_records)} new / {seen} already seen")

    if not new_records:
        print("[Weekly] All events already seen this cycle.")
        return

    # Filter + score
    qf = QualityFilter(config)
    scorer = Scorer(config)

    new_records = qf.filter(new_records)
    new_records = scorer.score(new_records)
    new_records.sort(key=lambda r: r.confidence_score, reverse=True)

    grade_counts = {}
    for r in new_records:
        g = r.confidence_grade
        grade_counts[g] = grade_counts.get(g, 0) + 1
    grade_str = ", ".join(f"{k}:{v}" for k, v in sorted(grade_counts.items()))
    print(f"[Weekly] Filtered+Scored: {len(new_records)} events — {grade_str}")

    # Generate Chinese titles (LLM batch translation with rule-based fallback)
    _generate_cn_titles(new_records)
    cn_count = sum(1 for r in new_records if r.title_cn)
    print(f"[Weekly] CN titles generated: {cn_count}/{len(new_records)}")

    # AI deep analysis
    deep_analysis = ""
    try:
        from src.ai.llm_client import LLMClient
        from src.ai.deep_analyzer import DeepAnalyzer

        client = LLMClient()
        analyzer = DeepAnalyzer(client, ROOT / "prompts")
        top_n = min(len(new_records), 15)
        deep_analysis = analyzer.analyze(new_records, top_n=top_n)
        print(f"[Weekly] AI deep analysis generated ({len(deep_analysis)} chars)")
    except Exception as e:
        print(f"[Weekly] AI skipped (will render data-only report): {e}")

    # Render
    renderer = MarkdownRenderer(str(ROOT / "output"))
    stats = {
        "本周采集": len(records),
        "去重后": len(new_records),
        "新事件": len(new_records),
        "可信度分布": grade_str,
        "独立生态覆盖": _eco_coverage(new_records),
    }
    renderer.render_weekly_report(new_records, deep_analysis=deep_analysis, stats=stats)

    print(f"[Weekly] ✅ Done — report written to output/")
    print(f"[Weekly] Top event: {new_records[0].title[:80] if new_records else 'N/A'}")


def _eco_coverage(records: list[EventRecord]) -> str:
    ecosystems: set[str] = set()
    for r in records:
        for c in r.citations:
            ecosystems.add(c.ecosystem)
    return f"{len(ecosystems)} ecosystems: {', '.join(sorted(ecosystems)[:8])}"


# ---- CLI entry ----

def main():
    parser = argparse.ArgumentParser(description="Weekly domain intelligence digest")
    parser.add_argument(
        "--mode", choices=["weekly", "daily"], default="weekly",
        help="Run mode: weekly (full pipeline) or daily (Tier 1 only)",
    )
    args = parser.parse_args()

    # Ensure root in path for absolute imports
    sys.path.insert(0, str(ROOT))

    config = load_config()
    print(f"[Main] Mode: {args.mode} | Sources: {len(config.get('sources', {}))}")

    if args.mode == "weekly":
        run_weekly(config)
    else:
        print("[Main] Daily mode not yet configured — use weekly.")


if __name__ == "__main__":
    main()
