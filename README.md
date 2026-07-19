# Yegor Brusnyak Portfolio

[![Static Site](https://img.shields.io/badge/Site-static_HTML-111827)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS](https://img.shields.io/badge/Styling-custom_CSS-264DE4?logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![GitHub Pages](https://img.shields.io/badge/Deploy-GitHub_Pages-222222?logo=github&logoColor=white)](https://pages.github.com/)
[![Portfolio](https://img.shields.io/badge/Focus-AI_engineering_portfolio-0F766E)](https://brusnyak.github.io/cv/)

Responsive portfolio and CV site for presenting applied AI engineering projects, automation systems, bot workflows, voice-agent direction, and full-stack delivery.

Live site: [brusnyak.github.io/cv](https://brusnyak.github.io/cv/)

## Overview

This repository contains a static portfolio site for Yegor Brusnyak. The page positions Yegor as a computer science student and full-stack AI engineer focused on practical systems that combine LLM workflows, backend APIs, automation, messaging bots, and operator tooling.

The site is intentionally lightweight: one static HTML page with custom CSS, visual project cards, contact actions, responsive layout, and GitHub Pages deployment.

## Positioning

| Area | Message |
| --- | --- |
| Role target | Full-Stack AI Engineer, Applied AI Engineer, AI Automation Developer. |
| Core angle | Practical AI systems connected to real workflows, users, and data. |
| Proof style | Project cards, live demos, GitHub links, and concise implementation summaries. |
| Audience | Recruiters, founders, hiring managers, and technical reviewers. |

## Featured project themes

| Theme | Examples |
| --- | --- |
| AI workflow automation | AgentOps Control Room, Channel Agent Runtime, missed-call workflows. |
| Recruiting AI | AI Recruitment Copilot with CV/JD parsing, matching, scoring, and observability. |
| Messaging bots | Telegram, Discord, Slack, and WhatsApp-style bot runtime concepts. |
| Voice agents | Missed-call recovery and lead follow-up automation. |
| Full-stack delivery | Static portfolio, dashboards, backend APIs, and operator tools. |

## Design direction

The site uses an Aptifolio-inspired layout:

- Sticky profile rail with portrait and contact actions.
- Compact technical navigation.
- Light interface with strong accent colour.
- Responsive project cards with visual proof panels.
- Mobile-first stacking for small screens.
- Minimal static deployment without a frontend framework.

## Site structure

```text
cv/
├── index.html                    # Portfolio content, styles, interactions, and layout
├── assets/                       # Portraits, project visuals, and supporting media
├── .github/workflows/static.yml  # GitHub Pages deployment workflow
└── README.md
```

## Deployment

The site deploys to GitHub Pages through `.github/workflows/static.yml`.

Deployment runs automatically on pushes to `main`.

Manual deployment is also available from the GitHub Actions tab through `workflow_dispatch`.

## Custom domain notes

Current public URL:

```text
https://brusnyak.github.io/cv/
```

Target custom domain direction:

```text
https://yegor.work.gd
```

Possible deployment paths:

| Option | Notes |
| --- | --- |
| GitHub Pages + CNAME | Point DNS to GitHub Pages and add a `CNAME` file. |
| VPS deployment | Serve the static files from `62.197.243.163` behind Caddy or Nginx. |
| Vercel deployment | Use a separate Vercel static deployment if custom-domain setup is easier there. |

## README style direction

This repository follows the shared portfolio README structure, adjusted for a static personal site:

- Short positioning statement at the top.
- Technology and deployment labels for fast scanning.
- Structured positioning, project-theme, design, and deployment tables.
- No architecture diagram unless the site grows into a multi-service app.

## License

No license file is currently included in this repository.
