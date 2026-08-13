---
title: "Launch HN: Bullet (YC S26) – A Faster Coding Agent"
url: "https://www.codewithbullet.com"
source_url: "https://news.ycombinator.com/item?id=49283063"
canonical_url: "https://www.codewithbullet.com"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-08-13T08:14:30+00:00"
fetched_at: "2026-08-13T23:42:16+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49283063
Original URL: https://www.codewithbullet.com
Author: adi1
Score: 76

Hi HN! We’re Adi and Alex, founders of Bullet, a faster coding agent.
Bullet started in a senior year dorm. We were fresh out of working at AppLovin and Citadel, and naturally thought we were on a sure path to startup success. We were going to use our skills optimizing stock pricing calculation speeds and agent document context to take over the world. So, Bullet started as an AI hedge fund, a browser-use agent, synthetic financial data (oof), a mobile IDE, and a bunch of other things. We wanted to build something people wanted, but it seemed like everything we built was just terrible, useless, or both.
So, we decided to do something completely different, something completely out of the blue, something that no one had ever done before. Solve a problem we actually had.
Over the course of six pivots, we suffered. Throughout all of our adventures, one final boss kept getting in our way. Claude Code and his little brother Codex. We were spending hours waiting for coding agents like Claude Code and Codex, and got so frustrated to the point that I downloaded the Claude Code whip. We had spent months of time waiting for six codebases-worth of useless coding agent work.
Lightbulb moment. There’s nothing more noble than destroying the institutions! Let’s take on Claude Code and Codex, we can do it! Piece of cake!
And so, Bullet started off as a side project. We used the Claude Code to improve the Claude Code:
1. Model routing. Do you regret giving a task to Fable when it could have literally been done by Sonnet?
2. Targeted code + context search. We think embedding the whole repo is dumb. We also think sticking the whole context (or compressed context) in chat is dumb. So we do faster and better greps over both.
3. Aggressive context hygiene. Tool output is bounded, stale screenshots disappear, we don’t re-read files…the garbage never floods the model.
4. Efficient turns. Batch independent investigation, make one surgical edit, then perform one focused verification. Internal measurement showed 16% fewer round trips and 27% lower cost.
5. The Flash. We prayed to Barry Allen for speed.
And thank the Flash, he gave us speed! On SWE-bench Verified, Bullet resolved 479/500 (95.8%) in one attempt, averaging 119s per task, 35–67% faster than mini-SWE-agent + Fable/Sol depending on task. Full results and methodology here (
https://www.codewithbullet.com/blog/benchmark-results.html
)
Eventually we started using it every day and never went back.
Listed above were just some of the things about Claude Code that frustrated us the most, but we are constantly optimizing every day (look at that, maybe we did learn something from our jobs).
In our development, the biggest insight was that model speed matters less than reducing round trips. Independent searches, reads, and commands should happen in parallel, while dependent editing and verification stay sequential. One surprising obstacle was code search, small issues like regex-dialect mismatches caused silent misses and sent agents down completely wrong paths, so we built targeted search with fallbacks and bounded context. The most interesting use case so far has been long iterative work (like benchmarks, data pipelines, and evaluation loops), where each step depends on the last and running multiple agents can’t help as much.
Here’s the video demo (
https://www.youtube.com/watch?v=rWVmG5fRKgE
)
We hope that you guys try out Bullet if you are suffering with speed as much as we were, and we hope it brings you joy, rainbows, and faster responses. And if it’s terrible, let us know it’s terrible (we’re masochists btw)! We'll be in the comments all day, you can also contact us at bullet@davidhf.com.
You can try it at
https://codewithbullet.com
.
P.S: we hid a code on the website, see if you can unlock the secret page at the footer, all built with Bullet
