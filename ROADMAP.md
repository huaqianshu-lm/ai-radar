# AI Radar Roadmap

> 用途：快速恢复当前项目上下文。只记录仍影响下一步的状态；已完成和最近验证各最多保留 10 条。

## 当前阶段

- v0 主链路已跑通，当前处于稳定性观察阶段。
- 日常链路包括：固定来源抓取、raw 快照、items JSONL、brief input、可选 Claude Code CLI 简报、质量检查和 Obsidian 导出。
- 简报已增加 Memora 入库判断；符合标准且 raw 完整的候选生成 Memora note，并登记原文与 note 链接。
- `Product Hunt AI` 已接入日常抓取，作为低权重的产品信号来源。
- X API 窄口径接入代码保留，但默认禁用，近期不纳入日常抓取、排查或提醒。
- GitHub Actions 远程抓取工作流已调整为只抓取 raw，并发布到独立 `remote-news` 分支；本地同步后继续 items、brief、Claude Code CLI、Obsidian 和 Memora。

## 已完成

- 2026-08-02：删除简报 Top 5 独立「能力与应用」区块，将模型能力和应用场景并入「摘要」要求，减少重复字段。
- 2026-08-02：简化 Top 5 条目为「发布时间 + 2–4 个要点 + 影响 + 原文链接」，合并重复判断，降低日常扫读成本；质量检查兼容旧格式。
- 2026-08-02：改为 Memora 入库闭环：仅来源充分、raw 完整且判断为“直接入库”的候选生成 Memora note；完成收尾后登记原文与 note 链接。
- 2026-08-01：简报模板增加「Product Hunt 产品信号」独立区块：当天存在 `Product Hunt AI` 候选时，至多 5 条产品均单独呈现，并明确其为低权重社区发现信号；当日简报已补入 4 条候选。
- 2026-08-01：接入 `Product Hunt AI` 官方 GraphQL 公开数据。固定读取 AI 分类近 24 小时精选产品，最多 5 条；Product Hunt 页面保存为 `source_url`，产品官网保存为 `canonical_url`，按 `community=2` 参与既有排序与去重。
- 2026-08-01：统一 GitHub Trending 简报生成规则与质量检查：条目必须带真实 `http(s)` 项目链接；缺少链接的线索不能进入该区块。已清理当日不合格条目并成功导出简报。
- 2026-07-30：确认当日 items 候选较少主要是 14 天历史去重正常生效，而非抓取或 RSS fallback 故障；短期不放宽去重策略。
- 2026-07-29：为 `TLDR AI` 和 `Hugging Face Blog` 增加详情页正文 fallback；RSS 摘要为空或过短时抓正文，单篇失败不影响主流程。
- 2026-07-29：items 新增 `display_summary`，供未来展示卡片使用；`summary` 保持供 brief 判断的完整候选摘要。
- 2026-07-29：完成事件聚类元数据及 brief prompt 兼容：同一 `cluster_key` 优先使用代表项，不物理合并 items。
- 2026-07-29：完成可解释的来源可信度映射与排序接入，不引入 AI 自动评分。
- 2026-07-29：接入 `TLDR AI`、`The Rundown AI` 与 Hacker News AI 发现源，并完成 canonical URL 优先去重。
- 2026-07-27：Obsidian 导出已接入完整流程；`./ai-radar` 可在简报质量检查通过后覆盖同步到配置的独立 Vault。

## 进行中

- 稳定性观察：等待 `TLDR AI` 或 `Hugging Face Blog` 出现新增 item，以确认详情页正文 fallback 对来源贡献统计中平均摘要长度的实际改善。
- 远程 raw 发布、本地继续处理链路和 macOS 本地自动同步任务已完成，远程抓取计划为每天 07:00，待首次 Actions 运行并观察定时日志。

## 下一步

1. 手动运行一次 `Remote news fetch`，确认 `remote-news` 分支出现当天 raw。
2. 在本地运行 `./ai-radar --remote`，确认本地 items、brief、Obsidian 和 Memora 链路继续工作。
3. 观察每天 08:00、16:00 运行的 macOS LaunchAgent 自动同步日志。
4. 观察 `Product Hunt AI` 在日常运行中的候选质量与去重命中，不因单日候选少而扩大时间窗口。
5. 等待 `TLDR AI` 或 `Hugging Face Blog` 出现新增 item，以确认详情页正文 fallback 对来源贡献统计中平均摘要长度的实际改善。

## 阻塞与注意事项

- 不设计 brief input 候选池，不补充近 3～7 天历史 items；`items` 和 brief input 均保持仅当日新增内容。候选不足时，简报应如实说明候选不足。
- 真实多来源事件合并与 newsletter 内原始新闻链接解析均暂不做；当前只保留已有的 canonical URL 去重和 cluster metadata。
- `data/wechat/` 当前被 Git 忽略；若需沉淀发布稿，须先确定存放与版本管理规则。
- 详情页 fallback 已生效，但目标来源在 2026-07-30 没有新增 raw，尚无新 item 级统计证据。
- Memora 入库目前只生成新 note；是否回写已有 wiki、建立 related 双向链接仍由 Memora 收尾工具和 AI 判断决定。

## 最近验证

- 2026-08-10：远程工作流收窄为只抓 raw，并新增 `remote-news` 分支发布、本地同步脚本、远程 raw 本地处理入口和 macOS LaunchAgent；远程抓取调整为每天 07:00，LaunchAgent 每天 08:00、16:00 运行，尚未在 GitHub Actions 上实际运行。
- 2026-08-01：Product Hunt 官方 API Token 与 GraphQL 查询验证成功；近 24 小时获取 4 条 AI 精选产品，标准 `normalize_items.py` 与 `prepare_brief_input.py` 产出中均包含 4 条 `Product Hunt AI` items，且可信度为 2、来源链接和 canonical URL 完整。完整 `run_daily.py` 在本执行器的时限内被中断，未将其标记为成功。
- 2026-08-01：当日简报经 GitHub Trending 链接规则修正后通过质量检查，并成功导出到 Obsidian。
- 2026-08-02：Memora 入库验证成功：2 条候选生成标准 note，更新 `index.md`、`log.md` 和 `知识库总览.md`；总览已记录原文链接 → note 链接，重复执行会跳过已有 note。Memora 全库检查仍有 2 条既有历史 raw 引用错误，不影响本次新 note 结构校验。
- 2026-07-30：`.venv/bin/python scripts/run_daily.py` 成功，生成 items、brief input 和 run summary；扫描 raw 68 个、写入 items 13 条、历史重复过滤 55 条。
- 2026-07-30：复查去重命中，55 个历史重复主要按 URL 命中 2026-07-21 至 2026-07-29 的记录，确认候选不足是预期行为。
- 2026-07-29：`TLDR AI` 与 `Hugging Face Blog` 的详情页正文 fallback 函数级检查成功；抓到的正文长度显著高于短 RSS 摘要。
- 2026-07-29：`.venv/bin/python scripts/run_daily.py --generate-brief --overwrite-brief` 成功；生成简报并通过质量检查，cluster metadata 未造成重复展开。
- 2026-07-29：`fetch_sources.py`、`normalize_items.py`、`prepare_brief_input.py` 的编译和分步流程验证成功；新增字段与聚类字段完整。
- 2026-08-02：完整 `run_daily.py` 在无外网 DNS 的执行环境中退出码为 0，Codex 根据当天 5 条 items 生成简报并通过质量检查，成功生成 4 条入库候选复核项；Claude Code CLI 调用仍因无输出被手动中断。
