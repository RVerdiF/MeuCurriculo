"""Projects: public builds and confidential professional systems as artifacts."""

from __future__ import annotations

import streamlit as st

from portfolio.config import esc
from portfolio.data.projects import PROFESSIONAL_PROJECTS, PUBLIC_PROJECTS, Project


def _flow(project: Project) -> str:
    steps = "".join(
        f"""
        <div class="flow-stage">
          <div class="flow-key">{esc(step.label)}</div>
          <div class="flow-detail">{esc(step.detail)}</div>
        </div>
        """
        for step in project.data_flow
    )
    return f'<div class="flow">{steps}</div>'


def _list(items: tuple[str, ...]) -> str:
    entries = "".join(f"<li>{esc(item)}</li>" for item in items)
    return f'<ul class="bullets">{entries}</ul>'


def _disclosure_body(project: Project) -> str:
    blocks = [
        f"""
        <div class="subsection">
          <div class="subsection-head"><span class="subsection-title">problem</span></div>
          <div class="muted">{esc(project.problem)}</div>
        </div>
        """,
        f"""
        <div class="subsection">
          <div class="subsection-head"><span class="subsection-title">context</span></div>
          <div class="muted">{esc(project.context)}</div>
        </div>
        """,
        f"""
        <div class="subsection">
          <div class="subsection-head"><span class="subsection-title">data flow</span></div>
          {_flow(project)}
        </div>
        """,
    ]
    if project.architecture:
        blocks.append(
            f"""
            <div class="subsection">
              <div class="subsection-head"><span class="subsection-title">architecture</span></div>
              {_list(project.architecture)}
            </div>
            """
        )
    if project.decisions:
        blocks.append(
            f"""
            <div class="subsection">
              <div class="subsection-head"><span class="subsection-title">technical decisions</span></div>
              {_list(project.decisions)}
            </div>
            """
        )
    if project.outcome:
        blocks.append(
            f"""
            <div class="subsection">
              <div class="subsection-head"><span class="subsection-title">outcome</span></div>
              {_list(project.outcome)}
            </div>
            """
        )
    if project.lessons:
        blocks.append(
            f"""
            <div class="subsection">
              <div class="subsection-head"><span class="subsection-title">lesson</span></div>
              <div class="muted">{esc(project.lessons[0])}</div>
            </div>
            """
        )
    return "".join(blocks)


def _links(project: Project) -> str:
    parts: list[str] = []
    if project.repo:
        parts.append(
            f"<a class='proj-link' href='{esc(project.repo)}' target='_blank' "
            f"rel='noopener noreferrer'>repository ↗</a>"
        )
    if project.live:
        parts.append(
            f"<a class='proj-link' href='{esc(project.live)}' target='_blank' "
            f"rel='noopener noreferrer'>live demo ↗</a>"
        )
    if not parts:
        parts.append("<span class='dim'>confidential · no public link</span>")
    return "".join(parts)


def _card(project: Project) -> str:
    kind_label = "public project" if project.kind == "public" else "production system"
    kind_class = "proj-kind--public" if project.kind == "public" else ""
    stack = " · ".join(project.stack)
    return f"""
    <article class="proj">
      <div class="proj-head">
        <h3 class="proj-name">{esc(project.name)}</h3>
        <span class="proj-kind {kind_class}">{esc(kind_label)}</span>
      </div>
      <div class="proj-body">
        <p class="proj-tagline">{esc(project.tagline)}</p>
        <div class="proj-stack">{esc(stack)}</div>
        <details class="disclosure proj-disclosure">
          <summary>inspect system</summary>
          <div class="disclosure-body">{_disclosure_body(project)}</div>
        </details>
      </div>
      <div class="proj-foot">
        {_links(project)}
        <span class="dim" style="margin-left:auto">{esc(project.domain)}</span>
      </div>
    </article>
    """


def render_public() -> None:
    cards = "".join(_card(project) for project in PUBLIC_PROJECTS)
    st.html(f'<div class="wrap"><div class="proj-grid">{cards}</div></div>')


def render_professional() -> None:
    cards = "".join(_card(project) for project in PROFESSIONAL_PROJECTS)
    st.html(
        f"""
        <div class="wrap">
          <div class="section-head" style="margin-top:var(--space-7)">
            <div class="eyebrow">professional systems</div>
            <h3 class="section-title">Systems that shipped inside a business</h3>
            <p class="section-sub">
              Employer-confidential work, described at the level the résumé already
              publishes: what the system does, which decisions were made and what changed.
              Internal architecture, client names and their data stay out of it.
            </p>
          </div>
          <div class="proj-grid">{cards}</div>
        </div>
        """
    )
