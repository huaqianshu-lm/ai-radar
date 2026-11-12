---
title: "Show HN: Yogurt – Free, private, open-source alternative to Granola"
url: "https://github.com/FrigadeHQ/yogurt"
source_url: "https://news.ycombinator.com/item?id=50454625"
canonical_url: "https://github.com/FrigadeHQ/yogurt"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-11-11T15:33:06+00:00"
fetched_at: "2026-11-12T03:39:04+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50454625
Original URL: https://github.com/FrigadeHQ/yogurt
Author: brownrout
Score: 190

Hey HN, I’m Eric and I want to share an OSS project that I’ve been building in my free time. Yogurt is a free, MIT licensed desktop app that uses on-device AI models to transcribe, summarize, and chat with your meetings.
Here's a quick demo video:
https://www.youtube.com/watch?v=BFfbXAwRq98
Similar to Granola, Yogurt runs in the background and does not join your calls. But unlike Granola, Yogurt is open-source, free to use, and private. Your meeting transcripts, call recordings, and summaries never leave your computer.
As small OSS models have gotten faster and more powerful, Yogurt seemed like a pretty obvious win for privacy and cost conscious folks. You do not need a frontier model to summarize meeting notes or answer questions about them. And if you want to make your notes available to a frontier model, you can just share it with Anthropic, OpenAI, etc. directly via Yogurt’s local MCP server. There’s no need to use a paid cloud service as a middleman.
I tried some of the most popular OSS note taking tools, and most were missing features like calendar integration, MCP server, etc. or required you to connect or create an account. And more than that, they didn’t feel polished enough for it to be something I actually wanted to use daily, and so I built Yogurt to scratch that itch. I spent a lot of time fine-tuning every UI interaction/animation and optimizing the model calls to get the most out of your hardware + make it snappy.
To support Windows/Mac/Linux, I decided to go with Electron. I use whisper.cpp for transcription and Apple’s on-device SpeechAnalyzer if your system supports it. For call summaries and questions, I use a local open weight LLM that automatically gets downloaded and set up based on what your hardware can handle without your cooling fans firing off like crazy (this part uses llama.cpp).
I’ve spent a lot of time working on details like echo detection/reduction, global/folder/local level search respectively, and auto-end recordings. Hope this is useful for any of you who have held out on using AI note tools for privacy or cost reasons, or for folks using cloud tools who want to switch to something free and open source that still feels great to use.
Would love to hear what you think about the onboarding and note taking experience :)
