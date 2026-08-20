---
title: "Show HN: I trained a 125M model to autocomplete piano on-device"
url: "https://simedw.com/2026/08/20/midi-autocomplete/"
source_url: "https://news.ycombinator.com/item?id=49373456"
canonical_url: "https://simedw.com/2026/08/20/midi-autocomplete/"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-08-20T12:04:38+00:00"
fetched_at: "2026-08-20T23:26:42+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49373456
Original URL: https://simedw.com/2026/08/20/midi-autocomplete/
Author: simedw
Score: 471

I trained a 125M-parameter transformer to autocomplete piano performances in real time (~108 notes/sec on an iPhone 15).
The idea is basically GitHub Copilot or Tabnine, except instead of prompting it with code, you prompt it by playing a few notes on a MIDI piano. The model then continues what you played, entirely on-device.
The app is free if anyone wants to try it. Happy to answer questions about the model, training, Core ML, or the many things that didn't work.
