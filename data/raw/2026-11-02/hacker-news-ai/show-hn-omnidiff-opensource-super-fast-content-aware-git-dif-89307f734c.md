---
title: "Show HN: OmniDiff – Opensource, super fast, content aware Git difftool, in Rust"
url: "https://github.com/ivankovic/omnidiff"
source_url: "https://news.ycombinator.com/item?id=50325253"
canonical_url: "https://github.com/ivankovic/omnidiff"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-11-01T13:02:30+00:00"
fetched_at: "2026-11-02T02:09:01+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50325253
Original URL: https://github.com/ivankovic/omnidiff
Author: FabCH
Score: 165

I have been researching what the ultimate diff tool would look like, based on actual diffs in open source repositories.
OmniDiff can diff: code (25 languages), config, images, PDFs, archives, cursors, fonts...
It's fast. It can diff C++ files of tens of thousands of lines in under 100ms, on a 2023 ThinkPad T14s.
It's open source. AGPLv3.
It's based on real diffs. I looked at the 7400 repositories that are listed in Gentoo packages, sampled 2000 diffs and solved them manually to get a good understanding of what is needed, before putting together the diff pipelines for each content type. Incidentally, this also forms the basis of the CI pipeline, so the robustness of the codebase is quite high.
I'm still developing it. It's v0.3.0 at this time. But I have been using it daily as my git difftool for months now, and it works well.
AI Disclosure: Yes, I do use AI. No, I do not vibecode.
