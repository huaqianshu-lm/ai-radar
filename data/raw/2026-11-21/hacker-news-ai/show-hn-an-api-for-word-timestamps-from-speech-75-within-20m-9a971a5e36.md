---
title: "Show HN: An API for word timestamps from speech, 75% within 20ms"
url: "https://quebec.yarn.so"
source_url: "https://news.ycombinator.com/item?id=50532515"
canonical_url: "https://quebec.yarn.so"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-11-17T15:16:45+00:00"
fetched_at: "2026-11-21T03:49:15+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50532515
Original URL: https://quebec.yarn.so
Author: jasperstory
Score: 72

Hey HN, we're Yarn (W24) and we make a video editing app for startups, and we built Quebec (
https://quebec.yarn.so
), an API that gives you accurate word timestamps from speech. We needed it because cutting a word even 50ms off from its true timing can ruin talking head footage (examples in the write up).
Accurate word timestamps usually come from a forced aligner, which takes the speech audio and a transcript and works out exactly when each word starts and ends. We weren't satisfied with the accuracy of Montreal Forced Aligner (MFA) or new models like ElevenLabs Cue (
https://elevenlabs.io/blog/cue-aligner
). Giving LLMs access to a waveform/spectrogram didn't help much either.
So we built our own. There are two particularly interesting parts:
- We wrote our own decoder around MFA's acoustic model that only lets each word land within 200ms of the rough timings. That made search small enough to solve exactly, so we don't need to use MFA's beam search.
- We added a small CNN, built on the first two layers of Whisper Tiny, that nudges each word boundary by up to 50ms. We couldn't find enough hand-labelled speech that allowed for commercial use, so we had Gemini label our own (17k word boundaries). It took a couple of hours and cost under $200. A net trained on Gemini's labels scored the same as one trained on human labels (73.9% vs. 74%).
One way to measure accuracy is % of word boundaries within 20ms of hand labels. Here are the results on Buckeye (hand-labelled American speech that we didn't train on):
- Quebec 75%
- MFA 61%
- ElevenLabs Cue 30%
If you want to try it, it's free until tomorrow night. 
You can point your agent at our docs at
https://quebec.yarn.so
, and send audio on its own or with your own transcript. After that, it costs $0.32 per hour with no signup (minimum $10 top-up). We serve it at cost. Caveats: only tested in English and slower than ElevenLabs.
Let us know if Quebec works well for you, and send us any samples that work badly (you can email support at yarn dot so). Also let us know if you've built or found a better aligner. In theory we would just switch to a better aligner, although we would probably just push a bit harder to make ours better.
Thanks!
Jasper
