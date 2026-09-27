---
title: "Turning GLM-5.3-Flash into a Jev-like decision model"
url: "https://www.privatemode.ai/blog/system-one-from-glm-flash"
source_url: "https://news.ycombinator.com/item?id=49857656"
canonical_url: "https://www.privatemode.ai/blog/system-one-from-glm-flash"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-09-26T15:49:04+00:00"
fetched_at: "2026-09-27T01:08:10+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49857656
Original URL: https://www.privatemode.ai/blog/system-one-from-glm-flash
Author: flxflx
Score: 13

We found an approach to get Jev-like properties from standard LLMs like GLM-5.3-Flash.
The core idea is to craft the input prompt so that the first output token answers the question. This makes it possible to get a decision with a single forward pass.
In the blog post, we describe the approach in detail for GLM-5.3-Flash and vLLM. We benchmark this setup against Jev and Laya. We find that our setup is on-par with Jev in terms of accuracy and speed and that it substantially outperforms Laya.
Still, in terms of costs per decision, Jev is several x better than our setup. In turn, our setup supports vision inputs.
