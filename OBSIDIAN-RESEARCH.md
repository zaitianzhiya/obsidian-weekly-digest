# Obsidian 插件生态 (Obsidian Plugins & Extensions) — 每周深度周报调研文档

> 本文件为 **Obsidian 插件与扩展生态** 领域的深度调研文档，用于驱动每周深度周报的自动化采集、分类、评分、摘要与渲染。
> 主题覆盖：官方插件市场动态、社区插件发布/更新、AI 插件、MCP 生态、安全事件、中文社区、主题与工作流。

---

## 1. 生态规模与现状 (2026)

### 1.1 概览

"Obsidian 插件生态"在本课题中定义为：**围绕 Obsidian 本地优先 Markdown 笔记软件构建的第三方扩展体系**，覆盖 **社区插件（Community Plugins）→ 主题（Themes）→ CSS 片段（Snippets）→ API/SDK → MCP 服务器 → AI 集成** 全链条。Obsidian 以"本地 Markdown 文件 + 插件系统"为核心哲学，其插件生态是支撑其成为"第二大脑"（Second Brain）首选工具的关键资产。

### 1.2 关键规模数据 (2026)

| 指标 | 数值 | 说明 |
|------|------|------|
| **累计插件/主题数量** | 4000+ | 自 2020 年 API 发布以来，社区创建的插件与主题总数 |
| **官方目录社区插件数** | ~2750 | obsidian-releases 官方社区目录收录的经过评审的插件 |
| **累计总下载量** | 120M+ | 所有社区插件的累计下载次数（2026 年中） |
| **下载量超 100 万插件数** | 10+ | 头部插件数量，Excalidraw 单款即达 685 万 |
| **Obsidian Community 上线** | 2026 年 5 月 | 官方全新社区平台，含自动化安全评审 |
| **积压提交清理** | 2300+ 个 | 上线数日内由自动化扫描完成积压插件提交审核 |

### 1.3 增长轨迹

- **2020 年**: Obsidian 1.0 前夜，API 发布（0.9.x 起），首批 ~40 个插件（老牌：Calendar、Periodic Notes、Kanban）
- **2021 年**: 插件数量破 1000，Dataview 出现引爆"数据库查询式笔记"
- **2022 年**: 插件破 1500，Obsidian 1.0 正式版，商业插件（付费）机制引入
- **2023-2024 年**: AI 插件元年——Smart Connections、Text Generator、Copilot 陆续出现；插件数量破 2000
- **2025 年**: MCP 生态爆发——kepano/obsidian-skills 成为现象级仓库（30.5k stars）；Claudian 官方 Claude 插件上线；插件逼近 2600
- **2026 年**: Obsidian Community 官方平台上线，自动化安全评审，生态从"野生长"进入"平台治理"阶段

### 1.4 生态特征

- **本地优先 (Local-first)**: 所有数据为本地 Markdown 文件，插件在此基础上叠加功能，无厂商锁定
- **自愿付费**: 核心功能免费（个人使用），商业化插件、Sync/Publish 增值服务构成收入
- **官方评审制**: 插件须经过 GitHub obsidian-releases 人工+自动化评审才能进入社区目录
- **AI 融合**: 2026 年最大趋势，RAG/本地模型/Agent/MCP 全面渗透

---

## 2. 最热门插件 Top 30（按下载量）

### 2.1 头部插件详细榜单 (Top 17 — 有公开下载数据)

