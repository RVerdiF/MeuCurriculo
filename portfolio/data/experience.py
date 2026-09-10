"""Professional history, kept short on purpose.

Each role answers six questions and stops: role, company, context, what I
owned, main impact, core technologies. The technical depth lives in
`portfolio.data.projects`, so nothing is told twice.

Every title, date and technology below comes from `CV.pdf`.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Role:
    id: str
    title: str
    company: str
    period: str
    location: str
    context: str
    owned: tuple[str, ...]
    impact: tuple[str, ...]
    technologies: tuple[str, ...]
    systems: tuple[str, ...] = field(default_factory=tuple)  # project ids
    progression: tuple[str, ...] = field(default_factory=tuple)
    current: bool = False


EXPERIENCE: tuple[Role, ...] = (
    Role(
        id="sapiens",
        title="Lead Engineer",
        company="Sapiens Management & Technologies",
        period="Nov 2025 — Present",
        location="Belo Horizonte, Brazil",
        context="Data consultancy on cloud platforms: AWS, dbt, Snowflake and Kubernetes.",
        owned=(
            "Lead client engagements from the business requirement through to a platform "
            "running in production.",
            "Run the engineering side of each engagement, including the MLOps and "
            "automation work.",
        ),
        impact=(
            "Engagements end in a working platform, with the ML and automation owned "
            "in-house rather than handed off.",
        ),
        technologies=("aws", "dbt", "snowflake", "kubernetes", "python", "mlops", "ci_cd"),
        current=True,
    ),
    Role(
        id="kraken",
        title="Analytics Engineer / Data Consultant",
        company="Kraken",
        period="Nov 2025 — Present",
        location="Brazil",
        context="Digital-asset business: analytics and reporting for partner areas.",
        owned=(
            "Build and maintain the data and analytics solutions the business makes "
            "decisions with.",
            "Automate recurring reports and operational processes.",
            "Raise data quality across analytics workflows, working with partner areas "
            "on requirements.",
        ),
        impact=(
            "Recurring reporting runs without a manual rebuild every cycle.",
        ),
        technologies=("sql", "python", "data_modeling", "data_quality", "automation"),
        systems=("analytics_platform",),
        current=True,
    ),
    Role(
        id="mercantil",
        title="Data Scientist / Data Analytics",
        company="Banco Mercantil",
        period="Nov 2019 — Nov 2025",
        location="Belo Horizonte, Brazil",
        context="Fraud prevention inside a bank: pipelines, predictive models and monitoring.",
        owned=(
            "Progressed from intern to fraud analyst to Data Scientist over six years.",
            "Built and maintained the pipelines and models behind transactional fraud "
            "detection.",
            "Managed tables, views and stored procedures in Snowflake, and automated the "
            "departmental processes around them.",
            "Applied AI/MLOps practices to production fraud workflows.",
        ),
        impact=(
            "~80% of recurring fraud-prevention processes automated.",
            "30%+ faster case resolution once the pipelines and models reached production.",
        ),
        technologies=(
            "python",
            "sql",
            "machine_learning",
            "anomaly_detection",
            "mlops",
            "docker",
            "kubernetes",
            "power_bi",
            "snowflake",
            "dbt",
            "fraud_analytics",
        ),
        systems=("fraud_monitoring", "ai_agents_mlops"),
        progression=("Intern", "Fraud Analyst", "Data Scientist"),
    ),
    Role(
        id="corporate",
        title="Founder & Lead Engineer",
        company="Corporate Gestão Empresarial",
        period="Aug 2018 — Present",
        location="Greater Belo Horizonte",
        context="Technical strategy for companies: AI, automation and data applied to "
        "business processes.",
        owned=(
            "Run the consulting work end to end, from the commercial conversation to the "
            "delivered system.",
            "Turn a business need into a technical roadmap, then own the delivery.",
        ),
        impact=(
            "Business processes improved, with decisions supported by the data coming out "
            "of them.",
        ),
        technologies=("python", "automation", "ai_workflows", "local_llm", "data_quality"),
        current=True,
    ),
)

ROLES_BY_ID: dict[str, Role] = {role.id: role for role in EXPERIENCE}
