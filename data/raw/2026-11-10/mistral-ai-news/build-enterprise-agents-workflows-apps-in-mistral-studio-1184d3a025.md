---
title: "Build Enterprise Agents, Workflows & Apps in Mistral Studio"
url: "https://mistral.ai/news/build-with-studio"
source_url: "https://mistral.ai/news/build-with-studio"
canonical_url: "https://mistral.ai/news/build-with-studio"
source: "Mistral AI News"
source_type: "official"
published_at: ""
fetched_at: "2026-11-10T04:30:14+00:00"
content_type: "markdown"
is_list_page: false
---

# Le Chonk brings the brains. Studio puts it to work.

Thinking

Summary

Mistral Large 4 (Le Chonk) enhances enterprise AI with advanced coding, cybersecurity, and document reasoning, while Mistral Studio provides a flexible platform for deploying agents, workflows, and apps across cloud, VPC, or on-premises environments. New features like managed agents, workflows, and enterprise context streamline business processes, enabling faster development and deployment of AI solutions. Customers like ABANCA and BNP Paribas already use Studio to automate tasks, improve efficiency, and maintain full control over their AI systems.

Mistral Large 4 (Le Chonk) pushes the frontier of what enterprises can build with open models. It does great for <u>coding</u>, delivers advanced <u>defensive cybersecurity capabilities</u>, and brings powerful reasoning to <u>complex documents</u> and <u>business tasks</u>.

Mistral Studio is our enterprise AI platform for putting that intelligence to work in your business. It lets your teams activate models quickly through agents, workflows and apps connected to your enterprise data and systems. Deploy them wherever you choose: in the cloud, in your own VPC, on-premises or across a combination of environments. And retain full control and understanding of the intelligence you create, from how your systems work to the knowledge they build.

Today, we’re expanding Studio with managed agents and apps, alongside new capabilities for workflows, enterprise context, agent observability and evaluations.

Customers and partners including ABANCA, Accenture, Alten, BNP Paribas, Capgemini, CMA CGM and Tata Consultancy Services already use Studio in production. With this release, your developers can build and deploy new use cases faster, then reuse that work across more of the business.

## **Agents, workflows and apps for your business processes**

Agents, workflows and apps serve different parts of a business process. An agent investigates and acts, a workflow coordinates execution and approvals, and an app gives employees a way to use these systems.

Studio brings all three together on shared infrastructure. You start with a model like Le Chonk and connect it to your enterprise data and systems through connectors and MCP servers. That foundation lets you easily build agents, workflows and apps with access to the context they need. Studio manages how they run and lets teams inspect what happened.

Through the new Mistral MCP server, developers can build with Mistral Vibe or the coding agent they already use, test locally and deploy to their Studio environment with one command. Studio handles hosting and execution, so teams can build on that foundation to get each new use case into production faster.

### **Build managed agents that investigate and act**

In Studio, developers can now build agents that carry out complex, multi-step tasks. Developers can equip them with skills that capture the team’s procedures, sandboxes where they can run code, and subagents to delegate parts of a task. Hooks let developers add custom logic at key points in execution, shaping how the agent works and integrates with existing systems.

Studio manages the runtime behind all that work, using the proven infrastructure that supports millions of Mistral Vibe sessions each week. Developers can focus on the agent’s capabilities and behaviour, while setting boundaries on the tools, data and actions it can access. That means getting capable agents into production faster, with less infrastructure to build and more control over how your agents operate.

Our engineering team built an agent in Studio to investigate production incidents. When an alert fires, engineers need to work out what happened, often under pressure to resolve the issue. The agent starts the investigation: it follows the team’s runbook, asks for approval before taking sensitive actions and posts its findings in Slack. Engineers pick up the investigation with useful context already gathered, saving the team hundreds of hours each month.

### **Automate processes with workflows**

Workflows define how a process runs: which steps follow fixed rules, where an agent reasons and when a person decides. Interrupted runs can resume where they left off. Teams can describe a process in Mistral Vibe and use it to generate, test and deploy a workflow, with code they can inspect and edit. Today’s release also adds event triggers from enterprise systems and a visual graph that makes each workflow’s logic easier to inspect.

Our product operations team built a workflow in Studio to sort ideas from internal teams and feedback from customers. Routing each submission to the right people is one of the team’s routine tasks, but one that takes time. A model identifies bugs and feature requests, then routing rules send them to the appropriate team. This saves the product operations team about 35 hours a week.

### **Build apps ready for enterprise use**

Coding agents make it easy to build an application, but putting it to work across an enterprise means meeting requirements for security, access and reliability. Studio provides hosting, authentication and access controls, helping developers get applications ready for enterprise use faster. Teams can build with pre-approved, reusable components, reducing the amount of new code that needs security review.

These applications can use agents and workflows, retrieve enterprise documents through search indexes and access shared context in Studio. Developers can test locally, then deploy with one command to make the application available at its own link or inside Mistral Vibe.

Our Applied AI team, which helps customers build AI solutions, built a staffing app in Studio. Previously, staffing a project meant manually matching team profiles and past experience against requirements spread across documents and tools.

The app uses an agent to recommend people and explain how their experience fits the project. Staffing leads get a shortlist with supporting evidence ready to review, helping Mistral assemble teams faster and uncover expertise that might otherwise be overlooked when staffing complex customer AI projects.

Each use case leaves the enterprise better equipped to build the next. More engineering effort goes into improving operations, with less time spent rebuilding the infrastructure around them.

## **Keep your AI sovereign**

Studio gives you control over where your AI runs, how it operates and the intelligence you build. Deploy both the models and the platform in your own cloud, VPC or on-premises environment. You can also use Mistral-hosted deployments or combine environments to meet your requirements. Sensitive data and the processes built around it can stay within your perimeter.

You choose the models, govern access to data and tools, and decide which actions require human approval. OpenTelemetry traces show each step of a run, including model calls, tool use and approvals, so your teams can see where a process slows down or fails. Evaluations let them test changes to prompts, models or tools against your own datasets before release. Those traces and evaluations remain theirs, preserving the operational knowledge they build through use.

Customers are already putting this into practice with systems built alongside our Solutions team. From penetration testing to KYC onboarding, they’re bringing <u>AI into critical operations</u> while keeping sensitive data and specialist knowledge under their control.

## **Get started**

Choose a process your team wants to improve and put Le Chonk to work in Studio.

- **Build an agent:** <u>Managed Agents documentation</u>· <u>Incident investigation cookbook</u>
- **Automate a process:** <u>Workflows documentation</u> · <u>Workflow cookbooks</u>
- **Create an app:** <u>Apps documentation</u> · <u>Document review cookbook</u>

Explore <u>interactive demos and enterprise use cases</u>, or read the <u>release notes</u> for the full list of updates.

For an enterprise rollout or a business-critical implementation, <u>talk to our team</u> about what you want to automate and where it needs to run.
