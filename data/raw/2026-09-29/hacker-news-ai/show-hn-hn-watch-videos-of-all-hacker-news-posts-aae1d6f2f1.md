---
title: "Show HN: HN.watch – Videos of all Hacker News posts"
url: "https://hn.watch/"
source_url: "https://news.ycombinator.com/item?id=49879401"
canonical_url: "https://hn.watch/"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-09-28T15:16:13+00:00"
fetched_at: "2026-09-29T02:30:16+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49879401
Original URL: https://hn.watch/
Author: mrborgen
Score: 132

Hi HN, I’m Per, founder of Scrimba (YC S20). We’ve spent the last decade teaching people how to code with an HTML-based video format. We’ve now plugged an LLM into it, so that people can create explainer videos about anything. It’s called “Scrimba Explain”.
To demo this technology for Hacker News, we built HN.watch. It’s like HN, but with explainer videos instead of articles. We create them on-the-fly the first time someone clicks on a link.
While there are obvious visual drawbacks of using HTML instead of diffusion models, there are three big benefits: - Speed: Much faster to generate than pixel-based videos (just a few seconds from click to playback) - Cost: Our cost per video is ~$0.04. (Excluding image generation, which some videos utilize. Quickly blows up the cost) - Easy editing: the above benefits also make AI-assisted editing cheap & fast
Our hypothesis is that if video creation goes from “dollars and minutes” to “cents and seconds”, a bunch of new use cases will be unlocked. Here are some we see already: - A video explanation of every single Pull Request (we do this internally) - Give every page in your internal/extrernal docs a video - Turn a complex article into a video in ~4 seconds (via our Chrome extension) - Course creators can quickly draft lessons before recording the real thing - People also create a lot of personal stuff stories for their kids, wedding invitations, birthdays, etc
The stack is based on an open-source programming language (Imba) created by our CTO, Sindre Aarsæther. It compiles to JavaScript, so it interoperates fully with the npm + node ecosystem. You can learn more here:
https://imba.io/
We’ve also built our own sync engine (OP), and a context management system for agents (Q). We feared this would make the LLMs struggle when writing code for us, as neither is in their training data (there’s very little Imba in there too). However, we’ve been pleasantly surprised to see that LLMs actually are really good at our stack. This is probably because the stack is extremely dense. Imba is compact, and so is OP, where a single declaration sets storage, sync, permissions, UI, and what the AI sees. This means there’s no translations between frontend, API, db and JSON where the model can get confused and get things wrong.
Simply said, instead of using React.js, Express, Supabase, and LangChain, we built it all from scratch. Definitely suffering from the “not invented here” syndrome, lol! As for the models, we use Gemini, GPTs, Inworld, ElevenLabs, and a few others.
If you want to try it out, just take your pick: - The Web UI (scrimba.com/explain) - MCP (add it to your coding agent) - ChatGPT Plugin - Chrome Extension
You can find a link to all of the above in our docs:
https://docs.scrimba.com/explain/introduction
And finally, a real pixel-based video of the tool:
https://www.youtube.com/watch?v=k6rbHmBxSEs
Would love to hear your feedback and if anyone has ideas for other use cases.
PS: I expect quite a bit of pushback from HN for this launch, given how fan of text the HN crowd is. This kind of tool is not for everyone. But there are a lot of people today who prefer videos over text, especially in the younger generations.
