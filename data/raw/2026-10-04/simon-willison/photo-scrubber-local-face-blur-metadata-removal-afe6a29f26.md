---
title: "Photo Scrubber — local face blur & metadata removal"
url: "https://simonwillison.net/2026/Sep/29/photo-scrubber/"
source_url: "https://simonwillison.net/2026/Sep/29/photo-scrubber/"
canonical_url: "https://simonwillison.net/2026/Sep/29/photo-scrubber/"
source: "Simon Willison"
source_type: "developer"
published_at: "2026-09-29T16:45:27+00:00"
fetched_at: "2026-10-04T02:26:47+00:00"
content_type: "markdown"
is_list_page: false
---

Tool:
Photo Scrubber — local face blur & metadata removal
I took a photograph of some protesters, then thought about how I don't like sharing photographs of strangers with identifiable faces. I
had GPT-6 Astra build
this experimental tool that would identify faces and automatically blur them out.
It uses Google's
MediaPipe
C++ library, compiled to WebAssembly via
@mediapipe/tasks-vision
, plus the
BlazeFace
face detection model.
Tags:
photography
,
tools
