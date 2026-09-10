"""Page shell: configuration, stylesheet injection, navigation and section frames.

Streamlit renders each `st.html` block as an independent DOM fragment, so a
section is built as: a heading block (which owns the anchor id and the top
rule) → content blocks → an end block that carries the bottom spacing. No
markup is left unbalanced across calls.
"""

from __future__ import annotations

import streamlit as st

from portfolio.components import payloads
from portfolio.config import NAV_SECTIONS, esc, island_template, render_island, stylesheet
from portfolio.data.profile import PROFILE

PAGE_TITLE = "Rafael Freitas | Data Engineer & Analytics Engineer"
PAGE_DESCRIPTION = (
    "Data Engineer / Analytics Engineer with 6+ years building cloud data platforms, "
    "automated pipelines and analytics for banking institutions and digital-asset "
    "platforms. dbt, Snowflake, AWS, Python, MLOps."
)


def configure_page() -> None:
    """Streamlit page configuration (title, icon, layout, description)."""
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon="🛠",
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items={"Get help": None, "Report a bug": None, "About": f"{PAGE_TITLE} — {PAGE_DESCRIPTION}"},
    )


def inject_design_system() -> None:
    """Load the stylesheet into the page document.

    Note: document metadata (<meta>) cannot be injected here — Streamlit renders
    `st.html` fragments in the page body and drops head-only tags. The page
    title comes from `set_page_config`, and the professional summary is carried
    as visible content (hero + résumé section), which is what readers see.
    """
    st.html(f"<style>{stylesheet()}</style>")


def render_navigation() -> None:
    """Sticky top navigation. Plain anchors — no Streamlit reruns involved."""
    links = "".join(f"<a href='#{sid}'>{esc(label)}</a>" for sid, label in NAV_SECTIONS)
    st.html(
        f"""
        <nav class="nav" aria-label="Sections">
          <div class="nav-inner">
            <a class="nav-brand" href="#home">
              {esc(PROFILE.short_name.split()[0].lower())}<span>@</span>portfolio
            </a>
            <div class="nav-links">{links}</div>
            <div class="nav-spacer"></div>
            <div class="nav-side">
              <span class="nav-status">
                <span class="status-dot" aria-hidden="true"></span>
                {esc(PROFILE.status)}
              </span>
            </div>
          </div>
        </nav>
        """
    )


def section(section_id: str, eyebrow: str, title: str, sub: str = "") -> None:
    """Heading block for a section: anchor target, top rule and title."""
    sub_markup = f'<p class="section-sub">{esc(sub)}</p>' if sub else ""
    st.html(
        f"""
        <section class="section" id="{esc(section_id)}">
          <div class="wrap">
            <div class="section-head">
              <div class="eyebrow">{esc(eyebrow)}</div>
              <h2 class="section-title">{esc(title)}</h2>
              {sub_markup}
            </div>
          </div>
        </section>
        """
    )


def section_end() -> None:
    """Bottom spacing for the section that was just rendered."""
    st.html('<div class="section-end" aria-hidden="true"></div>')


def island(name: str, data: dict, label: str, note: str = "") -> None:
    """Mount an interactive island with a labelled frame.

    ``height="content"`` lets Streamlit measure the frame and grow it as the
    content grows; srcdoc frames are same-origin, which is what lets an island
    scroll the page around it (the terminal does).
    """
    note_markup = f'<span class="island-note">{esc(note)}</span>' if note else ""
    st.html(
        f"""
        <div class="wrap">
          <div class="island-head">
            <span class="island-title">{esc(label)}</span>
            {note_markup}
          </div>
        </div>
        """
    )
    st.iframe(render_island(island_template(name), data=data), height="content")


__all__ = [
    "configure_page",
    "inject_design_system",
    "island",
    "payloads",
    "render_navigation",
    "section",
    "section_end",
]
