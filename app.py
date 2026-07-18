from html import escape
from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(
    page_title="Rafael Verdi de Freitas | Data & Analytics Engineer",
    page_icon="📊",
    layout="wide",
)


def local_css(file_name: str) -> None:
    """Load a stylesheet stored alongside this application."""
    css = (BASE_DIR / file_name).read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def render_card(title: str, subtitle: str, bullets: list[str]) -> None:
    """Render a consistently styled, semantic résumé card."""
    items = "".join(f"<li>{escape(bullet)}</li>" for bullet in bullets)
    list_markup = f"<ul>{items}</ul>" if items else ""
    st.markdown(
        f"""
        <article class="card">
            <h3 class="card-title">{escape(title)}</h3>
            <p class="card-subtitle">{escape(subtitle)}</p>
            {list_markup}
        </article>
        """,
        unsafe_allow_html=True,
    )


def render_skill_group(title: str, skills: list[str]) -> None:
    """Render a labelled, responsive group of skill tags."""
    tags = "".join(f'<span class="skill-tag">{escape(skill)}</span>' for skill in skills)
    st.markdown(
        f"""
        <section class="skill-group" aria-label="{escape(title)}">
            <h3>{escape(title)}</h3>
            <div class="skill-tags">{tags}</div>
        </section>
        """,
        unsafe_allow_html=True,
    )


local_css("style.css")

with open(BASE_DIR / "CV.pdf", "rb") as pdf_file:
    resume_pdf = pdf_file.read()


with st.container():
    details_column, photo_column = st.columns((3, 1))
    with details_column:
        st.title("Rafael Verdi de Freitas")
        st.subheader("Data & Analytics Engineer")
        st.caption("Belo Horizonte, Brazil — Remote (Americas time zones)")
        st.markdown(
            """
            <p class="contact-links">
                <a href="mailto:rafaelverdifreitas@hotmail.com">Email</a>
                <span aria-hidden="true">·</span>
                <a href="https://www.linkedin.com/in/rafael-verdi-de-freitas/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
                <span aria-hidden="true">·</span>
                <a href="https://github.com/RVerdiF" target="_blank" rel="noopener noreferrer">GitHub</a>
            </p>
            """,
            unsafe_allow_html=True,
        )
        st.download_button(
            label="Download résumé (PDF)",
            data=resume_pdf,
            file_name="Rafael_Verdi_de_Freitas_Resume.pdf",
            mime="application/pdf",
        )
    with photo_column:
        st.image(
            str(BASE_DIR / "1594050442709.jpeg"),
            caption="Rafael Verdi de Freitas",
            width="stretch",
        )

st.markdown("---")

summary_tab, projects_tab, experience_tab, education_tab = st.tabs(
    ["Summary & Skills", "Projects", "Experience", "Education & Credentials"]
)

with summary_tab:
    st.header("Professional Summary")
    st.write(
        "Data & Analytics Engineer with 6+ years designing cloud data warehouses "
        "and golden-table architectures for global banking institutions and "
        "digital-asset platforms. Built data and compliance infrastructure supporting "
        "complex financial and regulatory environments worldwide. Deep command of the "
        "modern data stack end to end—from AWS and dbt to Snowflake and Kubernetes—with "
        "a focus on MLOps, process automation, and fraud analytics."
    )

    st.markdown("---")
    st.header("Skills")
    for group_title, group_skills in {
        "Top Skills": [
            "Cloud Data Architecture",
            "Financial ML Infrastructure",
            "Autonomous AI/MLOps Agents",
            "Local LLM Deployment",
        ],
        "Core Stack": [
            "Python",
            "SQL",
            "AWS",
            "dbt",
            "Docker",
            "Snowflake",
            "Kubernetes",
            "Hex",
            "Power BI",
            "Airflow",
        ],
        "Specialties": [
            "Golden Table Architecture",
            "Cloud Data Engineering",
            "Data Pipelines",
            "ETL/ELT",
            "Data Modeling",
            "Data Quality",
            "Data Democratization",
            "Cross-Border Regulatory Compliance",
            "Process Automation",
            "MLOps",
            "Fraud Analytics",
        ],
    }.items():
        render_skill_group(group_title, group_skills)

