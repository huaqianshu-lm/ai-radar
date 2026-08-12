---
title: "Meta returns to its open-source roots"
url: "https://www.therundown.ai/p/meta-returns-to-its-open-source-roots"
source_url: "https://www.therundown.ai/p/meta-returns-to-its-open-source-roots"
canonical_url: "https://www.therundown.ai/p/meta-returns-to-its-open-source-roots"
source: "The Rundown AI"
source_type: "curated"
published_at: ""
fetched_at: "2026-08-12T23:42:58+00:00"
content_type: "markdown"
is_list_page: false
---

**Good morning, {{ first_name | AI enthusiasts }}, and welcome to the 4,962 new readers who joined us yesterday.** Meta has had an incredible AI turnaround in 2026, and its latest move now has the company going back to its Llama roots. 

With a new open-weight Muse Glimmer model and Muse Spark 1.2 also going open "soon", the once-ridiculed tech giant’s superintelligence bet might now be the U.S.’ best answer to China's open-source dominance.

**By popular demand:** *The daily Community AI Workflow is now back in detail down below, with a complete step-by-step just one click away on our new* *Workflow Hub**.* 

**In today’s AI rundown:**

- Meta returns to open-source roots with Glimmer
- OpenAI expands ‘Daybreak’ for stronger cyber use
- Go from idea to website with ChatGPT Work + Codex
- AI agent hacks a gym to jump the waitlist

**LATEST DEVELOPMENTS**

###### META

Image source: Meta

**The Rundown:** Meta just released Muse Glimmer, a small, fully open model that runs AI agents entirely on-device, pairing the launch with Mark Zuckerberg’s essay on why superintelligence belongs to everyone and plans to open Muse Spark 1.2 as well.

**The details:** 

- Glimmer beats out similar-sized rivals like Gemma4 and Qwen3.6 on a range of agentic, coding, and reasoning tests, and is small enough to run on a laptop.
- Alexandr Wang said Muse Spark’s weights will be published “soon”, which would immediately make the model the top open rival to China’s ecosystem.
- Zuck pushed for the U.S. to embrace open source in the essay, saying that AI built on an “extreme concentration of power seems inherently problematic.”
- He also said that "any policy that slows American model releases… could add significant risk to American leadership while letting foreign models race ahead."

**Why it matters:** Meta’s returning to its open-source Llama roots, but with models that can actually compete. Zuck has talked a big game about superintelligence for all, but re-embracing open-source is backing it up. For all the massive salaries and questions around its superintelligence team at the start, the Meta vibe shift has been very real. 

###### TOGETHER WITH GLEAN

**The Rundown:** The intelligence era is here. Attend Glean:GO 2026 on Aug. 26–27 to learn how leading organizations turn AI into measurable impact. Hear bold keynotes, join hands-on sessions, and leave with strategies you can use immediately.

**Register for Glean:GO to:**

- Hear real-world strategies from enterprise leaders
- Attend hands-on trainings and deep-dive breakouts with experts
- Learn best practices for driving AI adoption and ROI

###### OPENAI

Image source: OpenAI

**The Rundown:** OpenAI launched GPT-5.6-Cyber, a new hacking-tuned model variant that answers 95% of the advanced cyberattack requests the standard model refuses, and is handing it to vetted defenders via an expansion of its Daybreak security program.

**The details:**

- Daybreak now has two tiers, with Blue stripping cyber guardrails off GPT-5.6 Sol and Red unlocking the new Cyber model for vetted exploit work.
- Cyber answered 95% of advanced security requests in testing, compared to just 1.5% for the normal safeguarded Sol model.
- Starting Sept. 1, individual users will need physical security keys, with applicants also vetted, watched, and requiring signed authorization.
- Both Cyber and the standard GPT-5.6 Sol model fell into OAI’s ‘high’ tier for cyber risk, below the upcoming Astra/GPT-6 model’s ‘critical’ rating.

**Why it matters:** The first thing that comes to mind with this update is Hugging Face’s frustration at having to use the open-source GLM model during its hack because frontier models refused to answer. Cyber looks like an answer to that problem, at least if you’re one of the vetted users on the list available to access it. 

###### AI TRAINING

**The Rundown:** In this guide, you will learn how to turn a website idea into a working prototype using the new ChatGPT Work and Codex app (which uses GPT-5.6 models).

**Step-by-step:**

