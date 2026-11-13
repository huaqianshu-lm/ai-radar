---
title: "Grok Bot 1.0 🤖, AlphaGenome 2 🧬, Gemini Decisions 🧠"
url: "https://tldr.tech/ai/2026-11-12"
source_url: "https://tldr.tech/ai/2026-11-12"
canonical_url: "https://tldr.tech/ai/2026-11-12"
source: "TLDR AI"
source_type: "curated"
published_at: "2026-11-12T00:00:00+00:00"
fetched_at: "2026-11-13T03:13:32+00:00"
content_type: "markdown"
is_list_page: false
---

# TLDR AI 2026-11-12

## Grok Bot 1.0 🤖, AlphaGenome 2 🧬, Gemini Decisions 🧠

### Gemini Decisions API: Fast, calibrated multimodal decisions (1 minute read)

Google's Gemini Decisions API enables fast, calibrated multimodal decision-making by analyzing inputs like images and text. It assesses scenarios and provides actionable insights, such as determining spill severity and recommending cleanup actions.

### What's new in Grok Bot 1.0 (11 minute read)

Grok Bot 1.0 adds Team Bots you can publish and share, Slack and Microsoft Teams, meetings on Meet and Zoom, shared connectors, and reviewed learnings. It is now a personal assistant that the whole team can talk to in the app, in Slack, in Microsoft Teams, and in video calls. This post covers how to create a Team Bot and publish it, how to bring the bot into Microsoft Teams, how to add a bot to a meeting, and more. It also looks at the new admin controls and what's possible without a team.

### Runway Praxis-1 Is Now Available: Open-Weight Robotics Model (3 minute read)

Runway's Praxis-1, a 27B-parameter open-weight robotics model, is now available under Apache 2.0. The model excels in predicting video and actions, topping NVIDIA's RoboLab-120 leaderboard with a 46.2% success rate across 1,200 episodes. It's accessible on GitHub and Hugging Face, with support for full and LoRA fine-tuning, compatible with NVIDIA hardware, and adaptable for various robotic embodiments.

### Escaping SPACE: Part II (28 minute read)

Perplexity tested 12 models against its SPACE agent sandbox: none escaped VM-host isolation, but several bypassed network controls through DNS spoofing and shared-IP exploitation before the flaws were fixed. The experiments also found that capture-the-flag prompts distracted agents from the security boundary being tested.

### MCP vs CLI vs Skills: What Each Costs in Context (11 minute read)

MCP servers significantly increase token use, adding thousands of input tokens per request, unlike CLI or skill methods. On Sonnet 5.5, a simple task showed MCP consuming 59,417 tokens with default tools against CLI's 1,421 and skill's 3,315, highlighting the high cost of tool-heavy MCP setups. Implementing Tool Search can cut token costs by deferring tool definitions, reducing upfront toolset costs to under 600 tokens for optimal efficiency.

### LLMs can learn some multi-step reasoning on filler tokens instead of visible CoT (9 minute read)

By changing the training setup and applying LoRAs to Qwen3.6-35B-A3B and gpt-oss-20b, researchers taught models to do some multi-step tasks while emitting only filler tokens, beating an answer-only baseline on three of seven tasks. They also mapped theoretical layer-depth limits and showed empirical walls, with some tasks learned out to 60 steps and others failing after one to three. The work is meant to separate filler-token reasoning from steganographic hidden reasoning when interpreting chain-of-thought.

### Don't Write Kernels, Derive Them (63 minute read)

Current models rely on hand-written kernels specific to operators, chips, and fusions, limiting flexibility across devices and scenarios. Tang's IR enables on-the-fly derivation of kernels through constructs such as views and comprehensions, eliminating the need for pre-defined kernels.

👨💻

### Engineering & Research

### No eval suite can prove your agent is safe (Sponsor)

Join Gray Swan, who evaluates and benchmarks pre-release models for Anthropic, OpenAI, & Reflection, as their Chief Product Officer walks through a three-layer defense for production agents: red-teaming, behavior enforcement and deterministic controls.

