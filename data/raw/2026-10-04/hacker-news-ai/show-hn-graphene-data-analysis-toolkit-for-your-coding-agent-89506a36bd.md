---
title: "Show HN: Graphene – Data analysis toolkit for your coding agent"
url: "https://github.com/graphene-data/graphene"
source_url: "https://news.ycombinator.com/item?id=49927295"
canonical_url: "https://github.com/graphene-data/graphene"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-10-01T21:29:52+00:00"
fetched_at: "2026-10-04T02:26:47+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49927295
Original URL: https://github.com/graphene-data/graphene
Author: kcmarr
Score: 27

My friend and I have worked at a number of BI companies and thought: Can’t a coding agent do most of this now?
Almost. They just need a context/semantic layer to ensure query correctness and some kind of artifact for publishing findings and visualizations.
We built an open source project called Graphene that provides these tools:
- Semantic layer that’s more token-efficient than YAML, more deterministic than Markdown (eg, composable, callable metric macros), with a query API that’s well in-distribution (SQL).
- MDX-like files for dashboards (Markdown with inlined SQL + HTML components for viz with support for CSS and Javascript)
- Connects to popular data warehouses or local DuckDB
Your coding agent will build really in-depth reports and can ofc leverage any other skills or context that you've made available to it. We dogfood it inside a monorepo with our website, app source code, planning docs, etc so the agent has access to a ton of context. It’s also nice that the agent can add instrumentation, adjust pipelines and transformations, and add dashboards all in one PR.
If you want to try it out, just point your coding agent at
https://github.com/graphene-data/graphene/blob/main/docs/set...
and ask it to set up Graphene.
If you don’t have data to play with, you can clone our example project:
1. `git clone <
https://github.com/graphene-data/example-flights.git`
>
2. `cd example-flights && npm install`
Would love any/all feedback!
