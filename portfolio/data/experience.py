"""Professional history as structured systems history.

Every bullet, date and technology assignment below is taken from `CV.pdf`
and the résumé content previously published by this repository. Nothing is
inferred (for example, a technology is attached to a role only when the
résumé states it for that role's description).
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class FlowStage:
    """One stage of the delivery chain for a role (problem → outcome)."""

    key: str
    label: str
    detail: str


@dataclass(frozen=True)
class Impact:
    label: str
    detail: str


@dataclass(frozen=True)
class Role:
    id: str
    title: str
    company: str
    period: str
    start: str
    end: str
    location: str
    domain: str
    mission: str
    current: bool
    response: str  # what a terminal `experience` command prints
    responsibilities: tuple[str, ...]
    systems: tuple[str, ...]  # project ids from portfolio.data.projects
    technologies: tuple[str, ...]  # technology ids from portfolio.data.stack
    flow: tuple[FlowStage, ...]
    impacts: tuple[Impact, ...] = field(default_factory=tuple)
    progression: tuple[str, ...] = field(default_factory=tuple)


EXPERIENCE: tuple[Role, ...] = (
    Role(
        id="sapiens",
        title="Lead Engineer",
        company="Sapiens Management & Technologies",
        period="Nov 2025 — Present",
        start="2025-11",
        end="present",
        location="Belo Horizonte, Brazil",
        domain="Data consultancy · cloud data platforms",
        mission=(
            "Lead data consultancy engagements, owning delivery end to end — from "
            "business requirement to running platform."
        ),
        current=True,
        response=(
            "Sapiens Management & Technologies — Lead Engineer (Nov 2025 — Present)",
            "Leads data consultancy engagements on cloud platforms, owns delivery end "
            "to end and drives ML/MLOps initiatives.",
        ),
        responsibilities=(
            "Lead data consultancy engagements across cloud platforms (AWS, dbt, "
            "Snowflake, Kubernetes), delivering data and analytics solutions for clients.",
            "Drive ML/MLOps initiatives and automation to improve delivery and reliability "
            "of data products.",
            "Own end-to-end delivery and stakeholder alignment, translating business "
            "requirements into technical execution.",
        ),
        systems=(),
        technologies=("aws", "dbt", "snowflake", "kubernetes", "python", "mlops", "ci_cd"),
        flow=(
            FlowStage(
                key="problem",
                label="ENGAGEMENT",
                detail=(
                    "Client needs a data platform or analytics capability that has to run "
                    "in production, not a slide deck."
                ),
            ),
            FlowStage(
                key="platform",
                label="PLATFORM",
                detail="Cloud data platform built on AWS with dbt and Snowflake as the "
                "transformation and warehouse layer.",
            ),
            FlowStage(
                key="compute",
                label="RUNTIME",
                detail="Containerised workloads on Kubernetes, so environments stay "
                "reproducible from development to delivery.",
            ),
            FlowStage(
                key="ml",
                label="ML / MLOps",
                detail="MLOps initiatives and automation that improve reliability of the "
                "data products after go-live.",
            ),
            FlowStage(
                key="outcome",
                label="DELIVERY",
                detail="End-to-end ownership: requirements translated into technical "
                "execution, with stakeholder alignment along the way.",
            ),
        ),
        impacts=(),
    ),
    Role(
        id="kraken",
        title="Analytics Engineer / Data Consultant",
        company="Kraken",
        period="Nov 2025 — Present",
        start="2025-11",
        end="present",
        location="Brazil",
        domain="Digital assets · analytics engineering",
        mission=(
            "Keep analytics trustworthy for a digital-asset business: reliable data, "
            "automated recurring reporting, quality that survives partner hand-offs."
        ),
        current=True,
        response=(
            "Kraken — Analytics Engineer / Data Consultant (Nov 2025 — Present)",
            "Builds and maintains data and analytics solutions, automates recurring "
            "reporting and improves data reliability across analytics workflows.",
        ),
        responsibilities=(
            "Develop and maintain data and analytics solutions, supporting business "
            "decisions with reliable and accessible data.",
            "Automate recurring reports and operational processes, reducing manual effort "
            "and improving delivery reliability.",
            "Improve data reliability and quality across analytics workflows, collaborating "
            "with partner areas to translate requirements into deliverables.",
        ),
        systems=("production_analytics",),
        technologies=("sql", "python", "data_modeling", "data_quality", "automation"),
        flow=(
            FlowStage(
                key="problem",
                label="REQUIREMENT",
                detail="Business areas need numbers they can act on, and they need them "
                "without a manual rebuild every cycle.",
            ),
            FlowStage(
                key="model",
                label="DATA MODEL",
                detail="Data and analytics solutions modelled for reliability and "
                "accessibility rather than one-off queries.",
            ),
            FlowStage(
                key="automation",
                label="AUTOMATION",
                detail="Recurring reports and operational processes automated to cut "
                "manual effort.",
            ),
            FlowStage(
                key="quality",
                label="DATA QUALITY",
                detail="Reliability and quality work across analytics workflows, "
                "coordinated with partner areas.",
            ),
            FlowStage(
                key="outcome",
                label="DECISIONS",
                detail="Requirements turn into deliverables that business decisions can "
                "depend on.",
            ),
        ),
        impacts=(),
    ),
    Role(
        id="mercantil",
        title="Data Scientist / Data Analytics",
        company="Banco Mercantil",
        period="Nov 2019 — Nov 2025",
        start="2019-11",
        end="2025-11",
        location="Belo Horizonte, Brazil",
        domain="Banking · fraud prevention",
        mission=(
            "Move fraud prevention from manual review to monitored, automated detection — "
            "and prove it in production."
        ),
        current=False,
        response=(
            "Banco Mercantil — Data Scientist / Data Analytics (Nov 2019 — Nov 2025)",
            "Six years inside the fraud-prevention organisation: pipelines, predictive "
            "models, anomaly monitoring and automated processes.",
        ),
        responsibilities=(
            "Progressed from intern and fraud analyst to Data Scientist over six years "
            "within the fraud-prevention organization.",
            "Automated ~80% of recurring processes and delivered an end-to-end "
            "fraud-prevention solution.",
            "Built and maintained pipelines and models, leveraging ML, Docker, and "
            "Kubernetes to accelerate case resolution by 30%+.",
            "Monitored transactional activity with anomaly detection, and built "
            "dashboards/KPIs for fraud analytics.",
            "Applied AI/MLOps practices to production fraud-detection workflows.",
        ),
        systems=("fraud_monitoring", "snowflake_governance", "ai_agents_mlops"),
        technologies=(
            "python",
            "sql",
            "machine_learning",
            "fraud_analytics",
            "mlops",
            "docker",
            "kubernetes",
            "power_bi",
            "anomaly_detection",
            "snowflake",
            "dbt",
        ),
        flow=(
            FlowStage(
                key="problem",
                label="PROBLEM",
                detail="Fraud review depended on recurring manual work over transactional "
                "data, which capped how fast cases could move.",
            ),
            FlowStage(
                key="signals",
                label="SIGNALS",
                detail="Transactional activity monitored with statistical anomaly "
                "detection to surface what manual sampling missed.",
            ),
            FlowStage(
                key="models",
                label="MODELS",
                detail="Advanced algorithms and predictive models for transactional fraud "
                "prevention.",
            ),
            FlowStage(
                key="pipelines",
                label="PIPELINES",
                detail="Pipelines and models built and maintained with ML, Docker and "
                "Kubernetes.",
            ),
            FlowStage(
                key="automation",
                label="AUTOMATION",
                detail="~80% of recurring processes automated, from review steps to "
                "reporting.",
            ),
            FlowStage(
                key="visibility",
                label="VISIBILITY",
                detail="Institutional transaction-monitoring, KPI and Power BI dashboards "
                "for fraud analytics.",
            ),
            FlowStage(
                key="outcome",
                label="OUTCOME",
                detail="Case resolution accelerated by 30%+ and an end-to-end "
                "fraud-prevention solution delivered.",
            ),
        ),
        impacts=(
            Impact(
                label="AUTOMATION",
                detail="~80% of recurring processes automated inside fraud prevention.",
            ),
            Impact(
                label="RESOLUTION",
                detail="30%+ faster case resolution after pipelines and models went to "
                "production.",
            ),
        ),
        progression=("Intern", "Fraud Analyst", "Data Scientist"),
    ),
    Role(
        id="corporate",
        title="Founder & Lead Engineer",
        company="Corporate Gestão Empresarial",
        period="Aug 2018 — Present",
        start="2018-08",
        end="present",
        location="Greater Belo Horizonte",
        domain="Technical strategy · applied AI and automation",
        mission=(
            "Founder-side engineering: translate a commercial need into a technical "
            "roadmap and ship it with data and automation."
        ),
        current=True,
        response=(
            "Corporate Gestão Empresarial — Founder & Lead Engineer (Aug 2018 — Present)",
            "Technical strategic consulting for companies, applying AI, automation and "
            "data to business processes.",
        ),
        responsibilities=(
            "Founder and lead engineer providing technical strategic consulting for "
            "companies.",
            "Apply AI, automation, and data to improve business processes and support "
            "decision-making.",
            "Bridge commercial stakeholders and engineering, translating business needs "
            "into technical roadmaps.",
        ),
        systems=(),
        technologies=("python", "automation", "ai_workflows", "local_llm", "data_quality"),
        flow=(
            FlowStage(
                key="problem",
                label="BUSINESS",
                detail="A company has a commercial problem that needs a technical route "
                "out of it.",
            ),
            FlowStage(
                key="roadmap",
                label="ROADMAP",
                detail="Business need translated into a technical roadmap and scope "
                "commercial stakeholders can follow.",
            ),
            FlowStage(
                key="build",
                label="BUILD",
                detail="AI, automation and data applied directly to the business process.",
            ),
            FlowStage(
                key="outcome",
                label="DECISIONS",
                detail="Processes improved and decision-making supported with the "
                "resulting data.",
            ),
        ),
        impacts=(),
    ),
)

ROLES_BY_ID: dict[str, Role] = {role.id: role for role in EXPERIENCE}

# Employment chronology as displayed in the experience timeline.
TIMELINE_START = 2018
TIMELINE_END = 2026
