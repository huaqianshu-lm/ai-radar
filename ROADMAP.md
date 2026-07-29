# AI Radar Roadmap

## 当前阶段

v0 主链路已跑通，进入稳定性修复阶段。X API 窄口径来源接入代码暂时保留，但 X 抓取已从默认日常流程中收起，近期不再排查或运行。

已具备：固定来源配置、公开来源抓取、raw 快照、items JSONL、brief input、可选 Claude Code CLI 生成每日简报、每日简报本地导出到 Obsidian、公众号草稿生成。

暂时收起：X API recent search 固定来源接入，代码保留但默认禁用，近期不再纳入日常抓取、问题排查或提醒。

## 最近有效进度

- 2026-07-29：完成 Phase 5 轻量来源权重和规则评分整理，集中维护 `source_type` 到 `credibility_score` 的可解释映射：`official=5`、`developer=4`、`curated=4`、`discovery=3`、`aggregator=3`、`community=2`；items 排序在保留列表页降权的基础上加入可信度优先，不引入 AI 自动评分、`novelty_score` 或复杂主题价值评分。
- 2026-07-29：完成 Phase 4 最小精选源接入，确认 `https://tldr.tech/api/rss/ai` 为公开可解析 RSS，新增 `TLDR AI` curated 来源；确认 `https://www.therundown.ai/archive` 可公开访问且首屏 HTML 可提取 16 个稳定 `/p/...` newsletter 详情页链接，新增 `The Rundown AI` curated 来源，复用现有 `webpage` 模式和 `article_path_prefix: /p/`，不新增 archive parser；`curated` 的 `credibility_score` 设为 4。当前 TLDR RSS 只能稳定获得 newsletter archive URL，因此本阶段 `source_url` / `canonical_url` 均指向 TLDR archive；The Rundown 第一版仅把 newsletter 详情页作为 editorial source，不解析每期内部新闻、不解析发布时间、不做分页。
- 2026-07-29：完成 Phase 3 Hacker News 发现源接入，新增 `hacker_news` 抓取模式和 `Hacker News AI` 配置，使用 HN Firebase API 读取 top stories 和 item JSON；通过关键词 token 过滤 AI 相关 story，raw/items 中 `source_url` 记录 HN story，`canonical_url` 记录原始外部链接，`source_type` 为 `discovery`，`credibility_score` 为 3；未做事件聚类、复杂评分或 brief 结构修改。
- 2026-07-29：完成 Phase 2 canonical 优先去重，历史和当日去重键改为 `canonical_url` 优先、`url` 兜底，标题去重保持不变；未做事件聚类、评分或新数据源接入。运行 `.venv/bin/python -m py_compile scripts/normalize_items.py` 成功；运行 `.venv/bin/python scripts/run_daily.py` 成功，items 数量和去重统计保持正常；函数级检查确认 `dedupe_url_key` 会优先使用 `canonical_url` 并去除 tracking 参数与 fragment。
- 2026-07-29：完成 Phase 1 最小数据模型扩展，raw frontmatter 和 items JSONL 兼容性新增 `source_url` / `canonical_url`；当前已有来源默认两者等于 `url`，brief 结构、新数据源、评分和聚类均未改动。运行 `.venv/bin/python -m py_compile scripts/fetch_sources.py scripts/normalize_items.py` 成功；运行 `.venv/bin/python scripts/run_daily.py` 成功，生成 `data/items/2026-07-29.jsonl`、`data/inbox/2026-07-29-brief-input.md`、`data/inbox/2026-07-29-run-summary.md`，并确认 13 条 items 均包含 `source_url` / `canonical_url`。
- 2026-07-29：确认 AI Radar 数据源与数据模型渐进式迭代方案，并保存到 `local/AI新闻抓取系统_最终迭代方案.md`；后续按小步迭代执行，每次完成并验证后等待用户确认再进入下一步。
- 2026-07-28：按版本管理策略排除公众号草稿、`settings.json` 和 `.DS_Store`，仅保留可提交项目改动；项目规则增加每次文件改动后提醒检查并提交未提交文件。
- 2026-07-27：将 Obsidian 导出接入每日流程，新增 `--export-obsidian` / `--overwrite-obsidian` 参数；`./ai-radar` 默认在简报质量检查通过后覆盖同步到配置好的 Obsidian Vault，并在 run summary 中记录导出状态。
- 2026-07-27：按用户要求暂时收起 X 抓取；`X AI Watchlist` 在 `config/sources.yaml` 中改为默认禁用，X recent search 代码保留但近期不再纳入日常抓取、问题排查或提醒。
- 2026-07-27：调整 AI Daily Brief 默认排版规范，后续生成简报改用 `example.md` 验证过的引用块、加粗小标题和分段留白格式；同步更新 2026-07-27 简报排版，并让质量检查脚本兼容新格式。
- 2026-07-27：新增最小 Obsidian 导出脚本，可将指定日期 AI Daily Brief 复制到环境变量配置的独立 Obsidian Vault；默认导出到 Vault 内 `Daily Briefs/`，已在 iCloud Obsidian 目录创建 `AI Radar` 独立 Vault 并完成 2026-07-21、2026-07-27 简报导出验证。
- 2026-07-22：新增 X API recent search 固定来源接入，支持从环境变量或 `.env.local` 读取 `X_BEARER_TOKEN`；完整流程验证通过，X 来源失败不会中断 raw/items/brief input/run summary 生成。
- 2026-07-21：完整流程恢复，生成 40 个 raw、29 条 items、brief input 和 AI Daily Brief，简报质量检查通过。
- 2026-07-13：抓取与 items 仍有部分有效产出，写入 8 条 items，但 brief 生成失败。
- 2026-07-12：已生成 AI Daily Brief 和公众号草稿，是最近一次确认有公众号草稿的日期。

