---
layout: about
title: 소개
permalink: /ko/
lang: ko
ref: about
nav: false
subtitle: <a href='https://kaist.ac.kr/kr/'>KAIST</a> 전산학부 · 수리과학과 학부생

profile:
  align: left
  image: prof_pic.jpg
  image_circular: true # crops the image to make it circular
  more_info: >
    <i class="fa-solid fa-location-dot"></i> 대한민국 대전<br>
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

<p class="typed-tagline" data-phrases="ML/AI 수학적 이론|최적화|희소 복원|설명 가능한 AI|통계학">&gt;&nbsp;<span class="typed-text"></span><span class="typed-cursor">&#9608;</span></p>

저는 KAIST 전산학부(CS)와 수리과학과(MAS)에 재학 중인 학부 3학년 학생이며, 기계학습의 수학적 기초를 중심으로 연구에 관심을 두고 있습니다. 2030년 KAIST에서 전산학 학사 학위를 마칠 예정이며(병역 의무 기간 포함), 이후 기계학습 이론 분야에서 박사 과정에 진학할 계획입니다.

<div class="research-interests">
  <span>ML/AI 수학적 이론</span>
  <span>최적화</span>
  <span>희소 복원</span>
  <span>설명 가능한 AI</span>
  <span>통계학</span>
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
  <video class="only-light" autoplay loop muted playsinline disablepictureinpicture aria-label="애니메이션: 경사하강법이 Adam으로 발전하는 과정">
    <source src="{{ '/assets/video/optimizer_light.webm' | relative_url }}" type="video/webm">
  </video>
  <video class="only-dark" autoplay loop muted playsinline disablepictureinpicture aria-label="애니메이션: 경사하강법이 Adam으로 발전하는 과정">
    <source src="{{ '/assets/video/optimizer_dark.webm' | relative_url }}" type="video/webm">
  </video>
  <span class="optimizer-anim-caption">단순한 경사 한 걸음에서 Adam으로 — 모멘텀, 그리고 적응적으로.</span>
</div>
