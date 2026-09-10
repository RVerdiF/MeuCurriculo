"""RafaelOS — Data Systems Console.

Entry point for the Streamlit app. Renders one continuous page: navigation,
hero, metrics, terminal, experience, projects, lab and contact. Interactive
pieces are same-origin islands (see `portfolio/islands`); everything else is
static HTML driven by `portfolio/data`, so the page has no expensive reruns.

Run locally:

    streamlit run app.py
"""

from __future__ import annotations

from portfolio.components import (
    contact,
    experience,
    hero,
    lab,
    metrics,
    palette,
    projects,
    shell,
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
        "Six years of production work summarised by what can be verified. "
        "Every figure below is traceable to the shipped résumé.",
    )
    metrics.render()
    shell.section_end()

    # 02 — terminal
    shell.section(
        "terminal",
        "02 / console",
        "Query this portfolio the way you query a system",
        "The same structured data that renders this page, exposed as a small command "
        "line. Fixed command set, allowlisted, and nothing is executed on a server. "
        "Recruiters: the buttons under the prompt do everything the terminal does.",
    )
    terminal.render()
    shell.section_end()

    # 03 — experience
    shell.section(
        "experience",
        "03 / experience",
        "Career as system history",
        "Four engagements, ordered by what they built rather than by job title. "
        "Open any role to see the delivery chain: problem → signals → systems → outcome.",
    )
    experience.render_roles()
    experience.render_credentials()
    shell.section_end()

    # 04 — projects
    shell.section(
        "projects",
        "04 / projects",
        "Builds and production systems",
        "Public repositories with documentation, plus the confidential systems that "
        "shipped inside a business. Every card opens into problem, architecture, "
        "decisions and outcome.",
    )
    projects.render_public()
    projects.render_professional()
    shell.section_end()

    # 05 — lab
    shell.section(
        "lab",
        "05 / lab",
        "The parts you can play with",
        "Four interactions built the way I build platforms: an architecture explorer, "
        "a technology map with evidence, a fixed query console and a deterministic "
        "question lookup. No LLM API is called anywhere on this page.",
    )
    lab.render()
    shell.section_end()

    # 06 — contact + palette
    contact.render()
    palette.render()


main()
