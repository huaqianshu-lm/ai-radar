---
title: "Cursor's Origin hits GitHub on its worst day"
url: "https://www.therundown.ai/p/cursor-origin-hits-github-on-its-worst-day"
source_url: "https://www.therundown.ai/p/cursor-origin-hits-github-on-its-worst-day"
canonical_url: "https://www.therundown.ai/p/cursor-origin-hits-github-on-its-worst-day"
source: "The Rundown AI"
source_type: "curated"
published_at: ""
fetched_at: "2026-08-18T23:23:20+00:00"
content_type: "markdown"
is_list_page: false
---

**Good morning, {{ first_name | AI enthusiasts }}, and welcome to our 5,482 new readers.** If you were picking a day to launch a GitHub competitor, you couldn't script a better one than the morning the legacy platform suffered a massive outage.

Cursor just managed to hit that window, launching Origin as an alternative to the place the world has held its code for two decades. Microsoft is no stranger to defending from AI challengers, but one of its most entrenched products just joined the list.

**In today’s AI rundown:**

- Cursor's Origin hits GitHub on its worst day
- ByteDance cuts Hollywood's first AI video deal
- How to set up ChatGPT to write in your voice
- OpenAI, Nvidia’s new 8 GW AI power push

**LATEST DEVELOPMENTS**

###### CURSOR

Image source: Cursor

**The Rundown:** SpaceXAI’s coding platform Cursor just launched Origin, an early beta that hosts code repos and pull requests with agents built in, moving the company onto GitHub's turf the same day it suffered a massive outage for a large chunk of the day. 

**The details:** 

- The platform pairs each hosted repository with Cursor’s agent and review tool, keeping code browsing, follow-up edits, and human approval in one product.
- Users can sync their connected codebases right from GitHub, creating a live mirrored version that pushes to both platforms to test drive the new alternative.
- GitHub’s outage was its second major issue this month, with some functionality seeing performance issues for over 6 hours.
- Origin initially opens in beta for Cursor’s paid customers, with features built for large agent-native workloads set to be released “soon”.

**Why it matters:** While Cursor's GitHub ambitions weren’t a secret, launching mid-outage is timing that is hard to beat. Coding has been upended over the last few years by AI, but hosting has always stayed locked on Microsoft's legacy rails. Now, GitHub faces the same AI siege that the rest of Microsoft's product lineup has already felt. 

###### TOGETHER WITH HUBSPOT

**The Rundown:** HubSpot’s free, comprehensive  “How to Use ChatGPT at Work” guide provides 100+ ready-to-use prompts to help professionals boost efficiency and adopt AI-driven workflows.

**Inside, you’ll find:**

- A quick crash course to master ChatGPT in under 30 minutes
- Practical industry use cases to spark real-world inspiration
- 100+ prompts to streamline tasks and accelerate productivity
- Expert tips to tackle common AI roadblocks with confidence

__Get your free copy__ and join 10,000+ professionals leveling up with AI.

###### AI & HOLLYWOOD

Image source: Ruairi Robinson (@RuairiRobinson on X)

**The Rundown:** ByteDance agreed to a formal framework with Hollywood’s Motion Picture Association (MPA) that will implement film and TV copyright protections into its Seedance and Seedream models, months after it received a cease-and-desist notice. 

**The details:**

- A viral Seedance 2.0 clip of Tom Cruise fighting sparked the initial legal feud, which marked the MPA’s first cease-and-desist against a major AI company.
- ByteDance pushed back its worldwide release of 2.0 following the notice and baked heavier protections into last month’s 2.5 and Seedream 5.0 Pro releases.
- The framework will impact every app the models run on, including third-party servers like CapCut and Dreamina, as well as TikTok and its U.S. spinoff.

**Why it matters:** It only took a few years for AI video to jump from meme-grade clips to high-quality footage (see the latest Will Smith eating spaghetti clip), and many of the labs pushing hardest are coming out of China. ByteDance is one domino, but Kling, Alibaba’s Wan models, and others make for a tough problem for MPA to tackle entirely. 

###### AI TRAINING

**The Rundown:** In this guide, you will learn how to build a simple ChatGPT writing setup that turns rough ideas into natural-sounding drafts, saving you hours of copy-editing tweaks.

**Step-by-step:**

1. Open ChatGPT Work, go to Settings → Plugins → Skills, and turn on Humanize Writing. Write a draft. Type /humanize-writing and compare it with the original
2. Give ChatGPT a writing exercise like: “Write me a memo about the history of the Moon”
3. For level two, open the terminal and run “npx skills add blader/humanizer --global.” Then use /humanizer on a copy of the same draft and compare both
4. You should also try: “Write in Technical English. Use ASD-STE100 as a style reference.” It can make the copy more direct

