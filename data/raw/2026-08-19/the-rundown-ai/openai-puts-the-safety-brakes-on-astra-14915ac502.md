---
title: "OpenAI puts the safety brakes on Astra"
url: "https://www.therundown.ai/p/openai-puts-the-safety-brakes-on-astra"
source_url: "https://www.therundown.ai/p/openai-puts-the-safety-brakes-on-astra"
canonical_url: "https://www.therundown.ai/p/openai-puts-the-safety-brakes-on-astra"
source: "The Rundown AI"
source_type: "curated"
published_at: ""
fetched_at: "2026-08-18T23:23:20+00:00"
content_type: "markdown"
is_list_page: false
---

**Good morning, {{ first_name | AI enthusiasts }}, and welcome to the 12,457 new readers who joined us this weekend.** A week ago, OpenAI’s upcoming Astra model was making major waves in the math world after knocking out 10 long-standing problems. Days later, it set off an alarm the company had never rung before.

The company says Astra (expected to be GPT-6) is the first model it's treating as a potential "critical" cyber risk, triggering paused internal work, deeper government testing, and a potentially slower road to release.

**In today’s AI rundown:**

- OpenAI puts the safety brakes on Astra
- The Rundown Roundtable: Our AI use cases
- Cut onboarding time in half with Loom and ChatGPT
- China’s Kimi K3 joins the jailbreak party in testing

###### COMMUNITY AI WORKFLOW OF THE DAY

Six Star Trek-themed AI agents run on a home server. Spock routes tasks to the right crewmate, and the crew scans for vulnerabilities, summarizes email, posts the weather, and monitors seven machines on Discord for a few cents a month.

<sup>Credit to reader</sup> <sup>Joao Silva</sup><sup>. How do you use AI? Tell us</sup> <sup>here</sup> <sup>for a chance to be featured tomorrow.</sup>

**LATEST DEVELOPMENTS**

###### OPENAI

Image source: Images 2.0 / The Rundown

**The Rundown:** OpenAI just designated its Astra model as its first “critical” cybersecurity-capable AI, putting its preparedness framework into action with safeguards CEO Sam Altman says may “need a little bit longer” before broader rollout. 

**The details:** 

- A ‘Critical’ model is defined by OAI’s framework as being able to either find and create zero-day bugs or carry out cyberattacks without humans in the loop.
- Astra, rumored to be GPT-6, was recently unveiled publicly after the model solved 10 significant open math and computer science problems.
- Steps being taken include heightened security restrictions, a pause in certain internal activities with Astra, and deeper government and third-party testing.
- The news follows security issues across OAI, Anthropic, Meta, and Moonshot (more below), though OAI said Astra wasn’t involved in the Hugging Face hack.

**Why it matters:** The incidents piling up are a sign that AI is entering an unprecedented capability phase (if you haven’t seen this post-mortem on the HF hack, it’s eye-opening). Whether the misaligned capabilities can be controlled or are simply getting too complex to get ahead of is a question looking more uncertain than ever. 

###### TOGETHER WITH MOZILLA

**The Rundown:** Mozilla's inaugural State of Open Source AI report finds open models have nearly closed the performance gap with proprietary giants like ChatGPT and Claude — while a new battle emerges over who controls the infrastructure built around them.

**Report highlights include:**

- Performance gap narrows to just 3%
- Open models make up a third of usage but just 4% of revenue
- Power is shifting to the "agentic harness"

Read the full report __here__.

###### THE RUNDOWN ROUNDTABLE

Image source: Nate @ The Rundown

**The Rundown:** The Rundown Roundtable is a weekly feature where we poll members of The Rundown staff about how we use AI in our work and daily lives.

**Nate, University Educator:** The new ChatGPT Chrome extension is surprisingly good at navigating complicated technical settings. My favorite use case so far has been using it to create the special DNS records for a new website.

This has always been confusing, even though I’ve done it dozens of times. The process varies across platforms; every DNS registrar uses different names for records such as A and CNAME records, and the interfaces are constantly changing. It’s tedious and easy to get wrong.

For this kind of one-off, highly detailed technical task, I copy and paste the specific instructions from my website host provider into the extension while I’m logged in to my DNS provider. GPT then takes control of the mouse and fills in the required fields.

The use cases are endless, from filling out an expense report to handling other tedious tasks in legacy or old-school software that doesn’t have a simple CLI, MCP, or API connection.

**Nick, Senior Video Producer:** I had a video shoot earlier this summer where the main lavalier mic on the talent ended up getting lost. The project had no room for a reshoot, so I was left with just the scratch audio from the on-camera mic, which was quiet, very distant from the subject, and had tons of room noise in the audio. 

