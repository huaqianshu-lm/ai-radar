---
title: "Show HN: Pocketty – iPhone SSH terminal that pings you when an agent is blocked"
url: "https://pocketty.app/"
source_url: "https://news.ycombinator.com/item?id=50009634"
canonical_url: "https://pocketty.app/"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-10-08T18:11:52+00:00"
fetched_at: "2026-10-09T02:49:33+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=50009634
Original URL: https://pocketty.app/
Author: lukeed
Score: 25

Hello~! pocketty is an SSH terminal for iPhone and iPad, made for herdr. herdr keeps your agent panes alive on your computer and knows the state of each one: working, needs you, or done.
I made this in anger/desperation for the latter half of my recent paternity leave. Nap traps are sweet, but there's only so much doom-scrolling and movie-watching I can handle... In any event, I've been using it for the last couple months and no longer
have
to be my desk anymore to be productive. Now the nap-traps are still productive (when i want them to be) !
How it works:
- The app talks to your computer directly over plain SSH. Tailscale is the easy way to reach it from anywhere but any SSH host you can reach works.
- A small Rust daemon on the host watches herdr. When a pane needs you, it seals the alert to your phone's key with HPKE (X25519, ChaCha20-Poly1305). A stateless relay (pocketty's) on Cloudflare Workers passes the sealed bytes to APNs (Apple Push Notification servers), and a notification extension opens them on the phone. The relay can't read them and keeps nothing.
- Your SSH key is made in the Secure Enclave and can't be exported.
- The terminal uses libghostty-vt for state and draws with wgpu on Metal, so full-screen TUIs look like they do on your desk, albeit narrower.
- Diffs for each agent turn, a file browser, and previews of `localhost` dev servers your agent starts, all through the same SSH connection. No port forwarding to set up.
herdr and the daemon are optional. Without them, it's a normal SSH client.
There's no account to set up and no analytics or tracking in the app. 
The app runs a 14-day free trial, with full feature access. Then, if you're as happy as I am with it, then it can be yours forever with a one-time purchase: $99 for the first two weeks (launch promo) then $129 after that.
Happy to answer anything about the sealed push setup or running libghostty on iOS.
