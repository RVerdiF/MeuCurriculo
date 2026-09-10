"""Technology map, organized by responsibility and backed by evidence.

Only technologies named in the résumé (skills, roles, education or projects)
appear here. Each entry carries pointers to where it was actually used, so the
technology section is a claim with a reference instead of a list of logos.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Evidence:
    kind: str  # role | project | education | course
    ref: str
    detail: str


@dataclass(frozen=True)
class Technology:
    id: str
    name: str
    what: str
    evidence: tuple[Evidence, ...] = field(default_factory=tuple)
    tags: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class StackLayer:
    id: str
    label: str
    purpose: str
    technologies: tuple[str, ...]


STACK: tuple[StackLayer, ...] = (
    StackLayer(
        id="ingest",
        label="INGEST",
        purpose="Get data out of systems and into the platform",
        technologies=("python", "rest_apis", "extraction"),
    ),
    StackLayer(
        id="orchestrate",
        label="ORCHESTRATE",
        purpose="Make it run without a human in the loop",
        technologies=("airflow", "scheduling", "ci_cd"),
    ),
    StackLayer(
        id="transform",
        label="TRANSFORM",
        purpose="Turn raw data into models the business agrees on",
        technologies=("dbt", "sql", "data_modeling"),
    ),
    StackLayer(
        id="store",
        label="STORE",
        purpose="Warehouse and persistence layers",
        technologies=("snowflake", "sqlite", "data_warehousing", "golden_tables"),
    ),
    StackLayer(
        id="compute",
        label="COMPUTE",
        purpose="Process data that does not fit in memory",
        technologies=("spark", "pandas", "polars"),
    ),
    StackLayer(
        id="ship",
        label="SHIP",
        purpose="Run the same artifact everywhere",
        technologies=("docker", "kubernetes"),
    ),
    StackLayer(
        id="cloud",
        label="CLOUD",
        purpose="Where the platform lives",
        technologies=("aws", "athena"),
    ),
    StackLayer(
        id="analyze",
        label="ANALYZE",
        purpose="Make the result usable by people who are not engineers",
        technologies=("power_bi", "hex", "kpis", "self_service"),
    ),
    StackLayer(
        id="ai",
        label="AI / ML",
        purpose="Models and agents that change how work gets done",
        technologies=("machine_learning", "mlops", "ai_agents", "ai_workflows", "local_llm"),
    ),
)


TECHNOLOGIES: tuple[Technology, ...] = (
    Technology(
        id="python",
        name="Python",
        what="The working language: extraction, pipelines, modeling and automation.",
        tags=("language", "automation"),
        evidence=(
            Evidence("role", "mercantil", "Pipelines, models and process automation."),
            Evidence("project", "ai_agents_mlops", "Agents and MLOps pipelines."),
            Evidence("project", "paysim", "Query layer and streaming aggregation."),
            Evidence("project", "btc", "Feature engineering, training and prediction."),
            Evidence("project", "embrapa", "Extraction and API service."),
        ),
    ),
    Technology(
        id="sql",
        name="SQL",
        what="Query and modeling language behind every warehouse and analysis layer.",
        tags=("language", "modeling"),
        evidence=(
            Evidence("role", "mercantil", "Analysis and monitoring queries."),
            Evidence("project", "production_analytics", "Modeled analytics solutions."),
            Evidence("project", "snowflake_governance", "Tables, views and procedures."),
            Evidence("project", "paysim", "One targeted aggregation per view."),
        ),
    ),
    Technology(
        id="dbt",
        name="dbt",
        what="Transformation and business logic on top of the warehouse.",
        tags=("transform",),
        evidence=(
            Evidence("role", "sapiens", "dbt inside client cloud platform engagements."),
            Evidence("project", "snowflake_governance", "dbt beside Snowflake governance."),
            Evidence("course", "DBT e Snowflake", "triggo.ai · Jun 2023"),
        ),
    ),
    Technology(
        id="snowflake",
        name="Snowflake",
        what="Cloud warehouse: modeling, governance and performance.",
        tags=("warehouse",),
        evidence=(
            Evidence("role", "sapiens", "Snowflake as the warehouse layer."),
            Evidence("project", "snowflake_governance", "Tables, views, stored procedures."),
            Evidence("course", "DBT e Snowflake", "triggo.ai · Jun 2023"),
        ),
    ),
    Technology(
        id="aws",
        name="AWS",
        what="Cloud platform for data and ML workloads.",
        tags=("cloud",),
        evidence=(
            Evidence("role", "sapiens", "Client cloud platform engagements."),
            Evidence("project", "ai_agents_mlops", "Containerised delivery on AWS."),
            Evidence("education", "fiap", "Scalable ML in AWS environments."),
        ),
    ),
    Technology(
        id="athena",
        name="Athena",
        what="Querying data directly where it is stored on AWS.",
        tags=("cloud", "query"),
        evidence=(
            Evidence("skills", "", "Listed under Languages & Tools in the résumé."),
        ),
    ),
    Technology(
        id="kubernetes",
        name="Kubernetes",
        what="Running containerized workloads in production.",
        tags=("platform",),
        evidence=(
            Evidence("role", "sapiens", "Runtime for client platform work."),
            Evidence("role", "mercantil", "ML workloads and case-resolution pipelines."),
        ),
    ),
    Technology(
        id="docker",
        name="Docker",
        what="Packaging: the same artifact from laptop to production.",
        tags=("platform",),
        evidence=(
            Evidence("role", "mercantil", "Containerised models and pipelines."),
            Evidence("project", "embrapa", "Development and production Compose files."),
            Evidence("project", "ai_agents_mlops", "Container-based delivery."),
        ),
    ),
    Technology(
        id="airflow",
        name="Airflow",
        what="Scheduling and orchestration of data workflows.",
        tags=("orchestration",),
        evidence=(
            Evidence("skills", "", "Listed under Cloud & Infrastructure in the résumé."),
        ),
    ),
    Technology(
        id="spark",
        name="Spark",
        what="Distributed processing for large data volumes.",
        tags=("compute",),
        evidence=(
            Evidence("education", "fiap", "Hadoop and Spark platforms for scalable ML."),
        ),
    ),
    Technology(
        id="pandas",
        name="Pandas",
        what="Data manipulation for analysis and feature work.",
        tags=("compute",),
        evidence=(
            Evidence("project", "embrapa", "Extraction and reshaping."),
            Evidence("project", "btc", "Price series and feature engineering."),
        ),
    ),
    Technology(
        id="polars",
        name="Polars",
        what="High-performance aggregation when SQL is the wrong tool.",
        tags=("compute",),
        evidence=(
            Evidence("project", "paysim", "Streaming mule-account aggregation."),
        ),
    ),
    Technology(
        id="power_bi",
        name="Power BI",
        what="Dashboards and KPIs for the people making the decision.",
        tags=("analytics",),
        evidence=(
            Evidence("role", "mercantil", "Fraud analytics dashboards and KPIs."),
            Evidence("project", "fraud_monitoring", "KPI and Power BI visibility."),
            Evidence("course", "Análise de Dados e Power BI", "Escola Conquer · Sep 2023"),
        ),
    ),
    Technology(
        id="hex",
        name="Hex",
        what="Collaborative notebooks for analytics work.",
        tags=("analytics",),
        evidence=(
            Evidence("skills", "", "Listed under Analytics & BI in the résumé."),
        ),
    ),
    Technology(
        id="machine_learning",
        name="Machine Learning",
        what="Predictive models that run in production and get monitored there.",
        tags=("ml",),
        evidence=(
            Evidence("role", "mercantil", "Predictive fraud models."),
            Evidence("project", "btc", "LightGBM with time-series validation."),
            Evidence("education", "fiap", "Machine Learning Engineering specialization."),
        ),
    ),
    Technology(
        id="mlops",
        name="MLOps",
        what="Keeping models reproducible, deployable and monitored.",
        tags=("ml",),
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
        tags=("ai",),
        evidence=(
            Evidence("project", "ai_agents_mlops", "Agents orchestrated end to end."),
            Evidence("course", "AI Agents — Google", "Alura · Sep 2025"),
        ),
    ),
    Technology(
        id="local_llm",
        name="Local LLM",
        what="Models running on my own hardware, for work that cannot leave the building.",
        tags=("ai",),
        evidence=(
            Evidence("skills", "", "Listed under ML & Automation in the résumé."),
        ),
    ),
    Technology(
        id="ai_workflows",
        name="Autonomous Workflows",
        what="Automation that carries the process through to the end.",
        tags=("ai", "automation"),
        evidence=(
            Evidence("role", "corporate", "AI and automation applied to business processes."),
            Evidence("project", "ai_agents_mlops", "Workflow automation as a deliverable."),
        ),
    ),
    Technology(
        id="automation",
        name="Process Automation",
        what="Removing the manual step from a recurring process.",
        tags=("automation",),
        evidence=(
            Evidence("role", "mercantil", "~80% of recurring processes automated."),
            Evidence("role", "kraken", "Recurring reports and operational processes."),
        ),
    ),
    Technology(
        id="scheduling",
        name="Scheduling",
        what="Jobs that run on their own and keep the data fresh.",
        tags=("orchestration",),
        evidence=(
            Evidence("project", "btc", "Daily background price updates."),
        ),
    ),
    Technology(
        id="ci_cd",
        name="CI/CD",
        what="Automated build, test and delivery for data products.",
        tags=("orchestration", "platform"),
        evidence=(
            Evidence("project", "ai_agents_mlops", "CI/CD for MLOps delivery."),
            Evidence("education", "fiap", "CI/CD for model deployment."),
        ),
    ),
    Technology(
        id="rest_apis",
        name="REST APIs",
        what="Contracts for moving data between systems.",
        tags=("ingest",),
        evidence=(
            Evidence("project", "embrapa", "Designed and documented a public API."),
        ),
    ),
    Technology(
        id="extraction",
        name="Web Extraction",
        what="Getting data out of sources that only publish tables.",
        tags=("ingest",),
        evidence=(
            Evidence("project", "embrapa", "Category-level extraction modules."),
        ),
    ),
    Technology(
        id="data_modeling",
        name="Data Modeling",
        what="Structures that make the same question answerable twice.",
        tags=("transform",),
        evidence=(
            Evidence("role", "kraken", "Analytics solutions modeled for reuse."),
            Evidence("education", "puc-mgmt", "Dimensional modeling for warehouses."),
        ),
    ),
    Technology(
        id="data_warehousing",
        name="Data Warehousing",
        what="The layer everything else is built on.",
        tags=("store",),
        evidence=(
            Evidence("education", "puc-mgmt", "Dimensional modeling for warehouses."),
            Evidence("project", "snowflake_governance", "Warehouse objects under governance."),
        ),
    ),
    Technology(
        id="golden_tables",
        name="Golden Table Architecture",
        what="One agreed, curated source of truth per domain.",
        tags=("store",),
        evidence=(
            Evidence("skills", "", "Listed under Data Engineering in the résumé."),
        ),
    ),
    Technology(
        id="sqlite",
        name="SQLite",
        what="Local, query-first persistence for applications.",
        tags=("store",),
        evidence=(
            Evidence("project", "paysim", "Dataset served entirely through SQLite."),
            Evidence("project", "btc", "Prices, users and models persisted locally."),
        ),
    ),
    Technology(
        id="kpis",
        name="KPIs",
        what="Deciding what quality means before building the dashboard.",
        tags=("analytics",),
        evidence=(
            Evidence("role", "mercantil", "KPI dashboards for fraud analytics."),
        ),
    ),
    Technology(
        id="self_service",
        name="Self-Service Analytics",
        what="Analytics that the business can run without a queue.",
        tags=("analytics",),
        evidence=(
            Evidence("skills", "", "Listed under Analytics & BI in the résumé."),
        ),
    ),
    Technology(
        id="data_quality",
        name="Data Quality",
        what="Checks that stop bad data before it reaches a decision.",
        tags=("governance", "transform"),
        evidence=(
            Evidence("role", "kraken", "Reliability and quality across analytics workflows."),
            Evidence("role", "mercantil", "Quality work over monitoring data."),
        ),
    ),
    Technology(
        id="fraud_analytics",
        name="Fraud Analytics",
        what="Turning transaction behavior into detection.",
        tags=("domain", "analytics"),
        evidence=(
            Evidence("role", "mercantil", "Six years inside fraud prevention."),
            Evidence("project", "fraud_monitoring", "Predictive models and monitoring."),
            Evidence("project", "paysim", "Fraud-pattern exploration at scale."),
        ),
    ),
    Technology(
        id="anomaly_detection",
        name="Anomaly Detection",
        what="Statistical monitoring over activity that never stops.",
        tags=("ml", "monitoring"),
        evidence=(
            Evidence("role", "mercantil", "Transactional activity monitored continuously."),
            Evidence("project", "fraud_monitoring", "Anomaly monitoring in production."),
        ),
    ),
)


STACK_TECHNOLOGIES: dict[str, Technology] = {tech.id: tech for tech in TECHNOLOGIES}

# Domain knowledge is not a tool, but it is what makes the tooling decisions
# non-generic. Kept in its own strip instead of being mixed into the stack.
DOMAIN_KNOWLEDGE: tuple[tuple[str, str], ...] = (
    ("Financial Services", "Banking data, its constraints and its compliance reality."),
    ("Fraud Prevention", "Six years inside fraud prevention, from analyst to model owner."),
    ("Digital Assets", "Analytics for a digital-asset platform."),
    ("Banking", "Institutional systems and regulated data."),
    ("Compliance", "Governance frameworks, including LGPD/GDPR study."),
    ("Technical Strategy", "Founder-side consulting: business need to technical roadmap."),
)
