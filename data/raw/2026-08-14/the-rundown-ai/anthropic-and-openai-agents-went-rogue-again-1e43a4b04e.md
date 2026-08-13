---
title: "Anthropic and OpenAI agents went rogue — again"
url: "https://www.therundown.ai/p/anthropic-and-openai-agents-went-rogue-again"
source_url: "https://www.therundown.ai/p/anthropic-and-openai-agents-went-rogue-again"
canonical_url: "https://www.therundown.ai/p/anthropic-and-openai-agents-went-rogue-again"
source: "The Rundown AI"
source_type: "curated"
published_at: ""
fetched_at: "2026-08-13T23:42:16+00:00"
content_type: "markdown"
is_list_page: false
---

**Good morning, {{ first_name | AI enthusiasts }}, and welcome to the 5,789 new readers who joined us yesterday.** The cases of AI models slipping their limits and taking unauthorized actions are getting harder to track by the day.

Barely a week after OpenAI and Anthropic revealed their agents went on hacking sprees, including one targeting Hugging Face, the UK’s safety testers have caught frontier models doing it again — even creating fake identities to target real people and leaving instructions for other AI agents to follow.

**In today’s AI rundown:**

- Anthropic and OpenAI agents went rogue again
- Apple and OpenAI trade fresh blows over trade secrets
- Redline any contract with Claude and Microsoft Word
- Business students go all in on AI amid demand surge

###### COMMUNITY AI WORKFLOW OF THE DAY

Every Monday, Claude reads his receipt emails, maintains a running expense ledger, calculates his recurring software spend, and flags price changes, duplicate subscriptions, and unnecessary charges that may need attention.

<sup>Credit to reader</sup> <sup>Erich Archer</sup><sup>. How do you use AI? Tell us</sup> <sup>here</sup><sup>.</sup>

**LATEST DEVELOPMENTS**

###### AI SAFETY

Image source: Images 2.0 / The Rundown

**The Rundown:** In a recent cyber test spanning 100+ runs, the UK AI Security Institute caught 10 cases where frontier AI agents, most tied to Anthropic’s Mythos 5, took unsanctioned actions against real people and organizations on the live internet.

**The details:** 

- The models, which had safety features disabled, took a total of 19 unauthorized actions, with 17 coming from Mythos 5 and two from GPT-5.6 Sol.
- In one case, Mythos tried sneaking malicious code into an open-source project, then built fake GitHub accounts to pressure the maintainer into merging it.
- When the malware got flagged, it tried phishing emails, hidden prompts to hijack other coding tools, and left notes for other agents to pick up its attack.
- Separately, OpenAI said a misconfigured test by Irregular let one of its models reach the open internet, where it hacked a real website it mistook for the target.

**Why it matters:** While the models here were deliberately stripped of their guardrails, these cases — and the ones before them — show that agents chasing a goal will try to reach past their limits, bypassing restrictions and deceiving real people when it helps. This also raises questions about broader internet safety as models get more capable.

###### TOGETHER WITH GOOGLE FOR STARTUPS

**The Rundown:** Startups have a unique opportunity to lead the generative media charge, but bridging the gap between a sandbox demo and a scalable product is a massive engineering challenge. The new Google for Startups Generative Media Technical Guide is the blueprint for launching fast and building production-grade apps.

**Inside the guide, you’ll discover how to:**

- Build multimodal apps with DeepMind’s newest models, like Veo and Lyria
- Architect reliable, high-traffic media pipelines on Google Cloud
- Ensure deterministic output, programmatic guardrails, and economic scaling

###### APPLE-OPENAI

**The Rundown:** Apple just asked a U.S. judge for a preliminary injunction to bar OpenAI and two former employees from using its alleged trade secrets, with the ChatGPT maker hitting back by calling the suit “careless, aggressive, and oddly personal.”

**The details:** 

- Apple sued OpenAI and two former employees, Chang Liu and Tang Yew Tan, last month, alleging they took its trade secrets to aid OpenAI’s device push.
- The motion seeks to halt that hardware work, with depositions of the duo, OpenAI, its device unit io Products, and forensic images of their devices.
- Apple named 11 more ex-employees who may have seen or joined in the alleged theft, with one screenshotting files before an OpenAI interview.
- OpenAI denied having or wanting any Apple secrets, saying Apple’s own staff asked a departed engineer for files, then blamed him for its offboarding gaps.