| # | 插件 | 下载量 | 分类 | 核心功能 |
|---|------|--------|------|----------|
| 1 | **Excalidraw** | 6.85M | 画布/思维导图 | 白板手绘、草图→Obsidian、思维导图、图表嵌入 |
| 2 | **Templater** | 4.7M | 模板引擎/脚本 | 动态模板、JS 脚本嵌入、自动化文档生成 |
| 3 | **Dataview** | 4.6M | 数据库查询 | 用类似 SQL 的查询语言将笔记元数据动态渲染为表格/列表/任务 |
| 4 | **Tasks** | 3.7M | 任务管理 | GTD 任务管理、优先级/截止日期/重复任务、跨笔记聚合 |
| 5 | **Advanced Tables** | 3.1M | 表格增强 | Markdown 表格编辑增强、公式、表格导航 |
| 6 | **Calendar** | 2.9M | 日历 | 日历视图、日常笔记导航、日记体系 |
| 7 | **Git** | 2.9M | 版本控制 | 自动 Git 提交/拉取/备份、版本历史、跨设备同步 |
| 8 | **Kanban** | 2.4M | 看板 | 看板视图、任务卡片、拖拽管理 |
| 9 | **Style Settings** | 2.4M | 主题/UI | 让主题支持自定义选项面板，微调界面样式 |
| 10 | **Iconize** | 2.1M | 图标 | 给文件夹和文件添加图标，美化侧边栏/标签页 |
| 11 | **Remotely Save** | 2.0M | 同步备份 | 通过 S3/WebDAV/Dropbox 等远程保存，非官方同步方案 |
| 12 | **QuickAdd** | 1.9M | 快捷操作 | 捕获/宏/捕获框，一键快速添加笔记和模板 |
| 13 | **Copilot for Obsidian** | 1.6M | AI | RAG 聊天：与本地知识库对话、自定义 Agent 指令 |
| 14 | **Omnisearch** | 1.6M | 搜索增强 | 全库模糊搜索、OCR 结果索引、本地搜索 |
| 15 | **Claudian** | 1.5M | AI | 官方 Claude 集成：对话、知识库问答、Claude 插件目录 |
| 16 | **Importer** | 1.4M | 数据迁移 | 从 Notion/Evernote/Roam/Google Keep 等导入 |
| 17 | **Smart Connections** | 1.0M+ | AI | 本地语义搜索、自动关联笔记、智能聊天 |

### 2.2 Top 30 补全 (13-30 位 — 估算/历史下载量级别)

