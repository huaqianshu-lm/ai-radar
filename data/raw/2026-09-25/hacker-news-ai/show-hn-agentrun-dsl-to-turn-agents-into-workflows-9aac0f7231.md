---
title: "Show HN: AgentRun: DSL to turn agents into workflows"
url: "https://github.com/Parcha-ai/agentrun"
source_url: "https://news.ycombinator.com/item?id=49821438"
canonical_url: "https://github.com/Parcha-ai/agentrun"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-09-23T19:42:58+00:00"
fetched_at: "2026-09-25T01:12:09+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49821438
Original URL: https://github.com/Parcha-ai/agentrun
Author: miguelrios
Score: 39

Hi HN,
I just open sourced the DSL that our harness in grep.ai uses to turn repeatable parts of agent work into workflows. You can combine tool calls, code, Jev-powered system one decisions for things like routing and screening evidence, and agents when a step needs more investigation.
Our harness uses the traces and retro notes agents leave behind when doing a job to figure out which parts can become a workflow. The idea is to make the work easier to understand and avoid paying for a full agent loop where one isn’t needed.
For example, a research workflow can split a question into subquestions, send agents to research them in parallel, use Jev to screen the evidence, and have another agent write the report. You can inspect the steps, evaluate the evidence screening separately, or change one agent without rebuilding everything.
The DSL and examples are in our GitHub. There’s a scripted demo you can run without API keys:
https://github.com/Parcha-ai/agentrun
You can also use it as a Pi extension to build, inspect, and run workflows:
https://github.com/Parcha-ai/agentrun#use-it-in-pi
I would love to hear if this is useful to others.
More background on how AgentRun works in this video:
https://www.youtube.com/watch?v=vOVhtGjtwpg
. Or read about our use cases in this article:
https://x.com/MiguelriosEN/status/2101029313906987422
.
