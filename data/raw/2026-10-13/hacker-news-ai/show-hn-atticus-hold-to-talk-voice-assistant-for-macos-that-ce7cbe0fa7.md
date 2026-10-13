---
title: "Show HN: Atticus – Hold-to-talk voice assistant for macOS that runs on Claude -p"
url: "https://github.com/SaarthurR/atticus-mac"
source_url: "https://news.ycombinator.com/item?id=50049588"
canonical_url: "https://github.com/SaarthurR/atticus-mac"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-10-12T00:15:12+00:00"
fetched_at: "2026-10-13T03:23:08+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50049588
Original URL: https://github.com/SaarthurR/atticus-mac
Author: SaarthRanka
Score: 81

Hi HN! I'm Saarth. I'm in 9th grade, and I built Atticus.
Atticus is a fast and cheap Mac assistant that can do tasks for you. You hold down Control-Option-Space, speak or type your task, be it complex or a simple browser search, and Atticus will get on it.
The interesting part is that simple tasks, like opening apps, playing a Spotify playlist, or web queries, don't touch AI, and instead are processed locally and typically finish in under a second. For example, prompting Atticus to open apps takes around 0.08 seconds, sometimes even finishing before you finish your sentence, sort of like Jev.
Any tasks that are more complicated will be sent to Claude via claude -p, meaning you never need an API key and Atticus will run on your existing Claude Pro or Max plan. By using this approach, costs are also cut down immensely, with, on average, tasks costing a fraction of a cent.
To achieve Atticus' speed, it remembers shortcuts from each task it completes. When it does a task right for the first time, it saves its steps and replays them the next time without AI. For example, a workflow of creating a new meeting took about 30 seconds the first time around. Atticus then logs the exact steps to memory and takes 5-8 seconds on the next pass. To add to this, Atticus also learns about you as you use it more and from what's on your computer, including your name, your apps, and things you want it to remember, personalizing its answers to you.
To combat the safety concerns over giving an AI unrestricted access to your device, Atticus has toggleable restrictions, so before anything is deleted, sent, bought, or written to a file, the user is prompted before that action.
Some features I'm currently working on include a meeting copilot that capitalizes on Atticus' speed, allowing Atticus to listen in on meetings and answer questions in real time as they come in, personalized to the context of the meeting and what it knows about you.
To run Atticus, macOS 26 or higher is required for its voice transcription features. The voice transcription is also done locally by macOS.
Atticus is free, open source, and also very fresh, and I'm completely aware of its many rough edges, which is why I'd love to hear from everyone about what breaks and what you guys would like to see Atticus do!
