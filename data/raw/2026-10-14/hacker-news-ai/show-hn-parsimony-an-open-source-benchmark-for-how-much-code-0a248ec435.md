---
title: "Show HN: Parsimony – an open-source benchmark for how much code AI models add"
url: "https://parsimony.lasu.dev/"
source_url: "https://news.ycombinator.com/item?id=50077619"
canonical_url: "https://parsimony.lasu.dev/"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-10-13T19:50:31+00:00"
fetched_at: "2026-10-14T01:40:08+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50077619
Original URL: https://parsimony.lasu.dev/
Author: lasu
Score: 48

Existing benchmarks measure solve rate and token output/cost, but don't punish excess code, which makes a codebase harder to work with in the long term. I wanted to measure this since it matters most for long-term projects.
Method: it takes the patches that benchmarks already publish (DeepSWE, SWE-bench Verified, SWE-bench Live) and counts "coding units": syntax elements like statements, calls, names and literals. I didn't use lines of code, so cramming code isn't rewarded. Deleted code is subtracted, so it measures net units.
GPT-6 and Claude 5.5 have no public patches yet, so I ran them myself on 3–10 tasks on my own subscriptions (shown as faded circles, not ranked).
Any feedback or model contributions are welcome, especially public patch exports for newer models.
GitHub:
https://github.com/La5u/Parsimony
Not affiliated with any of the benchmarks.
