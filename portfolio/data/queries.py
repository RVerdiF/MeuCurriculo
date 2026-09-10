"""Read-only query model for the "Query my experience" console.

There is no SQL engine anywhere in this application. Every answer is computed
here, in Python, from the structured portfolio data. The browser only sends a
command string, matches it against these pre-computed lookups and renders the
rows it receives. User input never reaches a database, a shell or an
interpreter.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from portfolio.data.education import COURSES, EDUCATION
from portfolio.data.experience import ROLES_BY_ID
from portfolio.data.projects import PROJECTS_BY_ID as _PROJECTS
from portfolio.data.stack import STACK, STACK_TECHNOLOGIES

# Free-text domain tags used by the query console. Explicit on purpose: a
# lookup that can be audited beats fuzzy matching that guesses.
PROJECT_DOMAIN_TAGS: dict[str, tuple[str, ...]] = {
    "fraud_monitoring": ("financial", "fraud", "banking"),
    "paysim": ("financial", "fraud", "performance", "public"),
    "snowflake_governance": ("financial", "governance", "warehouse"),
    "production_analytics": ("analytics", "quality"),
    "ai_agents_mlops": ("ai", "mlops", "automation"),
    "btc": ("ml", "public", "automation"),
    "embrapa": ("public", "api", "ingestion"),
}

PROJECT_STACK_TAGS: dict[str, tuple[str, ...]] = {
    "fraud_monitoring": ("power bi", "python", "sql", "anomaly detection"),
    "paysim": ("polars", "sqlite", "streamlit", "sql", "python"),
    "snowflake_governance": ("snowflake", "sql", "dbt", "python"),
    "production_analytics": ("sql", "python", "automation"),
    "ai_agents_mlops": ("aws", "docker", "ci/cd", "python", "ai"),
    "btc": ("lightgbm", "streamlit", "sqlite", "pandas", "python"),
    "embrapa": ("fastapi", "docker", "pydantic", "pandas", "python"),
}


@dataclass(frozen=True)
class Result:
    """A ready-to-render tabular answer."""

    columns: tuple[str, ...]
    rows: tuple[tuple[str, ...], ...]
    note: str = ""
    sql: str = ""


@dataclass(frozen=True)
class Preset:
    id: str
    label: str
    sql: str
    description: str
    result: Result


def _evidence_rows(technology_id: str) -> tuple[tuple[str, ...], ...]:
    """Resolve a technology's evidence pointers into display rows."""
    tech = STACK_TECHNOLOGIES.get(technology_id)
    if tech is None:
        return ()
    rows: list[tuple[str, ...]] = []
    for item in tech.evidence:
        if item.kind == "role":
            role = ROLES_BY_ID.get(item.ref)
            if role is None:
                continue
            rows.append((role.title, role.company, item.detail))
        elif item.kind == "project":
            project = _PROJECTS.get(item.ref)
            if project is None:
                continue
            rows.append((project.name, project.kind, item.detail))
        elif item.kind == "education":
            match = next((e for e in EDUCATION if e.id == item.ref), None)
            if match is None:
                continue
            rows.append((match.title, match.institution, item.detail))
        elif item.kind == "course":
            match = next((c for c in COURSES if c.name == item.ref), None)
            label = f"{match.name} · {match.provider}" if match else item.ref
            rows.append((label, "certification", item.detail))
        elif item.kind == "skills":
            rows.append(("Résumé · Skills", "profile", item.detail))
    return tuple(rows)


def _project_rows(project_id: str) -> tuple[tuple[str, ...], ...]:
    project = _PROJECTS.get(project_id)
    if project is None:
        return ()
    outcome = project.outcome[0] if project.outcome else project.tagline
    return ((project.name, project.domain, outcome),)


# --- Lookups consumed by the browser -------------------------------------

EXPERIENCE_BY_TECHNOLOGY: dict[str, Result] = {}
for _tech in STACK_TECHNOLOGIES.values():
    _rows = _evidence_rows(_tech.id)
    if not _rows:
        continue
    _result = Result(
        columns=("ROLE / PROJECT", "CONTEXT", "WHAT IT WAS USED FOR"),
        rows=_rows,
        note=f"{len(_rows)} reference(s) for {_tech.name}",
    )
    EXPERIENCE_BY_TECHNOLOGY[_tech.id] = _result
    EXPERIENCE_BY_TECHNOLOGY[_tech.name.lower()] = _result