with projects_tab:
    st.header("Projects")
    st.write("Selected public projects. Use the repository link under each project to view its source code.")
    st.markdown("---")

    projects = [
        {
            "url": "https://github.com/RVerdiF/api-embrapa-tech-challenge",
            "title": "Embrapa API — Viticulture",
            "description": (
                "A FastAPI service for extracting and querying viticulture information "
                "from Embrapa's Vitibrasil portal."
            ),
            "technologies": "FastAPI, Docker, Pandas, Pydantic",
            "deployment_url": None,
        },
        {
            "url": "https://github.com/RVerdiF/TechChallenge3",
            "title": "BTC Prediction Project",
            "description": (
                "A modular machine-learning project for Bitcoin price prediction with an "
                "interactive Streamlit dashboard."
            ),
            "technologies": "Streamlit, Pandas, yfinance, scikit-learn, LightGBM, Plotly",
            "deployment_url": "https://techchallenge3rafaelfreitas.streamlit.app/",
        },
        {
            "url": "https://github.com/RVerdiF/PaysimViz",
            "title": "PaySim Dataset Explorer",
            "description": (
                "A Streamlit application for exploring and analyzing the PaySim synthetic "
                "financial dataset with a SQL-centric backend."
            ),
            "technologies": "Streamlit, Polars, SQLite, Pandas",
            "deployment_url": "https://rverdif-paysimviz-app-olphe6.streamlit.app/",
        },
    ]

    for project in projects:
        st.subheader(project["title"])
        st.write(project["description"])
        st.caption(f"Technologies: {project['technologies']}")
        project_links = f"[View repository]({project['url']})"
        if project["deployment_url"]:
            project_links += f" · [Open live project]({project['deployment_url']})"
        st.markdown(project_links)
        st.markdown("---")

    st.subheader("Selected Professional Projects")
    render_card(
        "Autonomous AI Agents & MLOps Pipelines",
        "Confidential project from a Data Scientist role",
        [
            "Designed, engineered, and orchestrated autonomous AI agents and robust MLOps pipelines to automate complex data workflows.",
            "Key technologies: Python, AI/ML, MLOps, CI/CD, Docker, AWS.",
        ],
    )
    render_card(
        "Advanced Fraud Detection Algorithms",
        "Confidential project from a Data Scientist role",
        [
            "Developed and implemented advanced algorithms for real-time transactional fraud prevention.",
            "Key technologies: Python, machine learning, predictive modeling, Apache Spark, Kafka.",
        ],
    )
    render_card(
        "Fraud Analytics & Transaction Monitoring",
        "Confidential project from Data Scientist and Data Analyst roles",
        [
            "Built and trained predictive fraud models alongside advanced algorithms for "
            "transactional fraud prevention.",
            "Built and maintained institutional transaction-monitoring systems and "
            "KPI/Power BI dashboards; monitored anomalies across fraud pipelines using "
            "statistical methods.",
            "Key technologies: Python, SQL, Power BI.",
        ],
    )
    render_card(
        "Production Data Pipelines & Trusted Data Layers",
        "Confidential project from an Analytics Engineer / Data Consultant role",
        [
            "Built production-grade data pipelines and analytics solutions for high-volume "
            "financial and regulatory workflows.",
            "Designed reusable data models and curated datasets to improve consistency, "
            "reliability, and access to trusted business data.",
            "Automated recurring reporting and operational processes to reduce manual effort "
            "and improve delivery reliability.",
        ],
    )
    render_card(
        "Data Governance & Automation in Snowflake",
        "Confidential project from a Data Analyst role",
        [
            "Created and managed tables, views, and stored procedures in Snowflake while automating departmental processes.",
            "Key technologies: Snowflake, Python, dbt, SQL, data governance.",
        ],
    )