**Pro tip:** Test Steps 2, 3, and 4 separately on the same writing sample, then compare what each method improves. The best mix will be different for everyone.

###### PRESENTED BY FIDDLER AI

**The Rundown:** Join Fiddler AI CEO and Dun & Bradstreet's Chief Data Officer in an upcoming webinar to learn why verified data is where agentic AI reliability must start, and what building that foundation takes.

**In this session, you'll learn to:**

- Build the verified data foundation agents depend on
- Govern autonomous data decisions
- Keep data lineage intact across multi-agent handoffs

###### AI INFRASTRUCTURE

Image source: SB Energy

**The Rundown:** OpenAI and Nvidia announced a new Ohio AI campus set to deliver nearly 8 GW of AI compute at a Cold War-era uranium plant in Pike County, Ohio, with Nvidia supplying every chip and backing the buildout with up to $105B of its own credit.

**The details:** 

- A 2028 target covers just the opening 800 MW build, with the rest being constructed on federal land cleaned up after the plant shut down.
- OAI is leasing the campus from SB Energy, with Nvidia also investing $1.5B in the company (which also has previous investments from OAI and SoftBank).
- Nvidia CEO Jensen Huang published an article alongside the news, saying frontier labs are constrained by infrastructure and financing, not demand.
- Huang also addressed claims Nvidia is funding its own sales via circular financing, saying: "No. OpenAI will pay the lease.”

**Why it matters:** Not sure that a deal between OAI, Nvidia, and an early Sam Altman investment company that is majority-owned by SoftBank is going to help the circular dealmaking allegations, but either way, this is one of the biggest AI buildouts to date. It also interestingly comes outside of Stargate, which has quietly had a rocky 2026.

**QUICK HITS**

###### COMMUNITY AI WORKFLOW OF THE DAY

Today's workflow comes from reader João Silva:

“Everyone I know who runs a second brain uses Obsidian. The app is free, but sync is a subscription, and most AI integrations quietly assume you have it. I went another way: Joplin, which is free and open source, with an agent that reads my notebook through Joplin's REST API, files my INBOX every morning while I sleep, and answers questions strictly from notes I actually wrote.

Every capture goes through joplin_capture.py and lands in a single INBOX folder with a source and timestamp attached. It requires no filing decisions at capture time, because filing at capture time is where second brains die. joplin_filer.py runs daily and scores each INBOX note against my existing folders. Confident matches are moved into place: a security note goes to the security folder.

Low-confidence notes stay in INBOX with the needs-review tag. Every move is logged to a FILER LOG note, and the filer never deletes anything. I ran it in dry-run mode for a week before letting it touch a single note, and I recommend doing the same.”

- 👨💻 Managed Deep Agents - Build and deploy deep agents with real-time monitoring, tracing, alerting, and high-level insights*
- ⚙️ Origin - Cursor's code hosting with GitHub sync and built-in agents
- 🗣️ Sonic-3.6 - Cartesia's new SOTA text-to-speech model in 44 languages
- 🤖 Grok Bot - xAI's always-on agent teammates with their own cloud computer

**Sponsored Listing*

**Join Edge Case:** Akamai Cloud’s Discord for devs building with WebAssembly, AI agents, & serverless. __Claim $300 in cloud credits & start building__.*

**Stripe** is reportedly acquiring AI model marketplace OpenRouter for over $7B, more than 5x the valuation the company raised at just months ago. 

**Voice AI startup Cartesia** released Sonic-3.6 in beta, a new text-to-speech model that covers 44 languages and tops Artificial Analysis' voice leaderboards.

**AI video platform Higgsfield** secured a new $400M Series B, more than quadrupling its valuation to $5.4B as its annualized revenue hit $700M.

**Voice dictation startup Wispr** raised $280M at a $2B valuation, coming alongside a preview of Canto, its first in-house speech model built for noisy real-world conditions.

**Sponsored Listing*

- Read our last AI newsletter: Dario Amodei logs on to answer the critics
- Read our last Tech newsletter: Google’s $99 Fitbit gets a wild new update
- Read our last Robotics newsletter: Robot vacuums finally learn gestures
- Today’s AI tool guide: How to set up ChatGPT to write in your voice
- RSVP to next workshop on Aug. 21: Land your first AI consulting gig

### That's it for today!

See you soon,

*Rowan, Zach, Shubham, Jennifer, and Nate — the humans behind The Rundown*
