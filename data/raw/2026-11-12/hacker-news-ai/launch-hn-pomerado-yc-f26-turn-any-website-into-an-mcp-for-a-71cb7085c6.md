---
title: "Launch HN: Pomerado (YC F26) – Turn any website into an MCP for agents"
url: "https://news.ycombinator.com/item?id=50455811"
source_url: "https://news.ycombinator.com/item?id=50455811"
canonical_url: "https://news.ycombinator.com/item?id=50455811"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-11-11T17:11:56+00:00"
fetched_at: "2026-11-12T03:39:04+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50455811
Author: alanjm23
Score: 51

Hi HN, we’re Alan and Akshay from Pomerado (
https://pomerado.ai/
). We connect your agents to any website by turning sites into deterministic, self-healing APIs in minutes, fully self-serve.
Agents are no longer limited by their intelligence, but rather by their ability to interact with systems. Airlines, banks, e-commerce, insurance portals, government sites, and legacy portals all lack APIs or MCPs and are common parts of personal assistant or business workflows. Agents instead rely on browser automation or computer use, which can be slow, expensive, and unreliable. And even if computer use were perfect, most companies have banned it out of security and compliance concerns.
We discovered this problem while tinkering with our own personal assistants. When OpenClaw came out, we wanted to “live our lives through our agents” and have them do everything for us. We soon found their usefulness was restricted by what tools they could connect to. For example, when trying to book flights, they fell back on computer use, which failed to checkout. These issues got magnified on repeated workflows, like searching many airlines at once.
Pomerado started off as a project to improve these personal assistant workflows. As we started building, we realized that just-in-time tool creation could have significant applications for AI builders in legacy verticals.
We’re ex-McKinsey and Scale AI, where we drove agent deployments in healthcare, professional services, and telecom. Each time, the biggest bottleneck was getting agents to interface well with legacy websites and apps.
Pomerado is what we built. It’s a self-serve platform where devs can create APIs for any website (even those they don’t own), in minutes. Users (or their coding agents) provide a short natural language description, answer a few questions about their workflow, and receive a MCP in less than an hour. Future tool calls use the deterministic MCP, which usually returns results in 5-30 seconds.
Here’s a walkthrough of our product:
https://youtu.be/Bi4jci7rgHo
In practice:
- Our agent opens a browser, explores the website, and performs the requested task once by writing HTTP requests or a Playwright script. This example run establishes how to navigate the website, interact with the relevant controls, and obtain the desired result. If any additional user input is needed (e.g., login, clarification) the agent will ask the user over MCP.
- Afterwards, the agent uses the example run, along with all of the data it recorded, to create a generalizable and repeatable API. Throughout this process, a separate Guardian model reviews the coding agent’s calls against a set of guardrails. We also run a battery of tests with synthetic inputs to ensure that the API is generalized and not overfit to one input. A final publication agent ensures that the integration publishes a reasonable and generalized input/output schema
- We also handle sites that require authentication and 2FA. For authentication, we pass off to a deterministic sign-in process to ensure the model and our recorders never read customer credentials. Users can store 2FA TOTP seeds or link their account to a Pomerado phone number for us to autofill 2FA for them as well
- If future runs fail, a maintenance job is kicked off to repair and improve the tool. The maintenance job can fix broken steps (e.g., a renamed button), add additional functionality (e.g., searching for business class flights in addition to economy), or add new guardrails (e.g., reservation dates must be in the future). We’ve even seen people improve tools by just saying “please make this faster”
Unlike computer use, our MCPs are deterministic at runtime, which makes them much faster and cheaper. By taking slightly longer to do a task the first time, you reap the benefits much more in the future. It’s a great fit for repeated, high-volume tasks you want your agent to do.
We’d love to have you try it! We have both an open-source (MIT) (
https://github.com/Pomerado/pomerado
) and a free hosted version (
https://app.pomerado.ai
).
So far, users of Pomerado include:
- A personal trainer using agents to prepare workouts and message clients. Before Pomerado, agents couldn’t login and use the site reliably, so this was all manual
- Car dealerships connecting their Grok Bots to legacy dealer systems, including marketplaces, CRMs, and ERPs. Dealers switched from computer use, which could take 1hr+
- Personal assistants using Pomerado to integrate with a broad range of consumer websites
Please ask any questions or share any feedback in the comments, thanks!