## 当前问题

- Hugging Face Blog 摘要偏短，生成简报时需要注意信息不足。
- `data/wechat/` 已按当前策略加入忽略，不纳入版本管理；如后续要沉淀公众号发布稿，需要重新确认存放和提交规则。
- 公众号草稿生成没有出现在 2026-07-21 run summary 中，需要后续确认是否仍纳入自动流程。

## 下一步

1. 等待用户确认 Phase 5 轻量评分整理结果是否符合预期。
2. 如确认继续，进入 Phase 6：事件聚类和多来源合并；先只做规则级方案，不直接进入复杂实现。

## 最近验证

- 2026-07-29：运行 `.venv/bin/python -m py_compile scripts/normalize_items.py` 成功；运行 `.venv/bin/python scripts/normalize_items.py --date 2026-07-29` 和 `.venv/bin/python scripts/prepare_brief_input.py --date 2026-07-29` 成功，`data/items/2026-07-29.jsonl` 写入 148 条，去重统计为 4 条当日重复、66 条历史重复；字段检查确认当前 items 中 `official=5`、`developer=4`、`curated=4`、`discovery=3`，前 20 条无列表页且排序优先高可信来源；运行 `.venv/bin/python scripts/run_daily.py` 成功，主流程继续生成 items、brief input 和 run summary。
- 2026-07-29：运行公开端点检查，确认 `https://tldr.tech/api/rss/ai` 返回 `text/xml` 且可解析出 20 条 RSS entries；确认 `https://www.therundown.ai/archive` 返回 `200 text/html`，页面 HTML 可提取 16 个 `/p/...` newsletter 详情页链接；`https://www.therundown.ai/feed` 和 `https://www.therundown.ai/rss` 返回 404，因此 The Rundown AI 改按 Archive 最小方案接入。运行 `.venv/bin/python -m py_compile scripts/fetch_sources.py scripts/normalize_items.py` 成功；运行 `.venv/bin/python scripts/fetch_sources.py --limit 20` 成功，`The Rundown AI` 抓取 16 条并写入 16 个 raw，raw 的 `url` / `source_url` / `canonical_url` 均为 `/p/...` 详情页且 `is_list_page: false`；运行 `.venv/bin/python scripts/run_daily.py` 成功，`The Rundown AI` 抓取 16 条，`data/items/2026-07-29.jsonl` 写入 148 条，去重统计为 4 条当日重复、66 条历史重复；检查确认 16 条 The Rundown items 的 `source_type` 为 `curated`，`credibility_score` 为 4，`is_list_page` 均为 false。
- 2026-07-29：运行 `.venv/bin/python -m py_compile scripts/fetch_sources.py scripts/normalize_items.py` 成功；函数级验证 `fetch_hacker_news` 成功返回 AI 相关 HN stories，并确认 `source_url` 为 HN story、`canonical_url` 为外部原始链接；运行 `.venv/bin/python scripts/run_daily.py` 成功，`Hacker News AI` 抓取 5 条并写入 raw，`data/items/2026-07-29.jsonl` 写入 18 条，去重统计为 1 条当日重复、27 条历史重复；检查确认 5 条 HN items 的 `source_type` 为 `discovery`，`credibility_score` 为 3。
- 2026-07-29：运行 `.venv/bin/python -m py_compile scripts/normalize_items.py` 成功；运行 `.venv/bin/python scripts/run_daily.py` 成功，生成 `data/items/2026-07-29.jsonl`、`data/inbox/2026-07-29-brief-input.md`、`data/inbox/2026-07-29-run-summary.md`，items 写入 13 条，去重统计为 1 条当日重复、27 条历史重复；函数级检查确认 `dedupe_url_key` 优先使用 `canonical_url` 并去除 tracking 参数与 fragment。
- 2026-07-29：运行 `.venv/bin/python -m py_compile scripts/fetch_sources.py scripts/normalize_items.py` 成功；运行 `.venv/bin/python scripts/run_daily.py` 成功，生成 `data/items/2026-07-29.jsonl`、`data/inbox/2026-07-29-brief-input.md`、`data/inbox/2026-07-29-run-summary.md`，并确认 13 条 items 均包含 `source_url` / `canonical_url`。
- 2026-07-28：运行 `.venv/bin/python -m py_compile scripts/fetch_sources.py scripts/check_brief.py scripts/run_daily.py scripts/export_obsidian.py` 成功；运行 `.venv/bin/python scripts/run_daily.py` 成功，生成 `data/items/2026-07-28.jsonl`、`data/inbox/2026-07-28-brief-input.md`、`data/inbox/2026-07-28-run-summary.md`，X 来源保持禁用，公众号草稿和本地 `settings.json` 已被忽略。
- 2026-07-27：运行 `.venv/bin/python -m py_compile scripts/run_daily.py scripts/export_obsidian.py` 成功；运行 `.venv/bin/python scripts/run_daily.py --help` 成功，确认新增 `--export-obsidian` / `--overwrite-obsidian` 参数；使用临时目录作为 `OBSIDIAN_VAULT_PATH` 运行 `.venv/bin/python scripts/run_daily.py --generate-brief --export-obsidian --overwrite-obsidian` 成功导出到临时 Vault；运行 `.venv/bin/python scripts/run_daily.py --generate-brief --export-obsidian --overwrite-obsidian` 成功导出到 iCloud Obsidian `AI Radar/Daily Briefs/2026-07-27-ai-daily-brief.md`，run summary 已记录 Obsidian 导出状态。
- 2026-07-27：运行 `.venv/bin/python scripts/run_daily.py` 成功，默认流程已跳过禁用的 `X AI Watchlist`，没有再出现 X 失败日志或 X 复查提醒；生成 `data/items/2026-07-27.jsonl`、`data/inbox/2026-07-27-brief-input.md`、`data/inbox/2026-07-27-run-summary.md`。
- 2026-07-27：运行 `.venv/bin/python scripts/check_brief.py --date 2026-07-27` 通过；运行 `.venv/bin/python -m py_compile scripts/check_brief.py` 成功；运行 `.venv/bin/python scripts/run_daily.py` 成功生成 `data/items/2026-07-27.jsonl`、`data/inbox/2026-07-27-brief-input.md`、`data/inbox/2026-07-27-run-summary.md`，X 来源因 `402` 失败且不影响主流程。
- 2026-07-27：运行 `.venv/bin/python scripts/export_obsidian.py --help` 成功；运行 `.venv/bin/python -m py_compile scripts/export_obsidian.py` 成功；使用临时目录作为 `OBSIDIAN_VAULT_PATH` 运行 `.venv/bin/python scripts/export_obsidian.py --date 2026-07-21` 成功复制到 `Daily Briefs/2026-07-21-ai-daily-brief.md`；运行 `.venv/bin/python scripts/run_daily.py` 成功生成 `data/items/2026-07-27.jsonl`、`data/inbox/2026-07-27-brief-input.md`、`data/inbox/2026-07-27-run-summary.md`，X 来源因 `402` 失败且不影响主流程；运行 `.venv/bin/python scripts/generate_brief.py --date 2026-07-27 --overwrite` 成功生成今日简报，运行 `.venv/bin/python scripts/export_obsidian.py --date 2026-07-27 --overwrite` 成功导出到 iCloud Obsidian `AI Radar/Daily Briefs/`，运行 `.venv/bin/python scripts/check_brief.py --date 2026-07-27` 通过。
- 2026-07-22：运行 `python3 -m py_compile scripts/fetch_sources.py` 成功；运行 `.venv/bin/python scripts/run_daily.py` 成功生成 `data/items/2026-07-22.jsonl`、`data/inbox/2026-07-22-brief-input.md`、`data/inbox/2026-07-22-run-summary.md`。X 来源未取回数据，run summary 中记录为单来源失败；token 泄露扫描通过。
- 2026-07-21：运行 `.venv/bin/python scripts/run_daily.py --generate-brief --overwrite-brief` 成功，`data/briefs/2026-07-21-ai-daily-brief.md` 已生成，质量检查通过。
