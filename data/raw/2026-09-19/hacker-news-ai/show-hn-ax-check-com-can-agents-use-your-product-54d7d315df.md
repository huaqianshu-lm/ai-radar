---
title: "Show HN: Ax-check.com – Can agents use your product?"
url: "https://www.ax-check.com/"
source_url: "https://news.ycombinator.com/item?id=49744416"
canonical_url: "https://www.ax-check.com/"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-09-17T18:08:02+00:00"
fetched_at: "2026-09-19T01:00:30+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49744416
Original URL: https://www.ax-check.com/
Author: 0x63_Problems
Score: 28

I'm the co-founder of Gauge, and I built ax-check.com to quickly test how well coding agents can onboard to your product.
You'll get a scorecard, specific suggested fixes, and three full coding sessions that show how agents read your site and use your product.
I built this because similar checks were too noisy. Most suggested obscure technical changes that don't actually make a difference in agent experience (or AX, hence ax-check.com).
This check starts by using DeepSeek 4.1 Flash to try to find key information about your product, starting from the homepage. In actual agent traffic data, we've seen that the key pages are the homepage, llms.txt, pricing, and the docs site (by traffic volume, and by influence), so we focus on those and ignore the rest. We also find that content negotiation for Markdown is legitimately helpful for agents to complete tasks faster and find what they're looking for, so the scan tests that your key pages can serve Markdown.
The other key piece is that we run actual coding agents in sandboxes, and have them try to onboard to your product. You can see the full trace and watch it happen live (we kick it off fresh when you enter a new site). We surface interesting findings like hallucinated URLs, inaccurate docs instructions, or product confusion.
It also detects whether the agents could complete a fully working onboarding autonomously, without being blocked by a login wall. This is still controversial, but I think finding ways to let agents safely onboard autonomously is going to be table stakes within a year for developer tools in particular.
The whole site is agent-friendly itself! You can generally just talk to your coding agent about ax-check.com and it can do the rest. Would really appreciate any feedback to make this useful.
