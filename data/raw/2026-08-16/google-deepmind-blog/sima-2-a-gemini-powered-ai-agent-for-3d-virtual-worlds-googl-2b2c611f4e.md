---
title: "SIMA 2: A Gemini-Powered AI Agent for 3D Virtual Worlds — Google DeepMind"
url: "https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds"
source_url: "https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds"
canonical_url: "https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds"
source: "Google DeepMind Blog"
source_type: "official"
published_at: ""
fetched_at: "2026-08-15T23:21:35+00:00"
content_type: "markdown"
is_list_page: false
---

# SIMA 2: An Agent that Plays, Reasons, and Learns With You in Virtual 3D Worlds

Last year, we introduced SIMA (Scalable Instructable Multiworld Agent), a generalist AI that could follow basic instructions across a wide range of virtual environments. SIMA was a crucial first step in teaching AI to translate language into meaningful action in rich, 3D worlds.

Today we’re introducing SIMA 2, the next milestone in our research creating general and helpful AI agents. By integrating the advanced capabilities of our Gemini models, SIMA is evolving from an instruction-follower into an interactive gaming companion. Not only can SIMA 2 follow human-language instructions in virtual worlds, it can now also think about its goals, converse with users, and improve itself over time.

This is a significant step in the direction of Artificial General Intelligence (AGI), with important implications for the future of robotics and AI-embodiment in general.

## The Power of Reasoning

The first version of SIMA learned to perform over 600 language-following skills, like “turn left,” “climb the ladder,” and “open the map,” across a diverse set of commercial video games. It operated in these environments as a person might, by “looking” at the screen and using a virtual keyboard and mouse to navigate, without access to the underlying game mechanics.

With SIMA 2, we’ve moved beyond instruction-following. By embedding a Gemini model as the agent's core, SIMA 2 can do more than just respond to instructions, it can think and reason about them.

SIMA 2’s new architecture integrates Gemini’s powerful reasoning abilities to help it understand a user’s high-level goal, perform complex reasoning in pursuit, and skillfully execute goal-oriented actions within games.

We trained SIMA 2 using a mixture of human demonstration videos with language labels as well as Gemini-generated labels. As a result, SIMA 2 can now describe to the user what it intends to do and detail the steps it's taking to accomplish its goals.

In testing, we have found that interacting with the agent feels less like giving it commands and more like collaborating with a companion who can reason about the task at hand.

And thanks to our collaboration with our existing and new game partners (see, Acknowledgements), we have been able to train and evaluate SIMA 2 on a wider array of games.

This is the power of Gemini brought to embodied AI: a world-class reasoning engine that can now perceive, understand, and take action in complex, interactive 3D environments.

## A Leap in Generalization Performance

The addition of Gemini has also led to improved generalization and reliability. SIMA 2 can now understand more complex and nuanced instructions than its predecessor and is far more successful at carrying them out, particularly in situations or games on which it’s never been trained, such as the new Viking survival game, ASKA, or MineDojo - a research implementation of the popular open-world sandbox game, Minecraft.

### SIMA 2 can understand and accomplish long and complex tasks

### SIMA 2 understands multimodal prompts

### SIMA 2 can understand different languages and even emojis

Moreover, its capacity to transfer learned concepts — for instance, taking its understanding of "mining" in one game and applying it to "harvesting" in another —is foundational to achieving the kind of broad generalization seen in human cognition. Indeed, as a result of this ability, SIMA 2’s performance is significantly closer to that of a human player on a wide range of tasks.

### The Ultimate Test: Playing in Newly-Imagined Worlds

To test the limits of SIMA 2’s generalization abilities, we combined it with another groundbreaking research project, **Genie 3**, which can generate new, real-time 3D simulated worlds from a single image or text prompt.

When we challenged SIMA 2 to play in these newly generated worlds, we found it was able to sensibly orient itself, understand user instructions, and take meaningful actions toward goals, despite never having seen such environments before. It demonstrated an unprecedented level of adaptability.

## Towards Scalable, Multitask Self-Improvement

One of SIMA 2’s most exciting new capabilities is its capacity for self-improvement. We’ve observed that, throughout the course of training, SIMA 2 agents can perform increasingly complex and new tasks, bootstrapped by trial-and-error and Gemini-based feedback.

For example, after initially learning from human demonstrations, SIMA 2 can transition to learning in new games exclusively through self-directed play, developing its skills in previously unseen worlds without additional human-generated data. In subsequent training, SIMA 2’s own experience data can then be used to train the next, even more capable version of the agent. We were even able to leverage SIMA 2’s capacity for self-improvement in newly created Genie environments – a major milestone toward training general agents across diverse, generated worlds.

This virtuous cycle of iterative improvement paves the way for a future where agents can learn and grow with minimal human intervention, becoming open-ended learners in embodied AI.

## Looking to the Future: The Journey to General Embodied Intelligence

