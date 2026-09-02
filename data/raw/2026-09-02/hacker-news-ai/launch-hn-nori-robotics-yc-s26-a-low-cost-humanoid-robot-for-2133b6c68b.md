---
title: "Launch HN: Nori Robotics (YC S26) – A low-cost humanoid robot for development"
url: "https://www.norirobotics.com/"
source_url: "https://news.ycombinator.com/item?id=49525153"
canonical_url: "https://www.norirobotics.com/"
source: "Hacker News AI"
source_type: "discovery"
published_at: "2026-09-01T17:35:10+00:00"
fetched_at: "2026-09-02T00:52:16+00:00"
content_type: "markdown"
is_list_page: false
---

HN story: https://news.ycombinator.com/item?id=49525153
Original URL: https://www.norirobotics.com/
Author: AntonioLi
Score: 112

Hey HN, I’m Antonio from Nori Robotics (
https://norirobotics.com
). We build a $1,688 bimanual mobile robot in San Francisco for robotics developers and researchers.
I started working on Nori while doing robotics research at Columbia. I was teaching robots through human demonstrations, but getting my hands on affordable hardware was difficult. Most labs have one or two expensive robots, which makes it hard to collect large datasets, run long experiments, or test across several robots.
So I built my own. After seven iterations the latest Nori has:
* 19 degrees of freedom
* Two 7+1 DOF arms with a 1.5 kg payload per arm
* A 55 kg telescoping lift
* A differential wheeled base
* Four 720p, 30 fps RGB cameras
* 2D lidar
* A dual microphone array with full-duplex voice communication
* A 432 Wh battery
* A Raspberry Pi 5 with 4 GB RAM (SLAM and safeties are run on board, heavier ACT and VLAs must be run from a computer via LAN or a server via WAN)
Getting this under $2,000 was the main engineering challenge. Nori has more than 100 moving and structural parts, so costs add up quickly across actuators, bearings, wiring, power delivery, and assembly. Some main choices we made to get the cost low was using high-ratio servos instead of QDD motors, and using a wheel base instead of legs.
We assemble each robot in San Francisco and have designed it to be easy to manufacture and repair (we offer 3D files to print repairs).
Our open SDK includes teleoperation and demonstration tools:
https://github.com/Nori-Robotics/nori-sdk-py
We also built a browser-based simulator so you can try it out:
https://lab.norirobotics.com/nori/model
We’ve shipped our first robot and are building the next batch. Eventually, we want people without robotics experience to teach Nori tasks and share them with other owners.
Currently the hardware is already capable of basic cleaning tasks, opening drawers, restocking shelves and pouring beers. Here is a video of Nori doing things:
https://youtube.com/shorts/VRfVXHfQvD8
We make money by selling the hardware for $1,688, with optional paid software on top. Parts of hardware are open source. More details are in our hardware paper:
https://doi.org/10.48550/arXiv.2605.16537
If you work in robotics, what would you build with a robot at this price? What would you change about the hardware?
