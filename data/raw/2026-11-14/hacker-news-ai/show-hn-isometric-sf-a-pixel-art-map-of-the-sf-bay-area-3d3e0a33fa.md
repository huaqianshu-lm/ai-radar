---
title: "Show HN: Isometric SF – A pixel-art map of the SF Bay Area"
url: "https://isometricsf.com/"
source_url: "https://news.ycombinator.com/item?id=50487228"
canonical_url: "https://isometricsf.com/"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-11-13T17:58:37+00:00"
fetched_at: "2026-11-14T02:55:58+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50487228
Original URL: https://isometricsf.com/
Author: juscha1
Score: 161

Technical Write-up:
https://www.justinchavez.com/blog/isometric-sf-how/
Hi HN! Showcasing this fun project. I took 1300 square miles of the SF Bay Area from Google Photorealistic 3D Tiles and transformed them into a cohesive pixel map. It's really fun to explore and stumble upon various famous landmarks like Apple Park, Palace of Fine Arts, or UC Berkeley.
The technicals involve using Nano Banana 2 to train a Qwen-Image-Edit 2511 LoRA which is used to prototype the style and generation methods. For final map I used Qwen to train a Klein 4B LoRA which reproduced the style at 1/4 of the cost. More details in the blog post.
Let me know what you think! I really enjoyed this process of fine-tuning smaller open source models.
If I did the map with Nano Banana 2 it would have cost around 7k USD!
Credit for the idea goes to Isometric NYC.
