# Profile README Portfolio Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild the GitHub Profile README as a polished portfolio-style profile with a refined hero banner, selected work cards, curated stack, links, and a subdued contribution graph.

**Architecture:** This is a static README redesign. `README.md` owns the GitHub-rendered content and layout, while `assets/banner-hero.svg` owns the hero artwork. No build tooling, runtime code, or GitHub Actions are added.

**Tech Stack:** GitHub Markdown, GitHub-compatible inline HTML, SVG, shields.io badges, github-readme-activity-graph.

---

### Task 1: Replace Hero Banner Asset

**Files:**
- Modify: `assets/banner-hero.svg`

- [ ] **Step 1: Replace the current SVG with a portfolio-cover banner**

Write this full content to `assets/banner-hero.svg`:

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="420" viewBox="0 0 1280 420" role="img" aria-labelledby="title desc">
  <title id="title">Jay Feng portfolio banner</title>
  <desc id="desc">A refined editorial cover banner for Jay Feng's GitHub profile.</desc>
  <rect width="1280" height="420" rx="32" fill="#f7f5f0"/>
  <rect x="34" y="34" width="1212" height="352" rx="24" fill="#fbfaf7" stroke="#1f2933" stroke-opacity="0.12"/>
  <path d="M82 98H1198" stroke="#1f2933" stroke-opacity="0.18"/>
  <path d="M82 322H1198" stroke="#1f2933" stroke-opacity="0.18"/>
  <circle cx="1074" cy="160" r="82" fill="#dbe7e4"/>
  <rect x="1006" y="226" width="168" height="56" rx="28" fill="#1f2933"/>
  <rect x="916" y="116" width="92" height="148" rx="46" fill="#c8d2ff"/>
  <text x="82" y="86" font-family="Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="18" fill="#4b5563" letter-spacing="4">PORTFOLIO / GITHUB PROFILE</text>
  <text x="82" y="206" font-family="Georgia, Times New Roman, serif" font-size="82" fill="#111827">Jay Feng</text>
  <text x="88" y="255" font-family="Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="26" fill="#374151">Developer &amp; Product-minded Builder</text>
  <text x="88" y="296" font-family="Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="20" fill="#6b7280">Clean interfaces, reliable systems, and AI-powered tools.</text>
  <text x="1032" y="262" font-family="Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="15" fill="#fbfaf7">SELECTED WORK</text>
  <text x="82" y="358" font-family="Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" font-size="15" fill="#6b7280">Design-aware engineering · Open source · Practical software</text>
</svg>
```

- [ ] **Step 2: Sanity-check the SVG file exists**

Run: `Get-Item assets\banner-hero.svg | Select-Object Name,Length`

Expected: `banner-hero.svg` exists and has non-zero length.

### Task 2: Rewrite README Layout

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Replace README content with the portfolio layout**

Write this full content to `README.md`:

```md
<div align="center">
  <img src="./assets/banner-hero.svg" alt="Jay Feng - Developer and Product-minded Builder" width="100%" />
</div>

<br />

<div align="center">

### Developer & Product-minded Builder

I design and build clean web experiences, reliable backend systems, and AI-powered tools with a focus on clarity, maintainability, and useful interaction.

