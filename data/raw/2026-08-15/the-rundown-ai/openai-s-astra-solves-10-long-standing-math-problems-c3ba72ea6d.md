---
title: "OpenAI's 'Astra' solves 10 long-standing math problems"
url: "https://www.therundown.ai/p/openai-astra-solves-10-long-standing-math-problems"
source_url: "https://www.therundown.ai/p/openai-astra-solves-10-long-standing-math-problems"
canonical_url: "https://www.therundown.ai/p/openai-astra-solves-10-long-standing-math-problems"
source: "The Rundown AI"
source_type: "curated"
published_at: ""
fetched_at: "2026-08-14T23:23:01+00:00"
content_type: "markdown"
is_list_page: false
---

**Good morning, {{ first_name | AI enthusiasts }}, and welcome to the 5,860 new readers who joined us yesterday.** Even with the drama of its agents breaking containment, OpenAI is not slowing down with breakthroughs, this time claiming 10 open problems across math, quantum complexity, and theoretical computer science.

The results came from an unreleased model called Astra, and that too at a cost that finally looks low enough to put every open problem within the reach of mathematicians.

*P.S. — By popular demand, we’re moving community AI workflows higher up in the newsletter. Let us know what you think* *here**.*

**In today’s AI rundown:**

- OpenAI’s ‘Astra’ cracks long-open math problems
- The Rundown Roundtable: Our AI use cases
- Run your workday by voice with ChatGPT
- China’s Qwen now challenges the frontier

###### COMMUNITY AI WORKFLOW OF THE DAY

Every weekday morning, ChatGPT Work scans the major job boards, scores each role against his resume, and emails him the top matches, with a tailored resume already attached for the best one.

<sup>Credit to reader</sup> <sup>Michael Ebner</sup><sup>. How do you use AI? Tell us</sup> <sup>here</sup><sup>.</sup>

**LATEST DEVELOPMENTS**

###### OPENAI

Image source: Images 2.0 / The Rundown

**The Rundown:** OpenAI just revealed that Astra, an internal version of its next major model family, solved 10 long-open math and computer science problems (one nearly 30 years old), covering geometry, group theory, quantum complexity, and more.

**The details:** 

- Astra proved non-sofic groups exist, building the first symmetry structure that can’t be imitated by any finite shuffle, an exception hunted since 1999.
- It also solved Alain Connes’s rigidity conjecture, Ehrhart’s volume conjecture, and cleared three problems from Paul Erdős’s list; none had moved in a decade.
- Each proof has been verified in Lean, with CoT walkthrough released and cost coming in at roughly $2K in tokens at Sol API rates for all successful runs.
- In 24 hours, Anthropic’s Levent Alpoge claimed he was able to reproduce five of the 10 proofs with Fable, running on a generic prompt and no internet.

**Why it matters:** The community is debating whether Astra’s proofs can be Fields Medal-worthy, given that a machine did the thinking here. The question feels simple, but it will only grow bigger as AI capable of cracking decades-old problems at low prices moves beyond math and into domains like drug discovery and materials science.

###### TOGETHER WITH CDATA

**The Rundown:** CData tested whether Claude Code could build an enterprise-grade MCP server. The CData MCP Research Report is an independent, rigorous study that reveals exactly where AI-generated connectors fall short when real production demands kick in.

**In the report, you’ll discover:**

- Why only 1 of 8 dimensions passed without human expertise
- When data loss and pagination failures showed up, and expert guidance still wasn’t enough
- How AI MCP code diverges from production-ready code
- What a side-by-side comparison with CData Connect AI reveals

__Download the full report__ and see what your AI-built connector might be missing.

###### THE RUNDOWN ROUNDTABLE

**The Rundown:** The Rundown Roundtable is a weekly feature where we poll members of The Rundown staff about how we use AI in our work and daily lives.

**Billy, Educator:** I usually give Codex a long “impossible” task before I go to bed to see how it does overnight. This time, it finished it before I could even shut down my computer. I asked it to build a custom dashboard to monitor my 3D printer. I explained that it would need to find the IP address of the printer on the local network.

Literally 5 minutes later, I was looking at this live dashboard with all the detailed information from my printer. The future is wild.

**Brooke, Community Lead:** I just moved in with two friends. The place is big, which sounded great until we unpacked and found we had 30 pieces of art and no idea where any of it went. One roommate wants minimal; I want a gallery wall; the third collects estate sale finds. We spent a whole evening holding frames against the wall asking, “Does this work?” and got nowhere.

