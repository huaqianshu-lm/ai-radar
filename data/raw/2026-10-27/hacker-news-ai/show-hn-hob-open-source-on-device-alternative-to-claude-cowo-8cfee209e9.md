---
title: "Show HN: Hob - Open-source, on device alternative to Claude Cowork and ChatGPT"
url: "https://github.com/FrigadeHQ/hob"
source_url: "https://news.ycombinator.com/item?id=50246238"
canonical_url: "https://github.com/FrigadeHQ/hob"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-10-26T16:12:29+00:00"
fetched_at: "2026-10-27T01:51:13+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50246238
Original URL: https://github.com/FrigadeHQ/hob
Author: pancomplex
Score: 117

Hey HN, I'm Christian and this is a new OSS project I've been noodling on for the last couple of weeks. Hob is a free, MIT-licensed desktop app for Mac, Windows and Linux that works on your files the way the Claude and ChatGPT desktop apps do, except the model runs on your own computer. It uses open-weight models (currently Gemma 4 and gpt-oss). All your chats and files never leave your system. The only things that go online are web search (can be turned off in settings) and any MCP connectors you add yourself.
Main features:
- Automatically finds the best open-weight model for your hardware on first install (Mac/Linux/Windows)
- Writes sandboxed Python code for ad hoc tools (data processing, document conversion, graphs etc.)
- Built-in web search (powered by SearXNG)
- MCP support
- Image recognition
- CRUD to your local filesystem
- Works fully offline with no internet
Before building this I tried every local AI app I could find, but it seemed each one had different problems. The main thing I noticed is that none of them could do what the ChatGPT and Claude apps do with your files, e.g. read and change files in a folder, look at images, run code in a sandbox, draw a chart. The most advanced thing any of them did was paste a plain text file into a small context window, which basically failed as soon as you had a file larger than a few KB. I couldn't find anything that could easily parse images and bigger PDFs.
The OSS solutions that were more advanced all seemed to default to hosted models (either OSS or closed), which defeats the entire point of the privacy that on-device OSS offers. They also seemed to push towards an account/open-core style business.
I build it using Electron bridged with llama.cpp in its own process. On initial load, the system will try and figure out if you have a compatible graphics card and if not default to CPU-only (I ran into a lot of issues of graphics card beeing seemingly compatible but then crashing on first query, there's a whole saga to this lol). Code execution happens in a sandbox that can only write to the chat's folder and has no network unless asked (sandbox-exec on macOS, Landlock on Linux and a low-integrity process on Windows). Images go to a small Qwen3-VL model. Dictation is a local Whisper model.
The hardest part was definitely to get the smaller models to use tools reliably. Ran into a ton of issues of 4B models happily saying "here's your chart" without ever calling the chart tool or get stuck in an infinite call loop. I spent a fair amount of the work building guards vs tweaking prompts (that didn't really work for small models).
I understand the pushback that local models are weaker than frontier cloud models. This is true, but for most tasks for most normal people, I'd argue you rarely need the newest frontier model. From my own evals, systems with 16+ GB of RAM do really well, and if you have a GPU or more RAM, you get very close to what you'll get out of the box with a frontier hosted model.
Excited to hear what you think and see how it runs on other systems!
