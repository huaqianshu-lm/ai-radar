---
title: "Show HN: Nari Qwen3-TTS and Qwen3-ASR – High accuracy, low latency and cost"
url: "https://narilabs.com/blog/nari-labs-leads-coval-voice-ai-benchmarks/"
source_url: "https://news.ycombinator.com/item?id=49699267"
canonical_url: "https://narilabs.com/blog/nari-labs-leads-coval-voice-ai-benchmarks/"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-09-14T16:07:58+00:00"
fetched_at: "2026-09-15T01:13:50+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49699267
Original URL: https://narilabs.com/blog/nari-labs-leads-coval-voice-ai-benchmarks/
Author: toebee
Score: 64

Hey HN, Toby from Nari Labs here.
We've been working on making OSS speech models super-fast. Last year, we built Dia, the first OSS text-to-speech model capable of doing natural dialogue. Since then, so many more great speech models have been released to the public.
But the market is still dominated by closed source models. We think that's an inference problem. Existing systems such as vLLM / SGLang are not well suited for multimodal inference. To prove this, we built an inference engine specialized for Qwen3-TTS and open-sourced it (
https://github.com/nari-labs/nari-qwen3-tts
). Running at sub-50 ms latency at 10 RPS, this showed open models can be run much faster and cheaper.
Since then, we've been working hard to bring cheap, fast, and high quality serving to all. And we've even beat closed models at their game!
Measured on the highly cited Coval (YC S24) voice AI benchmarks, our Qwen3-TTS endpoint not just is #2 in latency, but #1 in accuracy (WER) compared to 11Labs, Cartesia etc. while being the cheapest endpoint. Our Qwen3-ASR endpoint has the lowest latency and #2 accuracy, just 0.1% away from #1. It is the second cheapest model on the list.
It took a lot of clever inference engineering to make these models quick, perform well while keeping costs low. Interestingly, Alibaba's official endpoints seem to perform worse in terms of accuracy and latency compared to ours. But nonetheless, much love to the Qwen team for OSS-ing these amazing speech models.
We want to continue to push prices down to make speech technology a commodity - so that every app can have great TTS and STT without worrying about unit costs. We're also working on other parts of audio such as diarization - as well as video and world model inference. More to come!