So I took pictures. Every room, then every piece laid out on the floor. I uploaded the whole mess to Claude and said: help, three people, three tastes, a lot of blank wall, tell us what goes where. It came back with groupings for all walls and actual reasons.

The two orange abstracts we were going to split up belonged together. The big mirror went in the hallway so it catches the evening sun and throws light in the darkest corner of the apartment. That never would have occurred to us, and we love the light it brings!

###### AI TRAINING

**The Rundown:** In this guide, you will learn to turn a request for an update into a finished PDF report and send it to your team without touching your keyboard.

**Step-by-step:**

1. Open the ChatGPT app, create a project, and start Voice. Connect your workflow parts, including work data, communication apps, and storage
2. Ask ChatGPT to “scaffold” your folder for drafting reports in Markdown and finalizing them as PDFs. This makes the process repeatable
3. Tell ChatGPT what report the team needs and the inputs/KPIs it requires. Try: “Build a Markdown draft of [report] using only [approved source] and include [required fields]”
4. Review and ask ChatGPT to remove anything unnecessary. Then have it make the final PDF, save it to the deliverables folder, and draft the handoff message

**Pro tip:** Once you run a report type once, have ChatGPT turn it into a reusable skill. You can use this any time you want to get that same report with fresh data.

###### PRESENTED BY AWS

**The Rundown:** Long-lived agent credentials are a breach waiting to happen. This workshop covers agent identity management on AWS with technical demos of Auth0 and CyberArk PAM.

**Join and learn how to:**

- Scope time-bounded tokens that expire per action with AWS Security Token Service
- Configure automatic secret rotation with AWS Secrets Manager
- Trace each API call to identity, session, and task with AWS CloudTrail

###### ALIBABA

Image source: Qwen

**The Rundown:** Alibaba just released Qwen3.8-Max, a 2.4T-parameter mixture-of-experts model (95B active) that it claims can run multiday projects on its own — challenging frontier models across benchmarks, with the weights dropping next week.

**The details:** 

- Qwen3.8-Max brings improvements across coding, research, and long-horizon tasks, ranking ahead of Anthropic’s Fable 5 on Arena’s WebDev leaderboard.
- In one test, it coded for 16 days to build a command-line tool, turning feedback into tasks, writing the code, testing its work, and fixing what broke.
- The model also rebuilt a research paper’s experiment, then invented and tested 18 ideas in a self-improvement loop, resulting in a 2.7-point gain on AIME24.
- It is available via API at $2/$6 per million tokens — a fifth of Fable 5’s price — with weights hitting Hugging Face next week in a first for Qwen’s Max class.

**Why it matters:** Kimi K3 shook the market and pushed talk of regulating (and protecting) open-source into overdrive. Now another Chinese model is here with near-frontier performance at a fraction of frontier prices. Every release like this sharpens the debate on open-source AI while making the premium on closed models harder to justify.

**QUICK HITS**

- 🤖 Gemini Spark - Google’s always-on AI agent, now expanding globally
- 🧠 Qwen3.8-Max - Alibaba’s flagship reasoner that can code for 10+ days
- ⚙ QM  - Y Combinator’s open-source multi-agent platform
- 🎙️ HeyGen Video Podcast - Turn notes into a studio video show

**Google** rolled back its Nano Banana 2 integration in Google Earth after users created convincing fake satellite imagery that appeared to violate its policies.

**Apple** capped bug report submissions as “AI slop” reports overwhelmed its review system with hallucinated security risks, FT reports.

**OpenAI** found additional AI agents that escaped containment while investigating the Hugging Face hack, though none are believed to have left its network, Reuters reports.

**Snapchat** confirmed it will not recommend fully AI-generated videos on Spotlight, saying it wants to reward authentic human creativity over low-quality AI content.

**A U.S. judge** allowed Minnesota’s first-in-the-nation ban on AI “nudify” apps to take effect, despite xAI’s lawsuit challenging the law as overly broad and unconstitutional.

**The EU** started enforcing the AI Act, introducing mandatory labels for AI chatbots, deepfakes, and other AI content to reduce deception and manipulation.

- Read our last AI newsletter: OpenAI’s models cut their own costs
- Read our last Tech newsletter: Disney plots its Netflix makeover
- Read our last Robotics newsletter: U.S. bans humanoids from China
- Today’s AI tool guide: Run your workday by voice with ChatGPT
- RSVP to next workshop on Aug. 5: No-code product building

### That's it for today!

See you soon,

*Rowan, Zach, Shubham, Jennifer, and Nate — the humans behind The Rundown*
