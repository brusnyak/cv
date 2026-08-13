"""Render CV HTML pages to A4 PDFs via Playwright.

Usage:
    python3 scripts/build_pdfs.py              # build both PDFs
    python3 scripts/build_pdfs.py --main       # main CV only
    python3 scripts/build_pdfs.py --bot        # bot CV only
    python3 scripts/build_pdfs.py --serve      # start local server first, then build
"""

import argparse
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
MAIN_HTML = ROOT / "index.html"
BOT_HTML = ROOT / "bot" / "index.html"
MAIN_PDF = ASSETS / "yegor-brusnyak-cv.pdf"
BOT_PDF = ASSETS / "yegor-brusnyak-bot-cv.pdf"


def build_pdf(html_path: Path, output_path: Path, server_url: str | None = None) -> None:
    """Render an HTML file to A4 PDF using Playwright."""
    from playwright.sync_api import sync_playwright

    uri = server_url if server_url else html_path.resolve().as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(uri, wait_until="networkidle")
        # Wait for fonts and canvas to settle
        page.wait_for_timeout(800)
        page.pdf(
            path=str(output_path),
            format="A4",
            print_background=False,
        )
        browser.close()

    print(f"  -> {output_path.resolve()} ({output_path.stat().st_size / 1024:.0f} KB)")


def serve_and_build(html_path: Path, output_path: Path) -> None:
    """Start a local HTTP server, render, then kill the server."""
    server = subprocess.Popen(
        [sys.executable, "-m", "http.server", "8765", "--directory", str(ROOT)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        time.sleep(1)  # let server start
        url = f"http://localhost:8765/{html_path.relative_to(ROOT)}"
        build_pdf(html_path, output_path, server_url=url)
    finally:
        server.terminate()
        server.wait()


def main() -> None:
    parser = argparse.ArgumentParser(description="Build CV PDFs from HTML")
    parser.add_argument("--main", action="store_true", help="build main CV only")
    parser.add_argument("--bot", action="store_true", help="build bot CV only")
    parser.add_argument("--serve", action="store_true", help="start local HTTP server")
    args = parser.parse_args()

    build_main = args.main or not (args.main or args.bot)
    build_bot = args.bot or not (args.main or args.bot)

    ASSETS.mkdir(parents=True, exist_ok=True)

    if build_main and MAIN_HTML.exists():
        print("Building main CV PDF...")
        if args.serve:
            serve_and_build(MAIN_HTML, MAIN_PDF)
        else:
            build_pdf(MAIN_HTML, MAIN_PDF)

    if build_bot and BOT_HTML.exists():
        print("Building bot CV PDF...")
        if args.serve:
            serve_and_build(BOT_HTML, BOT_PDF)
        else:
            build_pdf(BOT_HTML, BOT_PDF)

    print("Done.")


if __name__ == "__main__":
    main()
