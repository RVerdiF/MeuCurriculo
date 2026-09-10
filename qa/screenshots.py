"""Capture the pages/sections used for the visual review.

    python3 qa/screenshots.py [--url http://127.0.0.1:8520/] [--out /tmp/portfolio-qa/shots]
"""

from __future__ import annotations

import argparse
from pathlib import Path

from playwright.sync_api import Page, sync_playwright


def frame_for(page: Page, title: str):
    for frame in page.frames:
        try:
            if frame.evaluate("() => document.title") == title:
                return frame
        except Exception:
            continue
    return None


def shoot(page: Page, out: Path, name: str, section: str | None = None) -> None:
    if section:
        page.evaluate(f"() => document.querySelector('{section}').scrollIntoView({{block:'start'}})")
        page.wait_for_timeout(700)
    page.screenshot(path=str(out / f"{name}.png"))
    print("shot", name)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8520/")
    parser.add_argument("--out", default="/tmp/portfolio-qa/shots")
    args = parser.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 950})
        page.goto(args.url, wait_until="networkidle")
        page.wait_for_timeout(3500)

        for name, section in (
            ("01-hero", "#home"),
            ("02-metrics", "#metrics"),
            ("03-terminal", "#terminal"),
            ("04-experience", "#experience"),
            ("05-projects", "#projects"),
            ("06-lab", "#lab"),
            ("07-contact", "#contact"),
        ):
            shoot(page, out, name, section)

        page.locator(".timeline details.disclosure summary").first.click()
        page.wait_for_timeout(600)
        shoot(page, out, "08-experience-open", "#experience")

        page.locator(".proj-grid details.disclosure summary").first.click()
        page.wait_for_timeout(600)
        shoot(page, out, "09-project-open", "#projects")

        for name, title in (
            ("10-explorer", "Architecture explorer"),
            ("11-stackmap", "Technology map"),
            ("12-console", "Query my experience"),
            ("13-ask", "Ask the data"),
        ):
            frame = frame_for(page, title)
            if frame:
                frame.frame_element().screenshot(path=str(out / f"{name}.png"))
                print("shot", name)

        terminal = frame_for(page, "Portfolio terminal")
        if terminal:
            terminal.fill("#term-input", "help")
            terminal.press("#term-input", "Enter")
            page.wait_for_timeout(300)
            terminal.fill("#term-input", "grep snowflake")
            terminal.press("#term-input", "Enter")
            page.wait_for_timeout(400)
            terminal.frame_element().screenshot(path=str(out / "14-terminal-output.png"))
            print("shot 14-terminal-output")

        # palette open, over the page
        page.wait_for_selector("#rafaelos-palette-trigger", timeout=15000)
        page.locator("#rafaelos-palette-trigger").click()
        page.wait_for_timeout(500)
        page.screenshot(path=str(out / "15-palette.png"))
        print("shot 15-palette")
        page.keyboard.press("Escape")

        for name, width, height in (("16-mobile", 390, 844), ("17-tablet", 834, 1112)):
            page.set_viewport_size({"width": width, "height": height})
            page.goto(args.url, wait_until="networkidle")
            page.wait_for_timeout(3000)
            page.screenshot(path=str(out / f"{name}-top.png"))
            page.evaluate("() => document.querySelector('#terminal').scrollIntoView({block:'start'})")
            page.wait_for_timeout(600)
            page.screenshot(path=str(out / f"{name}-terminal.png"))
            page.evaluate("() => document.querySelector('#lab').scrollIntoView({block:'start'})")
            page.wait_for_timeout(800)
            page.screenshot(path=str(out / f"{name}-lab.png"))
            print("shot", name)

        browser.close()


if __name__ == "__main__":
    main()
