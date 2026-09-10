"""Core stack: fourteen technologies, organised by what they are for.

The résumé names more tools than this. Anything that did not carry real work
in a role or a project stays out of the core list and keeps its label in
`TECH_LABELS`, so a role can still show it as a chip without the section
turning into a logo wall.

Each core technology carries `evidence`: the place it was actually used. That
makes the section a claim with a reference instead of a list.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Evidence:
    kind: str  # role | project | education | course | skills
    ref: str
    detail: str


@dataclass(frozen=True)
class Technology:
    id: str
    name: str
    what: str
    evidence: tuple[Evidence, ...]


@dataclass(frozen=True)
class StackGroup:
    id: str
    label: str
    purpose: str
    technologies: tuple[str, ...]


CORE_STACK: tuple[StackGroup, ...] = (
    StackGroup(
        id="languages",
        label="LANGUAGES",
        purpose="The two languages everything else is written or queried in",
        technologies=("python", "sql"),
    ),
    StackGroup(
        id="transform",
        label="TRANSFORM",
        purpose="Where business logic lives, once",
        technologies=("dbt",),
    ),
    StackGroup(
        id="orchestrate",
        label="ORCHESTRATE",
        purpose="Make it run without a human in the loop",
        technologies=("airflow",),
    ),
    StackGroup(
        id="warehouse",
        label="WAREHOUSE",
        purpose="Modelling, governance and performance",
        technologies=("snowflake",),
    ),
    StackGroup(
        id="cloud",
        label="CLOUD",
        purpose="Where the platform lives",
        technologies=("aws",),
    ),
    StackGroup(
        id="compute",
        label="COMPUTE",
        purpose="Processing that does not fit in memory",
        technologies=("spark", "pandas"),
    ),
    StackGroup(
        id="platform",
        label="PLATFORM",
        purpose="The same artifact from laptop to production",
        technologies=("docker", "kubernetes"),
    ),
    StackGroup(
        id="analytics",
        label="ANALYTICS",
        purpose="For the people making the decision",
        technologies=("power_bi",),
    ),
    StackGroup(
        id="ai",
        label="AI / ML",
        purpose="Models and agents that change how work gets done",
        technologies=("machine_learning", "mlops", "ai_agents"),
    ),
)

CORE_TECHNOLOGIES: tuple[Technology, ...] = (
    Technology(
        id="python",
        name="Python",
        what="The working language: extraction, pipelines, modelling and automation.",
        evidence=(
            Evidence("role", "mercantil", "Pipelines, models and process automation."),
            Evidence("role", "kraken", "Analytics and reporting automation."),
            Evidence("project", "ai_agents_mlops", "Agents and MLOps pipelines."),
            Evidence("project", "paysim", "Query layer and streaming aggregation."),
        ),
    ),
    Technology(
        id="sql",
        name="SQL",
        what="Query and modelling language behind every warehouse and analysis layer.",
        evidence=(
            Evidence("role", "mercantil", "Analysis, monitoring and warehouse objects."),
            Evidence("project", "analytics_platform", "Analytics solutions modelled for reuse."),
            Evidence("project", "paysim", "One targeted aggregation per view."),
        ),
    ),
    Technology(
        id="dbt",
        name="dbt",
        what="Transformation and business logic on top of the warehouse.",
        evidence=(
            Evidence("role", "sapiens", "dbt inside client cloud platform engagements."),
            Evidence("role", "mercantil", "Modelling alongside the Snowflake work."),
            Evidence("course", "DBT e Snowflake", "triggo.ai · Jun 2023"),
        ),
    ),
    Technology(
        id="airflow",
        name="Airflow",
        what="Scheduling and orchestration of data workflows.",
        evidence=(
            Evidence("skills", "", "Listed under Cloud & Infrastructure in the résumé."),
        ),
    ),
    Technology(
        id="snowflake",
        name="Snowflake",
        what="Cloud warehouse: modelling, governance and performance.",
        evidence=(
            Evidence("role", "sapiens", "Snowflake as the warehouse layer."),
            Evidence("role", "mercantil", "Tables, views and stored procedures."),
            Evidence("course", "DBT e Snowflake", "triggo.ai · Jun 2023"),
        ),
    ),
    Technology(
        id="aws",
        name="AWS",
        what="Cloud platform for data and ML workloads.",
        evidence=(
            Evidence("role", "sapiens", "Client cloud platform engagements."),
            Evidence("project", "ai_agents_mlops", "Containerized delivery on AWS."),
            Evidence("education", "fiap", "Scalable ML in AWS environments."),
        ),
    ),
    Technology(
        id="spark",
        name="Spark",
        what="Distributed processing for large data volumes.",
        evidence=(
            Evidence("education", "fiap", "Hadoop and Spark platforms for scalable ML."),
        ),
    ),
    Technology(
        id="pandas",
        name="Pandas",
        what="Data manipulation for analysis and feature work.",
        evidence=(
            Evidence("project", "paysim", "Aggregation and reshaping."),
            Evidence("education", "fiap", "Feature work in the ML specialization."),
        ),
    ),
    Technology(
        id="docker",
        name="Docker",
        what="Packaging: the same artifact from laptop to production.",
        evidence=(
            Evidence("role", "mercantil", "Containerized models and pipelines."),
            Evidence("project", "ai_agents_mlops", "Container-based delivery."),
        ),
    ),
    Technology(
        id="kubernetes",
        name="Kubernetes",
        what="Running containerized workloads in production.",
        evidence=(
            Evidence("role", "sapiens", "Runtime for client platform work."),
            Evidence("role", "mercantil", "ML workloads and case-resolution pipelines."),
        ),
    ),
    Technology(
        id="power_bi",
        name="Power BI",
        what="Dashboards and KPIs for the people making the decision.",
        evidence=(
            Evidence("role", "mercantil", "Fraud analytics dashboards and KPIs."),
            Evidence("project", "fraud_monitoring", "KPI and Power BI visibility."),
            Evidence("course", "Análise de Dados e Power BI", "Escola Conquer · Sep 2023"),
        ),
    ),
    Technology(
        id="machine_learning",
        name="Machine Learning",
        what="Predictive models that run in production and get monitored there.",
        evidence=(
            Evidence("role", "mercantil", "Predictive fraud models."),
            Evidence("project", "fraud_monitoring", "Models scoring transactions."),
            Evidence("education", "fiap", "Machine Learning Engineering specialization."),
        ),
    ),
    Technology(
        id="mlops",
        name="MLOps",
        what="Keeping models reproducible, deployable and monitored.",
        evidence=(
            Evidence("role", "sapiens", "MLOps initiatives in client engagements."),
            Evidence("role", "mercantil", "AI/MLOps in production fraud detection."),
            Evidence("project", "ai_agents_mlops", "MLOps pipelines with CI/CD."),
        ),
    ),
    Technology(
        id="ai_agents",
        name="AI Agents",
        what="Autonomous agents applied to multi-step data workflows.",
        evidence=(
            Evidence("project", "ai_agents_mlops", "Agents orchestrated end to end."),
            Evidence("course", "AI Agents — Google", "Alura · Sep 2025"),
        ),
    ),
)

CORE_BY_ID: dict[str, Technology] = {tech.id: tech for tech in CORE_TECHNOLOGIES}

# Display names for every technology id referenced anywhere on the page,
# including the tools that are not part of the core list. A role chip should
# never disappear just because a tool did not make the core fourteen.
TECH_LABELS: dict[str, str] = {
    "python": "Python",
    "sql": "SQL",
    "dbt": "dbt",
    "airflow": "Airflow",
    "snowflake": "Snowflake",
    "aws": "AWS",
    "spark": "Spark",
    "pandas": "Pandas",
    "polars": "Polars",
    "docker": "Docker",
    "kubernetes": "Kubernetes",
    "power_bi": "Power BI",
    "hex": "Hex",
    "machine_learning": "Machine learning",
    "mlops": "MLOps",
    "ai_agents": "AI agents",
    "ai_workflows": "Autonomous workflows",
    "local_llm": "Local LLM",
    "automation": "Process automation",
    "data_modeling": "Data modeling",
    "data_quality": "Data quality",
    "fraud_analytics": "Fraud analytics",
    "anomaly_detection": "Anomaly detection",
    "ci_cd": "CI/CD",
}


def label_of(technology_id: str) -> str:
    """Display name for a technology id, falling back to the id itself."""
    return TECH_LABELS.get(technology_id, technology_id)
