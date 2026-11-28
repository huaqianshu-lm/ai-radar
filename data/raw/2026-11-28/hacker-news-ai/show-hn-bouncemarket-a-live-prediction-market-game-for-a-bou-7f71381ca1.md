---
title: "Show HN: bouncemarket – a live prediction market game for a bouncing ball"
url: "https://bouncemarket.minhanhday.com/"
source_url: "https://news.ycombinator.com/item?id=50667726"
canonical_url: "https://bouncemarket.minhanhday.com/"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-11-27T15:01:50+00:00"
fetched_at: "2026-11-28T04:34:54+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50667726
Original URL: https://bouncemarket.minhanhday.com/
Author: mday404
Score: 341

a ball will fall. trade on where it lands.
I made this game! Some technical details:
The entire drop of the ball is simulated server-side, then streamed to each client as server-sent events with a small buffer. Every drop is deterministic from its starting position, so rounds can be replayed exactly for later analysis, but tiny variations in starting position can change the ultimate outcome.
There's some AI traders to keep the market moving, but they drop out in any round that has more than five people. They operate using a naive set of rules that I wrote for them, so they're not too hard to beat -- it's when the market is full of real people that it gets tricky.
Curious to get feedback on anything you would change, and especially whether the mechanics were clear right away or not.
