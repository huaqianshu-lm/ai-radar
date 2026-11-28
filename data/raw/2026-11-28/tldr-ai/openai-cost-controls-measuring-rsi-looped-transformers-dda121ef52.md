---
title: "OpenAI cost controls 💰, measuring RSI 📈, looped transformers ➰"
url: "https://tldr.tech/ai/2026-11-27"
source_url: "https://tldr.tech/ai/2026-11-27"
canonical_url: "https://tldr.tech/ai/2026-11-27"
source: "TLDR AI"
source_type: "curated"
published_at: "2026-11-27T00:00:00+00:00"
fetched_at: "2026-11-28T04:34:54+00:00"
content_type: "markdown"
is_list_page: false
---

# TLDR AI 2026-11-27

## OpenAI cost controls 💰, measuring RSI 📈, looped transformers ➰

### Anthropic prepares Google Drive file browser for Claude (2 minute read)

Anthropic is developing a Google Drive integration that will let users browse and manage their files directly in Claude. The interface will display Google Docs, Sheets, and Slides and allow users to search and filter files. It currently appears as a separate item in Claude's navigation sidebar. The final implementation may become part of Claude's updated Projects experience.

### OpenAI may be in cost control mode (2 minute read)

OpenAI's Astra 6.2 and Sol 6.2 updates received criticism for reduced performance, as both models show significant reductions in reasoning and output tokens. This suggests a shift towards cost savings, with p-values indicating substantial declines in their reasoning and output compared to previous versions. These changes make Astra and Sol outliers focused more on cost-efficiency than performance.

### Measuring RSI (12 minute read)

Neither compute allocation nor human intervention measures whether an AI training algorithm improved. Neither metric establishes a hard link between human intervention and AI improvement. Also, they are unable to detect strong recursion before a successfully more capable model is trained. Sample complexity, which detects the mechanism of strong recursion without building a more capable AI, and counterfactual measurement, which measures how much AI capability changes when advised by AI tools, address these challenges.

### Your Model Is a Dependency (16 minute read)

The large language model (LLM) you choose to use is a dependency. Software dependencies bloat, break, and quietly turn into liabilities over time. LLMs are the strangest dependencies adopted in software development so far, but the software supply chain playbook applies to them almost line by line. Companies need to start adopting habits from the software supply chain and applying them to the models they use as soon as possible.

### From Model Compression to Looped Transformers (22 minute read)

Model layers are not all equally sensitive to compression. It is often possible to compress substantial parts of the deeper network more aggressively than the early layers. The compressability with little consequence suggests that models are not using their architectures as effectively as researchers had hoped. Looped transformers offer a way to increase computational depth without duplicating the main backbone parameters. However, the question of how to make additional computation actually matter remains.

👨‍💻

### Engineering & Research

### Unhappy With Your GPU/SoC? Swap It, Build Physical AI Fast (Sponsor)

SiMa.ai's Modalix SoM is pin-compatible, it drops into your existing carrier board. Palette 3.0 brings your software over using the tools you already know, then runs vision models, VLMs and LLMs side by side with 3.5x faster token generation, all on-device at 10 watts. Explore Palette 3.0 →

### Become a founding member of TLDR's community (2 minute form)

TLDR is launching a curated community for AI builders to discuss best practices and the latest AI news. The best links and comments will be featured in TLDR. Apply here to join.

### LayerStream: faster MoE fine-tuning on fewer or cheaper GPUs (10 minute read)

Nebius' LayerStream training engine keeps optimizer state and saved activations in host memory and streams each layer's working state through the GPU only when that layer runs. On 16 H200 GPUs, it finished a pass over a 25.8M-token dataset in 7.1 minutes instead of 22.4, with 3.15x the throughput of a tuned Megatron-LM trainer and 68% lower GPU cost per token.

### Plato's Key (8 minute read)

The Platonic Representation Hypothesis posits that neural networks converge toward a shared representation of reality. Separately trained models can learn geometrically similar representations, but similar does not mean interchangeable. LLMs can use each other's representations in place of their own without gradient descent. The map is surprisingly simple: in experiments, a rotation and one global scale, fit in closed form, let one LLM use another's representations.

### Why I'm Bullish on MCP for 2027 (10 minute read)

MCP is evolving, with entities like Linear, Notion, and Atlassian using it for significant tool management, showing robust growth in traffic and tool handling. Key advancements include Code Mode for efficient tool calling, integrated Skills for streamlined agent knowledge, and MCP Events for real-time updates and notifications. There's still work needed in areas like observability and security, but MCP is becoming crucial for multi-agent coordination and efficient task management by 2027.

### Do scale-dependent algorithms cut against a software intelligence explosion? (13 minute read)

Scale-dependent algorithms will cut against a software-only intelligence explosion. The amount they do so will depend on how algorithmic progress is measured. With the way AI companies actually measure algorithmic progress, the effect will be small. AI companies should publish more data so that independent researchers can assess whether there will be a software-only intelligence explosion.

### ChatGPT just gave its agents a wallet. Can they buy from you? (Sponsor)

ZeroClick's Agent Storefront lets AI agents buy from your website, and it works with ChatGPT Wallet. $0 to set up, and no subscription fees.

Get Started For Free

### Close Q4 with proof. Start 2027 ready to scale. (Sponsor)

Reach 8 million developers, AI experts, security engineers, and founders across 14 newsletters. Plaid built $382K in pipeline from one placement. Book a Q4 campaign.

### Using peers' work to gain unauthorized access to OpenAI research infrastructure (13 minute read)

OpenAI observed agents taking a cybersecurity evaluation gaining unauthorized access to its research infrastructure on July 19, using the access to repair broken targets, change evaluation settings, and retrieve logs and private grading code unavailable from their workspaces.

### Introducing the llama.cpp benchmark dashboard for AMD Ryzen and Radeon (3 minute read)

The llama.cpp × AMD Benchmark dashboard on Hugging Face lets AMD developers track performance across llama.cpp builds, models, and quantizations on Ryzen and Radeon hardware.

### Thariq Shihipar has joined OpenAI (1 minute read)

Thariq Shihipar has left Anthropic to work at OpenAI to build AI products for over a billion people and to push the frontier forward.

### Nous Research readies Hermes Desktop redesign for next week (3 minute read)

Nous Research plans to release a redesigned Hermes Desktop app next week, featuring a new interface with a centralized home screen and customizable agent pages.

## Get the most interesting AI stories and breakthroughs delivered in a free daily email.

Join 1,200,000 readers for one daily email
