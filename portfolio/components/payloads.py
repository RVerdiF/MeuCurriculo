"""Serialisers that turn the content layer into island payloads.

Islands are plain HTML/CSS/JS rendered inside same-origin `st.iframe` frames.
They receive data — never markup — from here, so the browser side can stay
presentation-only and user input can never be interpreted as HTML.
"""

from __future__ import annotations

from typing import Any

from portfolio.config import NAV_SECTIONS, SECTIONS
from portfolio.data.architecture import ARCHITECTURE
from portfolio.data.education import COURSES, EDUCATION
from portfolio.data.experience import EXPERIENCE, ROLES_BY_ID
from portfolio.data.profile import METRICS, PROFILE
from portfolio.data.projects import PROFESSIONAL_PROJECTS, PROJECTS_BY_ID, PUBLIC_PROJECTS
from portfolio.data.queries import (
    ASK_INTENTS,
    EXPERIENCE_BY_TECHNOLOGY,
    PROJECTS_BY_DOMAIN,
    QUERY_PRESETS,
    STACK_BY_CATEGORY,
)
from portfolio.data.stack import STACK, STACK_TECHNOLOGIES

SECTION_FOR_KIND = {"role": "experience", "project": "projects", "tech": "lab"}


def _result_payload(result: Any) -> dict[str, Any]:
    return {
        "columns": list(result.columns),
        "rows": [list(row) for row in result.rows],
        "note": result.note,
    }


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


def role_payload(role_id: str) -> dict[str, Any]:
    role = ROLES_BY_ID[role_id]
    return {
        "id": role.id,
        "title": role.title,
        "company": role.company,
        "period": role.period,
        "location": role.location,
        "domain": role.domain,
        "mission": role.mission,
        "current": role.current,
        "response": list(role.response),
        "bullets": list(role.responsibilities),
        "tech": [STACK_TECHNOLOGIES[t].name for t in role.technologies if t in STACK_TECHNOLOGIES],
        "impacts": [{"label": i.label, "detail": i.detail} for i in role.impacts],
        "progression": list(role.progression),
        "systems": [
            {"id": pid, "name": PROJECTS_BY_ID[pid].name, "tagline": PROJECTS_BY_ID[pid].tagline}
            for pid in role.systems
            if pid in PROJECTS_BY_ID
        ],
    }


def project_payload(project_id: str) -> dict[str, Any]:
    project = PROJECTS_BY_ID[project_id]
    return {
        "id": project.id,
        "name": project.name,
        "kind": project.kind,
        "tagline": project.tagline,
        "summary": project.summary,
        "domain": project.domain,
        "problem": project.problem,
        "stack": list(project.stack),
        "decisions": list(project.decisions),
        "outcome": list(project.outcome),
        "repo": project.repo,
        "live": project.live,
        "status": project.status,
    }


def tech_payload(tech_id: str) -> dict[str, Any]:
    tech = STACK_TECHNOLOGIES[tech_id]
    layer = next((l for l in STACK if tech_id in l.technologies), None)
    evidence = [
        {"ref": _evidence_label(item.kind, item.ref), "detail": item.detail}
        for item in tech.evidence
    ]
    related: list[dict[str, str]] = []
    for item in tech.evidence:
        if item.kind == "role":
            role = ROLES_BY_ID.get(item.ref)
            if role:
                related.append({"label": role.company, "section": "experience"})
        elif item.kind == "project":
            project = PROJECTS_BY_ID.get(item.ref)
            if project:
                related.append({"label": project.name, "section": "projects"})
    seen: set[str] = set()
    unique_related = []
    for item in related:
        if item["label"] not in seen:
            seen.add(item["label"])
            unique_related.append(item)
    return {
        "id": tech.id,
        "name": tech.name,
        "what": tech.what,
        "layer": layer.label if layer else "",
        "layerLabel": (layer.label + " · " + layer.purpose) if layer else "",
        "evidence": evidence,
        "related": unique_related,
    }


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
            {"id": link.id, "label": link.label, "value": link.value, "href": link.href, "kind": link.kind}
            for link in PROFILE.links
        ],
    }


def terminal_payload() -> dict[str, Any]:
    return {
        "profile": _profile_payload(),
        "roles": [role_payload(role.id) for role in EXPERIENCE],
        "projects": [
            project_payload(project.id) for project in (*PUBLIC_PROJECTS, *PROFESSIONAL_PROJECTS)
        ],
        "tech": [tech_payload(tech.id) for tech in STACK_TECHNOLOGIES.values()],
        "metrics": [
            {
                "label": metric.label,
                "value": metric.value,
                "context": metric.context,
                "source": metric.source,
            }
            for metric in METRICS
        ],
        "layers": [
            {
                "id": layer.id,
                "label": layer.label,
                "tech": [STACK_TECHNOLOGIES[t].name for t in layer.technologies if t in STACK_TECHNOLOGIES],
            }
            for layer in STACK
        ],
        "sections": [{"id": sid, "label": label} for sid, label in SECTIONS],
    }


