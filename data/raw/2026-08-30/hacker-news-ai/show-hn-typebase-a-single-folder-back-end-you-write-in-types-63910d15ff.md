---
title: "Show HN: Typebase – A single-folder back end you write in TypeScript"
url: "https://typebase.io"
source_url: "https://news.ycombinator.com/item?id=49447178"
canonical_url: "https://typebase.io"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-08-26T11:33:31+00:00"
fetched_at: "2026-08-30T01:08:20+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49447178
Original URL: https://typebase.io
Author: andrewww-dev
Score: 97

Hey HN!
I built Typebase, a library that gives you Convex's DX with Supabase's openness.
After trying Supabase I liked how fast it is to spin up a DB and auth, but really didn't like using RLS and SQL for authorization. With Convex I loved how your server "lives" in your code, but disliked the DB model and the realtime-first defaults.
With Typebase you just write TS files inside a typebase/ folder in your existing repo. You can define your DB tables inside a schema.ts file and export server functions that your frontend calls like local functions, fully typed. Auth is built in.
Then one CLI command uploads your server to any of the available providers (Vercel, Cloudflare Workers or Deno Deploy for the servera and Neon for the DB), or generates the code so you can deploy it wherever you want.
Built on top of oRPC, Drizzle, and better-auth.
Happy to answer any questions or feedback!