| # | 插件 | 下载量级 | 分类 | 核心功能 |
|---|------|---------|------|----------|
| 18 | **Breadcrumbs** | ~950K | 知识管理 | 层级/亲缘关系图谱，构建知识网络导航 |
| 19 | **Periodic Notes** | ~900K | 日记体系 | 日/周/月/季度周期笔记的创建与导航 |
| 20 | **Obsidian Git**（或 Git 同族） | ~850K | 版本控制 | 备份历史快照、分支管理 |
| 21 | **Banners** | ~800K | 主题/UI | 笔记顶部横幅图片 |
| 22 | **Outliner** | ~780K | 大纲编辑 | 列表缩进/折叠增强、zoom 聚焦 |
| 23 | **Note Refactor** | ~750K | 知识管理 | 从笔记提取段落为独立笔记、自动链接 |
| 24 | **Pandoc Plugin** | ~700K | 写作导出 | 基于 Pandoc 的导出/导入与格式转换 |
| 25 | **Better Word Count** | ~680K | 写作工具 | 增强的字数统计、页数、阅读时间 |
| 26 | **Sliding Panes (Andy's Mode)** | ~650K | UI | 滑动画板式多列界面 |
| 27 | **Min3D** | ~600K | 主题/UI | 3D 标签墙、力导向图、思维导图全览 |
| 28 | **Buttons** | ~580K | 自动化 | 在笔记中插入可点击按钮执行动作 |
| 29 | **cMenu** | ~550K | 写作工具 | 编辑器浮动工具条快捷格式化 |
| 30 | **Zotero Integration** | ~520K | 学术引用 | Zotero 文献库整合、引用插入、学术笔记 |

### 2.3 头部插件规律总结

- **"瑞士军刀"型长红**: Excalidraw/Templater/Dataview 三巨头稳居前五，功能深度决定长青
- **工作流型刚需**: Tasks/Calendar/Kanban/Git 覆盖 GTD + 日历 + 看板 + 备份四大基本工作流
- **AI 插件快速上位**: Copilot(1.6M)/Claudian(1.5M) 均在 1-2 年内冲入前 20，是增速最快的类别
- **中文生态参与**: Excalidraw 等插件有活跃的中文社区插件汉化/教程生态

---

## 3. AI 插件趋势 (2026 最大趋势)

AI 是 2026 年 Obsidian 插件生态最重要的增长引擎。方向从"单点 AI 功能"走向"完整 Agent 工作流"。

### 3.1 主要 AI 插件图谱

| 插件 | 类型 | 定位 | 核心能力 |
|------|------|------|----------|
| **Smart Connections** | 本地语义搜索 | 知识关联 | 本地向量嵌入、笔记语义关联、与 AI 对话你的笔记 |
| **Copilot for Obsidian** | RAG 聊天 | 知识库问答 | 私有 RAG 管道、自定义系统提示、多模型支持（OpenAI/Claude/本地） |
| **Smart Composer** | AI 写作 | Cursor 风格 | 行内 AI 编辑、@提及笔记作为上下文、AI 重构文本 |
| **Text Generator** | 文本生成 | 通用生成 | 模板化文本生成、翻译/总结/续写，最早普及的 AI 插件之一 |
| **Local GPT** | 离线推理 | 隐私本地 | 本地模型（Ollama/llama.cpp）接入，完全离线 |
| **Khoj** | 自托管 | 个人 AI 助理 | 自托管语义搜索 + 聊天，支持多数据源 |
| **AI Transcriber** | 语音转写 | 本地 Whisper | 本地 Whisper 模型转写音频/会议/访谈为笔记 |
| **Claudian** | Claude 集成 | 官方原生 | 官方 Claude 对话、知识库 RAG、Claude 插件目录 |
| **Codian** | 本地编码 Agent | 代码助手 | 在 Obsidian 中运行本地编码 agent，读取/修改代码库 |
| **LLM Wiki** | LLM 知识库 | 结构化管理 | 用 LLM 自动整理/链接知识库页面 |

### 3.2 关键趋势总结

- **从"聊天"到"工作流"**: 单纯的聊天框已过时，转向"AI 深度嵌入写作/整理/复习"流程
- **隐私回归**: Smart Connections / Local GPT / AI Transcriber 强调本地模型，回应"笔记不应上传云端"的核心用户诉求
- **RAG 成为标配**: Copilot/Smart Connections/Claudian 都以"让 AI 读你的笔记"为核心，本地知识库问答
- **Agent 化**: Codian 等本地编码 Agent 显示 AI 插件从"辅助生成"走向"自主执行"

### 3.3 MCP (Model Context Protocol) 生态

MCP 是 2026 年 Obsidian AI 生态的基础设施，让 Claude/其他模型直接读写 Obsidian 库：

| 项目 | 类型 | 说明 |
|------|------|------|
| **kepano/obsidian-skills** | 官方技能包 | Obsidian CEO 开源，30.5k stars，定义 Claude 操作 Obsidian 的标准化技能 |
| **mcp-obsidian** | 社区 MCP 服务器 | 通用 MCP 服务器，暴露 vault 搜索/读取/创建笔记接口 |
| **obsidian-mcp-server** | 社区 MCP 服务器 | 类目实现，支持全文搜索、模糊匹配、笔记操作 |

MCP 的核心价值：**Agent（Claude 等）可以像人一样打开你的笔记库进行搜索、读取、创建**，与 Obsidian CLI 一起构成"让 AI 成为 Obsidian 深度用户"的通道。

---

## 4. 官方平台动态

### 4.1 Obsidian Community（2026 年 5 月上线）

官方新一代社区平台，标志 Obsidian 插件生态从"GitHub PR 评审"转向"官方目录治理"：

| 能力 | 说明 |
|------|------|
| **自动化恶意软件扫描** | 每版本对插件进行自动安全扫描，检测恶意代码/网络行为 |
| **Safety Scorecard** | 插件安全评分卡，展示权限使用、数据访问等安全画像 |
| **Access Disclosure** | 权限/数据访问披露声明，明确插件会访问什么数据 |
| **Verified Developer** | 已验证开发者徽章，增加可信度 |
| **积压清理** | 上线数日内自动化处理 2300+ 积压提交，大幅缩短审核排队 |

### 4.2 Obsidian 1.12 与 Agent 生态

- **Obsidian 1.12**: 引入 CLI flag，允许外部 Agent 以受控方式操作 Obsidian
- **Obsidian CLI**: 面向 Agent 的命令行工具，配合 kepano/obsidian-skills 形成"AI 原生工作流"
- 意义：官方主动拥抱 AI Agent 生态，把 Obsidian 定位为"AI 的第二大脑文件层"

### 4.3 产品线扩张

| 产品 | 类型 | 说明 |
|------|------|------|
| **Bases** | 官方 Notion-like 数据库 | Obsidian 官方结构化数据库，补足 Dataview 缺失的表格数据库体验 |
| **Obsidian Reader** | 阅读应用 | 阅读/标注 RRS 文章、论文、网页，与库同步 |
| **Web Clipper** | 网页剪藏 | 浏览器插件剪藏网页为 Markdown，模板化处理逻辑 |
| **Siri/Shortcuts** | 系统集成 | iOS 快捷指令操作 Obsidian（快速捕获/查询） |
| **Mobile Widgets** | 移动端小组件 | 桌面小组件快速捕获 |
| **Keychain** | 凭证管理 | 系统钥匙串集成，安全存储第三方凭证 |

### 4.4 官方 Roadmap 关注点（周报可追踪）

- Bases 正式版功能演进
- Obsidian 1.13+ 的 AI 原生特性
- Community 平台规则更新（审核标准、评分规则）
- Sync 与插件生态的互操作边界

---

## 5. 安全事件与机制

### 5.1 PHANTOMPULSE RAT 事件（2026 年 4 月）

Obsidian 生态最著名的安全事件：

- **攻击方式**: 社会工程学攻击（social engineering）——攻击者伪装成合法插件开发者，诱导用户安装恶意插件
- **恶意行为**: 植入 PHANTOMPULSE 远程访问木马（RAT），可窃取笔记数据、上传凭证、远程控制
- **传播途径**: 伪装插件提交 → 诱导安装，而非直接入侵官方市场
- **影响**: 触发官方安全评审体系全面升级，成为"社区目录需自动化安全扫描"的直接动因

### 5.2 官方安全机制

| 机制 | 说明 |
|------|------|
| **Remote Disable（远程禁用）** | 官方可远程禁用恶意插件；12 小时废弃检查（deprecation check）周期 |
| **每版本自动化扫描** | 每版发布均过自动化恶意代码扫描（Community 平台） |
| **Safety Scorecard** | 安全评分卡量化插件权限/行为风险 |
| **Access Disclosure** | 强制披露数据访问行为 |
| **Verified Developer** | 验证开发者身份，降低冒名风险 |
| **评审制升级** | 人工 + 自动化双层评审，高危行为（网络请求、代码执行）重点审查 |

### 5.3 对用户的安全建议（可写入周报安全专栏）

1. **只安装官方 Community 目录中的插件**，避免从来源不明的网页/网盘安装
2. 安装前查看 **Safety Scorecard 与 Access Disclosure**，警惕申请过多权限的插件
3. 关注 **Verified Developer** 徽章与插件 star/下载量/活跃度
4. 重要 vault 开启 **Git 备份 / Obsidian Sync 版本历史**，恶意插件被禁用后可回滚
5. 可疑插件及时上报，利用 **Remote Disable** 机制保护他人
6. 插件仅从 GitHub 官方仓库获取，不轻信"破解版/汉化整合包"

---

## 6. 插件分类体系 (Category System for Weekly Digest)

遵循既有周报项目的模式，设计 12 个 Obsidian 生态专属分类标签：

| Category | Label | Weight | Description |
|----------|-------|--------|-------------|
| **核心插件** | `#core_plugin` | 15% | Dataview、Templater、Tasks 等基础工作流插件的大版本更新、架构变化 |
| **AI 插件** | `#ai_plugin` | 20% | AI 插件发布/更新（Smart Connections、Copilot、Claudian、Codian 等）、本地模型、RAG |
| **可视化工具** | `#visual_tool` | 10% | Excalidraw、Kanban、Min3D、Graph 增强等画布/图表/看板类 |
| **知识管理流程** | `#pkm_workflow` | 12% | PARA/Zettelkasten/日记体系、双链、标签、Breadcrumbs 等 PKM 方法论工具 |
| **写作工具** | `#writing_tool` | 8% | 编辑器增强、Markdown 排版、Pandoc 导出、AI 写作辅助 |
| **同步与备份** | `#sync_backup` | 8% | Remotely Save、Git、Obsidian Sync 替代方案、加密备份 |
| **主题与界面** | `#theme_ui` | 7% | 主题发布/更新、Style Settings、CSS 片段、UI 布局 |
| **安全** | `#security` | 8% | 恶意插件、安全评审机制、数据泄露、安全最佳实践 |
| **开发者/API/MCP** | `#dev_api` | 12% | 插件 SDK、API 变化、MCP 服务器、kepano/obsidian-skills、开发工具 |
| **官方动态** | `#official_news` | 8% | Obsidian 官方更新（版本、Community 平台、Bases、Reader、CLI） |
| **中文社区** | `#chinese_community` | 3% | Pkmer、中文插件/主题、中文教程、汉化生态 |
| **新插件发布** | `#plugin_release` | 5% | 新插件首发、值得关注的插件新面孔 |

> 说明：`#chinese_community` 为跨领域标签，与其他分类叠加使用，不计入权重总和。

---

## 7. 信息来源体系 (Config Sources)

### Tier 1 — 一手/官方/原创新闻源 (14 sources)

| # | Source | Type | Language | What it provides |
|---|--------|------|----------|------------------|
| 1 | **obsidian.md 官方博客** | web_search | EN | 产品发布、功能公告、公司动态 |
| 2 | **obsidian.md Roadmap** | web_search | EN | 官方路线图更新、功能计划 |
| 3 | **obsidian.md Changelog** | web_search | EN | 版本更新日志（桌面/移动端） |
| 4 | **Obsidian Help/论坛官方版块** | web_search | EN | 官方公告、插件评审规则 |
| 5 | **Obsidian Community 平台** | web_search | EN | 新上架插件、Verified Developer、安全评分 |
| 6 | **kepano (Steph Ango) Twitter/X** | web_search | EN | CEO 动态、官方立场、产品方向 |
| 7 | **obsidian-releases GitHub** | web_search | EN | 插件发布/更新/下架事件流 |
| 8 | **Obsidian Forum (forum.obsidian.md)** | web_search | EN | 官方论坛插件发布/讨论、开发讨论 |
| 9 | **obsidianstats.com** | web_search | EN | 插件下载量/活跃度统计数据 |
| 10 | **Pkmer (PKM-er)** | web_search | ZH | 中文社区周报、插件中文文档、教程 |
| 11 | **少数派 sspai (Obsidian 标签)** | web_search | ZH | 中文 Obsidian 深度教程与测评 |
| 12 | **what's new (什么值得买 Obsidian)** | web_search | ZH | 中文用户分享插件体验 |
| 13 | **小红书 Obsidian 话题** | web_search | ZH | 中文社区插件推荐/讨论 |
| 14 | **Obsidian YouTube 频道** | web_search | EN | 官方/头部创作者视频更新（Nicole van der Hoeven 等） |

### Tier 2 — 二手/聚合/垂直信息源 (12 sources)

| # | Source | Type | Language | What it provides |
|---|--------|------|----------|------------------|
| 15 | **Reddit r/ObsidianMD** | web_search | EN | 社区讨论、插件推荐、问题求助热帖 |
| 16 | **r/ObsidianMD 周报聚合帖** | web_search | EN | 社区每周高赞/趋势话题 |
| 17 | **Obsidian Discord 社区** | web_search | EN | 实时开发讨论、插件作者动态 |
| 18 | **GitHub Trending (Obsidian 相关)** | web_search | EN | 高 star 的 Obsidian 插件/工具仓库 |
| 19 | **Hacker News (Obsidian 讨论)** | web_search | EN | 技术社区对 Obsidian 的讨论与关注 |
| 20 | **Eltacomaloki / Obsidian 插件目录站** | web_search | EN | 插件分类索引与推荐 |
| 21 | **obsidian-plugins.org** | web_search | EN | 第三方插件目录/统计 |
| 22 | **36 氪 / 极客公园 (效率工具版)** | web_search | ZH | 中文科技媒体 Obsidian/效率工具报道 |
| 23 | **知乎 Obsidian 话题** | web_search | ZH | 中文深度问答与评测 |
| 24 | **Bilibili Obsidian 教程区** | web_search | ZH | 中文视频教程与插件演示 |
| 25 | **OpenGithubs (效率工具)** | web_search | ZH/EN | GitHub 中文日报中 Obsidian 生态项目 |
| 26 | **Ruanyf 阮一峰周刊** | web_search | ZH/EN | 科技周刊中偶有 Obsidian/MCP 生态条目 |

---

## 8. 关键词体系 (80+ Keywords)

### 8.1 按分类映射的关键词

#### `#core_plugin` — 核心插件 (12 keywords)
| Keyword | 中文 | 说明 |
|---------|------|------|
| Dataview | 数据库查询插件 | 查询语言 DSL |
| Templater | 模板引擎 | 模板脚本 |
| Tasks | 任务管理 | GTD |
| Obsidian Git | Git 插件 | 版本控制 |
| QuickAdd | 快捷捕获 | 宏 |
| Periodic Notes | 周期笔记 | 日记体系 |
| 插件更新 | Plugin update | 大版本 |
| plugin release | 插件发布 | 新版本 |
| Obsidian plugin | 插件 | 通用 |
| core plugin | 核心插件 | 通用 |
| 双链 | Backlinks | 双链功能 |
| Graph View | 关系图谱 | 图谱功能 |

#### `#ai_plugin` — AI 插件 (15 keywords)
| Keyword | 中文 | 说明 |
|---------|------|------|
| Smart Connections | 智能关联 | 本地语义搜索 |
| Copilot for Obsidian | AI 副驾驶 | RAG 聊天 |
| Smart Composer | 智能写作 | AI 写作 |
| Text Generator | 文本生成 | 通用生成 |
| Local GPT | 本地模型 | 离线推理 |
| Khoj | 自托管 AI | 个人助理 |
| AI Transcriber | AI 转写 | 本地 Whisper |
| Claudian | 官方 Claude 插件 | Claude 集成 |
| Codian | 本地编码 Agent | 代码 Agent |
| LLM Wiki | LLM 知识库 | 结构化整理 |
| RAG | 检索增强生成 | 知识库问答 |
| local model | 本地模型 | Ollama |
| Ollama | 本地推理引擎 | llama.cpp |
| AI agent | AI 智能体 | Agent 工作流 |
| 大模型 插件 | AI 插件 | 中文通用 |

#### `#visual_tool` — 可视化 (10 keywords)
| Keyword | 中文 | 说明 |
|---------|------|------|
| Excalidraw | 白板画布 | 手绘/图表 |
| Kanban | 看板 | 任务看板 |
| Min3D | 3D 标签墙 | 3D 可视化 |
| Mermaid | 图表 | 图表渲染 |
| Mind map | 思维导图 | 导图插件 |
| Obsidian Canvas | 画布 | 官方画布 |
| Diagram | 图表 | 通用 |
| Flowchart | 流程图 | 流程 |
| timeline | 时间线 | 时间线插件 |
| graph plugin | 图谱插件 | 图谱增强 |

#### `#pkm_workflow` — 知识管理流程 (10 keywords)
| Keyword | 中文 | 说明 |
|---------|------|------|
| Zettelkasten | 卡片盒笔记法 | PKM 方法 |
| PARA | 任务管理法 | 组织方法 |
| Second Brain | 第二大脑 | 理念 |
| Breadcrumbs | 面包屑 | 层级导航 |
| Note Refactor | 笔记重构 | 拆分笔记 |
| Obsidian workflow | 工作流 | 通用 |
| 知识管理 | PKM | 中文通用 |
| 笔记方法 | note-taking | 方法论 |
| tagging | 标签 | 标签系统 |
| frontmatter | 属性元数据 | YAML 属性 |

#### `#writing_tool` — 写作工具 (8 keywords)
| Keyword | 中文 | 说明 |
|---------|------|------|
| Pandoc | 格式转换 | 导出工具 |
| Better Word Count | 字数统计 | 统计增强 |
| cMenu | 浮动工具条 | 格式工具栏 |
| Typewriter | 打字机模式 | 写作模式 |
| Outliner | 大纲编辑 | 列表增强 |
| 写作 插件 | writing plugin | 中文通用 |
| markdown editor | Markdown 编辑器 | 编辑器增强 |
| 导出 | export | 导出功能 |

#### `#sync_backup` — 同步与备份 (7 keywords)
| Keyword | 中文 | 说明 |
|---------|------|------|
| Remotely Save | 远程保存 | 同步方案 |
| Obsidian Sync | 官方同步 | 官方服务 |
| Obsidian Git | Git 备份 | 版本备份 |
| backup | 备份 | 通用 |
| 同步 | sync | 中文通用 |
| WebDAV | WebDAV | 同步协议 |
| encryption | 加密 | 加密备份 |

#### `#theme_ui` — 主题与界面 (7 keywords)
| Keyword | 中文 | 说明 |
|---------|------|------|
| Obsidian theme | 主题 | 主题发布 |
| Style Settings | 样式设置 | 主题自定义 |
| CSS snippet | CSS 片段 | 样式片段 |
| 主题 | theme | 中文通用 |
| AnuPpuccin | 流行主题 | 主题名 |
| Minimal theme | 极简主题 | 主题名 |
| UI 界面 | UI | 界面更新 |

#### `#security` — 安全 (8 keywords)
| Keyword | 中文 | 说明 |
|---------|------|------|
| PHANTOMPULSE | 恶意插件木马 | 安全事件 |
| RAT | 远程访问木马 | 恶意软件 |
| malware | 恶意软件 | 安全 |
| Remote Disable | 远程禁用 | 官方机制 |
| Safety Scorecard | 安全评分卡 | 安全评审 |
| Access Disclosure | 权限披露 | 数据访问 |
| 安全 | security | 中文通用 |
| malicious plugin | 恶意插件 | 安全 |

#### `#dev_api` — 开发者/API/MCP (12 keywords)
| Keyword | 中文 | 说明 |
|---------|------|------|
| MCP | Model Context Protocol | 模型上下文协议 |
| mcp-obsidian | MCP 服务器 | 社区实现 |
| obsidian-mcp-server | MCP 服务器 | 社区实现 |
| obsidian-skills | 官方技能包 | kepano/30.5k stars |
| Obsidian API | 插件 API | 开发接口 |
| plugin SDK | 插件 SDK | 开发工具 |
| Obsidian CLI | 命令行工具 | Agent 接入 |
| Claude 插件 | Claude plugin | AI 集成 |
| 开发者 | developer | 中文通用 |
| TypeScript | 插件语言 | 开发语言 |
| obsidian-releases | 发布仓库 | GitHub |
| plugin manifest | 插件清单 | manifest.json |

#### `#official_news` — 官方动态 (8 keywords)
| Keyword | 中文 | 说明 |
|---------|------|------|
| Obsidian Community | 官方社区平台 | 2026.05 上线 |
| Obsidian 1.12 | 版本更新 | CLI flag |
| Bases | 官方数据库 | Notion-like |
| Obsidian Reader | 阅读应用 | 官方阅读 |
| Web Clipper | 网页剪藏 | 官方剪藏 |
| Roadmap | 路线图 | 官方计划 |
| Changelog | 更新日志 | 版本日志 |
| 官方 | official | 中文通用 |

#### `#chinese_community` — 中文社区 (6 keywords)
| Keyword | 中文 | 说明 |
|---------|------|------|
| Pkmer | 中文社区 | pkmer.cn |
| 少数派 | sspai | 中文媒体 |
| 汉化 | 汉化包 | 中文翻译 |
| 中文教程 | 教程 | 中文教程 |
| 中文社区 | 社区 | 通用 |
| 小红书 | 小红书 | 中文平台 |

#### `#plugin_release` — 新插件发布 (8 keywords)
| Keyword | 中文 | 说明 |
|---------|------|------|
| new plugin | 新插件 | 首发 |
| plugin release | 插件发布 | 上新 |
| 新插件 | new plugin | 中文通用 |
| community plugin | 社区插件 | 目录收录 |
| first release | 首次发布 | 首发 |
| 插件推荐 | 推荐 | 评测推荐 |
| obsidian plugin list | 插件清单 | 榜单 |
| plugin spotlight | 插件聚焦 | 介绍 |

### 8.2 负向关键词 (置信度降低)

| Keyword | 理由 |
|---------|------|
| 纯主题外观讨论（无插件实质更新） | 非插件生态事件 |
| 个人使用心得/流水账 | 无生态价值 |
| 广告/推广软文 | 降级 |
| 疑似/可能/rumor（无验证） | 降级 |
| 纯 Discord/论坛闲聊 | 降级 |
| 无关效率工具（Notion 等竞品仅提及） | 需 Obsidian 关联性 |
| 加密货币/挖矿等无关噪音 | 过滤 |

---

## 9. 评分维度 (5-dim)

| Dimension | Weight | Description |
|-----------|--------|-------------|
| **Community Impact (社区影响力)** | 30% | 下载量/star/讨论热度、被引用程度、是否引发社区模式变革、头部创作者讨论 |
| **Novelty (新颖度)** | 25% | 全新插件首发、前所未有的功能方向、AI/MCP 等前沿能力、对现有工作流的突破 |
| **Practical Utility (实用价值)** | 20% | 实际解决用户痛点的程度、功能完成度、文档质量、易用性、可否立即上手 |
| **Security/Trust (安全与可信)** | 15% | 插件权限是否合理、有无安全审计结果、开发者可信度、恶意代码风险、官方推荐度 |
| **Ecosystem Significance (生态意义)** | 10% | 对生态基础设施的贡献（SDK/MCP/CLI）、是否定义新标准、官方与社区的连接 |

### 生态独立附加维度（叠加评分）

- **官方背书度**：是否获官方推荐、Verified Developer、出现在官方博客/文档
- **中文可及性**：是否有中文文档/汉化/中文教程，影响中文社区传播力
- **维护活跃度**：近 6 个月是否有更新、issue 响应、兼容 Obsidian 最新版

---

## 10. 事件条目质量门控

| 条件 | 动作 |
|------|------|
| 标题不含至少 1 个正面关键词 | PASS（降低置信度） |
| 内容长度 < 100 chars | PASS |
| 纯个人心得/无插件实质更新 | PASS |
| 社交媒体/自媒体无权威来源 | 降级至 C/D |
| 传闻/内幕无交叉验证 | 降级至 C |
| 安全事件（恶意插件等）必须官方/多源交叉验证 | 提升为 A 级优先 |
| AI 插件新能力必须实际可验证（非概念/PPT） | 降级至 C 或过滤 |
| 同一事件被多源报道（如官方博客 + Reddit + Pkmer） | 合并为一条，以官方源为主源 |
| 竞品（Notion/Logseq）内容无 Obsidian 关联 | 过滤 |
| 纯主题外观/换肤（无生态功能） | 降级或归档至 `#theme_ui` 附属 |

---

## 11. AI Prompt 工程 (Domain-specific)

### 11.1 中文摘要风格规则

1. **禁止裸术语**：每个专业术语/英文缩写在初次出现时至少用一句自然语言解释其实际含义和影响。
   - 例如 "RAG" → "检索增强生成，先在你自己的笔记里搜索相关内容，再把这些内容作为上下文送给 AI 回答，因此回答是基于你私人知识的"
   - 例如 "MCP" → "模型上下文协议，一种让 Claude 等 AI 模型与本地工具（如 Obsidian）安全交互的开放标准，相当于给 AI 装了读写你笔记的接口"
   - 例如 "Templater" → "模板引擎插件，可在新建笔记时自动填充日期、文件属性，甚至执行 JavaScript 脚本，把重复性笔记生成自动化"

2. **3 秒钩子**：一句话概括「是什么 + 为什么值得关注」
   - 好例："Claudian 发布知识库问答功能，你不再需要把笔记复制粘贴给 Claude，它直接读取你的 vault 回答——Obsidian 用户第一次有了官方的本地 RAG"
   - 坏例："某插件发布更新"（空洞无物）

3. **双层阅读**：
   - 第一层（粗体标题下第一句）：一分钟快速扫读
   - 第二层（后续段落）：包含版本号、下载量、功能细节、生态影响、中文可用性

4. **避免空话**：不使用"近期发生了"、"值得关注"、"具有重要意义" 等模板化用语；直接给事实+数字（下载量、版本号、日期）。

5. **去重规则**：同一插件事件被多个来源报道（如官方博客 + Reddit + Pkmer），合并为一条，以官方源为主源，其余作为交叉验证计数。

### 11.2 Obsidian 专属分析角度（每个事件覆盖至少 2 个角度）

- **用户价值视角**：该插件/更新解决了什么具体痛点，谁最受益（学生/研究者/创作者/开发者）
- **下载量/传播视角**：数据（下载量、star、论坛讨论数、Reddit 热度）及增长趋势
- **生态格局视角**：对同类插件的替代/竞争/互补，是否重塑生态分工
- **安全视角**：权限合理性、隐私影响、是否需要谨慎对待
- **中文社区视角**：中文用户能否用上（文档/汉化/教程），Pkmer/中文媒体的关注度
- **AI/Agent 视角**：与 MCP/CLI/Agent 工作流的结合度，是否属于 AI 原生功能
- **官方关系视角**：官方支持/推荐/收录状态，对插件长期存续的意义

---

## 12. 技术架构参考 (Weekly Digest Pipeline)

- **采集**: RealSearchCollector（Tier 1 真实搜索：obsidian.md 博客 + 官方论坛 + obsidianstats + Pkmer；Tier 2 关键词骨架：Reddit/YouTube/Discord）
- **AI**: Gemini 2.5 Flash（中文摘要 + 深度分析）
- **渲染**: MarkdownRenderer → `output/weekly/{YYYY}/{YYYY-WNN}.md`
- **部署**: GitHub Actions cron（建议每周二：周一官方发布日后的生态发酵窗口）
- **Watchdog**: 3× Tuesday 检查
- **双语标题**: 沿用既有项目标准，事件列使用中文+英文双语标题

---
*本文件为 Obsidian 插件生态 (Obsidian Plugins & Extensions) 领域的深度调研文档，用于驱动每周深度周报的自动化采集、分类、评分、摘要与渲染。*
