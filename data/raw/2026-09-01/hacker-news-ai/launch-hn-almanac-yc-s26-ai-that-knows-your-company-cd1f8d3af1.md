---
title: "Launch HN: Almanac (YC S26) – AI that knows your company"
url: "https://usealmanac.com/"
source_url: "https://news.ycombinator.com/item?id=49511007"
canonical_url: "https://usealmanac.com/"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-08-31T15:34:34+00:00"
fetched_at: "2026-09-01T01:42:22+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49511007
Original URL: https://usealmanac.com/
Author: kushagrchitkar
Score: 47

Hi HN, I'm Kushagra, one of three founders of Almanac, a Hermes with a brain that knows everything about your company.
We started our journey with setting up Hermes for our company, thinking it must be easy. We wanted an agent that would know every context about our company, so we could ask questions and get context-appropriate responses to.
This started a very annoying and difficult journey. Setting up Hermes, getting it to talk right, building OAuth apps for every connector myself, then feeding it context myself, and ultimately struggling with Hermes's default memory. At the same time, we saw our YC batchmates struggling with the same problem, and we saw an opportunity.
So we built Almanac. This is how it works. You sign up, you get a Hermes agent straight out of the box. You have a one-click connect to any account (Gmail, Calendar, Granola, PostHog, etc). You have personal accounts (only accessible by you) and also shared accounts (accessible by everyone in the company). The consequence being I can never see my cofounders' accounts.
The “brain” of this agent is wikis. We pull in information from your connected sources, and start organizing this information in two wikis. A personal one, for you, which understands who you are, what your preferences are, the people in your life, and the things going on in your life. The second wiki is a company wiki, which includes what the company is, what you’re working on, what the roadmap is, and what the blockers of the company are. Your agent ultimately has access to these two wikis and the original accounts, which invoke the feeling of “it just knows you.”
Here’s a demo:
https://www.youtube.com/watch?v=ajXP5PHuK18
We're three cofounders, Rohan, Kushagra, and Divit, and we've been friends for 11 years, since studying for the IIT-JEE. We all did Electrical Engineering (Rohan at IIT Delhi, me at IIT Kharagpur, Divit at BITS Pilani, Hyderabad), and Rohan and I later went to Harvard, where this pre-compilation layer became our capstone thesis. We have built multiple products around the idea of a pre-compiled knowledge layer.
Our main differentiating point is the way we approach memory and context in general. Most AI assistant tools treat memory as an afterthought. We have worked on wikis for AI for more than a year now, building products for Harvard and NASA. The one thing we have learnt is that one needs to spend a lot more compute upfront, in the pre-compilation of this knowledge base, to get it right.
Having this pre-compiled knowledge base enables a lot of interesting ideas. First is a proactive agent. Since I have compiled what’s going on in both my company and my current life, Almanac can start completing tasks on its own. Concretely, we run a background worker which takes a look at tasks that could be completed, pings the main agent, who then pings me, suggesting which tasks it could automate. As a result, I wake up to proactive notifications which look like “I already prepared a draft of your fundraising pitch deck, want to take a look?”
Second, long-horizon tasks. In our wikis, we maintain a section on ongoing projects, so Almanac can pick a task back up days later without losing the thread. Most agents are session-bound: they run once, finish, and forget. But a lot of real work isn't one shot; it plays out over hours and days with people in the loop. The clearest example is anything that involves waiting on a human, like scheduling a meeting, following up on a sales thread, or chasing a document. Almanac can send an email on your behalf, and because it's always on and remembers the project, it notices the reply four hours later and drafts the right follow-up in context.
Since launching, we've seen a lot of use cases for Almanac. One person runs her dog-rescue operation through it: finding available fosters, tracking pickups, and sending reminders for consent forms. Another researches Polymarket strategies with Almanac, where its memory holds what past strategies were, proposes new ones, and compares them against what went right or wrong last time. Another builds marketing campaigns on it without having to re-explain the business and the whole campaign every single time.
Regarding privacy and security, Almanac only accesses accounts you explicitly connect. Your OAuth credentials are held by our connection provider, not in Almanac’s database. We only store the wiki and the source behind its citations. So an email used as a citation may be retained as Markdown.
We’re live:
https://usealmanac.com
. We have a 7-day trial on all of our plans. Happy to hear if people have done similar setups, and what new features they’d like in Almanac. If you’re a company that wants to get an agent that actually gets tasks done, I would love to talk:
https://cal.com/team/almanac/demo
.