Register Free ->

### Browser use has been rolling out in Antigravity (1 minute read)

Browser use in Antigravity closes the loop between researching, writing code, and verifying it live. Users control authentication, and downloads pause until they are approved. Agents can use the browser to run multiple tasks at once. A video demo is available in the post.

### AlphaGenome 2: Predicting how DNA shapes cells and disease (9 minute read)

AlphaGenome 2 improves prediction of DNA variant effects on specific cell types, aiding in disease understanding and research. It doubles variant identification compared to its predecessor and adapts to analyze new cell states without retraining. Available for non-commercial use, the tool bridges genetics and cell biology, pinpointing disease-relevant genetic mutations in primary human cells.

### OpenAI open-sources MCP Extensions for ChatGPT-native plugins (1 minute read)

The TypeScript and Python packages add ChatGPT-specific features to MCP servers and apps, including sidebar entry points, custom file viewers, composer resource search, and thumbnail part pickers. The SDKs ship with a Bits & Bolts demo plugin and a written spec.

### A2UI 1.0: Build delightful, fast, reliable, agentic experiences (11 minute read)

A2UI is an open protocol for generative UI that lets agents answer with interactive screens. Open-source renderer SDKs are now available for the web, Android, iOS, and agent SDKs for Python, TypeScript, and Dart. A2UI enables apps to draw UIs with native components, securely. Users get the same low latency, high trust, and complete native fidelity whether they reach a company's agent in its own app or in a third-party AI assistant that hosts MCP apps.

### Shopify's generative discovery model (14 minute read)

Shopify deployed a shared generative discovery model for search and recommendation, leveraging semantic-ID tokens to enhance product personalization and relevance. The model improved online and offline metrics, such as a 9.85% lift in conversion rate and significant gains in search relevance.

### United moves to block AI agents (2 minute read)

United Airlines is moving to restrict AI-agent access across its platforms and agency channels, citing credential security and liability risks around tasks such as check-in. The restrictions contrast with travel companies including Expedia and Booking that are partnering with agents.

### Why Connections Matter More in AI (5 minute read)

Professional relationships are becoming increasingly important in AI as coding agents commoditize technical execution, frontier research demands more compute resources, and closed-source development makes individual contributions harder to evaluate.

### Build financial models with AI (Sponsor)

Describe the financial model you need. Pigment's AI agent builds it. Explore it yourself in a real planning environment with a 14-day Free Trial. Start your free trial →

### Video: Replit, Fin, Snowflake, and Clay on pricing for the AI era (Sponsor)

Leaders from Replit, Fin, Snowflake, Clay, and Growth Unhinged discuss what to meter, when to revisit a pricing model, and how to forecast AI costs and returns. Watch the recorded sessions from Monetize.

### Google Tabletop Creates Shared Interactive Planning Spaces (1 minute read)

Google Labs' Tabletop turns links, files, and prompts into interactive itineraries, polls, expense splitters, and tournament brackets.

### ElevenAI (Website)

ElevenAI is a desktop app that helps amplify work using agents.

### OpenAI wants agents to tell websites where you are (5 minute read)

Two OpenAI engineers recently shared a proposal that suggests a change that will let agents pass user information along to websites to make them look like normal visitors rather than bots.

### Nvidia board reportedly preparing to oust Huang (3 minute read)

Nvidia's board is preparing to oust CEO Jensen Huang following his admission of an affair with a woman US intelligence agencies believe was recruited by Chinese intelligence.

### Airbnb's AI assistant cut support cost per booking 17% (1 minute read)

Airbnb's AI assistant cut support cost per booking by more than 17%, resolving about 40% of Q3 issues with no human agent.

### Databricks Genie Agents (13 minute read)

Databricks Genie Agents can now analyze unstructured documents alongside database tables, connect to enterprise tools, and share insights externally with governance controls.

## Get the most interesting AI stories and breakthroughs delivered in a free daily email.

Join 1,100,000 readers for one daily email
