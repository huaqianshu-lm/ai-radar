---
title: "Introducing Muse Image and Muse Video"
url: "https://ai.meta.com/blog/introducing-muse-image-muse-video-msl"
source_url: "https://ai.meta.com/blog/introducing-muse-image-muse-video-msl"
canonical_url: "https://ai.meta.com/blog/introducing-muse-image-muse-video-msl"
source: "Meta AI Blog"
source_type: "official"
published_at: ""
fetched_at: "2026-09-13T00:39:38+00:00"
content_type: "markdown"
is_list_page: false
---

We’re excited to launch Muse Image and preview Muse Video, the first media generation models developed by Meta Superintelligence Labs.

Muse Image is our most advanced image generation model yet: it follows instructions faithfully, edits with precision, and composes from multiple references. It also brings agentic tool use capabilities and integrates with Muse Spark. Muse Video, built on the same pretraining base, delivers exceptional visual fidelity with native audio support.

Muse Image is available today across the Meta AI app and on __meta.ai__, Instagram Stories in the US, and WhatsApp in limited countries, and is coming soon to Facebook. Muse Video is coming soon to creators and Meta AI.

Muse Image: Agentic Image Generation

Instead of directly mapping prompts to images, Muse Image operates as an agent: it invokes search and coding tools to improve accuracy, self-refines its own generations, and improves through scaling test-time compute. Muse Image also integrates with Muse Spark, allowing the two models to share tools and plan jointly for powerful agentic media generation.

Tool Use

We provide Muse Image with access to tools to enhance its agentic capabilities.

**Coding.** During reinforcement learning, Muse Image learns to write and execute code that produces accurate plots and QR codes, and condition on rendered figures to improve the accuracy of generated images. Muse Spark and Muse Image also integrate to use the combination of code and media generation to create animated GIFs, websites with embedded images, and interactive visual games.

**Search.** Muse Image learns to search the web to ground generated images in factual and real-time information and visual references. Enabling search improves factual accuracy on knowledge-intensive prompts, particularly those involving current events and real-world facts.

Muse Image improves with search tool use. Win rate from internal ablation.

Self-Refinement

Muse Image reflects on and improves upon its own work within its chain of thought. This self-refining behavior can take different forms: a local edit to the current image draft when a small detail is off, a new image generation from scratch when larger parts are wrong, or a different tactic like tool use for more factually accurate generation. We didn’t design this behavior. Instead, it emerged during RL training simply because self-refinement produced better images and therefore higher reward.

Muse Image improves with emergent self-refinement. Win rate from internal ablation.

Test-Time Compute Scaling

Like language models, Muse Image improves the more it thinks at inference time. With more test-time compute, the model reasons more, uses more tool calls, and uses more self-refinement steps to improve its generations. Increasing reasoning strength (and thus test-time compute) improves human-preference Elo scores and shows an approximately log-linear scaling relationship. Notably, this compute spans two very different kinds of work — text tokens for reasoning, visual tokens for generation — yet quality is a function of the combined total compute.

We find that using the token budget judiciously matters just as much for effective test-time scaling. Best-of-N (BoN), where the model generates several images and keeps the best, improves quality early but saturates quickly. Spending that same compute on deliberate reasoning scales considerably better. Reasoning and tool use compound when combined. Tools let the model reach beyond what it already knows, whether by searching for references it lacks or writing code to get precise details right, filling gaps that reasoning alone can’t.

Muse Image improves with scaling test-time compute. Elo from internal ablation.

Image Editing

Muse Image edits images with precision, changing exactly what the user asks for. It can follow a variety of instructions as our examples show.

Muse Image maintains coherence across editing turns, supporting iterative refinement and open-ended brainstorming toward a target result.

Multi-Reference Image Composition

Muse Image can compose elements from many input reference images in the prompt, including people, objects, clothing, styles, and environments. It supports interleaving text and images inline in prompts for complex image compositions.

Image Benchmarks

Muse Image holds the No. 2 spot on Arena for text-to-image, single-image editing, and multi-image editing as measured by human preference Elo rankings at the time of writing.

Arena Elo rankings as of July 5, 2026.

Previewing Muse Video

Alongside the release of Muse Image, we’re sharing an early preview of Muse Video. It offers competitive performance in prompt adherence, visual fidelity, and temporal consistency. We’re investing in areas with current performance gaps, such as audio-video synchronization and physically accurate fast motion. Muse Video is coming soon to creators and in Meta AI.

On Arena, Muse Video ranks No. 3 in human-preference Elo for text-to-video at the time of writing.

Arena Elo rankings as of July 5, 2026

Content Seal

To help people verify whether an image is AI-generated, Muse Image includes Content Seal, our invisible watermarking system. Images created by Muse Image in the Meta AI app and on __meta.ai__ carry a hidden provenance signal that stays intact — even when cropped, compressed, resized, or screenshotted. We plan to extend Content Seal to video soon. We’re previewing a __detection tool__ that lets you check whether an image carries a Content Seal watermark, providing an initial way to help you better understand if an image was made with Meta AI.

Muse Image in Meta Products

Muse Image connects deeply with the Meta ecosystem. Our ongoing investments in image and video generation will further enable creators and businesses to generate dynamic content across Meta products.

Marketing assets for small businesses

Personalized presets directly in Instagram

Our latest updates delivered to your inbox

Subscribe to our newsletter to keep up with Meta AI news, events, research breakthroughs, and more.
