"""QA harness for the portfolio.

Runs the real page in a real browser: console errors, structure, terminal
interactions, island widgets, viewports, and a screenshot per viewport.

    python3 qa/check.py [--url http://127.0.0.1:8520/]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from playwright.sync_api import Page, sync_playwright

SHOTS = Path("/tmp/portfolio-qa")
FAILURES: list[str] = []
NOTES: list[str] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {name}" + (f" — {detail}" if detail else ""))
    if not condition:
        FAILURES.append(f"{name}: {detail}")


def frame_for(page: Page, title: str):
    for frame in page.frames:
        try:
            if frame.evaluate("() => document.title") == title:
                return frame
        except Exception:
            continue
    return None


def run(page: Page, url: str) -> None:
    errors: list[str] = []
    page.on("pageerror", lambda e: errors.append(f"pageerror: {e}"))
    page.on("console", lambda m: errors.append(f"console.{m.type}: {m.text}") if m.type == "error" else None)

    page.goto(url, wait_until="networkidle")
    page.wait_for_timeout(3500)

    # --- structure ---
    for section in ("home", "metrics", "terminal", "experience", "projects", "lab", "contact"):
        check(f"section #{section} exists", page.locator(f"#{section}").count() == 1)

    check("nav has 5 links", page.locator(".nav-links a").count() == 5)
    check("hero name rendered", "Rafael Verdi de Freitas" in page.inner_text(".hero-name"))
    check("résumé download link present", page.locator("a[download]").count() >= 1)
    check("résumé link points at static file",
          "app/static/CV.pdf" in (page.locator("a[download]").first.get_attribute("href") or ""),
          page.locator("a[download]").first.get_attribute("href") or "")
    check("details disclosures present", page.locator("details.disclosure").count() >= 5,
          f"{page.locator('details.disclosure').count()} disclosures")

    # --- document metadata / findable content ---
    check("page title is professional",
          "Data Engineer" in page.title() and "Rafael" in page.title(), page.title())
    visible = page.inner_text("body").lower()
    keywords = [word for word in ("data engineer", "dbt", "snowflake", "python", "fraud") if word in visible]
    check("recruiter keywords present in page content", len(keywords) >= 4, ",".join(keywords))

    # --- keyboard reachability ---
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    focused = page.evaluate(
        "() => { const el = document.activeElement; return el ? el.tagName + ':' + (el.textContent || '').trim().slice(0, 24) : 'none'; }"
    )
    check("tab reaches interactive content", focused.split(":")[0] in ("A", "BUTTON", "INPUT"), focused)
    focus_ring = page.evaluate(
        "() => { const el = document.activeElement; const cs = getComputedStyle(el); return cs.outlineStyle + '/' + cs.outlineWidth; }"
    )
    check("focus indicator is visible", "none" not in focus_ring.split("/")[0] or focus_ring.split("/")[1] not in ("0px", ""),
          focus_ring)

    # --- static résumé reachable ---
    href = page.locator("a[download]").first.get_attribute("href")
    response = page.request.get(url.rstrip("/") + "/" + href)
    check("static résumé serves 200", response.status == 200, f"status={response.status}")
    check("static résumé is a PDF", response.headers.get("content-type", "").startswith("application/pdf"),
          response.headers.get("content-type", ""))

    # --- terminal island ---
    term = frame_for(page, "Portfolio terminal")
    check("terminal island mounted", term is not None)
    if term:
        check("terminal boot banner", "portfolio data systems console" in term.inner_text("#term-body"))
        term.fill("#term-input", "whoami")
        term.press("#term-input", "Enter")
        page.wait_for_timeout(250)
        body = term.inner_text("#term-body")
        check("whoami prints identity", "Rafael Verdi de Freitas" in body and "6+" in body)

        term.fill("#term-input", "help")
        term.press("#term-input", "Enter")
        page.wait_for_timeout(250)
        body = term.inner_text("#term-body")
        check("help lists commands", "grep" in body and "cat" in body and "clear" in body)

        term.fill("#term-input", "grep dbt experience")
        term.press("#term-input", "Enter")
        page.wait_for_timeout(250)
        body = term.inner_text("#term-body")
        check("grep dbt returns matches", "match(es)" in body and "dbt" in body.lower())

        term.fill("#term-input", "stack")
        term.press("#term-input", "Enter")
        page.wait_for_timeout(250)
        body = term.inner_text("#term-body")
        check("stack prints layers", "TRANSFORM" in body and "dbt" in body)

        term.fill("#term-input", "cat experience/mercantil.md")
        term.press("#term-input", "Enter")
        page.wait_for_timeout(250)
        check("cat role file works", "Banco Mercantil" in term.inner_text("#term-body"))

        term.fill("#term-input", "ls projects")
        term.press("#term-input", "Enter")
        page.wait_for_timeout(250)
        check("ls projects lists files", "paysim.md" in term.inner_text("#term-body"))

        term.fill("#term-input", "rm -rf /")
        term.press("#term-input", "Enter")
        page.wait_for_timeout(250)
        check("unknown command is refused", "command not found" in term.inner_text("#term-body"))

        term.fill("#term-input", "sudo hire-rafael")
        term.press("#term-input", "Enter")
        page.wait_for_timeout(300)
        check("easter egg responds", "permission granted" in term.inner_text("#term-body"))

        # The island must survive its own commands: a mailto: used to navigate
        # the frame and silently kill everything the island drives.
        check("terminal island still alive after the egg", frame_for(page, "Portfolio terminal") is not None)
        check("palette trigger still live after the egg", page.locator("#rafaelos-palette-trigger").count() == 1)

        term.fill("#term-input", "__import__('os').system('id')")
        term.press("#term-input", "Enter")
        page.wait_for_timeout(250)
        check("python injection is refused", "command not found" in term.inner_text("#term-body"))

        # suggestion chip
        before = term.inner_text("#term-body")
        term.click(".chip-btn[data-cmd='impact']")
        page.wait_for_timeout(300)
        check("chip runs command", term.inner_text("#term-body") != before)

        term.fill("#term-input", "clear")
        term.press("#term-input", "Enter")
        page.wait_for_timeout(200)
        check("clear empties the log", term.inner_text("#term-body").strip() == "")

    # --- architecture explorer ---
    explorer = frame_for(page, "Architecture explorer")
    check("explorer island mounted", explorer is not None)
    if explorer:
        nodes = explorer.locator(".arch-node")
        check("explorer has nodes", nodes.count() >= 8, f"{nodes.count()} nodes")
        nodes.nth(3).click()
        page.wait_for_timeout(250)
        detail = explorer.inner_text("#arch-detail")
        check("explorer shows detail", len(detail) > 30)
        check("explorer detail has patterns", "PATTERNS" in detail or "ROLE IN THE SYSTEM" in detail)

    # --- stack map ---
    stackmap = frame_for(page, "Technology map")
    check("stack map island mounted", stackmap is not None)
    if stackmap:
        techs = stackmap.locator(".tech-btn")
        check("stack map has technologies", techs.count() >= 20, f"{techs.count()} buttons")
        target = stackmap.locator(".tech-btn[data-tech-id='dbt']")
        if target.count():
            target.click()
            page.wait_for_timeout(250)
            detail = stackmap.inner_text("#tech-detail")
            check("tech detail shows evidence", "dbt" in detail and "USED AT" in detail.upper())

    # --- query console ---
    console = frame_for(page, "Query my experience")
    check("query console island mounted", console is not None)
    if console:
        check("console shows a table", console.locator("table.result").count() == 1)
        console.click(".chip-btn[data-preset-id='financial_systems']")
        page.wait_for_timeout(250)
        check("preset returns rows", console.locator("table.result tbody tr").count() >= 1)
        console.fill("#console-input", "SELECT * FROM experience WHERE technology = 'snowflake';")
        console.press("#console-input", "Enter")
        page.wait_for_timeout(250)
        check("typed query resolves", console.locator("table.result tbody tr").count() >= 1)
        console.fill("#console-input", "DROP TABLE experience;")
        console.press("#console-input", "Enter")
        page.wait_for_timeout(250)
        check("unsupported query refused", "unsupported query" in console.inner_text("#result-note"))

    # --- ask the data ---
    ask = frame_for(page, "Ask the data")
    check("ask island mounted", ask is not None)
    if ask:
        questions = ask.locator(".ask-questions .chip-btn")
        check("ask has questions", questions.count() >= 5, f"{questions.count()} questions")
        questions.nth(2).click()
        page.wait_for_timeout(250)
        check("answer renders", len(ask.inner_text("#ask-answer")) > 60)
        ask.fill("#ask-input", "what has he automated?")
        ask.press("#ask-input", "Enter")
        page.wait_for_timeout(250)
        check("free question matches intent", "automation" in ask.inner_text("#ask-answer").lower()
              or "80%" in ask.inner_text("#ask-answer"))

    # --- command palette (same-origin injection into the page) ---
    trigger = page.locator("#rafaelos-palette-trigger")
    try:
        page.wait_for_selector("#rafaelos-palette-trigger", timeout=15000)
        found = True
    except Exception:
        found = False
    check("palette trigger injected into nav", found)
    if not found:
        return
    trigger.click()
    page.wait_for_timeout(400)
    check("palette opens", page.locator("#rafaelos-palette").count() == 1)
    page.fill("#rafaelos-palette .palette-input", "dbt")
    page.wait_for_timeout(300)
    items = page.locator("#rafaelos-palette .palette-item")
    check("palette filters", items.count() >= 1 and items.count() < 46, f"{items.count()} items")
    page.keyboard.press("Escape")
    page.wait_for_timeout(300)
    check("palette closes on escape", page.locator("#rafaelos-palette").count() == 0)

    # open a technology through the palette and confirm the stack map followed
    trigger.click()
    page.wait_for_timeout(300)
    page.fill("#rafaelos-palette .palette-input", "Technology: dbt")
    page.wait_for_timeout(300)
    page.locator("#rafaelos-palette .palette-item").first.click()
    page.wait_for_timeout(900)
    if stackmap:
        check("palette drove the stack map", "dbt" in stackmap.inner_text("#tech-detail").lower())

    # --- terminal command scrolls the page ---
    if term:
        term.fill("#term-input", "go projects")
        term.press("#term-input", "Enter")
        page.wait_for_timeout(1500)
        position = page.evaluate(
            "() => Math.round(document.getElementById('projects').getBoundingClientRect().top)"
        )
        check("terminal scrolls the page", 0 <= position <= 120, f"#projects top={position}")
        nav_top = page.evaluate("() => Math.round(document.querySelector('.nav').getBoundingClientRect().top)")
        check("navigation stays fixed while scrolling", 0 <= nav_top <= 4, f"nav top={nav_top}")

    check("no page errors", not errors, "; ".join(errors[:3]))
    NOTES.extend(errors[:5])


def viewports(page: Page, url: str) -> None:
    SHOTS.mkdir(parents=True, exist_ok=True)
    sizes = {
        "desktop": (1440, 900),
        "laptop": (1280, 800),
        "tablet": (834, 1112),
        "mobile": (390, 844),
    }
    for name, (width, height) in sizes.items():
        page.set_viewport_size({"width": width, "height": height})
        page.goto(url, wait_until="networkidle")
        page.wait_for_timeout(3000)
        overflow = page.evaluate(
            "() => ({scroll: document.documentElement.scrollWidth, client: document.documentElement.clientWidth})"
        )
        check(f"{name}: no horizontal overflow", overflow["scroll"] <= overflow["client"] + 1,
              json.dumps(overflow))
        page.screenshot(path=str(SHOTS / f"{name}-top.png"))
        page.evaluate("() => document.getElementById('lab').scrollIntoView()")
        page.wait_for_timeout(1200)
        page.screenshot(path=str(SHOTS / f"{name}-lab.png"))
        if name == "mobile":
            term = frame_for(page, "Portfolio terminal")
            if term:
                check("mobile: terminal input usable", term.locator("#term-input").is_visible())
                term.fill("#term-input", "whoami")
                term.press("#term-input", "Enter")
                page.wait_for_timeout(300)
                check("mobile: terminal responds", "Rafael Verdi de Freitas" in term.inner_text("#term-body"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8520/")
    args = parser.parse_args()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        run(page, args.url)
        viewports(page, args.url)
        browser.close()

    print("\n" + "=" * 70)
    print(f"{len(FAILURES)} failure(s)")
    for failure in FAILURES:
        print(" -", failure)
    print(f"screenshots: {SHOTS}")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
