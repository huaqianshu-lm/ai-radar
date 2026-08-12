# AI Radar 前端数据输出任务

接下来 AI-radar 不再参与前端页面设计。

AI-radar 的职责只保留在数据侧：

```text
抓取
↓
清洗
↓
去重
↓
整理
↓
输出稳定的前端数据
```

页面设计和前端视觉由另外的设计工具负责。

## 一、这次任务目标

请基于 AI-radar 当前真实项目、真实数据文件和真实字段，设计一个：

**最小、稳定、专门供前端页面消费的数据结构。**

不要根据页面效果反推复杂字段，也不要参与页面布局、视觉、CSS、组件等设计。

目标是让前端工具只需要读取一份标准数据，就可以独立完成页面。

---

## 二、当前前端真正需要的数据

第一版页面非常简单，每条新闻只展示：

```text
标题
短摘要
来源 · 来源类型 · 时间
```

点击新闻后打开原文。

因此目前前端最核心的数据只有：

- 新闻唯一标识
- 标题
- 短摘要
- 来源名称
- 来源类型
- 统一显示时间
- 时间来源类型
- 原文链接

现有项目中可能对应：

```text
title
display_summary
source
source_type
published_at
fetched_at
canonical_url
```

请先检查真实项目，不要假设字段一定完全如此。

---

## 三、时间处理规则

抓取阶段优先读取来源自身提供的发布时间。普通文章页依次尝试：

```text
JSON-LD datePublished
→ meta article:published_time
→ time[datetime]
```

如果都不存在，保持内部 `published_at` 为空，由 `fetched_at` 记录实际抓取时间。GitHub Trending 等没有文章发布时间的来源同样只记录 `fetched_at`。

前端输出层统一生成：

```text
display_time
time_type
```

- 有真实 `published_at`：`display_time = published_at`，`time_type = published`
- 没有真实发布时间：`display_time = fetched_at`，`time_type = fetched`
- `display_time` 统一为 ISO 8601 UTC 格式

前端使用 `display_time` 显示和排序，并根据 `time_type` 区分真实发布时间与收录时间，不能把抓取时间显示成发布时间。

标题与摘要的语言规则：

- 前端输出的 `title` 和 `summary` 必须是中文
- 产品名、模型名、机构名和必要的技术缩写可以保留原文
- 应清理 newsletter 问候语、模板变量、抓取标签和链接堆叠等无关内容
- 只能翻译和整理真实候选材料，不得补写材料中没有提供的事实
- `source` 和 `url` 继续保留真实来源信息

---

## 四、不要直接让前端依赖内部 items JSONL

现有 `items JSONL` 属于 AI-radar 内部数据结构。

前端最好不要直接依赖它。

建议增加一个很薄的“前端数据输出层”：

```text
AI-radar 内部数据
        ↓
前端数据转换
        ↓
frontend-data.json
        ↓
前端页面
```

这样以后 AI-radar 内部即使调整：

- raw 数据结构
- 聚类逻辑
- 摘要生成方式
- 内部评分
- category
- cluster
- 其他处理字段

只要前端数据结构保持稳定，页面就不需要跟着修改。

---

## 五、前端数据尽量保持简单

可以参考类似结构：

```json
{
  "date": "2026-08-11",
  "items": [
    {
      "id": "xxx",
      "title": "OpenAI 发布新的模型能力",
      "summary": "新版本进一步提升代码生成、工具调用以及长任务处理能力。",
      "source": "OpenAI News",
      "source_type": "official",
      "display_time": "2026-08-11T02:43:00Z",
      "time_type": "published",
      "url": "https://..."
    }
  ]
}
```

这里只是结构参考。

请先根据真实项目判断最终字段。

如果有必要，可以把内部字段：

```text
display_summary
canonical_url
```

在前端输出层转换成更简洁的：

```text
summary
url
```

这样前端不需要理解 AI-radar 内部字段命名。

---

## 六、source_type

请检查当前真实数据中：

```text
source_type
```

到底有哪些实际值。

例如可能存在：

```text
official
media
community
newsletter
research
```

但不要根据这里的示例新增不存在的类型。

请输出：

1. 当前真实 `source_type` 枚举值。
2. 每种类型大概有多少数据。
3. 是否存在为空、命名不统一或无法直接用于前端过滤的情况。

前端后续会根据这些真实值设计来源过滤。

---

## 七、当前暂时不需要提供给前端的字段

以下内容属于 AI-radar 内部逻辑，第一版前端暂时不需要：

```text
credibility_score
cluster_size
is_list_page
importance_score
relevance_score
category
should_archive
should_write
reason
raw_path
cluster_key
cluster_basis
cluster_rank
```

除非检查真实项目后发现某个字段是前端正常运行所必需，否则不要加入第一版前端数据结构。

原则是：

**能少就少。**

---

## 八、需要你完成的工作

请先只读检查真实项目，然后完成以下内容：

### 1. 检查现有数据

确认：

- items JSONL 实际路径
- 实际字段
- 每日数据如何组织
- `source_type` 实际值
- 时间字段格式
- `canonical_url` 的存在情况
- 是否已经存在稳定 ID
- 是否存在空标题、空摘要、空链接等异常情况

### 2. 设计最小前端数据结构

要求：

- 字段尽量少
- 命名清晰
- 前端容易使用
- 与 AI-radar 内部结构解耦
- 后续可以长期稳定使用

### 3. 给出一份真实示例数据

不要手写假数据。

请从当前项目真实抓取结果中选择若干条，转换成新的前端数据格式，方便后续交给设计工具。

### 4. 给出输出方案

说明未来 AI-radar 每次运行后，如何生成前端数据。

例如：

```text
data/frontend/latest.json
```

或者：

```text
data/frontend/2026-08-11.json
```

具体目录和命名请结合当前项目现有结构判断，不要为了这个功能大规模调整项目目录。

---

## 九、当前先不要做的事情

这一步不要：

- 设计网页
- 写 HTML
- 写 CSS
- 设计组件
- 决定页面颜色
- 决定页面布局
- 做 Dashboard
- 做每日简报页面
- 做 Product Hunt 专区
- 做 GitHub Trending 专区
- 做新闻详情页
- 增加新的 AI 分类逻辑

这些属于后续其他工具的工作。

AI-radar 这里只负责：

> **稳定地把新闻数据提供出来。**

---

## 十、最终希望得到的结果

请最终给我：

1. 当前真实数据情况的简短审计结果。
2. 推荐的前端数据结构。
3. 字段说明。
4. `source_type` 的真实枚举情况。
5. 一份基于真实数据生成的示例 JSON。
6. 推荐的数据输出路径和生成方式。
7. 如果需要修改项目，列出最小修改范围。

先给方案，不要直接做大规模代码修改。

整体原则：

> AI-radar 是数据生产者，前端设计工具是数据消费者，两者尽量解耦。
