"""Content layer: presentation-independent portfolio data.

Everything rendered by the application comes from these structured modules.
No professional fact is written inside rendering code, and nothing here is
invented: every field traces back to `CV.pdf` (shipped in this repository)
or to `projects.md`.
"""

from portfolio.data.education import COURSES, EDUCATION, LANGUAGES
from portfolio.data.experience import EXPERIENCE, ROLES_BY_ID
from portfolio.data.profile import METRICS, PROFILE, SUMMARY
from portfolio.data.projects import PROJECTS, PROJECTS_BY_ID
from portfolio.data.stack import CORE_BY_ID, CORE_STACK, CORE_TECHNOLOGIES, label_of

__all__ = [
    "CORE_BY_ID",
    "CORE_STACK",
    "CORE_TECHNOLOGIES",
    "COURSES",
    "EDUCATION",
    "EXPERIENCE",
    "LANGUAGES",
    "METRICS",
    "PROFILE",
    "PROJECTS",
    "PROJECTS_BY_ID",
    "ROLES_BY_ID",
    "SUMMARY",
    "label_of",
]
