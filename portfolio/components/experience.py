"""Experience — career as system history, with a deep dive per role."""

from __future__ import annotations

import streamlit as st

from portfolio.config import esc
from portfolio.data.education import COURSES, EDUCATION, LANGUAGES
from portfolio.data.experience import EXPERIENCE, Role
from portfolio.data.projects import PROJECTS_BY_ID
from portfolio.data.stack import STACK_TECHNOLOGIES


def _progression(role: Role) -> str:
    if not role.progression:
        return ""
    steps = ' <span class="arrow" aria-hidden="true">→</span> '.join(
        f'<span class="step">{esc(step)}</span>' for step in role.progression
    )
    return f'<div class="role-progression"><span>progression</span>{steps}</div>'


def _flow(role: Role) -> str:
    stages = "".join(
        f"""
        <div class="flow-stage">
          <div class="flow-key">{esc(stage.label)}</div>
          <div class="flow-detail">{esc(stage.detail)}</div>
        </div>
        """
        for stage in role.flow
    )
    return f'<div class="flow">{stages}</div>'


def _bullets(role: Role) -> str:
    items = "".join(f"<li>{esc(item)}</li>" for item in role.responsibilities)
    return f'<ul class="bullets">{items}</ul>'


def _impacts(role: Role) -> str:
    if not role.impacts:
        return ""
    items = "".join(
        f'<div class="impact"><div class="k">{esc(impact.label)}</div><div class="v">{esc(impact.detail)}</div></div>'
        for impact in role.impacts
    )
    return f'<div class="subsection"><div class="subsection-head"><span class="subsection-title">documented impact</span></div><div class="impact-row">{items}</div></div>'


def _systems(role: Role) -> str:
    if not role.systems:
        return ""
    chips = "".join(
        f'<span class="chip chip--accent">{esc(PROJECTS_BY_ID[pid].name)}</span>'
        for pid in role.systems
        if pid in PROJECTS_BY_ID
    )
    return f'<div class="subsection"><div class="subsection-head"><span class="subsection-title">systems built</span></div><div class="chips">{chips}</div></div>'


def _technologies(role: Role) -> str:
    names = [STACK_TECHNOLOGIES[t].name for t in role.technologies if t in STACK_TECHNOLOGIES]
    if not names:
        return ""
    chips = "".join(f'<span class="chip">{esc(name)}</span>' for name in names)
    return f'<div class="subsection"><div class="subsection-head"><span class="subsection-title">technologies</span></div><div class="chips">{chips}</div></div>'


def _role(role: Role) -> str:
    current = " role--current" if role.current else ""
    status = " · current" if role.current else ""
    return f"""
    <article class="role{current}">
      <div class="role-head">
        <h3 class="role-title">{esc(role.title)}</h3>
        <span class="role-company">{esc(role.company)}</span>
        <span class="role-period">{esc(role.period)}{status}</span>
      </div>
      <div class="role-domain">{esc(role.domain)} · {esc(role.location)}</div>
      <p class="role-mission">{esc(role.mission)}</p>
      {_progression(role)}
      <details class="disclosure">
        <summary>deep dive: how the system gets built</summary>
        <div class="disclosure-body">
          <div class="subsection">
            <div class="subsection-head"><span class="subsection-title">delivery chain</span></div>
            {_flow(role)}
          </div>
          <div class="subsection">
            <div class="subsection-head"><span class="subsection-title">responsibilities</span></div>
            {_bullets(role)}
          </div>
          {_impacts(role)}
          {_systems(role)}
          {_technologies(role)}
        </div>
      </details>
    </article>
    """


def render_roles() -> None:
    timeline = "".join(_role(role) for role in EXPERIENCE)
    st.html(f'<div class="wrap"><div class="timeline">{timeline}</div></div>')


def _education_card(item) -> str:
    details = "".join(f"<div>{esc(detail)}</div>" for detail in item.details)
    return f"""
    <article class="card">
      <div class="card-title">{esc(item.title)}</div>
      <div class="card-sub">{esc(item.institution)} · {esc(item.period)}</div>
      <div class="card-body">{details}</div>
    </article>
    """


def render_credentials() -> None:
    education = "".join(_education_card(item) for item in EDUCATION)
    courses = "".join(
        f'<li><span>{esc(course.name)}</span><span class="provider">{esc(course.provider)} · {esc(course.year)}</span></li>'
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
            <div class="eyebrow">education · credentials · languages</div>
            <h3 class="section-title">Formal grounding, kept current</h3>
            <p class="section-sub">
              Machine Learning Engineering on top of a management and data-analysis
              background. That combination is why the systems here are built around
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