SIMA 2’s ability to operate across diverse gaming environments is a crucial proving ground for general intelligence, allowing agents to master skills, practice complex reasoning, and learn continuously through self-directed play.

While SIMA 2 is a significant step toward generalist, interactive, embodied intelligence, it is fundamentally a research endeavor, and its current limitations highlight critical areas for future work. We find the agents still face challenges with very long-horizon, complex tasks that require extensive, multi-step reasoning and goal verification. SIMA 2 also has a relatively short memory of its interactions - it must use a limited context window to achieve low-latency interaction. Finally, executing precise, low-level actions via the keyboard and mouse interface and achieving robust visual understanding of the complex 3D scenes remain open challenges that the entire field continues to address.

This research provides a fundamental validation for a new path in action-oriented AI. SIMA 2 confirms that an AI trained for broad competency, leveraging diverse multi-world data and the powerful reasoning of Gemini, can successfully unify the capabilities of many specialized systems into one coherent, generalist agent.

SIMA 2 also offers a strong path toward application in robotics. The skills it learned - from navigation and tool use to collaborative task execution - are some of the fundamental building blocks for the physical embodiment of intelligence needed for future AI assistants in the physical world.

## Responsible Development

SIMA 2 is an interactive, human-centered agent that’s fun to engage with, particularly in the entertaining way it explains its own reasoning. As with all our advanced and foundational technologies, we remain deeply committed to developing SIMA 2 responsibly, from the outset. This is particularly true with regard to its technical innovations, particularly the ability to self-improve.

As we’ve built SIMA 2, we’ve worked with our Responsible Development & Innovation Team. As we continue to explore the potential applications, we are announcing SIMA 2 as a limited research preview and providing early access to a small cohort of academics and game developers. This approach allows us to gather crucial feedback and interdisciplinary perspectives as we explore this new field and continue to build our understanding of risks and their appropriate mitigations. We look forward to working further with the community to develop this technology in a responsible way.

Learn more about SIMA

## Acknowledgements

This research was developed by the SIMA 2 team: Maria Abi Raad, John Agapiou, Frederic Besse, Andrew Bolt, Sarah Chakera, Harris Chan, Jeff Clune, Alexandra Cordell, Martin Engelcke, Ryan Faulkner, Maxime Gazeau, Arne Olav Hallingstad, Tim Harley, Ed Hirst, Drew Hudson, Laura Kampis, Sheleem Kashem, Thomas Keck, Matija Kecman, Oscar Knagg, Alexander Lerchner, Bonnie Li, Yulan Liu, Cong Lu, Maria Loks-Thompson, Joseph Marino, Kay McKinney, Piermaria Mendolicchio, Anna Mitenkova, Alexandre Moufarek, Fabio Pardo, Ollie Purkiss, David Reichert, John Reid, Tyson Roberts, Daniel P. Sawyer, Tim Scholtes, Daniel Slater, Hubert Soyer, Kaustubh Sridhar, Peter Stys, Tayfun Terzi, Davide Vercelli, Bojan Vujatovic, Jane X. Wang, Luyu Wang, Duncan Williams, and Lei M. Zhang.

For their leadership, guidance, and support, we thank: Satinder Singh Baveja, Adrian Bolton, Zoubin Ghahramani, Raia Hadsell, Demis Hassabis, Shane Legg, Volodymyr Mnih, and Daan Wierstra.

With much gratitude to partial contributors and past members: Alex Cullum, Karol Gregor, Rosemary Ke, Junkyung Kim, Matthew Jackson, Andrew Lampinen, Loic Matthey, Hannah Openshaw, and Zhengdong Wang.

Special thanks to all of the game developers who partnered with us: Coffee Stain (*Valheim, Satisfactory, Goat Simulator 3),* Foulball Hangover (*Hydroneer),* Hello Games (*No Man's Sky),* Keen Software House (*Space Engineers),* RubberbandGames (*Wobbly Life),* Strange Loop Games (*Eco),* Thunderful Games (*ASKA, The Gunk, Steamworld Build*), Digixart (*Road 96*), and Tuxedo Labs & Saber Interactive (*Teardown).*

We thank Vika Koriakin, Duncan Smith, Nilesh Ray, Matt Miller, Leen Verburgh, Ashyana Kachra, Phil Esposito, Dimple Vijaykumar, Piers Wingfield, Lucie Kerley for their invaluable partnership in developing and refining key components of this project.

We also thank Jack Parker-Holder, Shlomi Fruchter, and the rest of the Genie team for access to the Genie 3 model.

We’d like to recognize the many teams across Google and Google DeepMind that have contributed to this effort including Legal, Marketing, Communications, Responsibility and Safety Council, Responsible Development and Innovation, Policy, Strategy and Operations, and our Business and Corporate Development teams. We'd also like to thank all GDM teams that are not explicitly mentioned here for their continued support.

Finally, we dedicate this work to the memory of our colleagues Felix Hill and Fabio Pardo, whose contributions to our field continue to inspire us.
