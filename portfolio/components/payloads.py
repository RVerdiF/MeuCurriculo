"""Serialisers that turn the content layer into island payloads.

Islands are plain HTML/CSS/JS rendered inside same-origin `st.iframe` frames.
They receive data, never markup, so the browser side stays presentation-only
and user input can never be interpreted as HTML.
"""

from __future__ import annotations

from typing import Any

from portfolio.config import NAV_SECTIONS, SECTIONS
from portfolio.data.education import COURSES, EDUCATION
from portfolio.data.experience import EXPERIENCE, ROLES_BY_ID
from portfolio.data.profile import METRICS, PROFILE
from portfolio.data.projects import PROJECTS, PROJECTS_BY_ID
from portfolio.data.stack import CORE_BY_ID, CORE_STACK, label_of


def _tech_names(technology_ids: tuple[str, ...]) -> list[str]:
    return [label_of(tech_id) for tech_id in technology_ids]


def _evidence_label(kind: str, ref: str) -> str:
    if kind == "role":
        role = ROLES_BY_ID.get(ref)
        return f"{role.title} · {role.company}" if role else ref
    if kind == "project":
        project = PROJECTS_BY_ID.get(ref)
        return project.name if project else ref
    if kind == "education":
        match = next((item for item in EDUCATION if item.id == ref), None)
        return f"{match.title.split(',')[0]} · {match.institution}" if match else ref
    if kind == "course":
        match = next((item for item in COURSES if item.name == ref), None)
        return f"{match.name} · {match.provider}" if match else ref
    return "Résumé · skills"


def _profile_payload() -> dict[str, Any]:
    return {
        "name": PROFILE.name,
        "short": PROFILE.short_name,
        "role": PROFILE.role,
        "subtitle": PROFILE.subtitle,
        "location": PROFILE.location,
        "availability": PROFILE.availability,
        "summary": PROFILE.summary,
        "years": PROFILE.years_experience,
        "status": PROFILE.status,
        "user": PROFILE.terminal_user,
        "host": PROFILE.terminal_host,
        "links": [
            {
                "id": link.id,
                "label": link.label,
                "value": link.value,
                "href": link.href,
                "kind": link.kind,
            }
            for link in PROFILE.links
        ],
    }


def _role_payload(role_id: str) -> dict[str, Any]:
    role = ROLES_BY_ID[role_id]
    return {
        "id": role.id,
        "title": role.title,
        "company": role.company,
        "period": role.period,
        "location": role.location,
        "context": role.context,
        "owned": list(role.owned),
        "impact": list(role.impact),
        "tech": _tech_names(role.technologies),
        "progression": list(role.progression),
        "current": role.current,
        "systems": [
            {"id": pid, "name": PROJECTS_BY_ID[pid].name, "tagline": PROJECTS_BY_ID[pid].tagline}
            for pid in role.systems
            if pid in PROJECTS_BY_ID
        ],
    }


def project_payload(project_id: str) -> dict[str, Any]:
    """Everything one project island renders, including its architecture map."""
    project = PROJECTS_BY_ID[project_id]
    return {
        "id": project.id,
        "name": project.name,
        "kind": project.kind,
        "domain": project.domain,
        "tagline": project.tagline,
        "problem": project.problem,
        "built": list(project.built),
        "architecture": [
            {
                "id": stage.id,
                "label": stage.label,
                "kind": stage.kind,
                "detail": stage.detail,
                "notes": list(stage.notes),
                "tech": list(stage.tech),
                "branch": stage.branch,
            }
            for stage in project.architecture
        ],
        "decisions": list(project.decisions),
        "stack": list(project.stack),
        "impact": list(project.impact),
        "repo": project.repo,
        "live": project.live,
        "status": project.status,
    }


def terminal_payload() -> dict[str, Any]:
    return {
        "profile": _profile_payload(),
        "roles": [_role_payload(role.id) for role in EXPERIENCE],
        "projects": [
            {
                "id": project.id,
                "name": project.name,
                "kind": project.kind,
                "domain": project.domain,
                "tagline": project.tagline,
                "problem": project.problem,
                "built": list(project.built),
                "decisions": list(project.decisions),
                "impact": list(project.impact),
                "stack": list(project.stack),
                "repo": project.repo,
                "live": project.live,
            }
            for project in PROJECTS
        ],
        "groups": [
            {
                "id": group.id,
                "label": group.label,
                "purpose": group.purpose,
                "tech": _tech_names(group.technologies),
            }
            for group in CORE_STACK
        ],
        "metrics": [
            {
                "label": metric.label,
                "value": metric.value,
                "context": metric.context,
                "source": metric.source,
            }
            for metric in METRICS
        ],
        "sections": [{"id": sid, "label": label} for sid, label in SECTIONS],
    }


def corestack_payload() -> dict[str, Any]:
    return {
        "groups": [
            {
                "id": group.id,
                "label": group.label,
                "purpose": group.purpose,
                "tech": [
                    {"id": tech_id, "name": label_of(tech_id)}
                    for tech_id in group.technologies
                    if tech_id in CORE_BY_ID
                ],
            }
            for group in CORE_STACK
        ],
        "tech": [
            {
                "id": tech.id,
                "name": tech.name,
                "what": tech.what,
                "group": next(
                    (group.label for group in CORE_STACK if tech.id in group.technologies),
                    "",
                ),
                "evidence": [
                    {
                        "ref": _evidence_label(item.kind, item.ref),
                        "detail": item.detail,
                    }
                    for item in tech.evidence
                ],
            }
            for tech in CORE_BY_ID.values()
        ],
        "nav": [{"id": sid, "label": label} for sid, label in NAV_SECTIONS],
    }
