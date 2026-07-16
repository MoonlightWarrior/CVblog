---
layout: about
title: about
permalink: /
lang: en
ref: about
subtitle: <a href='https://kaist.ac.kr/kr/'>KAIST</a> CS/MAS Undergraduate

profile:
  align: left
  image: prof_pic.jpg
  image_circular: true # crops the image to make it circular
  more_info: >
    <i class="fa-solid fa-location-dot"></i> Daejeon, Republic of Korea<br>
    <i class="fa-solid fa-envelope"></i> <a href="mailto:moonlightkim@kaist.ac.kr">moonlightkim@kaist.ac.kr</a>

selected_papers: false # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: true # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: false
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
---

<p class="typed-tagline" data-phrases="ML/AI Mathematical Theory|Optimization|Sparse Recovery|Explainable AI|Statistics">&gt;&nbsp;<span class="typed-text"></span><span class="typed-cursor">&#9608;</span></p>

I am a third-year undergraduate student in Computer Science and Mathematical Sciences at KAIST, with research interests across the mathematical foundations of machine learning. I expect to complete my B.S. in 2030 (including mandatory military service) and plan to pursue a Ph.D. in machine learning theory.

<div class="research-interests">
  <span>ML/AI Mathematical Theory</span>
  <span>Optimization</span>
  <span>Sparse Recovery</span>
  <span>Explainable AI</span>
  <span>Statistics</span>
</div>

<style>
  .research-interests {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 1rem;
  }
  .research-interests span {
    display: inline-block;
    padding: 0.32rem 0.75rem;
    border: 1px solid var(--global-theme-color);
    border-radius: 999px;
    font-size: 0.85rem;
    line-height: 1.1;
    color: var(--global-theme-color);
    transition: background-color 0.2s ease, color 0.2s ease;
  }
  .research-interests span:hover {
    background-color: var(--global-theme-color);
    color: var(--global-hover-text-color);
  }
</style>

<div class="optimizer-anim">
  <video class="only-light" autoplay loop muted playsinline disablepictureinpicture aria-label="Animation: gradient descent evolving into Adam">
    <source src="{{ '/assets/video/optimizer_light.webm' | relative_url }}" type="video/webm">
  </video>
  <video class="only-dark" autoplay loop muted playsinline disablepictureinpicture aria-label="Animation: gradient descent evolving into Adam">
    <source src="{{ '/assets/video/optimizer_dark.webm' | relative_url }}" type="video/webm">
  </video>
  <span class="optimizer-anim-caption">From a plain gradient step to Adam — momentum, then made adaptive.</span>
</div>
