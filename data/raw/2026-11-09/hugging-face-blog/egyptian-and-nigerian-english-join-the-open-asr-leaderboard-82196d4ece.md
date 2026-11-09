---
title: "Egyptian and Nigerian English join the Open ASR Leaderboard"
url: "https://huggingface.co/blog/open-asr-leaderboard-liva"
source_url: "https://huggingface.co/blog/open-asr-leaderboard-liva"
canonical_url: "https://huggingface.co/blog/open-asr-leaderboard-liva"
source: "Hugging Face Blog"
source_type: "developer"
published_at: "2026-11-06T00:00:00+00:00"
fetched_at: "2026-11-09T02:25:51+00:00"
content_type: "markdown"
is_list_page: false
---

#### RW-Voice EQ ASR

Explore and compare English speech‑recognition model performance

A few months ago, we added private data to the Open ASR Leaderboard: 11 splits from Appen and DataOceanAI covering scripted and conversational speech from five accents (blog). The community response was great, with many **highlighting the importance of held-out sets for trustworthy evaluations**. Since then, we added one more private split for Indian-accented English with Voice Arena (blog).

We’re excited to announce a new collaboration with Liva AI to add even more private data with two new accents: **Egyptian** 🇪🇬 and **Nigerian** 🇳🇬.

| Dataset | Accent | Duration \[h\] | Style | Transcription | 
|---|---|---|---|---|
| Liva AI Conversational EG | Egyptian | 1.34 | Conversational, spontaneous | Punctuated, cased, with disfluencies. | 
| Liva AI Conversational NG | Nigerian | 1.55 | Conversational, spontaneous | Punctuated, cased, with disfluencies. | 

This is part of our continued effort to improve representation in ASR evals (more accents and more languages) and to improve trust (new private data to minimize benchmaxxing, and new data providers). We’re excited to see the community continuing to push ASR performance for the world 🤗

With these new accents, we can now present a richer breakdown of accents, based on Kachru’s Three Circles (kudos to Hume AI for this idea in their leaderboard). The Open ASR Leaderboard will now report:

As more accents join, we’ll split the Outer and Expanding Circles.

Liva AI collects multimodal interaction data through consumer products used by real people. Because Liva owns both the collection environment and distribution, it can design products around specific model gaps across domains, industries, languages, modalities, and interaction types. This gives it access to natural, high-context behavior that emerges through real product use, rather than artificially elicited or task-based interactions.