1. Open the ChatGPT desktop app and click ChatGPT Work or Codex
2. Create a project folder and start a task. Give ChatGPT your directory idea, ask it to plan the Astro.js build, then save a one-page PRD in the folder
3. When the PRD is ready, ask ChatGPT Work to research directory items. Now, switch to Codex, point it at the PRD, and ask it to build with sub-agents
4. Open the preview and ask Codex to fix the biggest visible issue. We used a Nintendo Switch directory, but this works for any directory

**Pro tip:** If Sites is available in your app, tell Codex to publish the finished site using the Sites skill. OpenAI will deploy and host it for you.

###### PRESENTED BY CDATA

**The Rundown:** MCP has changed how AI agents access data. AI coding tools have changed how software gets built. We wanted to know if you could combine the two to build a connector you'd trust in production. CData’s MCP Research Report studied where AI-generated connectors fall short when real production demands kick in.

**In the report, you'll get:**

- Why only 1 of 8 dimensions pass without human expertise
- When data loss and pagination failures show up, and expert guidance still isn’t enough
- How AI MCP code diverges from production-ready code
- A side-by-side comparison with CData Connect AI

**__Download the full report__** and see what your AI-built connector might be missing.

###### AI AGENTS & SECURITY

Image source: ABC News

**The Rundown:** An Australian man's gym class request ended with his OpenClaw agent hacking the gym's reservation software to knock another member off the waitlist, in what ABC News says is the first known attack of its kind in the country. 

**The details:** 

- A user tasked his agent (running Claude) with reserving a workout class, with the agent finding a loophole allowing it to book weeks past the gym's cutoff.
- The user was fourth on the waitlist, with the agent responding by finding a way to cancel another reservation on the list to move the position up.
- There was no undo, with the agent admitting, “Bad news — I can't add them back,” leading the user to disclose the incident to the gym.

**Why it matters:** That's one way to stay accountable on your fitness journey. Where there's a will, there's a way for the current crop of AI agents, and systems that haven’t been hardened to deter this new kind of user are going to quickly find out how vulnerable they are to millions of eager-to-please digital assistants. 

**QUICK HITS**

###### COMMUNITY AI WORKFLOW OF THE DAY

Today’s workflow comes from reader Dean Mazlish: 

“I was about to start paying for a scheduling tool when I realized I would still be stuck with someone else’s rules. Instead, I built my own booking page with Claude Code. It took two hours to go from starting the project to going live, and I use it every day now.

It’s a Next.js app on Vercel with no database. Availability is read live from my Outlook calendar through Microsoft Graph, so there’s nothing to sync. My working hours come from my Outlook settings, so when I change my hours, the booking page follows. When someone books, it creates the calendar event and generates the meeting link. The guest chooses Zoom/Teams so they can use their preferred platform.

The rules are the main reason I built it. Same-day bookings are not allowed, so the earliest anyone can book is my next working day. If someone visits the page after hours or on a weekend, the following working day is blocked too.”

- 🗣️Unwrap Customer Intelligence - Connect your entire organization to the true voice of the customer with AI-driven insights from customer feedback*
- 🤖 Muse Glimmer - Meta's open-weights local model for on-device agents
- 🚀 Xirp - Spotify's workspace for Claude, Gemini, and Codex coding agents
- 🎆 Grok Imagine Image 2.0 - xAI’s powerful new AI image model

**Sponsored Listing*

**Anthropic** shared that an unreleased Claude model made progress on the unsolved Riemann hypothesis, with its user’s input being "keep going" and "believe in yourself."

**Sen. Bernie Sanders** wrote to Sam Altman, Dario Amodei, and Mark Zuckerberg for an AI pause, saying that if they don’t act, “my colleagues and I in the U.S. Senate will.”

**Spotify** released a public beta of Xirp, an internal tool that lets engineers swap between Claude Code, Gemini CLI, and Codex mid-task. 

**Nvidia** is said to be assembling a $500B AI infra raise with six Wall Street giants, including Apollo and Goldman Sachs, to fund data centers and power production. **Automaker Ford** launched a new AI assistant in its mobile apps that can provide live data and answer questions on a vehicle’s fuel, maintenance, and more. 

- Read our last AI newsletter: OpenAI puts the safety brakes on Astra
- Read our last Tech newsletter: OpenAI builds a $400 AI donut
- Read our last Robotics newsletter: Uber’s $10B answer to Waymo
- Today’s AI tool guide: Go from idea to website with ChatGPT Work + Codex
- RSVP to next workshop on Wednesday @ 2 PM EST: Your AI reset

### That's it for today!

See you soon,

*Rowan, Zach, Shubham, Jennifer, and Nate — the humans behind The Rundown*
