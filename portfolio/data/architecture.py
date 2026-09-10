"""Interactive architecture model — how a data platform gets built here.

The diagram is deliberately opinionated but only contains stages, technologies
and references that appear in the résumé. Each node carries the detail panel
content (role, patterns, related experience) so the front end never invents
copy for it.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ArchNode:
    id: str
    label: str
    stage: int
    kind: str  # source | process | store | serve
    summary: str
    role: str
    patterns: tuple[str, ...] = field(default_factory=tuple)
    technologies: tuple[str, ...] = field(default_factory=tuple)
    experience: tuple[str, ...] = field(default_factory=tuple)
    projects: tuple[str, ...] = field(default_factory=tuple)
    branch: str = "main"  # main | dashboard | automation | ai | cross


ARCHITECTURE: tuple[ArchNode, ...] = (
    # Stage 0 — sources
    ArchNode(
        id="core_banking",
        label="Core banking transactions",
        stage=0,
        kind="source",
        summary="Transactional data from regulated banking systems.",
        role="Source system",
        patterns=("Transactional monitoring", "Fraud signals", "Anomaly baselines"),
        technologies=("sql",),
        experience=("mercantil",),
        projects=("fraud_monitoring",),
    ),
    ArchNode(
        id="digital_assets",
        label="Digital-asset platform",
        stage=0,
        kind="source",
        summary="Operational and analytics data for a digital-asset business.",
        role="Source system",
        patterns=("Recurring reporting", "Reliability checks", "Partner hand-offs"),
        technologies=("sql", "python"),
        experience=("kraken",),
        projects=("production_analytics",),
    ),
    ArchNode(
        id="public_data",
        label="Public data sources",
        stage=0,
        kind="source",
        summary="Sources that publish tables or APIs and nothing else.",
        role="Source system",
        patterns=("Web extraction", "Market data APIs"),
        technologies=("extraction", "rest_apis"),
        experience=(),
        projects=("embrapa", "btc"),
    ),
    # Stage 1 — ingestion
    ArchNode(
        id="ingestion",
        label="Ingestion",
        stage=1,
        kind="process",
        summary="Python pulls, validates and lands the data.",
        role="Bring data in without letting malformed records through",
        patterns=(
            "Extraction modules per source category",
            "Validation at the boundary (Pydantic)",
            "Chunked ingestion for datasets that do not fit in memory",
        ),
        technologies=("python", "rest_apis", "pandas", "sqlite"),
        experience=("mercantil", "corporate"),
        projects=("embrapa", "paysim"),
    ),
    # Stage 2 — raw
    ArchNode(
        id="raw",
        label="Raw layer",
        stage=2,
        kind="store",
        summary="What arrived, as it arrived — typed and traceable.",
        role="Debuggable landing zone",
        patterns=("No silent transformations", "Reprocessing without re-extracting"),
        technologies=("sqlite", "snowflake"),
        experience=(),
        projects=("paysim",),
    ),
    # Stage 3 — transform
    ArchNode(
        id="transform",
        label="Transformation",
        stage=3,
        kind="process",
        summary="dbt and SQL turn raw data into models the business agreed on.",
        role="Where business logic lives — once, in version control",
        patterns=(
            "Reusable models instead of per-analyst queries",
            "Data quality checks in the pipeline",
            "Documented models so the definition is not a rumour",
            "Golden tables for the agreed source of truth",
        ),
        technologies=("dbt", "sql", "data_modeling", "golden_tables", "snowflake"),
        experience=("sapiens", "kraken"),
        projects=("snowflake_governance", "production_analytics"),
    ),
    # Stage 4 — curated
    ArchNode(
        id="curated",
        label="Curated models",
        stage=4,
        kind="store",
        summary="The layer dashboards, automation and models are allowed to read.",
        role="Contract between engineering and the business",
        patterns=("Dimensional modelling", "Stored procedures for repeated logic"),
        technologies=("snowflake", "data_warehousing", "kpis"),
        experience=("mercantil", "kraken"),
        projects=("snowflake_governance",),
    ),
    # Stage 5 — consumption branches
    ArchNode(
        id="dashboards",
        label="Dashboards",
        stage=5,
        kind="serve",
        branch="dashboard",
        summary="Power BI and Hex for the people making the decision.",
        role="Self-service visibility",
        patterns=("KPI definition before chart design", "Self-service analytics"),
        technologies=("power_bi", "hex", "kpis", "self_service"),
        experience=("mercantil",),
        projects=("fraud_monitoring",),
    ),
    ArchNode(
        id="automation",
        label="Automation",
        stage=5,
        kind="serve",
        branch="automation",
        summary="Recurring reports and operational processes that stop being manual.",
        role="Remove the human step, not just report on it",
        patterns=("Process automation", "Recurring reporting", "Scheduled jobs"),
        technologies=("automation", "python", "scheduling", "ci_cd"),
        experience=("mercantil", "kraken", "corporate"),
        projects=("production_analytics",),
    ),
    ArchNode(
        id="ai_workflows",
        label="AI workflows",
        stage=5,
        kind="serve",
        branch="ai",
        summary="Models and agents that execute the workflow, not only describe it.",
        role="ML and agents in production",
        patterns=(
            "MLOps instead of one-off notebooks",
            "Autonomous agents for multi-step workflows",
            "Fraud models monitored after go-live",
        ),
        technologies=("machine_learning", "mlops", "ai_agents", "ai_workflows", "local_llm"),
        experience=("mercantil", "sapiens", "corporate"),
        projects=("ai_agents_mlops", "fraud_monitoring", "btc"),
    ),
    # Cross-cutting band
    ArchNode(
        id="orchestration",
        label="Orchestration",
        stage=9,
        kind="process",
        branch="cross",
        summary="Nothing above runs by hand.",
        role="Cross-cutting",
        patterns=("Airflow · scheduled jobs · CI/CD"),
        technologies=("airflow", "scheduling", "ci_cd"),
        experience=("sapiens",),
        projects=("btc", "ai_agents_mlops"),
    ),
    ArchNode(
        id="platform",
        label="Platform",
        stage=9,
        kind="process",
        branch="cross",
        summary="The same artefact runs everywhere it is deployed.",
        role="Cross-cutting",
        patterns=("Docker images · Kubernetes workloads · AWS services"),
        technologies=("docker", "kubernetes", "aws", "athena"),
        experience=("sapiens", "mercantil"),
        projects=("ai_agents_mlops", "embrapa"),
    ),
    ArchNode(
        id="governance",
        label="Governance",
        stage=9,
        kind="process",
        branch="cross",
        summary="Definitions, quality and access are engineering artefacts.",
        role="Cross-cutting",
        patterns=("Data quality checks · LGPD/GDPR awareness · curated contracts"),
        technologies=("data_quality", "data_warehousing", "snowflake"),
        experience=("mercantil", "kraken"),
        projects=("snowflake_governance",),
    ),
)

ARCHITECTURE_NODES: dict[str, ArchNode] = {node.id: node for node in ARCHITECTURE}
