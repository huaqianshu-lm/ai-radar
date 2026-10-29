---
title: "DeepSeek DeepInfer 🐋, PyTorch on TPUs ⚡, Ramp’s agent framework 👨‍💻"
url: "https://tldr.tech/ai/2026-10-21"
source_url: "https://tldr.tech/ai/2026-10-21"
canonical_url: "https://tldr.tech/ai/2026-10-21"
source: "TLDR AI"
source_type: "curated"
published_at: "2026-10-21T00:00:00+00:00"
fetched_at: "2026-10-29T02:11:18+00:00"
content_type: "markdown"
is_list_page: false
---

# TLDR AI 2026-10-21

## DeepSeek DeepInfer 🐋, PyTorch on TPUs ⚡, Ramp’s agent framework 👨💻

### Voxtral 3: Voice Agent SDK & Speech Models in 50+ Languages (7 minute read)

Voxtral 3 offers advanced speech-to-text and text-to-speech capabilities across 50+ languages. Featuring models like Small Transcribe 3 for multilingual transcription and Mini TTS 3 for natural emotional speech, it includes a voice agent SDK combining real-time listening, reasoning, and speaking, enabling seamless interactions and task execution over phone or web.

### Google and Meta Bring Native PyTorch Support to TPUs (17 minute read)

TorchTPU is an open-source PyTorch backend designed to make running and migrating models to Google's TPUs easier. It supports training and inference through optimized eager execution, torch.compile integration, and native hardware acceleration.

👨💻

### Engineering & Research

### Build a voice agent in minutes with LiveKit (Sponsor)

In less than 10mins, you can build and deploy an AI voice agent with LiveKit for free. 1M people have already built with LiveKit and the platform powers AI voice agents at Spotify, Headspace, and xAI.

Try it free → cloud.livekit.io

### llm-d (Website)

llm-d is a Kubernetes-native stack for distributed LLM inference. It runs vLLM, SGLang, and more across clusters, turning single-node engines into production-grade serving on local hardware. llm-d provides tested deployment recipes for common production patterns that are adaptable starting points across models, hardware, and workloads. It runs production LLM inference across GPUs, TPUs, XPUs, CPUs, and emerging NPUs with consistent performance patterns, so teams can deploy once and scale anywhere with predictable cost and behavior.

### DeepSeek V4.1 Flash: Large-Scale Inference Deployment (15 minute read)

DeepInfer combines distributed inference, caching, load balancing, and speculative decoding to improve efficiency. DeepSeek processes 155 trillion tokens daily per cluster and earns $38 in revenue per GPU-hour while open-sourcing much of its inference framework.

### Making every harness durable (7 minute read)

Vercel's durable-harness allows agent harnesses to run durably in the cloud out-of-the-box. It allows users to run Pi, OpenCode, Codex, and Claude Code durably on Vercel or self-hosted on their own Postgres instance. durable-harness ensures that sessions survive crashes mid-turn and keep running even if the browser disconnects. Turns that lose function partway through continue from the log on a new one without manual retry and without repeating what already finished.

### Building Laminar: Ramp's Managed Agents Platform (14 minute read)

Laminar is an in-house agent harness for Ramp's agentic products. It features secure conversation history storage, session compaction, standard interfaces for tool calling, message queuing and steering, subagents, multiplayer chat support, observability tooling, and much more. The first version of Laminar was built in six weeks with a small team of obsessive, experienced engineers who worked with and steered the agents. Its code was generated entirely by agents using the most powerful models available at the time. While building in-house has become cheaper, Ramp still needs good engineers to be on-call, keep the platform healthy, and figure out what product teams actually need and how it fits into the bigger picture.

## Get the most interesting AI stories and breakthroughs delivered in a free daily email.

Join 1,100,000 readers for one daily email
