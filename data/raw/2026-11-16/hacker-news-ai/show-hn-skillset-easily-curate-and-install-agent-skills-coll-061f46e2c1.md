---
title: "Show HN: Skillset: Easily curate and install agent skills collection"
url: "https://github.com/itsmeyaw/skillset"
source_url: "https://news.ycombinator.com/item?id=50511761"
canonical_url: "https://github.com/itsmeyaw/skillset"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-11-15T22:53:37+00:00"
fetched_at: "2026-11-16T02:36:10+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50511761
Original URL: https://github.com/itsmeyaw/skillset
Author: itsmeyaw
Score: 4

Hi everyone!
Installing skills globally in ~/.agents or ~/.claude consumes too much context, yet manually installing specific skills for every project is tedious. Wouldn't it be better to group skills for programming, backend architecture, or graphic design into collections, and install them with a single command only when needed?
To solve this, I built Skillset. It acts as a wrapper around the Vercel Skill CLI that batch-installs sets of skills from multiple sources using a single JSON file, essentially npm for skills!
While similar tools exist, most are written from scratch, which makes me concerned about their compatibility. Because Vercel’s Skill CLI is already the de facto standard (imo!), Skillset uses it directly as an underlying library. So it guarantees seamless compatibility across teams, regardless of whether they use Skillset or the standard Vercel CLI.
