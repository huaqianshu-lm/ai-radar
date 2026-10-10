---
title: "Show HN: Proton Drive for Linux"
url: "https://oss.lsantos.dev/proton-drive-linux-fs/"
source_url: "https://news.ycombinator.com/item?id=50003545"
canonical_url: "https://oss.lsantos.dev/proton-drive-linux-fs/"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-10-08T09:10:42+00:00"
fetched_at: "2026-10-10T02:09:20+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50003545
Original URL: https://oss.lsantos.dev/proton-drive-linux-fs/
Author: khaosdoctor
Score: 35

Hello everyone, I wanted to share this small project that I have.
It's born out of a necessity that I had, because Proton doesn't ship a Linux version of the drive yet (it's apparently coming out later this year but who knows?) and all the current solutions are hacky and wonky at best. But for the time being I really needed to mount my Proton drive on my Linux machine the way I mounted it on my Mac, so I (and my faithful AI slave) did this small utility that allows you to mount your Proton Drive in a FUSE FS like if it is a local folder.
It's fully written in Go because Proton's drive SDK and API libs are all in Go, and there's a community project on top of the reverse engineered proton API there too. I am not a Go developer, I know the foundations, so of course I used AI quite a lot, I am not super proud of it, but I am using it daily and testing it myself for a few months before releasing here.
Hope you like it, feedbacks are welcome, just please be mindful of the person on the other side :)
