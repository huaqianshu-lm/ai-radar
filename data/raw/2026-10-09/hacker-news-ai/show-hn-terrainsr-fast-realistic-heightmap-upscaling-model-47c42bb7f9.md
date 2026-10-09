---
title: "Show HN: TerrainSR – fast, realistic heightmap upscaling model"
url: "https://huggingface.co/joe-gibbs/terrainsr"
source_url: "https://news.ycombinator.com/item?id=49986740"
canonical_url: "https://huggingface.co/joe-gibbs/terrainsr"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-10-07T01:24:17+00:00"
fetched_at: "2026-10-09T02:49:33+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49986740
Original URL: https://huggingface.co/joe-gibbs/terrainsr
Author: joegibbs
Score: 30

This is a model that I made for a historical game. I wanted to have a 1:1 scale model of Europe, but my problem was that 100m data was too low-res while 10m LIDAR data was patchy, took hundreds of GBs to store and was full of manmade objects like mines, buildings and so on.
I trained this model on undeveloped landscape so that it can quickly add plausible erosion features, rocks, etc to the low-resolution height data and sort of reconstruct what the terrain would look like before any human interference.
