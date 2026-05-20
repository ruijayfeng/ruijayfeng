# Profile README Portfolio Design

## Goal

Redesign the GitHub Profile README for `ruijayfeng` into a refined portfolio-style profile. The page should feel like a designer/developer personal homepage: calm, editorial, visually considered, and focused on selected work instead of badge-heavy GitHub decoration.

## Direction

Use a "Gallery Cover" structure:

1. A wide hero banner that behaves like a portfolio cover.
2. A short identity section for Jay Feng.
3. A selected work section with three refined project cards.
4. A compact stack section.
5. A links/contact section.
6. A restrained contribution graph at the bottom.

## Visual Style

- Tone: minimal, editorial, premium, portfolio-like.
- Palette: near-white, ink black, soft gray, and one muted accent such as mist blue or graphite.
- Layout: generous whitespace, clean dividers, centered max-width content.
- Avoid: trophy walls, visitor counters, typing animations, excessive badges, heavy neon, terminal styling, and cluttered stats.
- Banner: replace the current terminal-flavored SVG with a new portfolio cover SVG using large type, fine rules, subtle geometric blocks, and a small descriptor line.

## Content Structure

Hero banner:

- Title: `Jay Feng`
- Descriptor: `Developer & Product-minded Builder`
- Supporting line: `Clean interfaces, reliable systems, and AI-powered tools.`

Intro:

- One short paragraph that positions Jay Feng as someone who designs and builds clean web experiences, backend systems, and AI-powered tools.

Selected Work:

- Three project cards using GitHub-compatible HTML tables.
- Each card includes a title, one-sentence description, stack tags, and a link.
- When exact project links are not available in the current repository context, use neutral "Coming soon" or profile-level links so the layout remains polished without invalid destinations.

Stack:

- Use restrained badges or text chips for core technologies.
- Keep the stack compact and curated.

Links:

- CSDN, Zhihu, Bilibili, and Email.
- Fix the current mojibake by rewriting README content as UTF-8 text.

Contribution:

- Keep the existing activity graph concept but restyle it to match the lighter portfolio theme.
- Place it after the main portfolio content so it supports the profile instead of leading it.

## Constraints

- Must render well on GitHub README without relying on external CSS.
- Use Markdown, simple HTML, shields, and SVG assets only.
- Keep the README easy to maintain manually.
- Do not add build tooling or GitHub Actions in this pass.

## Acceptance Criteria

- README no longer contains mojibake text.
- First viewport has a strong portfolio-cover visual.
- The page reads as a curated personal portfolio, not a stats dashboard.
- All links are clear and scannable.
- The contribution graph is visually subordinate to the selected work and identity sections.
