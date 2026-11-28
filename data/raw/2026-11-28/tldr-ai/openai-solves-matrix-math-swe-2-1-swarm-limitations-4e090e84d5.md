---
title: "OpenAI solves matrix math 🔢, SWE-2.1 💻, swarm limitations 🐝"
url: "https://tldr.tech/ai/2026-11-25"
source_url: "https://tldr.tech/ai/2026-11-25"
canonical_url: "https://tldr.tech/ai/2026-11-25"
source: "TLDR AI"
source_type: "curated"
published_at: "2026-11-25T00:00:00+00:00"
fetched_at: "2026-11-28T04:34:54+00:00"
content_type: "markdown"
is_list_page: false
---

# TLDR AI 2026-11-25

## OpenAI solves matrix math 🔢, SWE-2.1 💻, swarm limitations 🐝

### Cognition's SWE-2.1 (3 minute read)

Cognition released SWE-2.1, an upgraded coding and agent model trained with reinforcement learning on top of Kimi K3. It roughly doubles SWE-2's score on the Terminal-Bench 4.1 coding benchmark to 50.0 and adds stronger security skills.

### Introducing Ternary Bonsai 2.5 27B: Powering Agentic Coding and Private Knowledge Work (4 minute read)

Ternary Bonsai 2.5 27B has substantially stronger agentic coding, multi-turn tool use, and multi-step task execution abilities than its predecessor. It retains the previous release's 5.9 GB footprint while significantly improving the capabilities developers need to build agents that work with private files and tools on-device. It is by far the strongest AI model of its memory footprint for agentic workloads.

### Claude Artifacts Become Mac and Windows Apps (3 minute read)

Claude artifacts can now be installed as Mac and Windows apps, in beta on all plans. Each app gets its own icon and window, updates when the artifact changes, and can be shared.

### Jensen Huang Reinstated As Nvidia CEO at Behest of President Trump (45 minute read)

Jensen Huang's reinstatement as Nvidia's CEO is a sign of the state of US democracy, the country's free market economy and rule of law, and the integrity of its government. It will factor into every decision made and every trade on the stock market for years to come. Nvidia will likely go back to maximizing how many chips it can sell to China. The situation is still far from over as there are ongoing investigations.

### Swarms do not yet raise the roof (46 minute read)

Swarm-based LLM configurations, coordinated groups of agents, deliver faster but less efficient results compared to single agents at equal token budgets. Adding more agents to a swarm introduces a performance penalty that grows with size, leading to quality degradation. Experiments reveal that previous "swarm premiums" result from single agents becoming stale over time. Given fresh context resets, single agents outperform swarms, suggesting that current swarm strategies primarily accelerate compute rather than significantly enhancing capabilities.

### What VP ≠ VNP Means (3 minute read)

The Anthropic proof that VP≠VNP means that there is no way to find the permanent of a matrix of 0s and 1s if we are limited to arithmetic circuits of size polynomial in the input-size. This means that for P to equal NP, there must be some trick to computing permanents using AND/OR/NOT on the bits of the input that is better than addition and multiplication. There are many problems where access to Boolean operators is helpful, but it isn't clear how they would help with the permanent. There is a $1 million prize for a solution to this problem.

### Amazon says hackers' AI agents found and exploited 0-day with little human input (5 minute read)

Amazon said AI agents running on Cairn, an open source penetration-testing framework, found and exploited a zero-day in a medical imaging AI app on a university server with no human oversight beyond a goal prompt. Palo Alto Networks separately tracked a Cairn campaign that ran 25 autonomous operations against at least 19 organizations in the semiconductor, defense, and civil society sectors, breaching at least 10. Amazon's warning: agentic offensive operations are already happening, and defenders should prepare for their speed and persistence.

### ML compiler eng, your job is NP-hard (4 minute read)

Layout search is computationally hard. However, in reality, there are generally just a few places to put a conversion in a specific kernel. The tricky part is picking an option, as this requires relying on a potentially inaccurate model of how expensive those ops are given the subsequent software stack and the hardware itself.

## Get the most interesting AI stories and breakthroughs delivered in a free daily email.

Join 1,200,000 readers for one daily email
