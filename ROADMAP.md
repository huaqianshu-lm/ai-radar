# AI Radar Roadmap

## 当前阶段

v0 主链路已跑通，进入稳定性修复阶段。X API 窄口径来源接入代码暂时保留，但 X 抓取已从默认日常流程中收起，近期不再排查或运行。

已具备：固定来源配置、公开来源抓取、raw 快照、items JSONL、brief input、可选 Claude Code CLI 生成每日简报、每日简报本地导出到 Obsidian、公众号草稿生成。

暂时收起：X API recent search 固定来源接入，代码保留但默认禁用，近期不再纳入日常抓取、问题排查或提醒。

## 最近有效进度

- 2026-07-30：完成默认流程下候选不足原因观察，确认 `data/items/2026-07-30.jsonl` 只有 13 条主要是正常的 14 天历史去重效果，不是抓取失败或 RSS fallback 失效；当天 raw 68 个中 55 个被历史去重过滤，过滤基本按 URL 命中历史记录，`TLDR AI`、`The Rundown AI`、`Hugging Face Blog`、官方博客和 GitHub Trending 等来源当天候选大多已在 2026-07-21 至 2026-07-29 期间进入过 raw/items。当前不建议立刻放宽 items 去重，否则会把旧新闻重新推入 brief input；后续更合理的方向是单独设计 brief input 候选池策略，而不是改 raw append-only 或 items 去重语义。
- 2026-07-30：完成 Phase 7 第二小步的次日 fresh run 观察，默认流程成功生成 `data/items/2026-07-30.jsonl`、`data/inbox/2026-07-30-brief-input.md` 和 `data/inbox/2026-07-30-run-summary.md`；本次 `TLDR AI` / `Hugging Face Blog` 抓取成功但新增 raw 均为 0，候选被 14 天历史去重过滤，未进入当日来源贡献统计，因此本次只能确认主流程无异常和短摘要提醒消失，不能作为目标来源平均摘要长度已改善的直接证据。
- 2026-07-29：完成 Phase 7 第二小步 RSS 摘要质量修复，给 `TLDR AI` 和 `Hugging Face Blog` 显式开启 `fetch_article_content: true`，当 RSS entry 摘要为空或过短时回退抓取详情页正文；单篇失败只记录日志，不影响来源和主流程；未全局开启 RSS 全文抓取、未拆 TLDR newsletter、未引入 AI 摘要。
- 2026-07-29：完成 Phase 7 第一小步前端展示短摘要字段，`items` 新增 `display_summary`，由 raw 正文确定性截断生成，作为未来前端新闻卡片展示用短摘要；`summary` 保持原有 brief 判断用途和约 500 字符上限，不改 brief 结构、不做前端、不引入 AI 摘要。
- 2026-07-29：完成 Phase 6 第三小步实际简报验证，使用当前 cluster metadata prompt 生成 `data/briefs/2026-07-29-ai-daily-brief.md`，质量检查通过；本次 items 写入 152 条，cluster 总数 152、multi-item cluster 0、max cluster size 1，因此实际输出主要验证了 prompt 兼容性和无重复展开退化问题，尚未覆盖多条目 cluster 的真实合并表达。
- 2026-07-29：完成 Phase 6 第二小步 brief prompt 使用 cluster metadata，提示生成简报时同一 `cluster_key` 不重复展开，优先使用 `cluster_rank: 0` 的代表项，其他同 cluster 条目只作为辅助证据；仍不物理合并 items、不改变 JSONL 行数、不改变最终 brief 结构。
- 2026-07-29：完成 Phase 6 第一小步事件聚类元数据，`items` 逐条新增 `cluster_key`、`cluster_basis`、`cluster_size`、`cluster_rank`，仅用于观察同一事件候选，不物理合并、不减少 JSONL 行数、不改 brief prompt、不做跨天聚类或 AI 聚类；run summary 新增「事件聚类观察」区块，记录 cluster 总数、多条目 cluster 数和最大 cluster size。
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

- `TLDR AI` / `Hugging Face Blog` 已启用详情页正文 fallback，2026-07-30 默认流程短摘要提醒已消失；但这两个来源当天新增 raw 均为 0，候选被 14 天历史去重过滤，仍需等它们实际产生新 item 后再确认来源贡献统计中的平均摘要长度。
- 2026-07-30 当天 items 只有 13 条，经检查主要是 14 天历史去重正常生效：68 个 raw 中 55 个命中历史重复，绝大多数按 URL 命中，不是抓取失败；短期不建议放宽 items 去重把旧内容重新送入 brief input。
- `data/wechat/` 已按当前策略加入忽略，不纳入版本管理；如后续要沉淀公众号发布稿，需要重新确认存放和提交规则。
- 公众号草稿生成没有出现在 2026-07-21 run summary 中，需要后续确认是否仍纳入自动流程。

## 下一步

1. 等待用户确认是否提交 Phase 7 改动。
2. 如确认继续，下一小步建议先讨论并设计 brief input 候选池策略：保持 `items` 只代表当日新增内容，同时考虑在候选不足时是否从近 3～7 天高质量历史 items 中补充一个单独的“近期仍可参考候选”区块，避免日更来源重复刷屏，也避免当天新增过少导致简报素材不足。

