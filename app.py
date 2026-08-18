from html import escape
from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(
    page_title="Rafael Verdi de Freitas | Data Engineer / Data Science / Analytics Engineer",
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
        st.subheader("Data Engineer / Data Science / Analytics Engineer")
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
        "Data Engineer / Data Science / Analytics Engineer with 6+ years of experience "
        "in cloud data platforms, automated pipelines, fraud prevention, and analytics "
        "for banking institutions and digital-asset platforms. Focus on data engineering, "
        "automation, MLOps, fraud analytics, and data quality."
    )

    st.markdown("---")
    st.header("Skills")
    for group_title, group_skills in {
        "Data Engineering": [
            "Data Pipelines",
            "Data Modeling",
            "Data Warehousing",
            "Golden Table Architecture",
            "Data Quality",
        ],
        "Analytics & BI": [
            "Power BI",
            "Hex",
            "KPIs",
            "Self-Service Analytics",
        ],
        "Cloud & Infrastructure": [
            "AWS",
            "Kubernetes",
            "Docker",
            "Airflow",
        ],
        "Languages & Tools": [
            "Python",
            "SQL",
            "dbt",
            "Snowflake",
            "Athena",
        ],
        "ML & Automation": [
            "Machine Learning",
            "Fraud Analytics",
            "MLOps",
            "AI Agents",
            "Autonomous Workflows",
            "Local LLM",
        ],
        "Domain Expertise": [
            "Financial Services",
            "Fraud Prevention",
            "Digital Assets",
            "Banking",
            "Compliance",
            "Process Automation",
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
        "Fraud Analytics & Transaction Monitoring",
        "Confidential project from Data Scientist and Data Analyst roles",
        [
            "Developed advanced algorithms and predictive fraud models for transactional "
            "fraud prevention.",
            "Built and maintained institutional transaction-monitoring systems, KPI/Power BI "
            "dashboards, and statistical anomaly monitoring.",
            "Key technologies: Python, SQL, Power BI.",
        ],
    )
    render_card(
        "Production Data & Analytics Solutions",
        "Confidential project from an Analytics Engineer / Data Consultant role",
        [
            "Developed and maintained data and analytics solutions supporting business decisions with reliable, accessible data.",
            "Automated recurring reporting and operational processes to reduce manual effort and improve delivery reliability.",
            "Improved data reliability and quality across analytics workflows, collaborating with partner areas to turn requirements into deliverables.",
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
        "Lead Engineer",
        "Sapiens Management & Technologies | Nov 2025 – Present | Belo Horizonte, Brazil",
        [
            "Lead data consultancy engagements across cloud platforms (AWS, dbt, Snowflake, Kubernetes), delivering data and analytics solutions for clients.",
            "Drive ML/MLOps initiatives and automation to improve delivery and reliability of data products.",
            "Own end-to-end delivery and stakeholder alignment, translating business requirements into technical execution.",
        ],
    )
    render_card(
        "Analytics Engineer / Data Consultant",
        "Kraken | Nov 2025 – Present | Belo Horizonte, Brazil",
        [
            "Develop and maintain data and analytics solutions, supporting business decisions with reliable and accessible data.",
            "Automate recurring reports and operational processes, reducing manual effort and improving delivery reliability.",
            "Improve data reliability and quality across analytics workflows, collaborating with partner areas to translate requirements into deliverables.",
        ],
    )
    render_card(
        "Data Scientist / Data Analytics",
        "Banco Mercantil | Nov 2019 – Nov 2025 | Belo Horizonte, Brazil",
        [
            "Progressed from intern and fraud analyst to Data Scientist over six years within the fraud-prevention organization.",
            "Automated ~80% of recurring processes and delivered an end-to-end fraud-prevention solution.",
            "Built and maintained pipelines and models, leveraging ML, Docker, and Kubernetes to accelerate case resolution by 30%+.",
            "Monitored transactional activity with anomaly detection, and built dashboards/KPIs for fraud analytics.",
            "Applied AI/MLOps practices to production fraud-detection workflows.",
        ],
    )
    render_card(
        "Founder & Lead Engineer",
        "Corporate Gestão Empresarial | Aug 2018 – Present | Greater Belo Horizonte",
        [
            "Founder and lead engineer providing technical strategic consulting for companies.",
            "Apply AI, automation, and data to improve business processes and support decision-making.",
            "Bridge commercial stakeholders and engineering, translating business needs into technical roadmaps.",
        ],
    )

with education_tab:
    st.header("Education")
    render_card(
        "Postgraduate Specialization (Lato Sensu), Machine Learning Engineering",
        "FIAP | 2025 – 2026",
        [
            "Advanced study of classic machine learning and deep learning models, including supervised, unsupervised, and reinforcement learning.",
            "Hands-on implementation of scalable ML solutions in AWS cloud environments, including Hadoop and Spark platforms.",
            "Advanced techniques in NLP, computer vision, and generative AI models, including GPT-4 and Stable Diffusion.",
            "End-to-end MLOps practices, including automated data pipelines, Docker containerization, and CI/CD for model deployment.",
        ],
    )
    render_card(
        "Postgraduate Specialization (Lato Sensu), Management & Strategic Data Analysis",
        "Pontifícia Universidade Católica de Minas Gerais | 2022 – 2023",
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
            ("Portuguese", "Full Professional Proficiency / C2"),
            ("English", "Highly Proficient"),
        ]
    )
    st.markdown(
        f'<article class="card"><ul class="credential-list">{language_items}</ul></article>',
        unsafe_allow_html=True,
    )