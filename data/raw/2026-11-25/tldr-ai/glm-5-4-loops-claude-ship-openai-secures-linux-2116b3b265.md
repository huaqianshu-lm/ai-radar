---
title: "GLM-5.4 loops 🔁, Claude Ship 🚢, OpenAI secures Linux 🔒"
url: "https://tldr.tech/ai/2026-11-24"
source_url: "https://tldr.tech/ai/2026-11-24"
canonical_url: "https://tldr.tech/ai/2026-11-24"
source: "TLDR AI"
source_type: "curated"
published_at: "2026-11-24T00:00:00+00:00"
fetched_at: "2026-11-25T05:15:31+00:00"
content_type: "markdown"
is_list_page: false
---

# TLDR AI 2026-11-24

## GLM-5.4 loops 🔁, Claude Ship 🚢, OpenAI secures Linux 🔒

### Introducing Natural Voice (8 minute read)

Natural Voice enables voice agents to securely process payments during calls, eliminating the need for out-of-band transfers and reducing customer drop-off. By handling PCI compliance, it allows businesses to offer seamless payment experiences without additional compliance burdens. This innovation benefits industries like restaurants, healthcare, and auto services by integrating payment processing directly into voice interactions, enhancing conversion rates and operational efficiency.

### Claude Ship (3 minute read)

Claude Ship is a set of Anthropic agents that help get GitHub pull requests ready to merge. Code Review flags issues, PR Steward pushes fixes, and Claude Approvals checks changes against a team's approval policy.

### GLM-5.4 (5 minute read)

Z.ai has released GLM-5.4, its first flagship model built on a Loop Transformer. The design reuses a shared block of layers to reason more deeply without adding parameters. Z.ai says it reaches intelligence comparable to 2T to 3T parameter models, and it is available now on the GLM Coding Plan.

### Supercharging transformer residual connections (4 minute read)

Google's DeepCrossAttention (DCA) enhances transformer residual connections by allowing each layer to dynamically select and route features from preceding layers, reducing information dilution and parameter count by 30-40%. Unlike traditional residual connections, DCA uses dynamic routing and depth-wise cross-attention mechanisms to achieve faster convergence and better quality with minimal parameter increase. Tested on large datasets like C4 and LM1B, DCA improves training efficiency and perplexity compared to standard models, proving a shift towards dynamic residual routing for scalable LLMs.

### I used to orchestrate agents. Now I orchestrate orchestrators (24 minute read)

MindRoom significantly enhances AI-driven coding by integrating multiple models in one room, efficiently managing up to forty concurrent sessions with seamless context switching. This approach, which utilizes minimal sub-agents, boosts productivity by maintaining low token overhead and offering a compact, card-based interface that organizes tasks by status.

👨‍💻

### Engineering & Research

### Talk through the idea on a walk. Wispr Flow Notetaker on iPhone turns it into clean notes (Sponsor)

Think out loud on your own, or record an in-person conversation and stay present in it. Wispr Flow Notetaker on iPhone gives you a clean summary and a full transcript afterward, synced to your desktop. It keeps recording when your phone is locked. Get Notetaker on iPhone

### OpenAI and Cisco introduce Shirudo (5 minute read)

Shirudo is an open-source runtime from OpenAI and Cisco that protects running Linux systems while teams roll out patches. It lets teams deploy temporary shields that block exploits without restarting the service.

### Recursive Self-Editing: LLMs Program Their Own Weight Edits for Self-Improvement (1 minute read)

Today's language models improve themselves through data, training recipes, or scaffolds. Whenever their weights change, gradient descent writes the update, not the model. SELFWRITE lets the model write its own weights. Each generation, the current model studies its own reasoning on fresh training problems, inspects its own weights and activations in a persistent Python session, and writes a program that constructs a low-rank weight edit for itself from white-box primitives. It can raise gate accuracy and accuracy on a held-out test split that the loop never sees without a single gradient step.

### Become a founding member of TLDR's AI community (2 minute form)

TLDR is launching a curated community for AI builders to discuss major news and launches. The best links and comments will be featured in TLDR AI. Apply here to join.

### Faster Quantum Algorithms with Agents and Formal Verification (4 minute read)

Google DeepMind used teams of Gemini 4 agents to find cheaper versions of known quantum algorithms, with each result proven correct in the Lean theorem prover. One circuit for fusion energy research cut its computing cost by 11.8x.

### NVIDIA Board Reinstates Jensen Huang as President, CEO, and Board Director (3 minute read)

NVIDIA reinstates Jensen Huang as President, CEO, and Board Director following unanimous Board approval and US government input confirming no national security risk. A committee of independent directors is investigating claims of Huang being targeted by foreign intelligence and will proceed with legal counsel's support. NVIDIA is forming a National Security and Export Control Committee and will appoint a Chief Compliance Officer to enhance oversight.

### Amazon snaps up Decart's AI optimization tech for $7.5B as it prepares to sell Trainium chips (1 minute read)

Amazon has acquired the technology behind the Decart Optimization Stack (DOS), as well as Decart's founding team and team of AI researchers and engineers, for $7.5 billion. Decart has made a name for itself by building interactive real-time models and AI video-generation tools. Its DOS software helps AI models run efficiently on Nvidia, Amazon, and Google's hardware. More efficient compute means better training, better reinforcement learning, faster inference, and better models for customers at a lower cost.

### You talk at 220 wpm and type at 45. Write the way you talk (Sponsor)

Wispr Flow turns what you say into clean, formatted text in every app, with the filler words gone. Mac, Windows, iPhone and Android. Try Wispr Flow free

### AI Is Changing the Cyber Risk Landscape. What's Next? (Sponsor)

AI is changing how threats emerge, how organizations manage risk, and how security decisions get made. Join HUMAN Security for CISO perspectives on leading cybersecurity in the age of AI. Save your seat.

### OpenWorks (6 minute read)

OpenAI's OpenWorks initiative partners AI experts with US small businesses to offer free, hands-on AI support.

### Grok Bot to Get Local Computer Use (2 minute read)

Grok Bot's Mac app has local computer use in the works, which would let it operate desktop apps directly instead of only cloud virtual machines.

### RL infrastructure at Microsoft AI (15 minute read)

Rocket is Microsoft AI's in-house reinforcement learning framework for post-training MAI Base 2, a three-trillion-parameter model, without distilling from third-party models.

## Get the most interesting AI stories and breakthroughs delivered in a free daily email.

Join 1,200,000 readers for one daily email
