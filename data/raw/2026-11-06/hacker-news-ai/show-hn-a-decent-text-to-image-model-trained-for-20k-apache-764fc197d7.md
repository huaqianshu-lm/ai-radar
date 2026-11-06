---
title: "Show HN: A decent text-to-image model trained for ~$20K (Apache 2.0 Weights)"
url: "https://www.linum.ai/field-notes/pjit-21k"
source_url: "https://news.ycombinator.com/item?id=50368208"
canonical_url: "https://www.linum.ai/field-notes/pjit-21k"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-11-04T16:45:11+00:00"
fetched_at: "2026-11-06T03:15:50+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50368208
Original URL: https://www.linum.ai/field-notes/pjit-21k
Author: schopra909
Score: 164

My brother and I run a 2-person lab that trains our own generative video models from scratch. The ultimate goal is a set of creative tools that make it easier for anyone to make animation.
Video models today are too slow/expensive and lack sufficient controls. Creativity is an iterative process. You make, you tweak, you get better. In our opinion, they're not usable yet for storytelling.
When we set out to build Linum v3 (our next video model) earlier this year, the primary goal was to bring the cost envelope of inference down significantly. If our model is fast and cheap, it's the first step (of many) towards useful creative tools.
Typically, you see "latent diffusion models". A VAE (Variational Autoencoder) compresses the input data into a smaller "latent space" and the diffusion model learns how to generate within this subspace.
Over the past few months, we've been publishing our work on efficient pixel-space diffusion models. These throw away the VAE, having the diffusion model learn a latent-space optimized for its exact task.
This serves 3 purposes:
1) Simplify Architecture (no 2-stage model training)
2) Faster Convergence (11x faster convergence vs. our latent diffusion counterpart)
3) Cheaper Inference (4x more aggressive token reduction in attention context-windows, without significant loss in quality)
This past month we were pressure testing our latest architecture (Pyramid-JiT) by training a text-to-image model longer than the typical one-off experiment. Specifically, we trained it for ~$20K on 660M samples.
We were surprised by the quality of results, so we thought we'd release it as open weights for the community (Apache 2.0). The research itself is already public, on our website.
For us, it's a big stepping stone towards cheaper video models, since pretty much all video models start as image models. We like to say these models have to learn nouns before they learn verbs.
