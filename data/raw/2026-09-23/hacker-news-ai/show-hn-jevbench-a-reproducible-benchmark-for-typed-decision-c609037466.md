---
title: "Show HN: JevBench, a reproducible benchmark for typed decision models"
url: "https://benchmarkheaven.com/jev-models"
source_url: "https://news.ycombinator.com/item?id=49800574"
canonical_url: "https://benchmarkheaven.com/jev-models"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-09-22T13:01:03+00:00"
fetched_at: "2026-09-23T01:17:54+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49800574
Original URL: https://benchmarkheaven.com/jev-models
Author: florianstandhar
Score: 60

Hi HN! I built JevBench because Jev kicks ass, and the world deserves to know how the serious open source and fake lookalike projects
really
perform in comparison.
Jev-class models return bounded choices and probabilities instead of text, and are disruptively faster and cheaper than LLMs, while being similarly intelligent on the text input they operate on.
JevBench allows looking at accuracy, latency and price all at once, in a weighted way - you can even configure the weighting.
A full run asks 534 English decisions. The v1.3 score combines chance-corrected Intelligence, Calibration, Speed and Cost.
Leaderboard right now:
#1 - Jev            74.4
  #2 - SemIf          73.1
  #3 - djev           73.0
  #4 - Winnow-12B Q8  71.2
  #5 reflex 4B        70.3.
MIT harness, public items, frozen artifacts, scoring code and public per-task outcomes:
https://github.com/fstandhartinger/jevbench
Two no-signup demos:
https://who-is-right.app.mintapis.com
https://is-it-ai-slop.app.mintapis.com
Limitations: English-only; latency from one German server; local/demo latency gets a disclosed ×2 adjustment (+150 ms on my servers) which is an informed assumption; held-out prompts still reach evaluated services; ~1-point gaps can be noise.
Wdyt?