PROJECTS_BY_DOMAIN: dict[str, Result] = {}
for _project in _PROJECTS.values():
    _tags = PROJECT_DOMAIN_TAGS.get(_project.id, ())
    for _tag in (*_tags, *_project.domain.replace("·", " ").split()):
        _key = _tag.strip().lower()
        if not _key:
            continue
        _existing = PROJECTS_BY_DOMAIN.get(_key)
        _row = _project_rows(_project.id)[0]
        if _existing is None:
            PROJECTS_BY_DOMAIN[_key] = Result(
                columns=("PROJECT", "DOMAIN", "DOCUMENTED OUTCOME"),
                rows=(_row,),
                note=f"{_project.name} · matched domain '{_key}'",
            )
        elif _row not in _existing.rows:
            PROJECTS_BY_DOMAIN[_key] = Result(
                columns=_existing.columns,
                rows=(*_existing.rows, _row),
                note=f"{len(_existing.rows) + 1} project(s) matched domain '{_key}'",
            )

STACK_BY_CATEGORY: dict[str, Result] = {}
for _layer in STACK:
    _rows = tuple(
        (STACK_TECHNOLOGIES[t].name, STACK_TECHNOLOGIES[t].what)
        for t in _layer.technologies
        if t in STACK_TECHNOLOGIES
    )
    if not _rows:
        continue
    _result = Result(
        columns=("TECHNOLOGY", "WHAT I USE IT FOR"),
        rows=_rows,
        note=f"{_layer.label} · {_layer.purpose}",
    )
    STACK_BY_CATEGORY[_layer.id] = _result
    STACK_BY_CATEGORY[_layer.label.lower()] = _result


# --- Presets shown as buttons and pre-typed statements -------------------

QUERY_PRESETS: tuple[Preset, ...] = (
    Preset(
        id="dbt_experience",
        label="dbt experience",
        sql="SELECT * FROM experience WHERE technology = 'dbt';",
        description="Every place dbt shows up, with the reference behind it.",
        result=EXPERIENCE_BY_TECHNOLOGY.get("dbt", Result((), ())),
    ),
    Preset(
        id="financial_systems",
        label="financial systems",
        sql="SELECT project, impact FROM projects WHERE domain = 'financial';",
        description="Financial and fraud-facing systems, with what they changed.",
        result=PROJECTS_BY_DOMAIN.get(
            "financial",
            Result(
                columns=("PROJECT", "DOMAIN", "DOCUMENTED OUTCOME"),
                rows=(),
                note="No project matched.",
            ),
        ),
    ),
    Preset(
        id="aws_projects",
        label="AWS projects",
        sql="SELECT * FROM experience WHERE technology = 'aws';",
        description="Where AWS was used, and in which capacity.",
        result=EXPERIENCE_BY_TECHNOLOGY.get("aws", Result((), ())),
    ),
    Preset(
        id="ai_workflows",
        label="AI workflows",
        sql="SELECT technology FROM stack WHERE category = 'ai';",
        description="AI and ML capability, and what it was applied to.",
        result=STACK_BY_CATEGORY.get(
            "ai", Result(columns=("TECHNOLOGY", "WHAT I USE IT FOR"), rows=())
        ),
    ),
    Preset(
        id="automation",
        label="automation",
        sql="SELECT * FROM experience WHERE technology = 'automation';",
        description="Everything that removes a manual step from a recurring process.",
        result=EXPERIENCE_BY_TECHNOLOGY.get("automation", Result((), ())),
    ),
    Preset(
        id="performance",
        label="performance work",
        sql="SELECT project, impact FROM projects WHERE domain = 'performance';",
        description="Systems built around memory and throughput constraints.",
        result=PROJECTS_BY_DOMAIN.get(
            "performance",
            Result(
                columns=("PROJECT", "DOMAIN", "DOCUMENTED OUTCOME"),
                rows=(),
                note="No project matched.",
            ),
        ),
    ),
)


# --- Ask the data --------------------------------------------------------

@dataclass(frozen=True)
class AskIntent:
    id: str
    question: str
    keywords: tuple[str, ...]
    headline: str
    answer: tuple[str, ...]
    refs: tuple[str, ...] = field(default_factory=tuple)


def _tech_answer(technology_id: str, headline: str) -> tuple[tuple[str, ...], tuple[str, ...]]:
    tech = STACK_TECHNOLOGIES.get(technology_id)
    if tech is None:
        return (), ()
    lines = [tech.what]
    refs: list[str] = []
    for item in tech.evidence[:4]:
        if item.kind == "role":
            role = ROLES_BY_ID.get(item.ref)
            if role:
                lines.append(f"{role.title} at {role.company}: {item.detail}")
                refs.append(role.id)
        elif item.kind == "project":
            project = _PROJECTS.get(item.ref)
            if project:
                lines.append(f"{project.name}: {item.detail}")
                refs.append(project.id)
        else:
            lines.append(item.detail)
    return tuple(lines), tuple(dict.fromkeys(refs))