[Work](#selected-work) · [Stack](#stack) · [Links](#links) · [Contact](mailto:fz.dev@foxmail.com)

</div>

---

## Selected Work

<table>
  <tr>
    <td width="33%" valign="top">
      <h3>Interface Systems</h3>
      <p>Clean, practical interfaces for tools, dashboards, and product workflows.</p>
      <p><code>Frontend</code> <code>UX</code> <code>Design Systems</code></p>
      <a href="https://github.com/ruijayfeng">View profile</a>
    </td>
    <td width="33%" valign="top">
      <h3>Backend Craft</h3>
      <p>Reliable service-side architecture, data flow, and maintainable application logic.</p>
      <p><code>C++</code> <code>Backend</code> <code>Systems</code></p>
      <a href="https://github.com/ruijayfeng?tab=repositories">Browse repositories</a>
    </td>
    <td width="33%" valign="top">
      <h3>AI Tools</h3>
      <p>Small, useful experiments that combine automation, interaction, and product thinking.</p>
      <p><code>AI</code> <code>Automation</code> <code>Prototyping</code></p>
      <a href="mailto:fz.dev@foxmail.com">Discuss an idea</a>
    </td>
  </tr>
</table>

## Stack

<p>
  <img src="https://img.shields.io/badge/C++-111827?style=flat-square&logo=cplusplus&logoColor=white" alt="C++" />
  <img src="https://img.shields.io/badge/JavaScript-111827?style=flat-square&logo=javascript&logoColor=F7DF1E" alt="JavaScript" />
  <img src="https://img.shields.io/badge/Vue-111827?style=flat-square&logo=vuedotjs&logoColor=4FC08D" alt="Vue" />
  <img src="https://img.shields.io/badge/React-111827?style=flat-square&logo=react&logoColor=61DAFB" alt="React" />
  <img src="https://img.shields.io/badge/Node.js-111827?style=flat-square&logo=nodedotjs&logoColor=5FA04E" alt="Node.js" />
  <img src="https://img.shields.io/badge/AI_Tools-111827?style=flat-square&logo=openai&logoColor=white" alt="AI Tools" />
</p>

## Links

<p>
  <a href="https://blog.csdn.net/SDFsoul">
    <img src="https://img.shields.io/badge/CSDN-Writing-1f2933?style=flat-square" alt="CSDN" />
  </a>
  <a href="https://space.bilibili.com/YOUR_BILIBILI_ID">
    <img src="https://img.shields.io/badge/Bilibili-Video-1f2933?style=flat-square&logo=bilibili&logoColor=white" alt="Bilibili" />
  </a>
  <a href="https://www.zhihu.com/people/ruijayfeng">
    <img src="https://img.shields.io/badge/Zhihu-Notes-1f2933?style=flat-square&logo=zhihu&logoColor=white" alt="Zhihu" />
  </a>
  <a href="mailto:fz.dev@foxmail.com">
    <img src="https://img.shields.io/badge/Email-fz.dev%40foxmail.com-1f2933?style=flat-square" alt="Email" />
  </a>
</p>

## Contribution

<img src="https://github-readme-activity-graph.vercel.app/graph?username=ruijayfeng&bg_color=fbfaf7&color=374151&line=8fa6a3&point=111827&area=true&area_color=dbe7e4&hide_border=true" alt="Jay Feng GitHub activity graph" width="100%" />
```

- [ ] **Step 2: Check for mojibake**

Run: `Select-String -Path README.md,assets\banner-hero.svg -Pattern '馃|鑱|绀|闂|鐑|锟'`

Expected: no matches.

### Task 3: Verify Renderability and Git State

**Files:**
- Inspect: `README.md`
- Inspect: `assets/banner-hero.svg`
- Inspect: `docs/superpowers/specs/2026-05-20-profile-readme-portfolio-design.md`
- Inspect: `docs/superpowers/plans/2026-05-20-profile-readme-portfolio.md`

- [ ] **Step 1: Confirm referenced local asset path**

Run: `Test-Path assets\banner-hero.svg`

Expected: `True`.

- [ ] **Step 2: Inspect README headings**

Run: `Select-String -Path README.md -Pattern '^## |^### '`

Expected: headings for `Developer & Product-minded Builder`, `Selected Work`, `Stack`, `Links`, and `Contribution`.

- [ ] **Step 3: Review git diff**

Run: `git diff -- README.md assets/banner-hero.svg docs/superpowers/specs/2026-05-20-profile-readme-portfolio-design.md docs/superpowers/plans/2026-05-20-profile-readme-portfolio.md`

Expected: diff only contains the planned portfolio README redesign, SVG banner replacement, spec, and implementation plan.
