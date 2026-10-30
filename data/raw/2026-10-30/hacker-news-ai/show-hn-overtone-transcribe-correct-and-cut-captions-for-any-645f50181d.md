---
title: "Show HN: Overtone – Transcribe, correct and cut captions for any screen shape"
url: "https://github.com/lonthq/overtone-captions"
source_url: "https://news.ycombinator.com/item?id=50293115"
canonical_url: "https://github.com/lonthq/overtone-captions"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-10-29T17:48:17+00:00"
fetched_at: "2026-10-30T02:26:05+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50293115
Original URL: https://github.com/lonthq/overtone-captions
Author: rvanderlinden
Score: 37

Hi HN, I'm Ruud, co-founder of Lont. We turn company emails into personalized videos.
Video captions cost us manual work twice: fixing misheard words, then fixing layout, like lines ending on “the”.
Overtone uses multiple models to listen to the audio: gpt-transcribe, Azure STT, and Elevenlabs Scribe. When they return conflicting results, Overtone sends small clips to the models again, and then lets an LLM decide what was actually said.
The LLM is like a human doing a sanity check on the transcription model. Humans would easily recognize a word to be different based on context. The LLM basically does the same, using an optional context prompt + its world knowledge. Because of this the Word Error Rate (WER) on many test files is lower when using Overtone, compared to just using a model without it.
Sure, the cost is higher because we use up to 3 different STT models + an LLM, but it still removes mistakes, reducing the time needed to fix captions to a minimum, and reducing the chance you'll miss something. For us it's worth it. For ultra high volume use cases it may not be.
The rules-based cutter nicely cuts the transcript into captions that look good, depending on screen size: 16:9 is different from 9:16, and the Overtone Format we created supports any type really. Pauses become breaks, captions are grouped per speaker, and names/numbers are never spread out over multiple captions.
How to add these captions to your videos? A videojs plugin can do this automatically, so you don't burn in your captions. The plugin lets you cycle between styled captions, plain captions, and off. You can burn them into an MP4 file with overtone burn.
Quickly try it out just the cutter? Try:
npx overtone-captions recut yoursub.srt
Transcribing audio with API keys works too. Use --dry-run to show a cost estimate before you send.
We open-sourced this first version (MIT) because we believe many people can benefit from this, especially if your captions just need to be good. There's plenty of room to improve though, so we've made it easy to help contribute to add style packs, languages, and providers/models.
You can find a demo at:
https://overtone.lont.ai/
Find the code and benchmarks here:
https://github.com/lonthq/overtone-captions
