"""Content layer — presentation-independent portfolio data.

Everything rendered by the application comes from these structured modules.
No professional fact is written inside rendering code, and nothing here is
invented: every field traces back to `CV.pdf` (shipped in this repository),
the résumé content previously published by `app.py`, or `projects.md`.
"""

from portfolio.data.architecture import ARCHITECTURE, ARCHITECTURE_NODES
from portfolio.data.education import COURSES, EDUCATION, LANGUAGES
from portfolio.data.experience import EXPERIENCE, ROLES_BY_ID
from portfolio.data.profile import METRICS, PROFILE, SUMMARY
from portfolio.data.projects import PROFESSIONAL_PROJECTS, PUBLIC_PROJECTS
from portfolio.data.queries import ASK_INTENTS, QUERY_PRESETS
from portfolio.data.stack import STACK, STACK_TECHNOLOGIES

__all__ = [
    "ARCHITECTURE",
    "ARCHITECTURE_NODES",
    "ASK_INTENTS",
    "COURSES",
    "EDUCATION",
    "EXPERIENCE",
    "LANGUAGES",
    "METRICS",
    "PROFILE",
    "PROFESSIONAL_PROJECTS",
    "PUBLIC_PROJECTS",
    "QUERY_PRESETS",
    "ROLES_BY_ID",
    "STACK",
    "STACK_TECHNOLOGIES",
    "SUMMARY",
]
