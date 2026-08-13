# Yegor Brusnyak — CV & Portfolio

[![GitHub Pages](https://img.shields.io/badge/Deploy-GitHub_Pages-222?logo=github)](https://brusnyak.github.io/cv/)
[![Website](https://img.shields.io/badge/Site-brusnyak.github.io/cv-2554e8)](https://brusnyak.github.io/cv/)
[![PDF](https://img.shields.io/badge/CV-PDF-red)](https://brusnyak.github.io/cv/assets/yegor-brusnyak-cv.pdf)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

Applied AI engineer portfolio. Interactive website, printable PDF CV, and linked GitHub projects — all generated from this repository.

**Live site:** [brusnyak.github.io/cv](https://brusnyak.github.io/cv/)

---

## Quick Links

| What | Where |
| --- | --- |
| Website | [brusnyak.github.io/cv](https://brusnyak.github.io/cv/) |
| CV PDF | [assets/yegor-brusnyak-cv.pdf](assets/yegor-brusnyak-cv.pdf) |
| Bot CV PDF | [assets/yegor-brusnyak-bot-cv.pdf](assets/yegor-brusnyak-bot-cv.pdf) |
| Bot proof page | [bot/index.html](bot/index.html) |
| GitHub | [github.com/brusnyak](https://github.com/brusnyak) |
| LinkedIn | [linkedin.com/in/yegor-brusnyak](https://linkedin.com/in/yegor-brusnyak) |

---

## Repository Structure

```
cv/
├── index.html              # Portfolio website (single page)
├── README.md               # This file
├── assets/                 # Images, PDFs, styles, scripts
│   ├── yegor-brusnyak-cv.pdf
│   ├── yegor-brusnyak-bot-cv.pdf
│   ├── yegor-portrait.jpg  # og:image + bot proof page
│   ├── cv-framework.css    # bot proof page only
│   └── cv-framework.js     # bot proof page only
├── bot/                    # Bot development proof page
│   └── index.html
├── scripts/                # Build tools
│   └── build_pdfs.py
├── .github/workflows/      # CI/CD
│   └── static.yml          # GitHub Pages deployment
└── .gitignore
```

---

## Build Instructions

The website is a single static HTML page — no build step required.

### Serve locally

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

### Generate PDFs

Both PDFs are rendered from the HTML pages via Playwright. The PDFs always match the live page content.

```bash
pip install playwright
python3 -m playwright install chromium

python3 scripts/build_pdfs.py           # build both PDFs
python3 scripts/build_pdfs.py --main    # main CV only
python3 scripts/build_pdfs.py --bot     # bot CV only
python3 scripts/build_pdfs.py --serve   # build via local HTTP server (for JS-heavy pages)
```

**How it works:** `scripts/build_pdfs.py` loads the HTML page in headless Chromium and exports it as an A4 PDF using Playwright's `page.pdf()`. The HTML includes `@media print` CSS that strips interactive elements and optimises the layout for print. Update the HTML, re-run the script, and the PDF is in sync — no manual maintenance.

### Deploy

Push to `main` — the GitHub Action at `.github/workflows/static.yml` deploys to GitHub Pages automatically.

---

## Versioning

CV PDFs are versioned by date. The current release:

| Version | Date | Changes |
| --- | --- | --- |
| v2026.07 | Jul 2026 | Updated projects, added experience, improved skills |

Releases published on [GitHub Releases](https://github.com/brusnyak/cv/releases) with the PDF attached as a downloadable asset.

---

## Automation Roadmap

- [x] GitHub Pages deployment on push
- [x] PDF generation from HTML via Playwright
- [x] Automatic GitHub Release creation with PDF artifact
- [ ] Version badge in README

---

## License

MIT — see [LICENSE](LICENSE) (added automatically when releasing).

---

*Built by Yegor Brusnyak. Last updated: July 2026.*