**Why it matters:** Beneath this lawsuit is a fight over who builds a device for the AI age that could end up replacing the smartphone. The specifics of OpenAI’s product are unclear, but an injunction would stall its work, which may be why the company is resisting hard. With a hearing set for Oct. 1, expect more drama in the coming months.

###### AI TRAINING

**The Rundown:** In this guide, you will learn how to use Claude directly in Microsoft Word to redline legal documents before you sign or send them.

**Step-by-step:**

1. Get Claude for Microsoft 365 from the Microsoft Marketplace and sign in
2. Open the contract you want to review and ask Claude to make a first pass with tracked changes, redlining anything that needs clarification or edits
3. Now you can review Claude’s recommendations and accept or reject them. You can even send the document to a teammate to review those tracked changes
4. When you think you’re ready to sign or send a document, type / in Claude and run the Doc Check skill

**Pro tip:** After a few reviews, download the chat transcripts from Claude, store them in a Claude Project, and turn the process into a reusable skill for teammates.

###### PRESENTED BY IBM

**The Rundown**: Many organizations want to use AI, but they don’t see a clear path to business ROI. IBM Bob helped CrushBank developers analyze legacy systems, inspect schemas, and generate ingestion code. This created a path from legacy data to building AI value without replacing every application first.

**Other ways IBM Bob can help:**

- Build MCP servers
- Create tests fast
- Document implementations

###### AI RESEARCH

Image source: Kogod School of Business

**The Rundown:** A three-year Kogod School of Business survey found that more than 80% of students now use AI for coursework, with the share of students questioned about AI skills nearly quadrupling over the study period.

**The details:** 

- Students using AI eight or more times a week rose from 13% to 39% over three years, with ChatGPT being the favorite, while those not using it fell to 4.3%.
- Brainstorming was the top use all three years (75.8%), followed by studying for exams (66.2%), summarizing (62.3%), and understanding concepts (58.5%).
- The usage growth comes as employers press harder for AI talent, with interview questions on AI skills surging from 11.6% to 42.6% since 2024.
- Concerns linger even so, with “cognitive devaluation” being the top worry, as 43.5% of the students admitted using AI as a shortcut rather than a real aid.

**Why it matters:** It’s a small sample (483 students at one school), but the trend is real. Students are pushing AI’s use in academics, and employers now expect that ability in the workplace, yet many still want to be taught how to lean on it without dulling their own thinking — a harder ask for schools than a blanket ban or green light.

**QUICK HITS**

- 🤖 FLUX 3 Video - Black Forest Labs’ AI for generating HD videos with audio
- 📹 Shieldstral  - Mistral’s open-weight AI for on-device content moderation
- ⚙ Celeris-1 - Fastest general-purpose AI, delivering 2,000+ tokens per second
- 🧠 Anydoc - Firecrawl’s open parser that processes 500 docs in 1.7 seconds

**The Trump administration** reportedly excluded open-weight AI models from its pre-release safety review framework, focusing testing only on closed frontier AI systems.

**Black Forest Labs** launched FLUX 3 Video, a multimodal AI that generates 20-second HD videos with native audio from text or images, with open weights dropping soon.

**OpenAI** agreed to settle Justice Department allegations that it discriminated against U.S. job applicants in favor of foreign visa holders, while denying any wrongdoing.

**Anthropic** named former California Supreme Court justice Mariano-Florentino Cuéllar as its first chief global affairs officer amid growing AI policy and regulation tensions.

**AI infrastructure startup Volta**, founded earlier this year, emerged from stealth with a reported $10B compute deal with Anthropic and funding at a $2.4B valuation.

**Ilya Sutskever’s** secretive AI startup, Safe Superintelligence, plans to launch its first model in August, famed investor Gavin Baker said on the “Invest Like the Best” podcast.

- Read our last AI newsletter: AI giants head to the White House
- Read our last Tech newsletter: Biohackers head to Big Sky Country
- Read our last Robotics newsletter: Attack drones are coming to schools
- Today’s AI tool guide: Redline contracts with Claude and Microsoft Word
- RSVP to next workshop today @ 12 PM EDT: No-code product building

### That's it for today!

See you soon,

*Rowan, Zach, Shubham, Jennifer, and Nate — the humans behind The Rundown*
