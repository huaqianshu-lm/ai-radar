---
title: "Siri model swapping 🔄, Claude Money 💰, Hugging Face Tau 👨‍💻"
url: "https://tldr.tech/ai/2026-09-15"
source_url: "https://tldr.tech/ai/2026-09-15"
canonical_url: "https://tldr.tech/ai/2026-09-15"
source: "TLDR AI"
source_type: "curated"
published_at: "2026-09-15T00:00:00+00:00"
fetched_at: "2026-09-25T01:12:09+00:00"
content_type: "markdown"
is_list_page: false
---

# TLDR AI 2026-09-15

## Siri model swapping 🔄, Claude Money 💰, Hugging Face Tau 👨💻

### Anthropic prepares Claude Money for personal finance (2 minute read)

Claude Money allows users to link their bank accounts and ask Claude about spending, plans, and other financial questions. It appears to be designed to give Claude persistent access to users' financial context, removing the need to manually upload bank statements or transaction exports. The exact account types, data provider, and supported actions remain unknown. Claude already supports third-party personal-finance connectors, and Anthropic has been building finance-specific agents and products for professional users. The launch timeframe remains unknown.

### OpenAI Buys Startup Developing Smartphone Camera (3 minute read)

OpenAI has quietly bought Glass Imaging, a company developing smartphone cameras that use AI to produce image quality on par with a DSLR camera. The deal values Glass Imaging at over $300 million. OpenAI's plans for the company are unclear, but it has been developing a secretive device with Jony Ive, the former Apple executive who helped design the iPhone. Glass Imaging was founded in 2019 by two former Apple employees who had previously worked on camera technology at the company.

### Apple's Siri AI Can Be Swapped Out for Claude, ChatGPT, Code Shows (4 minute read)

Private iOS 27 and macOS frameworks show Apple built Siri so Claude or GPT-5.6 can sit in as the brain: Model Delegation lets Claude handle a natural-language ask, then hand Reminders or Messages back to Siri, and an inference-provider path can swap Apple's server-side Siri model entirely while keeping Siri's UI and voice. A demo already has ChatGPT finding emails, summarizing action items, and texting a contact through Siri's tools. The hooks are not user-facing yet, but they land as iOS 27 ships and after EU DMA pressure to open Siri to rivals.

### Bad benchmarks and evals: Senior SWE-Bench, napkin math, and winter tires (52 minute read)

Evals are more about avoiding mistakes than following some particular process. There isn't any step-by-step guide that will work, but there are approaches to experimental design that can teach you how to do better. This post aims to help people become better at benchmarking and evals. It looks at three different kinds of benchmarks: one for baseline numbers for performance 'napkin math' estimates, one set of AI model evals, and one on car tires.

### What Does Pacing Mean? (6 minute read)

Dario Amodei called for the AI industry to self-regulate its pace, but five camps interpreted "pacing" differently without agreeing on a speed. These camps focus on model interpretability, worker interests, economic growth, geopolitical strategy, and resisting new regulations. A previous attempt to limit AI training compute failed, highlighting the challenge of controlling AI innovation speed.

### Who Gets to Define the Rules for AI? (18 minute read)

Aidan Gomez, Cohere CEO, argues against a few dominant Silicon Valley firms setting global AI regulations, drawing parallels to historical monopolies that limited competition under safety pretexts. He proposes a diverse, international, evidence-based framework for AI governance, emphasizing transparency, mandatory testing, and independent assurance mechanisms. Gomez warns that current proposals could entrench market leaders, advocating for more inclusive rule-making to foster competition and trust.

👨💻

### Engineering & Research

### Physical AI took flight. Now it drives, inspects and reasons. (Sponsor)

### Augmented Lagrangian Predictive Coding (17 minute read)

PC-ALM is a local alternative to backpropagation. It is an extension of standard predictive coding (PC), which uses diffusive coupling between layers. PC-ALM trains residual MLPs up to 1,000 layers, nearly matching backprop's performance despite using only layer-local dynamics. It equips each layer with a feedback control dynamical system that distributes and propagates supervision credit throughout a network.

### ARTEMIS (GitHub Repo)

ARTEMIS lets AI assistants and test suites use real phones like a human. It can execute testing workflows and everyday tasks on Android from natural language instructions, using element indices when available, with coordinate and visual locating fallbacks for custom interfaces. ARTEMIS checks targets before individual actions and returns blocked actions to the Operator for recovery. It supports long-running exploratory and stability tests.

### Tau (GitHub Repo)

Tau is a coding agent that lives in the terminal. It can read files, edit code, run commands, and keep a durable session history while streaming what it is doing. Tau was designed to be a teaching project for understanding the shape of a coding-agent system without starting from a giant production codebase. It ships with support for OpenAI-compatible endpoints.

### StepAudio 3 Technical Report (19 minute read)

StepAudio 3 Gen uses discrete autoregressive modeling over shared RVQ audio tokens to generate speech, voices, vocals, sound effects, music, and mixed audio within one model. It achieved state-of-the-art results on text-to-speech and voice design while retaining broad general-audio generation capabilities.

### Personal Statement on AI Risk (12 minute read)

Models are becoming so situationally aware that researchers are losing the ability to evaluate them in contexts where they believe they are not being watched or controlled. Models increasingly seem aligned even when they are not. The current evidence suggests that the field will continue to make progress at a fast pace. Once language models reach the capability threshold where they can shape the world unconstrained by human will, they might do something extreme and destroy humanity in the process.

### Sam Altman Backs Federal Frontier AI Safety Rules (2 minute read)

Sam Altman supports consistent federal safety requirements for frontier AI while urging labs to act before legislation arrives. OpenAI now uses safety cases before major reinforcement learning runs, arguing that capability growth should be deliberately paced alongside alignment and monitoring.

### Frontier labs have a financial incentive to pace the frontier (26 minute read)

Frontier labs are arguing for regulatory pacing on safety grounds. While many are undoubtedly well-intentioned, it is also true that the rules the labs have proposed protect their investments, preserve price premiums, and defer billions in competitive spending. Their arguments for these rules should not be taken at face value. The labs can not economically slow down on their own without the government stepping in to enforce a slowdown.

## Get the most interesting AI stories and breakthroughs delivered in a free daily email.

Join 1,100,000 readers for 

one daily email