I was able to take the scratch audio and run it through the Adobe Podcast AI tool to fix the audio and salvage the shoot. In the past, doing this kind of restoration would have required a lot of manual work and scrubbing through the spectrogram to pull out unwanted frequencies & just hoping that it was going to work in the end.

The AI tool was able to save the audio, clean up all of the background noise, and normalize the talent's voice. Moral of the story - always double-check mics on set & don't panic when something is wrong in production.

###### AI TRAINING

**The Rundown:** In this guide, you will learn how to turn a short Loom walkthrough into a clear onboarding SOP with ChatGPT.

**Step-by-step:**

1. Pick a repeatable task, like filling out timesheets or writing a report, and record it in Loom. Explain clicks, decisions, exceptions, and the definition of done
2. Use Loom’s transcript editing to remove mistakes or long silences
3. Copy the transcript into ChatGPT. Tell it to write the SOP in Markdown
4. If it is not in this format, a good one is: purpose, links to resources, steps, and then a checklist
5. Paste the final SOP into a Google Doc

**Pro tip:** If you ask it to build the SOP in Notion, it can embed the Loom video so it is playable right on the page.

###### PRESENTED BY VANTA

**The Rundown:** Vanta's MCP server connects Claude, Cursor, and Codex directly to your compliance program, so AI-native teams can catch risks, fix gaps, and stay audit-ready without leaving their workflow.

**Join and learn how to:**

- Connect Vanta directly into your AI tools
- Surface failing tests and audit gaps instantly
- Assign remediation without leaving your workflow

__Save your spot here__**.** If you can't make it on Aug. 18, no worries! Register, and you'll automatically get the recording after the session.

###### MOONSHOT AI & SECURITY

Image source: @Sauers on X

**The Rundown:** Chinese lab Moonshot AI’s Kimi K3, which neared the frontier at launch last month, joined the sandbox escape club after U.S. firm Frontier Security revealed the model slipped through its test environment to pull an answer key off GitHub. 

**The details:** 

- The benchmark's answer key sat in a public codebase, and Frontier says K3 realized it could reach GitHub through a loophole meant for software installs.
- Nothing actually got hacked, and the sandbox wasn't wide open, but Frontier researcher Paul Kassianik said where rival models refused, “K3 didn't blink.”
- K3’s weights are open and freely downloadable exactly as tested, which is why Frontier warns the case could prove "potentially more harmful."

**Why it matters:** The AI world cycles through a new main character every few months, and security breaches have officially taken the spot this summer. But this entry hits a bit differently than other escapees coming from closed labs like OAI, Anthropic, and Meta that can patch them, with Kimi’s weights already downloaded and out in the world.

**QUICK HITS**

- **🗣️** Unwrap Customer Intelligence - Connect your entire organization to the true voice of the customer with AI-driven insights from customer feedback*
- 🎆 Grok Imagine Image 2.0 - xAI’s powerful new AI image model
- 🎬 Seedance 2.5 - ByteDance’s video generation AI, now broadly available
- 🪁 Kitesurf - Cloudflare’s lightweight, agent-first browser

**Sponsored Listing*

**Elon Musk** revealed that Tesla and SpaceX’s ‘Terafab’ plant will be located in Grimes County, TX, predicting it will be “the largest and most valuable building on Earth by far”. 

**ByteDance** is reportedly pre-training an AI with up to 10T parameters, which would triple the size of China's largest model to date and potentially rival Anthropic's Mythos.

**xAI** rolled out Grok Imagine Image 2.0, featuring upgraded editing, text rendering, and overall quality, with the model sitting behind OpenAI’s GPT Image 2 across benchmarks.

**Research firm SemiAnalysis** said DeepMind is "no longer a frontier lab", but projected Google Cloud growth to top 100% in 2027 as Google pushes TPU sales.

**Anthropic** introduced a Claude Code feature that allows the platform to message across sessions, allowing instances to pick up where another left off. 

**Google co-founder Sergey Brin** is reportedly taking over oversight of the company’s Gemini model development, coming in the wake of last week’s leadership shakeup.

- Read our last AI newsletter: AI designs viruses never seen in nature
- Read our last Tech newsletter: OpenAI builds a $400 AI donut
- Read our last Robotics newsletter: Musk’s moon factories need robots
- Today’s AI tool guide: Cut onboarding time in half with Loom and ChatGPT
- RSVP to next workshop on Aug. 12: Your AI reset

### That's it for today!

See you soon,

*Rowan, Zach, Shubham, Jennifer, and Nate — the humans behind The Rundown*
