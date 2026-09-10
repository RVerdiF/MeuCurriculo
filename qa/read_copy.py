"""Eyeball the rendered copy: pull the page's visible text and a few island
answers, so the humanizer pass can be judged on what a visitor actually reads."""
from __future__ import annotations

from playwright.sync_api import sync_playwright

URL = "http://127.0.0.1:8520/"

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 1000})
    page.goto(URL, wait_until="networkidle")
    page.wait_for_timeout(1500)

    def show(title, text, limit=1400):
        print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")
        print(text[:limit])

    show("HERO", page.inner_text(".hero"))
    show("METRICS NOTE", page.inner_text(".metrics-grid + .section-sub"))
    show("ROLE MISSIONS", "\n\n".join(
        f"{p} / {c} / {m}\n  mission: {mi}"
        for p, c, m, mi in [
            (
                page.inner_text(f".role:nth-of-type({i}) .role-period"),
                page.inner_text(f".role:nth-of-type({i}) .role-company"),
                page.inner_text(f".role:nth-of-type({i}) .role-title"),
                page.inner_text(f".role:nth-of-type({i}) .role-mission"),
            )
            for i in range(1, 5)
        ]
    ), limit=2000)

    show("PROJECT LESSONS", page.inner_text("#projects"), limit=900)

    for title, selector in (("ASK: first intent", None), ("TERMINAL whoami", None)):
        pass

    # Terminal: run whoami + a grep
    term = next(
        f for f in page.frames if f.query_selector("#term-input")
    )
    term.fill("#term-input", "whoami")
    term.press("#term-input", "Enter")
    page.wait_for_timeout(400)
    term.fill("#term-input", "grep dbt experience")
    term.press("#term-input", "Enter")
    page.wait_for_timeout(500)
    show("TERMINAL OUTPUT", term.inner_text("#term-body"), limit=1800)

    ask = next(f for f in page.frames if f.query_selector("#ask-answer"))
    ask.click("#ask-questions button:nth-child(1)")
    page.wait_for_timeout(300)
    show("ASK: dbt", ask.inner_text("#ask-answer"))
    ask.click("#ask-questions button:nth-child(6)")
    page.wait_for_timeout(300)
    show("ASK: business impact", ask.inner_text("#ask-answer"))

    browser.close()
