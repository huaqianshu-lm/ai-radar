---
title: "Show HN: Eigendrum - Draw any shape and hear what it sounds like as a drum"
url: "https://baselashraf81.github.io/eigendrum/"
source_url: "https://news.ycombinator.com/item?id=49246366"
canonical_url: "https://baselashraf81.github.io/eigendrum/"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-08-10T16:53:31+00:00"
fetched_at: "2026-08-15T23:21:35+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49246366
Original URL: https://baselashraf81.github.io/eigendrum/
Author: BaselAshraf81
Score: 191

Hi HN, I built Eigendrum, a web tool that solves the 2D wave equation for arbitrary shapes so you can hear what they sound like as drums.
How it works:
* Solves -∇²u = λu using finite element analysis (Kφ = λMφ) on a triangle mesh.
* Validated to <0.1% error against closed-form solutions for circles (Bessel zeros) and rectangles.
* Sound model factors in strike location, Rayleigh damping, and mallet width.
* Includes Kac drums I & II to demonstrate identical sound spectra from different geometries.
* No frameworks, build steps, or dependencies.
Repo and tests:
https://github.com/BaselAshraf81/eigendrum
Happy to answer any questions about the FEM solver or Web Audio setup!
https://eigendrum.com/#p=circle