def explorer_payload() -> dict[str, Any]:
    nodes = []
    for node in ARCHITECTURE:
        nodes.append(
            {
                "id": node.id,
                "label": node.label,
                "stage": node.stage,
                "kind": node.kind,
                "branch": node.branch,
                "summary": node.summary,
                "role": node.role,
                "patterns": list(node.patterns),
                "tech": [STACK_TECHNOLOGIES[t].name for t in node.technologies if t in STACK_TECHNOLOGIES],
                "experience": [
                    {"id": rid, "title": ROLES_BY_ID[rid].title, "company": ROLES_BY_ID[rid].company}
                    for rid in node.experience
                    if rid in ROLES_BY_ID
                ],
                "projects": [
                    {"id": pid, "name": PROJECTS_BY_ID[pid].name}
                    for pid in node.projects
                    if pid in PROJECTS_BY_ID
                ],
            }
        )
    return {"nodes": nodes}


def stackmap_payload() -> dict[str, Any]:
    return {
        "layers": [
            {
                "id": layer.id,
                "label": layer.label,
                "purpose": layer.purpose,
                "tech": [
                    {"id": t, "name": STACK_TECHNOLOGIES[t].name}
                    for t in layer.technologies
                    if t in STACK_TECHNOLOGIES
                ],
            }
            for layer in STACK
        ],
        "tech": [tech_payload(tech.id) for tech in STACK_TECHNOLOGIES.values()],
    }


def console_payload() -> dict[str, Any]:
    return {
        "presets": [
            {
                "id": preset.id,
                "label": preset.label,
                "sql": preset.sql,
                "description": preset.description,
                "result": _result_payload(preset.result),
            }
            for preset in QUERY_PRESETS
        ],
        "lookups": {
            "technology": {key: _result_payload(value) for key, value in EXPERIENCE_BY_TECHNOLOGY.items()},
            "domain": {key: _result_payload(value) for key, value in PROJECTS_BY_DOMAIN.items()},
            "category": {key: _result_payload(value) for key, value in STACK_BY_CATEGORY.items()},
        },
        "supported": [
            "SELECT * FROM experience WHERE technology = 'dbt';",
            "SELECT project, impact FROM projects WHERE domain = 'financial';",
            "SELECT technology FROM stack WHERE category = 'ai';",
        ],
    }


def ask_payload() -> dict[str, Any]:
    intents = []
    for intent in ASK_INTENTS:
        refs = []
        seen: set[str] = set()
        for ref in intent.refs:
            if ref in seen:
                continue
            seen.add(ref)
            if ref in ROLES_BY_ID:
                role = ROLES_BY_ID[ref]
                refs.append(
                    {
                        "id": ref,
                        "label": role.title + " · " + role.company,
                        "section": "experience",
                    }
                )
            elif ref in PROJECTS_BY_ID:
                refs.append({"id": ref, "label": PROJECTS_BY_ID[ref].name, "section": "projects"})
        intents.append(
            {
                "id": intent.id,
                "question": intent.question,
                "keywords": list(intent.keywords),
                "headline": intent.headline,
                "answer": list(intent.answer),
                "refs": refs,
            }
        )
    return {"intents": intents}


def palette_payload() -> dict[str, Any]:
    items: list[dict[str, str]] = []
    for section_id, label in NAV_SECTIONS:
        items.append(
            {
                "label": "Go to " + label,
                "hint": "section",
                "kind": "nav",
                "target": section_id,
                "keywords": section_id,
            }
        )
    items.extend(
        [
            {
                "label": "Open terminal",
                "hint": "interactive shell",
                "kind": "terminal",
                "target": "",
                "keywords": "terminal shell console cli",
            },
            {
                "label": "Download résumé (PDF)",
                "hint": "action",
                "kind": "resume",
                "target": "resume",
                "keywords": "cv resume pdf download",
            },
            {
                "label": "Open LinkedIn",
                "hint": "rafael-verdi-de-freitas",
                "kind": "link",
                "href": next(link.href for link in PROFILE.links if link.id == "linkedin"),
                "keywords": "linkedin profile",
            },
            {
                "label": "Open GitHub",
                "hint": "RVerdiF",
                "kind": "link",
                "href": next(link.href for link in PROFILE.links if link.id == "github"),
                "keywords": "github code repositories",
            },
            {
                "label": "Email Rafael",
                "hint": PROFILE.email,
                "kind": "link",
                "href": f"mailto:{PROFILE.email}",
                "keywords": "email contact mail",
            },
            {
                "label": "Run: experience",
                "hint": "terminal command",
                "kind": "terminal",
                "target": "experience",
                "keywords": "experience roles jobs history",
            },
            {
                "label": "Run: projects",
                "hint": "terminal command",
                "kind": "terminal",
                "target": "projects",
                "keywords": "projects builds systems",
            },
            {
                "label": "Run: impact",
                "hint": "terminal command",
                "kind": "terminal",
                "target": "impact",
                "keywords": "impact metrics results",
            },
        ]
    )
    for tech in STACK_TECHNOLOGIES.values():
        layer = next((l for l in STACK if tech.id in l.technologies), None)
        items.append(
            {
                "label": "Technology: " + tech.name,
                "hint": layer.label if layer else "",
                "kind": "tech",
                "target": tech.id,
                "keywords": tech.id + " " + " ".join(tech.tags),
            }
        )
    return {"items": items}
