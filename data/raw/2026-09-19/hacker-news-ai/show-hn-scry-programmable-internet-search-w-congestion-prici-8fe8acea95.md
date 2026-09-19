---
title: "Show HN: Scry, programmable internet search w/ congestion pricing"
url: "https://scry.io/"
source_url: "https://news.ycombinator.com/item?id=49748041"
canonical_url: "https://scry.io/"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-09-17T23:15:57+00:00"
fetched_at: "2026-09-19T01:00:30+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49748041
Original URL: https://scry.io/
Author: Xyra
Score: 43

Meet Scry, a 500 TB NVMe internet index in ClickHouse that you can run ~arbitrary readonly SQL and some of Datalog over, and I handle the problem of resource-contention with congestion-based micro-auction pricing. When there's capacity, the service is free for non-commercial use.
---
Hello. It's 2026, we're training simulated fruit fly brains to play Beat Saber, do we still have to be stuck with internet (re)search as fn: natural language -> black box we can't do anything about -> ranked_list/summary?
There is a long history of people trying to do very fancy things that end up being done in relational databases and a little SQL. There is a gravity to them, a bitter lesson, just like scaling of generalized ml training methods. I mean many, many information products can be built off essentially giant real-time OLAP databases and frontier LLMs writing brilliant SQL+Datalog+vector+Jev etc. queries.
Google Search, Tavily, Exa essentially have the problem of
mapping
your agents' context you are willing to provide, to a tiny subset of their index. You pay a fixed cost to an extremely hard problem that has a distribution of hardness, which means YOU eat the downsides when they are running out of budgeted compute to help you out.
Their algorithms are opaque to the caller, there's really not much user control, and there's not a serious opportunity to communally improve search recipes, like the lexical+Jev recipes you trust to select bleeding edge AI builders.
Furthermore, search companies aren't even pursuing text-to-SQL anymore (several have talked to me)... they made up their minds during the traumatic 2024 text-to-sql days. They were just too early.
I hope you enjoy. I'm intent on scaling this paradigm on differentiated hardware over much more data, so any compelling use cases or queries I could show off, would be much appreciated!