with experience_tab:
    st.header("Professional Experience")
    render_card(
        "Founder & Lead Engineer",
        "Sapiens Management & Technologies | Nov 2025 – Present | Belo Horizonte, Brazil",
        [
            "Boutique data consultancy contracted by international enterprises and global digital-asset firms to design, scale, and optimize mission-critical data platforms and analytics infrastructure.",
            "Specialize in modern data stack deployment (AWS, dbt, Snowflake, Kubernetes), financial ML infrastructure, and production-grade automated tracking pipelines under strict global compliance constraints.",
            "Own end-to-end SLA and delivery management, aligning data strategy with cross-functional business requirements to drive operational cost efficiency.",
        ],
    )
    render_card(
        "Analytics Engineer / Data Consultant",
        "Kraken | Nov 2025 – Present | Tier-1 global digital-asset platform; engaged via Sapiens Management & Technologies",
        [
            "Built production-grade data pipelines and analytics solutions for high-volume financial and regulatory workflows in a global digital-asset environment.",
            "Designed reusable data models and curated datasets that improved consistency, reliability, and access to trusted business data.",
            "Automated recurring reporting and operational processes, reducing manual effort and improving delivery reliability.",
            "Developed AI-powered workflow agents to streamline scheduling coordination, task routing, and multi-step operational processes.",
            "Partnered with compliance, operations, analytics, and engineering stakeholders to translate complex requirements into maintainable data products.",
        ],
    )
    render_card(
        "Data Scientist (promoted from Intern / Fraud Analyst)",
        "Banco Mercantil | Nov 2019 – Nov 2025 | Belo Horizonte, Brazil",
        [
            "Progressed over six years from intern to Data Scientist within the fraud-prevention organization, moving from transactional pattern analysis into building and owning the bank's fraud-detection infrastructure end to end.",
            "Built and maintained institutional transaction-monitoring systems (PIX, TEDs) and KPI/Power BI dashboards; created and governed tables, views, tasks, and procedures in Snowflake using Python, dbt, and SQL.",
            "Designed transactional fraud-prevention algorithms and trained predictive ML/AI fraud models, accelerating case-resolution speed by 30%+; monitored anomalies across fraud pipelines using statistical methods.",
            "Developed and orchestrated autonomous AI/MLOps agents and automated workflows using agile practices integrated with DevOps platforms.",
        ],
    )
    render_card(
        "Data Consultant (Advisor)",
        "Corporate Gestão Empresarial | Aug 2018 – Present | Greater Belo Horizonte",
        [
            "Act as the strategic liaison between commercial stakeholders and engineering, translating complex business requirements into technical product roadmaps and platform features.",
            "Oversee workflow automations and data-driven operational improvements to streamline business administration.",
        ],
    )

with education_tab:
    st.header("Education")
    render_card(
        "Postgraduate Specialization (Lato Sensu), Machine Learning Engineering",
        "FIAP | Feb 2025 – Feb 2026",
        [
            "Advanced study of classic machine learning and deep learning models, including supervised, unsupervised, and reinforcement learning.",
            "Hands-on implementation of scalable ML solutions in AWS cloud environments, including Hadoop and Spark platforms.",
            "Advanced techniques in NLP, computer vision, and generative AI models, including GPT-4 and Stable Diffusion.",
            "End-to-end MLOps practices, including automated data pipelines, Docker containerization, and CI/CD for model deployment.",
        ],
    )
    render_card(
        "Postgraduate Specialization (Lato Sensu), Management & Strategic Data Analysis",
        "Pontifícia Universidade Católica de Minas Gerais | Aug 2022 – Oct 2023",
        [
            "Data-driven culture, data-governance frameworks (LGPD/GDPR), and agile project management.",
            "Advanced analytics with Python, ETL/ELT processes, and dimensional modeling for data warehouses.",
        ],
    )
    render_card(
        "Major, Business Administration",
        "Pontifícia Universidade Católica de Minas Gerais | Jan 2018 – Dec 2021",
        ["Foundation in strategic management, finance, marketing, and organizational processes."],
    )
    render_card(
        "Distance Learning, Entrepreneurship, Business and Startups",
        "Fast MBA | 2020",
        [],
    )

    st.markdown("---")
    st.header("Courses & Certifications")
    courses = [
        ("AI Agents — Google", "Alura | Sep 2025"),
        ("Financial Markets", "Yale University | Sep 2023"),
        ("Análise de Dados e Power BI", "Escola Conquer | Sep 2023"),
        ("DBT e Snowflake", "triggo.ai | Jun 2023"),
        ("Data Analysis with Python", "freeCodeCamp | Jun 2022"),
        ("Yellow Belt — Lean Six Sigma", "FM2S Educação e Consultoria | Jan 2022"),
        ("Introdução à Ciência de Dados 2.0", "Data Science Academy | Apr 2020"),
        ("Lean Six-Sigma — White Belt Certification", "Escola EDTI | Mar 2020"),
        ("Transformando Ideias em Negócios", "Corporate Gestão Empresarial | Jan 2015"),
    ]
    course_items = "".join(
        f"<li><strong>{escape(course)}</strong><br><span>{escape(provider)}</span></li>"
        for course, provider in courses
    )
    st.markdown(
        f'<article class="card"><ul class="credential-list">{course_items}</ul></article>',
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.header("Languages")
    language_items = "".join(
        f"<li><strong>{escape(language)}</strong> — {escape(level)}</li>"
        for language, level in [
            ("Portuguese", "Native / Bilingual"),
            ("English", "Full Professional"),
        ]
    )
    st.markdown(
        f'<article class="card"><ul class="credential-list">{language_items}</ul></article>',
        unsafe_allow_html=True,
    )