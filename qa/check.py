"""QA harness for the portfolio.

Runs the real page in a real browser and checks the things a visitor depends
on: the page loads clean, identity and résumé are reachable, the terminal works
and refuses anything outside its command set, the systems expand, the stack
answers with evidence, and nothing breaks on narrow screens.

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

SECTIONS = ("home", "metrics", "terminal", "experience", "projects", "stack", "contact")
ISLANDS = {
    "terminal": "Portfolio terminal",
    "project": "Project architecture",
    "stack": "Core stack",
}


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


def frames_for(page: Page, title: str) -> list:
    found = []
    for frame in page.frames:
        try:
            if frame.evaluate("() => document.title") == title:
                found.append(frame)
        except Exception:
            continue
    return found


def terminal(page: Page):
    return frame_for(page, ISLANDS["terminal"])


def run_terminal(term, page: Page, command: str, wait: int = 350) -> str:
    term.fill("#term-input", command)
    term.press("#term-input", "Enter")
    page.wait_for_timeout(wait)
    return term.inner_text("#term-body")


def structure(page: Page, url: str) -> None:
    """Identity, résumé and links, in under a screen of scrolling."""
    for section in SECTIONS:
        check(f"section #{section} present", page.locator(f"#{section}").count() == 1)
    check("nav has 5 links", page.locator(".nav-links a").count() == 5)

    check("hero name rendered", "Rafael Verdi de Freitas" in page.inner_text(".hero-name"))
    hero = page.inner_text(".hero").lower()
    check("hero states the role", "data engineer" in hero and "analytics engineer" in hero)
    check("hero meta has 3 rows", page.locator(".hero-meta > div").count() == 3)
    check("availability stated once, in the nav",
          "available" in page.inner_text(".nav-status").lower() and
          "available" not in page.inner_text(".hero-meta").lower())
    check("hero has exactly 2 primary actions",
          page.locator(".hero-actions .btn").count() == 2,
          f"{page.locator('.hero-actions .btn').count()} buttons")
    check("hero has 2 secondary links", page.locator(".hero-links a").count() == 2)

    resume = page.locator("a[download]").first
    href = resume.get_attribute("href") or ""
    check("résumé download link present", href.endswith("CV.pdf"), href)

    response = page.request.get(url.rstrip("/") + "/app/static/CV.pdf")
    check("résumé is served as a PDF",
          response.ok and "application/pdf" in response.headers.get("content-type", ""),
          f"{response.status} {response.headers.get('content-type', '')}")

    linkedin = page.locator(".hero-links a").first.get_attribute("href") or ""
    github = page.locator(".hero-links a").nth(1).get_attribute("href") or ""
    check("LinkedIn points at the profile", "linkedin.com/in/rafael-verdi-de-freitas" in linkedin, linkedin)
    check("GitHub points at the profile", github.rstrip("/").endswith("RVerdiF"), github)

    check("metrics carry a source", page.locator(".metric-source").count() >= 3,
          f"{page.locator('.metric-source').count()} sources")
    check("experience lists 4 roles", page.locator(".role").count() == 4)
    check("credentials section present", page.locator(".card").count() >= 4)


def terminal_checks(page: Page) -> None:
    term = terminal(page)
    check("terminal island mounted", term is not None)
    if not term:
        return

    body = term.inner_text("#term-body")
    check("terminal boot banner", "portfolio data systems console" in body)

    body = run_terminal(term, page, "help")
    listed = sum(1 for name in ("help", "whoami", "experience", "projects", "stack", "grep", "open", "contact", "clear") if name in body)
    check("help lists the command set", listed == 9, f"{listed}/9 listed")

    body = run_terminal(term, page, "whoami")
    check("whoami returns identity", "Rafael Verdi de Freitas" in body)

    body = run_terminal(term, page, "experience")
    check("experience lists roles", "Banco Mercantil" in body and "Kraken" in body)
    body = run_terminal(term, page, "experience kraken")
    check("experience <company> details a role", "what I owned" in body and "impact" in body)

    body = run_terminal(term, page, "projects")
    check("projects lists the systems", "Fraud Analytics" in body and "PaySim" in body)
    body = run_terminal(term, page, "projects paysim")
    check("projects <id> details a system", "problem" in body and "key decisions" in body)

    body = run_terminal(term, page, "stack")
    check("stack lists groups", "LANGUAGES" in body and "AI / ML" in body)

    body = run_terminal(term, page, "grep dbt")
    check("grep finds a technology", "match(es)" in body, body.splitlines()[-1][:60] if body else "")
    body = run_terminal(term, page, "grep zzzz")
    check("grep reports no matches", "no matches" in body)

    body = run_terminal(term, page, "contact")
    check("contact prints the email", "rafaelverdifreitas@hotmail.com" in body)

    body = run_terminal(term, page, "definitelynotacommand")
    check("unknown command is refused", "command not found" in body)

    for removed in ("ls", "cat profile.md", "go projects", "sudo hire-rafael"):
        body = run_terminal(term, page, removed)
        check(f"removed command refused: {removed}", "command not found" in body)

    body = run_terminal(term, page, "__import__('os').system('id')")
    check("python injection is refused", "command not found" in body and "uid=" not in body)

    # history recall and tab completion
    term.fill("#term-input", "whoami")
    term.press("#term-input", "Enter")
    page.wait_for_timeout(200)
    term.press("#term-input", "ArrowUp")
    check("history recall works", term.input_value("#term-input") == "whoami")
    term.fill("#term-input", "exp")
    term.press("#term-input", "Tab")
    page.wait_for_timeout(150)
    check("tab completion works", term.input_value("#term-input").strip() == "experience")

    # chip buttons run commands too, so a non-terminal visitor is served
    before = term.inner_text("#term-body")
    term.locator(".chip-btn[data-cmd='projects']").click()
    page.wait_for_timeout(400)
    check("chip runs a command", term.inner_text("#term-body") != before)

    term.press("#term-input", "Control+l")
    page.wait_for_timeout(200)
    term.fill("#term-input", "whoami")
    term.press("#term-input", "Enter")
    page.wait_for_timeout(300)
    check("ctrl+L clears the log", "Rafael Verdi de Freitas" in term.inner_text("#term-body"))
    term.fill("#term-input", "clear")
    term.press("#term-input", "Enter")
    page.wait_for_timeout(300)
    check("clear empties the log", term.inner_text("#term-body").strip() == "")

    # the terminal drives the page it sits in
    run_terminal(term, page, "whoami")
    term.locator(".term-jump").last.click()
    page.wait_for_timeout(1200)
    top = page.evaluate("() => Math.round(document.getElementById('experience').getBoundingClientRect().top)")
    check("terminal jump scrolls the page", abs(top) < 120, f"#experience top={top}")


def project_checks(page: Page) -> None:
    projects = frames_for(page, ISLANDS["project"])
    check("4 project islands mounted", len(projects) == 4, f"{len(projects)} islands")
    if not projects:
        return

    first = projects[0]
    # Labels are CSS-uppercased and can wrap, so compare on collapsed whitespace.
    text = " ".join(first.inner_text(".proj").lower().split())
    for label in ("problem", "what i built", "architecture", "key decisions", "stack", "impact"):
        check(f"project block: {label}", label in text)

    nodes = first.locator(".arch-node")
    check("architecture has stages", nodes.count() >= 4, f"{nodes.count()} nodes")
    detail_before = first.inner_text("#arch-detail")
    check("architecture shows a detail panel", len(detail_before) > 30)
    nodes.last.click()
    page.wait_for_timeout(300)
    check("clicking a stage changes the detail", first.inner_text("#arch-detail") != detail_before)

    labels = [set(first.locator(".arch-node").all_inner_texts())]
    labels.append(set(projects[3].locator(".arch-node").all_inner_texts()))
    check("each project has its own architecture", labels[0] != labels[1],
          f"{sorted(labels[0])[:2]} vs {sorted(labels[1])[:2]}")

    paysim = projects[3]
    repo = paysim.locator("a.proj-link").first.get_attribute("href") or ""
    check("public project links its repository", "github.com/RVerdiF/PaysimViz" in repo, repo)
    check("professional project states it is confidential",
          "confidential" in projects[0].inner_text(".proj-links").lower())


def stack_checks(page: Page) -> None:
    stack = frame_for(page, ISLANDS["stack"])
    check("core stack island mounted", stack is not None)
    if not stack:
        return
    buttons = stack.locator(".tech-btn")
    check("core stack shows 14 technologies", buttons.count() == 14, f"{buttons.count()} buttons")
    check("technologies are grouped", stack.locator(".layer").count() == 9,
          f"{stack.locator('.layer').count()} groups")
    detail = stack.inner_text("#tech-detail")
    check("stack shows evidence for the default technology", "used in" in detail.lower())
    stack.locator(".tech-btn[data-tech-id='dbt']").click()
    page.wait_for_timeout(300)
    detail = stack.inner_text("#tech-detail")
    check("clicking a technology shows where it was used",
          "dbt" in detail.lower() and "sapiens" in detail.lower(), detail.splitlines()[:3])


def keyboard_checks(page: Page, url: str) -> None:
    """Walk the tab order from a clean load.

    Earlier interactions leave the focus deep inside an island, where Tab would
    move to the next frame instead of the next page element, so reload first.
    """
    page.goto(url, wait_until="networkidle")
    page.wait_for_timeout(2500)

    stops = []
    for _ in range(4):
        page.keyboard.press("Tab")
        page.wait_for_timeout(120)
        stops.append(
            page.evaluate(
                """() => {
                    const el = document.activeElement;
                    if (!el) return {tag: null};
                    const style = getComputedStyle(el);
                    return {
                        tag: el.tagName,
                        label: (el.textContent || '').trim().slice(0, 24),
                        outline: style.outlineStyle !== 'none' && parseFloat(style.outlineWidth) > 0
                    };
                }"""
            )
        )

    interactive = [stop for stop in stops if stop.get("tag") in {"A", "BUTTON"}]
    ringed = [stop for stop in stops if stop.get("outline")]
    check("tab reaches interactive elements", bool(interactive), json.dumps(stops[:2]))
    check("keyboard focus paints a ring", bool(ringed),
          json.dumps([s.get("label") for s in ringed][:2]))


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
        page.evaluate("() => document.getElementById('projects').scrollIntoView()")
        page.wait_for_timeout(1200)
        page.screenshot(path=str(SHOTS / f"{name}-projects.png"))
        if name == "mobile":
            term = terminal(page)
            if term:
                check("mobile: terminal input usable", term.locator("#term-input").is_visible())
                body = run_terminal(term, page, "whoami")
                check("mobile: terminal responds", "Rafael Verdi de Freitas" in body)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://127.0.0.1:8520/")
    args = parser.parse_args()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        errors: list[str] = []
        page.on("pageerror", lambda e: errors.append(f"pageerror: {e}"))
        page.on("console", lambda m: errors.append(f"console.{m.type}: {m.text}") if m.type == "error" else None)

        page.goto(args.url, wait_until="networkidle")
        page.wait_for_timeout(3500)

        structure(page, args.url)
        terminal_checks(page)
        project_checks(page)
        stack_checks(page)
        keyboard_checks(page, args.url)

        page.evaluate("() => window.scrollTo(0, 1200)")
        page.wait_for_timeout(400)
        nav_top = page.evaluate("() => Math.round(document.querySelector('.nav').getBoundingClientRect().top)")
        check("navigation stays fixed while scrolling", 0 <= nav_top <= 4, f"nav top={nav_top}")

        check("no page errors", not errors, "; ".join(errors[:3]))
        NOTES.extend(errors[:5])

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
