---
title: "Show HN: Running 104GB Qwen3.8-Flash-Next on 48GB Mac with at ~12 tok/s"
url: "https://github.com/carloslfu/slotstream"
source_url: "https://news.ycombinator.com/item?id=49524447"
canonical_url: "https://github.com/carloslfu/slotstream"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-09-01T16:42:46+00:00"
fetched_at: "2026-09-02T00:52:16+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49524447
Original URL: https://github.com/carloslfu/slotstream
Author: carloslfu
Score: 138

I built slotstream, a way to run Qwen3.8-Flash-Next 4-bit on a low-memory mac starting from 16GB, a 125B parameter model that would need 100GB+ memory/RAM, thanks to expert-offloading/ssd-streaming. Easy to install/update, and mac-native using MLX and Swift.
It ships with auto-mode, which makes a good tradeoff between memory usage and speed. I'll be implementing and porting the MTP module for speculative decoding next