## 最近验证

- 2026-07-30：分析 `data/raw/2026-07-30/` 与 `data/items/2026-07-30.jsonl` 的来源分布和历史重复命中，确认当天 raw 68 个、items 13 条，过滤掉的 55 个候选主要按 URL 命中 2026-07-21 至 2026-07-29 历史 raw；`TLDR AI` 5/5、`The Rundown AI` 16/16、`Hugging Face Blog` 5/5、多数官方博客和 GitHub Trending 候选均为历史重复，进入 items 的主要是 `Hacker News AI` 5 条、`Simon Willison` 4 条、`OpenAI News` 3 条、`Latent Space` 1 条。结论是候选不足主要来自去重策略正常生效，暂不建议放宽 items 去重。
- 2026-07-30：运行 `.venv/bin/python scripts/run_daily.py` 成功，生成 `data/items/2026-07-30.jsonl`、`data/inbox/2026-07-30-brief-input.md` 和 `data/inbox/2026-07-30-run-summary.md`；本次扫描 raw 68 个、写入 items 13 条、历史重复过滤 55 条，`Hacker News AI` 新增 raw 2 条；`TLDR AI` / `Hugging Face Blog` 抓取均成功但新增 raw 0 条，且未进入来源贡献统计，run summary 今日提醒为“今日无明显异常”，说明默认流程已不再提示这两个来源摘要偏短，但仍需等目标来源产生新 item 后确认平均摘要长度。
- 2026-07-29：运行 `.venv/bin/python -m py_compile scripts/fetch_sources.py` 成功；内存级验证 `fetch_source()` 显示 `Hugging Face Blog` 5 条内容长度分别为 11951、7612、9082、36382、15885，`TLDR AI` 5 条内容长度分别为 6833、5073、6287、7148、4673，确认详情页正文 fallback 生效且 TLDR 仍保持一期 newsletter 一个 item；运行 `.venv/bin/python scripts/run_daily.py` 成功，因当天目标 URL 旧 raw 已存在且 raw 只追加不覆盖，本次新增 raw 0 条，run summary 中 TLDR AI / Hugging Face Blog 的 `avg summary chars` 仍沿用旧 raw 统计，需要下一天 fresh raw 继续观察；字段复查确认 156 条 items 均包含 `summary`、`display_summary` 和 cluster metadata。
- 2026-07-29：运行 `.venv/bin/python -m py_compile scripts/normalize_items.py` 成功；运行 `.venv/bin/python scripts/normalize_items.py --date 2026-07-29` 和 `.venv/bin/python scripts/prepare_brief_input.py --date 2026-07-29` 成功，字段检查确认 152 条 items 均包含 `summary` 和 `display_summary`，`summary` 最大长度 503、`display_summary` 最大长度 163，cluster metadata 无缺失；运行 `.venv/bin/python scripts/run_daily.py` 成功，本次新增 4 个 raw，`data/items/2026-07-29.jsonl` 写入 156 条，复查确认 156 条 items 均包含 `display_summary`，run summary 正常生成且摘要偏短提醒仍基于 `summary`。
- 2026-07-29：运行 `.venv/bin/python scripts/run_daily.py --generate-brief --overwrite-brief` 成功，生成 `data/briefs/2026-07-29-ai-daily-brief.md`，质量检查通过；本次新增 1 个 HN raw，`data/items/2026-07-29.jsonl` 写入 152 条，去重统计为 4 条当日重复、66 条历史重复，run summary 显示 cluster 总数 152、multi-item cluster 0、max cluster size 1；人工抽查简报结构正常，未出现 cluster 字段暴露或同一 cluster 重复展开问题。
- 2026-07-29：运行 `.venv/bin/python scripts/prepare_brief_input.py --date 2026-07-29` 成功；检查确认 `data/inbox/2026-07-29-brief-input.md` 包含 `cluster_key`、`cluster_rank: 0`、`cluster_size` 以及“同一 `cluster_key` 的条目不要重复展开”规则；运行 `.venv/bin/python scripts/run_daily.py` 成功，items 写入 151 条，去重统计为 4 条当日重复、66 条历史重复，brief input 和 run summary 均正常生成。
- 2026-07-29：运行 `.venv/bin/python -m py_compile scripts/normalize_items.py scripts/run_daily.py` 成功；运行 `.venv/bin/python scripts/normalize_items.py --date 2026-07-29` 和 `.venv/bin/python scripts/prepare_brief_input.py --date 2026-07-29` 成功；字段检查确认 148 条 items 均包含 `cluster_key`、`cluster_basis`、`cluster_size`、`cluster_rank`，无空 cluster 字段，rank 无异常，当时 cluster 总数 148、multi-item cluster 0、max cluster size 1；运行 `.venv/bin/python scripts/run_daily.py` 成功，新增 3 个 raw 后 `data/items/2026-07-29.jsonl` 写入 151 条，去重统计为 4 条当日重复、66 条历史重复，run summary 正常生成「事件聚类观察」区块，复查确认 151 条 items 均有 cluster metadata，cluster 总数 151、multi-item cluster 0、max cluster size 1。
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
