# AI Radar Roadmap

> 用途：快速恢复当前项目上下文。只记录仍影响下一步的状态；已完成和最近验证各最多保留 10 条。

## 当前阶段

- 原 v0 范围已结束，项目进入前端接入与自动发布阶段；现有前端将放入同一仓库的 `web/`。
- 目标链路为 GitHub Actions 每日抓取和处理数据、Gemini 自动生成中文标题摘要、前端读取 `latest.json`，并发布到 Cloudflare Pages。
- 前端数据输出契约、中文标题摘要和时间显示规则已确定；自动翻译导出、普通网页发布时间提取和前端动态加载尚未实现。
- 简报已增加 Memora 入库判断；符合标准且 raw 完整的候选生成 Memora note，并登记原文与 note 链接。
- 当前线上发布平台确定为 Cloudflare Pages，但尚未创建或修改任何 Cloudflare 配置。

## 已完成

- 2026-08-12：更新项目范围，允许同仓库 `web/` 前端、Gemini 中文翻译、GitHub Actions 每日数据处理和 Cloudflare Pages 静态部署；原 v0 约束作废。
- 2026-08-11：基于当日 35 条真实 items 生成 `data/frontend/latest.json`，按稳定的 8 字段契约输出中文标题和中文短摘要，并区分真实发布时间与收录时间。
- 2026-08-11：统一发布时间与前端显示规则：普通文章页后续按 JSON-LD、文章 meta、`time[datetime]` 顺序提取发布时间；前端通过 `display_time` 和 `time_type` 区分真实发布时间与收录时间。
- 2026-08-11：按实际 Memora 入库链路修正 v0 范围规则：自动新增合格 note 并更新索引、日志和知识库总览，同时运行关联 note / wiki 更新建议；不自动改写已有 note / wiki、不自动写回 `related`，也不更新 `data/tracking/`。
- 2026-08-11：修正 GitHub Trending 候选不足说明的质量检查误判；检查器改为在对应区块识别“候选不足”，当日简报已重新通过检查并导出到 Obsidian。
- 2026-08-02：删除简报 Top 5 独立「能力与应用」区块，将模型能力和应用场景并入「摘要」要求，减少重复字段。
- 2026-08-02：简化 Top 5 条目为「发布时间 + 2–4 个要点 + 影响 + 原文链接」，合并重复判断，降低日常扫读成本；质量检查兼容旧格式。
- 2026-08-02：改为 Memora 入库闭环：仅来源充分、raw 完整且判断为“直接入库”的候选生成 Memora note；完成收尾后登记原文与 note 链接。
- 2026-08-01：简报模板增加「Product Hunt 产品信号」独立区块：当天存在 `Product Hunt AI` 候选时，至多 5 条产品均单独呈现，并明确其为低权重社区发现信号；当日简报已补入 4 条候选。
- 2026-08-01：接入 `Product Hunt AI` 官方 GraphQL 公开数据。固定读取 AI 分类近 24 小时精选产品，最多 5 条；Product Hunt 页面保存为 `source_url`，产品官网保存为 `canonical_url`，按 `community=2` 参与既有排序与去重。

## 进行中

- 等待将现有前端项目移入 `web/`，确认其技术栈、构建命令和当前示例数据位置。
- 设计每日云端数据链路，保留最近 14 天历史 items 用于去重，并通过翻译缓存减少 Gemini API 调用。
- 原远程工作流仍只发布 raw 到 `remote-news`；在用户确认 CI/CD 改动前不调整。

## 下一步

1. 将现有前端代码放入 `web/`，检查技术栈、构建命令和写死数据的位置。
2. 改造前端读取 `/data/latest.json`，并补齐加载中、加载失败和空数据状态。
3. 实现普通文章页发布时间提取、Gemini 中文翻译缓存，以及日期归档、索引和 `latest.json` 自动导出。
4. 单独确认后调整 GitHub Actions，使其每日恢复历史数据、处理新增内容、构建前端并准备部署产物。
5. 按 Cloudflare 操作约束逐步确认并创建 Pages 项目、配置部署凭据、执行首次发布。

## 阻塞与注意事项

- 现有前端代码尚未进入当前仓库，其技术栈和构建方式待检查；在此之前不确定具体迁移改动。
- GitHub Actions 属于 CI/CD 配置，修改前必须单独说明改动与风险并取得确认。
- Cloudflare Pages 尚未配置；绑定仓库、设置环境变量和首次生产部署必须逐步取得确认。
- Gemini 免费额度和 Cloudflare 免费套餐均属于外部平台政策，实施时需重新核对；自动化失败必须保留上一版有效页面与数据。
- 不设计 brief input 候选池，不补充近 3～7 天历史 items；`items` 和 brief input 均保持仅当日新增内容。候选不足时，简报应如实说明候选不足。
- 真实多来源事件合并与 newsletter 内原始新闻链接解析均暂不做；当前只保留已有的 canonical URL 去重和 cluster metadata。

## 最近验证

- 2026-08-11：`data/frontend/latest.json` 通过 JSON 解析、字段完整性和中文内容检查，共 35 条；22 条为 `published`，13 条为 `fetched`，全部具有稳定 ID、中文标题、中文摘要、来源、显示时间和原文链接。
- 2026-08-11：只读审计当日 35 条 items，22 条具有真实发布时间，13 条来自普通网页或 GitHub Trending、仅有抓取时间；项目规则、前端数据任务和页面显示参考已统一对应处理方式。
- 2026-08-11：核对 `scripts/archive_notes.py` 与 Memora `tools/finalize_ingest.py`，确认自动链路会新增 note、重建索引、补写日志、刷新知识库总览并生成关联 / wiki 建议，但不会自动改写已有 note / wiki 或写回 `related`。
- 2026-08-11：当日简报中的「今日 GitHub Trending 候选不足」说明可被质量检查正确识别；缺少说明的反例仍会失败。简报质量检查通过，Obsidian 导出文件与项目简报内容一致。
- 2026-08-10：远程工作流收窄为只抓 raw，并新增 `remote-news` 分支发布、本地同步脚本、远程 raw 本地处理入口和 macOS LaunchAgent；远程抓取调整为每天 07:00，LaunchAgent 每天 08:00、16:00 运行，尚未在 GitHub Actions 上实际运行。
- 2026-08-01：Product Hunt 官方 API Token 与 GraphQL 查询验证成功；近 24 小时获取 4 条 AI 精选产品，标准 `normalize_items.py` 与 `prepare_brief_input.py` 产出中均包含 4 条 `Product Hunt AI` items，且可信度为 2、来源链接和 canonical URL 完整。完整 `run_daily.py` 在本执行器的时限内被中断，未将其标记为成功。
- 2026-08-01：当日简报经 GitHub Trending 链接规则修正后通过质量检查，并成功导出到 Obsidian。
- 2026-08-02：Memora 入库验证成功：2 条候选生成标准 note，更新 `index.md`、`log.md` 和 `知识库总览.md`；总览已记录原文链接 → note 链接，重复执行会跳过已有 note。Memora 全库检查仍有 2 条既有历史 raw 引用错误，不影响本次新 note 结构校验。
- 2026-07-30：`.venv/bin/python scripts/run_daily.py` 成功，生成 items、brief input 和 run summary；扫描 raw 68 个、写入 items 13 条、历史重复过滤 55 条。
- 2026-07-30：复查去重命中，55 个历史重复主要按 URL 命中 2026-07-21 至 2026-07-29 的记录，确认候选不足是预期行为。
