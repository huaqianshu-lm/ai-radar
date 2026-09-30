---
title: "We tested our own WAF with frontier AI models. Here’s what we found"
url: "https://blog.cloudflare.com/adaptive-ai-waf-testing/"
source_url: "https://blog.cloudflare.com/adaptive-ai-waf-testing/"
canonical_url: "https://blog.cloudflare.com/adaptive-ai-waf-testing/"
source: "Cloudflare AI Blog"
source_type: "developer"
published_at: "2026-09-29T13:00:00+00:00"
fetched_at: "2026-09-30T01:52:38+00:00"
content_type: "markdown"
is_list_page: false
---

We built a WAF tester that adapted each request based on what the WAF blocked or passed. This helped us explore variations that a fixed test might miss. We ran it across six attack categories on an authorized staging environment and discovered detection gaps worth fixing.  Here’s how the loop worked, what got through, and what we did about it.
