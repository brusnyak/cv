# Yegor Brusnyak - Portfolio

Responsive portfolio/CV site for AI automation, bot development, LLM workflows, and full-stack AI systems.

## Live

Current GitHub Pages URL:

https://brusnyak.github.io/cv/

Target custom domain:

[https://yegor.work.gd](https://yegor-brusnyak.vercel.app/)

## Positioning

The page presents Yegor as a computer science student and AI automation developer focused on practical systems:

- messaging bots and webhooks
- LangGraph/LLM workflow automation
- voice-agent and missed-call workflows
- backend APIs and operator tooling
- responsive frontend delivery

## Featured Projects

- Channel Agent Runtime - LangGraph-backed Telegram, Discord, Slack, and WhatsApp-style bot runtime.
- AI Recruitment Copilot - CV/JD parsing, RAG candidate matching, fit scoring, and observability.
- AgentOps Control Room - control room for configurable AI outbound workflows.
- Recareo / Missed-Call Automation - AI phone workflow direction for missed-call recovery and lead follow-up.

## Design Direction

Inspired by Aptifolio-style portfolio structure:

- sticky compact navigation
- profile rail with portrait and fast contact actions
- dark technical interface style
- project cards with visual proof panels
- responsive mobile-first stacking

## Deploy

This repository deploys to GitHub Pages through `.github/workflows/static.yml` on pushes to `main`.

For `yegor.work.gd`, either:

- point DNS to GitHub Pages and add a `CNAME` file, or
- deploy the static files to the VPS at `62.197.243.163` behind Caddy/Nginx.