_dbt_lines, _dbt_refs = _tech_answer("dbt", "dbt")
_python_lines, _python_refs = _tech_answer("python", "Python")
_aws_lines, _aws_refs = _tech_answer("aws", "AWS")
_ai_lines, _ai_refs = _tech_answer("ai_agents", "AI agents")

ASK_INTENTS: tuple[AskIntent, ...] = (
    AskIntent(
        id="dbt",
        question="What experience does Rafael have with dbt?",
        keywords=("dbt", "transform", "transformation", "model"),
        headline="dbt",
        answer=tuple(
            [
                "dbt shows up where the transformation layer needs an owner:",
                *_dbt_lines[1:],
            ]
        ),
        refs=_dbt_refs,
    ),
    AskIntent(
        id="financial",
        question="What financial systems has he built?",
        keywords=("financial", "bank", "banking", "fraud", "finance", "fintech"),
        headline="Financial systems",
        answer=(
            "Six years inside fraud prevention at a bank, plus analytics for a "
            "digital-asset platform:",
            "Fraud Analytics & Transaction Monitoring: predictive models, institutional "
            "monitoring, anomaly detection and Power BI KPIs. Case resolution improved "
            "by 30%+.",
            "PaySim Dataset Explorer: a public fraud-dataset explorer built around "
            "memory-safe, query-driven aggregation.",
            "Data Governance & Automation in Snowflake: warehouse objects and stored "
            "procedures that automate departmental processes.",
        ),
        refs=("mercantil", "fraud_monitoring", "paysim", "snowflake_governance"),
    ),
    AskIntent(
        id="python",
        question="Where has he used Python?",
        keywords=("python", "coding", "programming", "language"),
        headline="Python",
        answer=tuple(["Python is the working language across the portfolio.", *_python_lines[1:]]),
        refs=_python_refs,
    ),
    AskIntent(
        id="automation",
        question="What has he automated?",
        keywords=("automate", "automation", "manual", "process", "efficiency"),
        headline="Automation",
        answer=(
            "~80% of recurring fraud-prevention processes were automated at Banco "
            "Mercantil, which is the number I would put in front of a hiring manager.",
            "Recurring reports and operational processes automated for a digital-asset "
            "platform.",
            "Autonomous AI agents and MLOps pipelines built to execute multi-step data "
            "workflows.",
            "Reporting automation and operational processes as a consultant.",
        ),
        refs=("mercantil", "kraken", "ai_agents_mlops"),
    ),
    AskIntent(
        id="cloud",
        question="What is his cloud experience?",
        keywords=("cloud", "aws", "snowflake", "infrastructure", "kubernetes", "athena"),
        headline="Cloud",
        answer=tuple(
            [
                "AWS is the cloud platform I work in, with Snowflake as the warehouse:",
                *_aws_lines[1:],
                "Kubernetes and Docker are how that work actually runs.",
            ]
        ),
        refs=_aws_refs,
    ),
    AskIntent(
        id="impact",
        question="What projects demonstrate business impact?",
        keywords=("impact", "result", "business", "outcome", "value", "metric"),
        headline="Business impact",
        answer=(
            "Documented outcomes, all traceable to the résumé:",
            "30%+ faster fraud case resolution after pipelines and models reached "
            "production.",
            "~80% of recurring fraud-prevention processes automated.",
            "Analytics delivery for a digital-asset platform where recurring reporting "
            "stopped being manual.",
            "An end-to-end fraud-prevention solution delivered inside a bank.",
        ),
        refs=("mercantil", "fraud_monitoring", "kraken", "production_analytics"),
    ),
    AskIntent(
        id="ai",
        question="What is his experience with AI?",
        keywords=("ai", "ml", "machine learning", "agent", "llm", "mlops", "model"),
        headline="AI / ML",
        answer=tuple(
            [
                "Machine learning in production fraud detection, plus agents and MLOps:",
                *_ai_lines[1:],
                "Applied AI/MLOps practices carried into production fraud-detection "
                "workflows.",
            ]
        ),
        refs=(*_ai_refs, "mercantil"),
    ),
    AskIntent(
        id="data_engineering",
        question="What kind of data engineering does he do?",
        keywords=("data engineering", "pipeline", "platform", "warehouse", "etl", "elt"),
        headline="Data engineering",
        answer=(
            "The shape of the work is the same in every engagement: get the data out of "
            "the source, make it trustworthy, then make it useful.",
            "INGEST · Python and REST APIs over systems that publish data and nothing "
            "else.",
            "TRANSFORM · dbt and SQL, with modeling that survives a second question.",
            "STORE · Snowflake, or SQLite where the application owns the data.",
            "SHIP · Docker and Kubernetes, so the same artifact runs everywhere.",
            "ANALYZE · Power BI and Hex for the people making the decision.",
        ),
        refs=("sapiens", "kraken", "production_analytics", "snowflake_governance"),
    ),
)
