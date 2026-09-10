"""Projects: four selected systems, each mounted as its own interactive island.

Each card arrives with its own architecture map, so the architecture is
evidence of real work rather than a generic diagram, and the page never tells
the same story twice.
"""

from __future__ import annotations

import streamlit as st

from portfolio.components import payloads, shell
from portfolio.config import esc
from portfolio.data.projects import PROJECTS


def _kind_label(kind: str) -> str:
    return "production system" if kind == "professional" else "public project"


def render_selected() -> None:
    for project in PROJECTS:
        shell.island(
            "project",
            payloads.project_payload(project.id),
            project.name,
            f"{_kind_label(project.kind)} · {project.domain}",
        )
        st.html('<div class="wrap" style="height:var(--space-6)"></div>')

    st.html(
        f"""
        <div class="wrap">
          <p class="section-note">
            {esc(str(len(PROJECTS)))} systems, chosen for what they show about how the work
            gets done. Confidential work is described at the level the résumé already
            publishes: internal architecture, client names and their data stay out of it.
          </p>
        </div>
        """
    )
