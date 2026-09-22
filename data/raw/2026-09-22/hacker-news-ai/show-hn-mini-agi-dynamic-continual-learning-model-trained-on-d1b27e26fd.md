---
title: "Show HN: Mini-AGI – Dynamic continual learning model trained on 8GB VRAM"
url: "https://github.com/volotat/mini-AGI/"
source_url: "https://news.ycombinator.com/item?id=49783133"
canonical_url: "https://github.com/volotat/mini-AGI/"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-09-21T04:42:37+00:00"
fetched_at: "2026-09-22T01:28:29+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49783133
Original URL: https://github.com/volotat/mini-AGI/
Author: volotat
Score: 249

Sorry for the pretentious name, I know, I know.. It just contains all the pieces I would like to see a AGI model to have, and I can't stand the temptation. Before throwing rocks at me, please take a glance at the Readme, and I hope it will cover your mood a little bit.
So, first of all it does work and you can see the sample from the whole training run here:
https://raw.githubusercontent.com/volotat/mini-AGI/refs/head...
Here is the scaling law graph I have so far, and it looks very promising:
https://github.com/volotat/mini-AGI/blob/main/assets/scaling...
The model was built under my deep dissatisfaction so we cannot really train even moderately big models (1B+ scale) on the consumer's hardware. We can inference and fine-tune them for sure, but I would like to have full control over what the model sees over the training run, so it is fully aligned with my interests, not some corporations.
I was thinking about for some time and come up with two interesting ideas I thought worth pursuing: MoE with a lot of experts that gets added and pruned from the model while it trains, where only a small subset of of experts are actually in use at any particular moment + batch 1 training on the single continuous stream of data.
First allows us to be bounded only by the disk space in terms of number of parameters and load and unload experts only when they are needed. The second (if figured out and it turns out to be doable) allows us to get aways with small VRAM capacity because we do not need to store big randomized batches and their respective gradients.
I started brainstorming with Claude and after some time we found an approach that seems to be promising, and low and behold, a few weeks pass and you can see the results yourself.
Obviously, I did use AI in the process of making this project and I am pretty sure it would be completely impossible for me to do something like this without it, so I hope it is more than justified.
The model is still running over the first of 7.8B characters corpus I selected for training, so the weights are not out yet, and it's about a couple weeks of waiting until they are cooked at the current reading speed. And yeah, the model just read continuous interleaved passages from the dataset, each by 32K characters long each as a single stream. Just as you or I would do.
The set up seems to be really simple so you can git clone the project, run it and observe everything for yourself.
Thanks for your attention.
