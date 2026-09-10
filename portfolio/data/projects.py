"""Project catalogue.

Public projects carry the detail documented in `projects.md` (the repository's
own project notes). Professional projects stay at the level the résumé already
publishes: no employer-confidential detail, no invented architecture.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class FlowStep:
    label: str
    detail: str


@dataclass(frozen=True)
class Project:
    id: str
    name: str
    kind: str  # "public" | "professional"
    tagline: str
    domain: str
    summary: str
    problem: str
    context: str
    stack: tuple[str, ...]
    architecture: tuple[str, ...]
    data_flow: tuple[FlowStep, ...]
    decisions: tuple[str, ...]
    outcome: tuple[str, ...]
    lessons: tuple[str, ...] = field(default_factory=tuple)
    repo: str | None = None
    live: str | None = None
    status: str | None = None
    roles: tuple[str, ...] = field(default_factory=tuple)


PUBLIC_PROJECTS: tuple[Project, ...] = (
    Project(
        id="paysim",
        name="PaySim Dataset Explorer",
        kind="public",
        tagline="Fraud dataset exploration without loading the dataset",
        domain="fraud analytics · data engineering",
        summary=(
            "A Streamlit explorer for the multi-gigabyte PaySim synthetic financial "
            "dataset, built around a SQL-centric backend and streaming aggregation."
        ),
        problem=(
            "The interesting questions about a fraud dataset are aggregate ones: mule "
            "accounts, balance-draining transactions, whether the fraud flag actually "
            "works. Answering them by loading the whole dataset into memory is what "
            "crashes the app."
        ),
        context=(
            "Built as an interview-grade project: the constraint was performance and "
            "memory safety on a dataset that does not fit comfortably in RAM."
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
        architecture=(
            "SQLite backend: the dataset is ingested once and queried from there, so it "
            "never has to sit in a DataFrame.",
            "Query layer: every chart maps to one targeted SQL aggregation.",
            "Parallel executor: independent queries run together through "
            "ThreadPoolExecutor.",
            "Polars stage: aggregations that SQL handles badly, such as mule-account "
            "ranking, run in streaming chunks.",
            "Streamlit UI: home statistics, exploration views and fraud-specific analyses.",
        ),
        data_flow=(
            FlowStep("SOURCE", "PaySim synthetic dataset downloaded from Kaggle."),
            FlowStep(
                "INGESTION",
                "Chunked CSV ingestion into SQLite, memory-safe by construction.",
            ),
            FlowStep("QUERY", "One targeted aggregation per chart, executed in parallel."),
            FlowStep(
                "AGGREGATE",
                "Polars streaming pass for mule-account aggregation, released chunk by chunk.",
            ),
            FlowStep("SURFACE", "Streamlit views: dataset health, distributions, fraud flags."),
        ),
        decisions=(
            "Query-per-chart instead of load-everything: the UI only ever pulls the "
            "aggregate it renders.",
            "Polars streaming for the aggregations SQL is not built for, with the "
            "intermediate dataset never materialised.",
            "Data-aware startup: the app checks whether the dataset exists and offers a "
            "one-click Kaggle download through Streamlit secrets.",
        ),
        outcome=(
            "Analysis of a multi-gigabyte fraud dataset that stays stable instead of "
            "crashing on load.",
            "Mule-account and balance-draining fraud views that answer questions the raw "
            "dataset does not.",
        ),
        lessons=(
            "Memory was a design constraint, not a tuning detail. Deciding up front that "
            "the dataset would never be held in memory is what made the app stable.",
        ),
        repo="https://github.com/RVerdiF/PaysimViz",
        live="https://rverdif-paysimviz-app-olphe6.streamlit.app/",
        status="repository · live demo",
    ),
    Project(
        id="btc",
        name="BTC Prediction Pipeline",
        kind="public",
        tagline="A modular ML pipeline with per-user models and backtesting",
        domain="machine learning · MLOps",
        summary=(
            "An end-to-end Bitcoin price-prediction project: scheduled data collection, "
            "feature engineering, LightGBM classification, persistence and an interactive "
            "dashboard."
        ),
        problem=(
            "A prediction project only becomes interesting once the whole loop exists: "
            "data arrives on a schedule, features are reproducible, models are stored, "
            "and the result can be tested against a strategy."
        ),
        context=(
            "Built to exercise modular Python architecture: every responsibility "
            "(API, auth, features, training, orchestration, logging) lives in its own "
            "handler."
        ),
        stack=(
            "Python",
            "Streamlit",
            "LightGBM",
            "scikit-learn",
            "Pandas",
            "Plotly",
            "SQLite",
            "yfinance",
            "joblib",
        ),
        architecture=(
            "ApiHandler: market data collection through yfinance.",
            "DataHandler: price database, model database and feature engineering.",
            "ModelHandler: training and prediction, persisted with joblib.",
            "BacktestHandler: simulates a strategy on top of the trained model.",
            "Orchestration: daily background update so the dashboard is never stale.",
            "AuthHandler: multi-user access with per-user models and settings.",
            "LogHandler: centralized logging across the pipeline.",
        ),
        data_flow=(
            FlowStep("COLLECT", "Daily price series pulled from Yahoo Finance."),
            FlowStep("STORE", "Prices persisted to SQLite, with the last update recorded."),
            FlowStep(
                "FEATURES",
                "Technical indicators computed: SMA, RSI, EMA, MACD, Bollinger Bands and "
                "the Stochastic Oscillator.",
            ),
            FlowStep("TARGET", "Binary next-day direction (up / down)."),
            FlowStep(
                "TRAIN",
                "LightGBM classifier evaluated with TimeSeriesSplit (3 folds), scored on "
                "accuracy and F1.",
            ),
            FlowStep(
                "PERSIST",
                "Model, metrics and parameters stored per user in SQLite.",
            ),
            FlowStep(
                "SERVE",
                "Streamlit dashboard: price history, next-day prediction with confidence, "
                "custom training and backtesting.",
            ),
        ),
        decisions=(
            "TimeSeriesSplit instead of random cross-validation: the split respects "
            "chronology, so the evaluation does not leak the future.",
            "Per-user persistence of models and training parameters, so a session can "
            "resume where it stopped.",
            "Data updates run in a background thread; the interface never blocks on I/O.",
        ),
        outcome=(
            "A complete loop from scheduled ingestion to a served prediction and a "
            "backtested strategy.",
            "A dashboard where a user can retrain with their own parameters and keep the "
            "result.",
        ),
        lessons=(
            "I stopped treating the schedule as an operational detail. The daily update "
            "is the part that makes the dashboard worth opening.",
        ),
        repo="https://github.com/RVerdiF/TechChallenge3",
        live="https://techchallenge3rafaelfreitas.streamlit.app/",
        status="repository · live demo",
    ),
    Project(
        id="embrapa",
        name="Embrapa Viticulture API",
        kind="public",
        tagline="A documented REST layer over public agricultural data",
        domain="data engineering · APIs",
        summary=(
            "A FastAPI service that extracts viticulture data from Embrapa's Vitibrasil "
            "portal and exposes it as validated, filterable JSON endpoints."
        ),
        problem=(
            "The source data is published as web tables. Anything downstream, whether an "
            "analysis or a model, needs it as a typed API with predictable filters."
        ),
        context=(
            "Built as a data-engineering challenge: extraction, validation, containerized "
            "delivery and documentation, end to end."
        ),
        stack=(
            "Python",
            "FastAPI",
            "Pydantic",
            "Pandas",
            "Docker",
            "Docker Compose",
            "PyYAML",
        ),
        architecture=(
            "Scraping layer: extraction modules per dataset category.",
            "Models: Pydantic schemas validating data at the API boundary.",
            "Routers: one route group per category, plus filter endpoints.",
            "Utils and YAML configuration: extraction settings kept out of the code.",
            "Delivery: Dockerfile with separate development and production Compose files.",
        ),
        data_flow=(
            FlowStep("SOURCE", "Embrapa Vitibrasil portal tables."),
            FlowStep(
                "EXTRACT",
                "Scraping modules per category: production, commercialisation, processing, "
                "exports, imports.",
            ),
            FlowStep("VALIDATE", "Pydantic models type-check and normalise every record."),
            FlowStep(
                "SERVE",
                "REST endpoints by category, product, year, quantity range and combined "
                "filters, with Swagger documentation.",
            ),
            FlowStep("CONSUME", "JSON consumers: analysis, dashboards or an ML model."),
        ),
        decisions=(
            "Validation at the boundary with Pydantic, so downstream consumers never see "
            "malformed records.",
            "Filters as first-class endpoints (category, product, year, minimum and maximum "
            "quantity, combined), instead of forcing clients to post-process.",
            "Separate Compose files for development (hot reload) and production.",
        ),
        outcome=(
            "A documented API with five dataset categories and composable filters.",
            "A documented extension path: the same data feeding a production-forecasting "
            "model.",
        ),
        lessons=(
            "Writing the schema down changed how I built the extractors, because every "
            "field had to mean something specific. That is the difference between a "
            "scraper and a service.",
        ),
        repo="https://github.com/RVerdiF/api-embrapa-tech-challenge",
        live=None,
        status="repository (hosted demo retired)",
    ),
)


PROFESSIONAL_PROJECTS: tuple[Project, ...] = (
    Project(
        id="fraud_monitoring",
        name="Fraud Analytics & Transaction Monitoring",
        kind="professional",
        tagline="Production fraud detection, monitoring and KPI visibility",
        domain="banking · fraud prevention",
        summary=(
            "Predictive fraud models and institutional transaction-monitoring, with "
            "statistical anomaly monitoring and Power BI dashboards over the results."
        ),
        problem=(
            "Fraud review needed to move from periodic manual analysis to continuous "
            "detection with visible outcomes."
        ),
        context="Confidential work from Data Scientist and Data Analyst roles.",
        stack=("Python", "SQL", "Power BI", "anomaly detection", "predictive models"),
        architecture=(
            "Predictive models for transactional fraud prevention.",
            "Institutional transaction-monitoring system.",
            "Statistical anomaly monitoring over transactional activity.",
            "KPI and Power BI dashboards for fraud analytics.",
        ),
        data_flow=(
            FlowStep("SIGNALS", "Transactional activity feeds continuous monitoring."),
            FlowStep("DETECTION", "Predictive models and algorithms score transactions."),
            FlowStep("MONITORING", "Statistical anomaly detection surfaces deviations."),
            FlowStep("REVIEW", "Analysts work the cases the system raises."),
            FlowStep("VISIBILITY", "KPI and Power BI dashboards close the loop."),
        ),
        decisions=(
            "I shipped detection and visibility together, because a model nobody can watch "
            "is a model that gets switched off.",
        ),
        outcome=(
            "30%+ faster case resolution in the fraud-prevention workflow.",
            "Institutional monitoring plus dashboards that made fraud performance "
            "measurable.",
        ),
        roles=("mercantil",),
    ),
    Project(
        id="ai_agents_mlops",
        name="Autonomous AI Agents & MLOps Pipelines",
        kind="professional",
        tagline="Agents and MLOps automating complex data workflows",
        domain="AI systems · MLOps",
        summary=(
            "Designed, engineered and orchestrated autonomous AI agents and MLOps "
            "pipelines to automate complex data workflows."
        ),
        problem=(
            "Data workflows with many recurring steps consume engineering time that "
            "should be spent on the next problem."
        ),
        context="Confidential work from a Data Scientist role.",
        stack=(
            "Python",
            "AI/ML",
            "MLOps",
            "CI/CD",
            "Docker",
            "AWS",
            "AI agents",
        ),
        architecture=(
            "Autonomous agents executing multi-step data workflows.",
            "MLOps pipelines keeping models and data products reproducible.",
            "CI/CD and containerized delivery on AWS.",
        ),
        data_flow=(
            FlowStep("TRIGGER", "A workflow step is queued or scheduled."),
            FlowStep("AGENTS", "Autonomous agents execute the steps end to end."),
            FlowStep("MLOPS", "Pipelines version, test and deploy the resulting artifacts."),
            FlowStep("OUTCOME", "Recurring manual effort removed from the workflow."),
        ),
        decisions=(
            "Automation went through CI/CD like any other deliverable. Versioned pipelines "
            "are what let someone else own the workflow later.",
        ),
        outcome=(
            "Complex data workflows automated end to end.",
            "AI/MLOps practices carried into production fraud-detection workflows.",
        ),
        roles=("mercantil",),
    ),
    Project(
        id="production_analytics",
        name="Production Data & Analytics Solutions",
        kind="professional",
        tagline="Analytics that business decisions can depend on",
        domain="analytics engineering",
        summary=(
            "Data and analytics solutions supporting business decisions with reliable, "
            "accessible data, plus automation of recurring reporting."
        ),
        problem=(
            "Recurring reports and operational processes were rebuilt by hand every "
            "cycle, which made delivery slow and quality inconsistent."
        ),
        context="Confidential work from an Analytics Engineer / Data Consultant role.",
        stack=("SQL", "Python", "data modeling", "data quality", "automation"),
        architecture=(
            "Data and analytics solutions modeled for reliability and accessibility.",
            "Automated recurring reporting and operational processes.",
            "Data reliability and quality work across analytics workflows.",
        ),
        data_flow=(
            FlowStep("REQUIREMENT", "Partner areas bring the business question."),
            FlowStep("MODEL", "Data is modeled so the answer is repeatable."),
            FlowStep("AUTOMATE", "Recurring reporting stops being manual."),
            FlowStep("DELIVER", "Requirements land as deliverables, not one-off extracts."),
        ),
        decisions=(
            "Requirements translated with partner areas before modeling, so the "
            "deliverable matches the decision being made.",
        ),
        outcome=(
            "Manual effort reduced and delivery reliability improved.",
            "Data reliability and quality raised across analytics workflows.",
        ),
        roles=("kraken",),
    ),
    Project(
        id="snowflake_governance",
        name="Data Governance & Automation in Snowflake",
        kind="professional",
        tagline="Governed warehouse objects and automated processes",
        domain="data governance · Snowflake",
        summary=(
            "Created and managed tables, views and stored procedures in Snowflake while "
            "automating departmental processes."
        ),
        problem=(
            "A warehouse without governed objects and automated routines becomes a "
            "collection of private queries."
        ),
        context="Confidential work from a Data Analyst role.",
        stack=("Snowflake", "SQL", "Python", "dbt", "data governance"),
        architecture=(
            "Tables, views and stored procedures managed in Snowflake.",
            "Departmental processes automated around the warehouse.",
            "Governance practices applied to the modeled objects.",
        ),
        data_flow=(
            FlowStep("MODEL", "Tables and views created and maintained in Snowflake."),
            FlowStep("PROCEDURE", "Stored procedures encapsulate the repeated logic."),
            FlowStep("AUTOMATE", "Departmental processes run without manual intervention."),
        ),
        decisions=(
            "Repeated logic pushed into stored procedures so it lives in one place instead "
            "of in every analyst's query.",
        ),
        outcome=(
            "Departmental processes automated on top of a governed warehouse layer.",
        ),
        roles=("mercantil",),
    ),
)


PROJECTS_BY_ID: dict[str, Project] = {
    project.id: project for project in (*PUBLIC_PROJECTS, *PROFESSIONAL_PROJECTS)
}
