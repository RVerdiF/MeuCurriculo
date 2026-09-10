"""Experience: six answers per role, then a compact credentials strip.

Technical depth does not live here. Anything that needs architecture, data
flow or decisions belongs in the projects section, which is why this file is
short.
"""

from __future__ import annotations

import streamlit as st

from portfolio.config import esc
from portfolio.data.education import COURSES, EDUCATION, LANGUAGES
from portfolio.data.experience import EXPERIENCE, Role
from portfolio.data.projects import PROJECTS_BY_ID
from portfolio.data.stack import label_of


def _chips(role: Role) -> str:
    tech = "".join(f'<span class="chip">{esc(label_of(t))}</span>' for t in role.technologies)
    systems = "".join(
        f'<span class="chip chip--accent">{esc(PROJECTS_BY_ID[pid].name)}</span>'
        for pid in role.systems
        if pid in PROJECTS_BY_ID
    )
    return f'<div class="chips">{tech}{systems}</div>'


def _role(role: Role) -> str:
    current = " role--current" if role.current else ""
    status = " · current" if role.current else ""
    progression = ""
    if role.progression:
        steps = ' <span class="arrow" aria-hidden="true">→</span> '.join(
            f'<span class="step">{esc(step)}</span>' for step in role.progression
        )
        progression = f'<div class="role-progression"><span>progression</span>{steps}</div>'
    owned = "".join(f"<li>{esc(item)}</li>" for item in role.owned)
    impact = "".join(f"<li>{esc(item)}</li>" for item in role.impact)
    return f"""
    <article class="role{current}">
      <div class="role-head">
        <h3 class="role-title">{esc(role.title)}</h3>
        <span class="role-company">{esc(role.company)}</span>
        <span class="role-period">{esc(role.period)}{status}</span>
      </div>
      <div class="role-domain">{esc(role.context)} · {esc(role.location)}</div>
      {progression}
      <div class="role-columns">
        <div class="subsection">
          <div class="subsection-head"><span class="subsection-title">what I owned</span></div>
          <ul class="bullets">{owned}</ul>
        </div>
        <div class="subsection">
          <div class="subsection-head"><span class="subsection-title">impact</span></div>
          <ul class="bullets bullets--impact">{impact}</ul>
        </div>
      </div>
      {_chips(role)}
    </article>
    """


def render_roles() -> None:
    timeline = "".join(_role(role) for role in EXPERIENCE)
    st.html(f'<div class="wrap"><div class="timeline">{timeline}</div></div>')


def render_credentials() -> None:
    """Education, certifications and languages, folded in to keep the page short."""
    education = "".join(
        f"""
        <article class="card">
          <div class="card-title">{esc(item.title)}</div>
          <div class="card-sub">{esc(item.institution)} · {esc(item.period)}</div>
          <div class="card-body">{"".join(f"<div>{esc(d)}</div>" for d in item.details)}</div>
        </article>
        """
        for item in EDUCATION
    )
    courses = "".join(
        f'<li><span>{esc(course.name)}</span>'
        f'<span class="provider">{esc(course.provider)} · {esc(course.year)}</span></li>'
        for course in COURSES
    )
    languages = "".join(
        f'<li><span>{esc(name)}</span><span class="provider">{esc(level)}</span></li>'
        for name, level in LANGUAGES
    )
    st.html(
        f"""
        <div class="wrap">
          <div class="section-head" style="margin-top:var(--space-7)">
            <div class="eyebrow">education · certifications · languages</div>
            <h3 class="section-title">Formal grounding, kept current</h3>
            <p class="section-sub">
              Machine Learning Engineering on top of a management and data-analysis
              background. That combination is why the systems above are built around
              decisions as much as around tables.
            </p>
          </div>
          <div class="education-grid">{education}</div>
          <div class="education-grid" style="margin-top:var(--space-4)">
            <article class="card">
              <div class="card-title">Courses &amp; certifications</div>
              <div class="card-sub">{len(COURSES)} entries</div>
              <ul class="credential-list" style="margin-top:var(--space-3)">{courses}</ul>
            </article>
            <article class="card">
              <div class="card-title">Languages</div>
              <div class="card-sub">working languages</div>
              <ul class="credential-list" style="margin-top:var(--space-3)">{languages}</ul>
            </article>
          </div>
        </div>
        """
    )
