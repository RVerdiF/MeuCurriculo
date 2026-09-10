"""RafaelOS — Data Systems Console.

Entry point for the Streamlit app. One page, seven sections: hero, metrics,
console, experience, selected systems, core stack, contact. Interactive pieces
are same-origin islands (see `portfolio/islands`); everything else is static
HTML driven by `portfolio/data`, so the page has no expensive reruns.

Run locally:

    streamlit run app.py
"""

from __future__ import annotations

from portfolio.components import (
    contact,
    experience,
    hero,
    metrics,
    projects,
    shell,
    stack,
    terminal,
)


def main() -> None:
    shell.configure_page()
    shell.inject_design_system()
    shell.render_navigation()

    # 00 — hero
    hero.render()

    # 01 — metrics
    shell.section(
        "metrics",
        "01 / system metrics",
        "Documented numbers, each with a source",
        "Six years of production work, summarized by the numbers that can be "
        "checked. Every figure below comes from the shipped résumé.",
    )
    metrics.render()
    shell.section_end()

    # 02 — console
    shell.section(
        "terminal",
        "02 / data systems console",
        "Query this portfolio the way you query a system",
        "The same structured data that renders this page, exposed as a small command "
        "line. Fixed command set, allowlisted, and nothing runs on a server. The "
        "buttons under the prompt do everything the terminal does.",
    )
    terminal.render()
    shell.section_end()

    # 03 — experience
    shell.section(
        "experience",
        "03 / experience",
        "Career as system history",
        "Four engagements, each answering the same six questions: role, company, "
        "context, what I owned, impact and stack. The architecture lives in the "
        "systems below, where it belongs.",
    )
    experience.render_roles()
    experience.render_credentials()
    shell.section_end()

    # 04 — selected systems
    shell.section(
        "projects",
        "04 / selected systems",
        "Four systems, opened up",
        "Each one carries the same six blocks: problem, what I built, architecture, key "
        "decisions, stack and impact. The architecture map is interactive, so you can "
        "see what each stage actually does.",
    )
    projects.render_selected()
    shell.section_end()

    # 05 — core stack
    shell.section(
        "stack",
        "05 / core stack",
        "Fourteen technologies, with references",
        "Grouped by what they are for rather than by percentage. Every technology "
        "shows where it was used, so the list is evidence instead of a logo wall.",
    )
    stack.render()
    shell.section_end()

    # 06 — contact
    contact.render()


main()
