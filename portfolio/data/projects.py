"""Selected systems.

Four of them, on purpose. Each one carries the same six blocks (problem, what
I built, architecture, decisions, stack, impact) and nothing else, so the
project section is the technical centre of the site instead of a second
résumé.

Public work comes from this repository's own project notes (`projects.md`);
professional work stays at the level `CV.pdf` already publishes. No employer
architecture, no client names, no invented detail.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ArchStage:
    """One node of a project's architecture map."""

    id: str
    label: str
    kind: str  # source | process | store | serve
    detail: str
    notes: tuple[str, ...] = field(default_factory=tuple)
    tech: tuple[str, ...] = field(default_factory=tuple)
    branch: str = ""  # set on stages that belong to a side lane


@dataclass(frozen=True)
class Project:
    id: str
    name: str
    kind: str  # professional | public
    domain: str
    tagline: str
    problem: str
    built: tuple[str, ...]
    architecture: tuple[ArchStage, ...]
    decisions: tuple[str, ...]
    stack: tuple[str, ...]
    impact: tuple[str, ...]
    repo: str | None = None
    live: str | None = None
    status: str | None = None
    roles: tuple[str, ...] = field(default_factory=tuple)


PROJECTS: tuple[Project, ...] = (
    Project(
        id="fraud_monitoring",
        name="Fraud Analytics & Transaction Monitoring",
        kind="professional",
        domain="banking · fraud prevention",
        tagline="Detection, monitoring and KPI visibility running in production",
        problem=(
            "Fraud review depended on recurring manual work over transactional data, "
            "which capped how fast cases could move and left performance hard to measure."
        ),
        built=(
            "Predictive models and algorithms that score transactions for fraud.",
            "An institutional transaction-monitoring system with statistical anomaly "
            "detection over transactional activity.",
            "KPI and Power BI dashboards that made fraud performance visible, plus "
            "automation of the recurring review and reporting steps.",
        ),
        architecture=(
            ArchStage(
                id="transactions",
                label="Core banking transactions",
                kind="source",
                detail="Transactional data from regulated banking systems.",
                notes=("Monitoring feed", "Anomaly baselines"),
                tech=("SQL",),
            ),
            ArchStage(
                id="detection",
                label="Detection",
                kind="process",
                detail="Predictive models and algorithms score each transaction.",
                notes=("Predictive models for transactional fraud prevention",),
                tech=("Python", "Machine learning"),
            ),
            ArchStage(
                id="monitoring",
                label="Monitoring",
                kind="process",
                detail="Statistical anomaly detection runs continuously over activity.",
                notes=("Deviations surfaced instead of sampled by hand",),
                tech=("Anomaly detection",),
            ),
            ArchStage(
                id="pipelines",
                label="Pipelines",
                kind="process",
                detail="The pipelines and models the detection depends on.",
                notes=("Built and maintained in production", "30%+ faster case resolution"),
                tech=("Docker", "Kubernetes", "MLOps"),
            ),
            ArchStage(
                id="visibility",
                label="Dashboards",
                kind="serve",
                detail="KPI and Power BI dashboards for fraud analytics.",
                notes=("KPI definition before chart design",),
                tech=("Power BI",),
                branch="visibility",
            ),
        ),
        decisions=(
            "Detection and visibility shipped together, because a model nobody can watch "
            "is a model that gets switched off.",
            "Anomaly detection kept separate from the predictive models, so an unusual "
            "week shows up as a signal instead of quietly skewing a score.",
        ),
        stack=("Python", "SQL", "Power BI", "anomaly detection", "predictive models"),
        impact=(
            "30%+ faster case resolution in the fraud-prevention workflow.",
            "~80% of recurring fraud-prevention processes automated.",
        ),
        roles=("mercantil",),
    ),
    Project(
        id="ai_agents_mlops",
        name="AI Agents & MLOps Pipelines",
        kind="professional",
        domain="AI systems · MLOps",
        tagline="Agents and MLOps pipelines executing multi-step data workflows",
        problem=(
            "Data workflows with many recurring steps consume engineering time that "
            "should be going into the next problem."
        ),
        built=(
            "Autonomous AI agents that execute multi-step data workflows end to end.",
            "MLOps pipelines that version, test and deploy the resulting artifacts.",
            "CI/CD and containerized delivery for both, on AWS.",
        ),
        architecture=(
            ArchStage(
                id="trigger",
                label="Trigger",
                kind="source",
                detail="A workflow step is queued or scheduled.",
                notes=("Scheduled and event-driven entry points",),
            ),
            ArchStage(
                id="agents",
                label="Agents",
                kind="process",
                detail="Autonomous agents execute the workflow steps.",
                notes=("Multi-step execution", "Built to run unattended"),
                tech=("Python", "AI agents"),
            ),
            ArchStage(
                id="mlops",
                label="MLOps",
                kind="process",
                detail="Pipelines version, test and deploy the artifacts.",
                notes=("Automation as a versioned deliverable", "Reproducible runs"),
                tech=("MLOps", "CI/CD"),
            ),
            ArchStage(
                id="delivery",
                label="Delivery",
                kind="store",
                detail="Containerized deployment on AWS.",
                notes=("Same artifact from development to production",),
                tech=("Docker", "AWS"),
            ),
            ArchStage(
                id="outcome",
                label="Outcome",
                kind="serve",
                detail="Recurring manual effort removed from the workflow.",
                notes=("Someone else can own the workflow later",),
                branch="outcome",
            ),
        ),
        decisions=(
            "Automation went through CI/CD like any other deliverable. Versioned pipelines "
            "are what let someone else own the workflow later.",
            "Agents kept narrow and observable, because an unattended workflow that fails "
            "silently costs more time than the manual one it replaced.",
        ),
        stack=("Python", "AI agents", "MLOps", "CI/CD", "Docker", "AWS"),
        impact=(
            "Complex data workflows automated end to end.",
            "AI/MLOps practices carried into production fraud-detection workflows.",
        ),
        roles=("mercantil",),
    ),
    Project(
        id="analytics_platform",
        name="Data & Analytics Platform Delivery",
        kind="professional",
        domain="analytics engineering · digital assets",
        tagline="Analytics the business can act on, without a manual rebuild each cycle",
        problem=(
            "Recurring reports and operational processes were rebuilt by hand every "
            "cycle, which made delivery slow and quality inconsistent."
        ),
        built=(
            "Data and analytics solutions modeled for reuse, so the same question does "
            "not have to be solved twice.",
            "Automation for recurring reports and operational processes.",
            "Data reliability and quality work across analytics workflows, agreed with "
            "partner areas before modeling.",
        ),
        architecture=(
            ArchStage(
                id="requirement",
                label="Requirement",
                kind="source",
                detail="Partner areas bring the business question.",
                notes=("Requirements agreed before modeling",),
            ),
            ArchStage(
                id="model",
                label="Data model",
                kind="process",
                detail="Data is modeled once and reused.",
                notes=("Solutions built for reuse, not one-off queries",),
                tech=("SQL", "Data modeling"),
            ),
            ArchStage(
                id="automation",
                label="Automation",
                kind="process",
                detail="Recurring reporting stops being manual.",
                notes=("Operational processes run on their own",),
                tech=("Python", "Automation"),
            ),
            ArchStage(
                id="quality",
                label="Data quality",
                kind="store",
                detail="Reliability and quality checked across analytics workflows.",
                notes=("Quality work coordinated with partner areas",),
                tech=("Data quality",),
            ),
            ArchStage(
                id="decisions",
                label="Decisions",
                kind="serve",
                detail="Deliverables the business decisions can depend on.",
                notes=("Requirements land as deliverables",),
                branch="decisions",
            ),
        ),
        decisions=(
            "Requirements translated with partner areas before modeling, so the "
            "deliverable matches the decision being made.",
            "Recurring work pushed into automation rather than re-run by hand, which is "
            "where most of the delivery time was going.",
        ),
        stack=("SQL", "Python", "data modeling", "data quality", "automation"),
        impact=(
            "Manual effort reduced and delivery reliability improved.",
            "Data reliability and quality raised across analytics workflows.",
        ),
        roles=("kraken",),
    ),
    Project(
        id="paysim",
        name="PaySim Dataset Explorer",
        kind="public",
        domain="fraud analytics · data engineering",
        tagline="Fraud dataset exploration without loading the dataset",
        problem=(
            "The interesting questions about a fraud dataset are aggregate ones: mule "
            "accounts, balance-draining transactions, whether the fraud flag actually "
            "works. Answering them by loading the whole dataset into memory is what "
            "crashes the app."
        ),
        built=(
            "A query-driven explorer: the dataset is ingested into SQLite once and every "
            "chart asks one targeted aggregation.",
            "A Polars streaming pass for the aggregations SQL handles badly, such as "
            "mule-account ranking.",
            "Fraud-specific views for mule accounts, balance draining and flag quality.",
        ),
        architecture=(
            ArchStage(
                id="dataset",
                label="PaySim dataset",
                kind="source",
                detail="Synthetic financial dataset published on Kaggle.",
                notes=("Multi-gigabyte CSV",),
            ),
            ArchStage(
                id="ingestion",
                label="Ingestion",
                kind="process",
                detail="Chunked CSV ingestion into SQLite.",
                notes=("Memory-safe by construction", "Optionally fetched on first run"),
                tech=("Python", "SQLite"),
            ),
            ArchStage(
                id="query",
                label="Query layer",
                kind="process",
                detail="One targeted aggregation per view, executed in parallel.",
                notes=("ThreadPoolExecutor", "The UI only pulls what it renders"),
                tech=("SQL",),
            ),
            ArchStage(
                id="aggregate",
                label="Aggregation",
                kind="process",
                detail="Polars streaming pass for mule-account ranking.",
                notes=("Chunks released as they are processed",),
                tech=("Polars", "Pandas"),
            ),
            ArchStage(
                id="surface",
                label="Views",
                kind="serve",
                detail="Streamlit views: dataset health, distributions, fraud flags.",
                notes=("Analysis of a multi-gigabyte dataset that stays stable",),
                tech=("Streamlit",),
                branch="surface",
            ),
        ),
        decisions=(
            "Query-per-chart instead of load-everything: the UI only ever pulls the "
            "aggregate it renders.",
            "Memory was treated as a design constraint. Deciding up front that the "
            "dataset would never be held in memory is what made the app stable.",
        ),
        stack=(
            "Python",
            "Streamlit",
            "SQLite",
            "SQL",
            "Polars",
            "Pandas",
            "concurrent.futures",
        ),
        impact=(
            "A multi-gigabyte fraud dataset analysed in an app that stays up.",
            "Mule-account and balance-draining views that answer questions the raw "
            "dataset does not.",
        ),
        repo="https://github.com/RVerdiF/PaysimViz",
        live="https://rverdif-paysimviz-app-olphe6.streamlit.app/",
        status="repository · live demo",
    ),
)

PROJECTS_BY_ID: dict[str, Project] = {project.id: project for project in PROJECTS}
