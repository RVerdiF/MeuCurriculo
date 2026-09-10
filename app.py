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
    st.html(f"<style>{css}</style>")


local_css("style.css")

with open(BASE_DIR / "CV.pdf", "rb") as pdf_file:
    resume_pdf = pdf_file.read()

# Accessible skip link for keyboard navigation
st.html('<a href="#summary-skills" class="skip-link">Skip to main content</a>')

# Hero Section
with st.container():
    details_column, photo_column = st.columns((3, 1))
    with details_column:
        st.html(
            """
            <header class="hero-header">
                <h1 class="hero-name">Rafael Verdi de Freitas</h1>
                <p class="hero-role">Data Engineer / Data Science / Analytics Engineer</p>
                <p class="hero-location">
                    <span class="location-dot" aria-hidden="true"></span>
                    Belo Horizonte, Brazil &mdash; Remote (Americas time zones)
                </p>
                <div class="contact-links" aria-label="Contact and Social Links">
                    <a class="contact-badge" href="mailto:rafaelverdifreitas@hotmail.com">Email</a>
                    <span class="link-separator" aria-hidden="true">&middot;</span>
                    <a class="contact-badge" href="https://www.linkedin.com/in/rafael-verdi-de-freitas/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
                    <span class="link-separator" aria-hidden="true">&middot;</span>
                    <a class="contact-badge" href="https://github.com/RVerdiF" target="_blank" rel="noopener noreferrer">GitHub</a>
                </div>
            </header>
            """
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

    st.html(
        """
        <div class="hero-stats" role="list">
            <div class="stat-card" role="listitem">
                <span class="stat-value">6+ Years</span>
                <span class="stat-label">Experience in Data &amp; Analytics Platforms</span>
            </div>
            <div class="stat-card" role="listitem">
                <span class="stat-value">End-to-End</span>
                <span class="stat-label">Cloud Pipelines &amp; MLOps Solutions</span>
            </div>
            <div class="stat-card" role="listitem">
                <span class="stat-value">FinTech &amp; Crypto</span>
                <span class="stat-label">Fraud Prevention &amp; Anomaly Detection</span>
            </div>
            <div class="stat-card" role="listitem">
                <span class="stat-value">Remote</span>
                <span class="stat-label">Americas Time Zones Availability</span>
            </div>
        </div>
        """
    )

# Sticky In-Page Navigation
st.html(
    """
    <nav class="site-nav" aria-label="Portfolio Sections">
        <ul class="nav-list">
            <li><a href="#summary-skills" class="nav-link">Summary &amp; Skills</a></li>
            <li><a href="#projects" class="nav-link">Projects</a></li>
            <li><a href="#experience" class="nav-link">Experience</a></li>
            <li><a href="#education-credentials" class="nav-link">Education &amp; Credentials</a></li>
        </ul>
    </nav>
    """
)


# Section 1: Summary & Skills
def render_summary_skills() -> None:
    """Render the professional summary and grouped skill tags."""
    skill_groups = {
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
    }

    groups_markup = []
    for group_title, skills in skill_groups.items():
        tags = "".join(f'<span class="skill-tag">{escape(s)}</span>' for s in skills)
        groups_markup.append(
            f"""
            <div class="skill-group-card">
                <h3>{escape(group_title)}</h3>
                <div class="skill-tags">{tags}</div>
            </div>
            """
        )
    skills_grid_html = "".join(groups_markup)

    st.html(
        f"""
        <section id="summary-skills" class="portfolio-section" aria-labelledby="heading-summary-skills">
            <div class="section-header">
                <h2 id="heading-summary-skills" class="section-title">Summary &amp; Skills</h2>
            </div>
            <article class="card summary-card">
                <h3 class="card-title">Professional Summary</h3>
                <p class="summary-text">
                    Data Engineer / Data Science / Analytics Engineer with 6+ years of experience
                    in cloud data platforms, automated pipelines, fraud prevention, and analytics
                    for banking institutions and digital-asset platforms. Focus on data engineering,
                    automation, MLOps, fraud analytics, and data quality.
                </p>
            </article>
            <h3 class="subsection-title">Skills</h3>
            <div class="skills-grid">{skills_grid_html}</div>
        </section>
        """
    )


# Section 2: Projects
def render_projects() -> None:
    """Render public repository projects and selected professional engagements."""
    public_projects = [
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

    pub_cards = []
    for p in public_projects:
        tech_tags = "".join(
            f'<span class="tech-tag">{escape(t.strip())}</span>'
            for t in p["technologies"].split(",")
        )
        repo_btn = (
            f'<a class="project-btn project-btn-primary" href="{escape(p["url"])}" '
            f'target="_blank" rel="noopener noreferrer">View repository &rarr;</a>'
        )
        live_btn = ""
        if p.get("deployment_url"):
            live_btn = (
                f'<a class="project-btn" href="{escape(p["deployment_url"])}" '
                f'target="_blank" rel="noopener noreferrer">Open live project &nearr;</a>'
            )
        pub_cards.append(
            f"""
            <article class="card project-card">
                <div>
                    <h3 class="card-title">{escape(p["title"])}</h3>
                    <p class="project-desc">{escape(p["description"])}</p>
                </div>
                <div>
                    <div class="project-tech">
                        <span class="tech-label">Technologies</span>
                        <div class="tech-tags">{tech_tags}</div>
                    </div>
                    <div class="project-actions">
                        {repo_btn}
                        {live_btn}
                    </div>
                </div>
            </article>
            """
        )
    pub_projects_html = "".join(pub_cards)

    pro_projects = [
        {
            "title": "Autonomous AI Agents & MLOps Pipelines",
            "subtitle": "Confidential project from a Data Scientist role",
            "bullets": [
                "Designed, engineered, and orchestrated autonomous AI agents and robust MLOps pipelines to automate complex data workflows.",
                "Key technologies: Python, AI/ML, MLOps, CI/CD, Docker, AWS.",
            ],
        },
        {
            "title": "Fraud Analytics & Transaction Monitoring",
            "subtitle": "Confidential project from Data Scientist and Data Analyst roles",
            "bullets": [
                "Developed advanced algorithms and predictive fraud models for transactional fraud prevention.",
                "Built and maintained institutional transaction-monitoring systems, KPI/Power BI dashboards, and statistical anomaly monitoring.",
                "Key technologies: Python, SQL, Power BI.",
            ],
        },
        {
            "title": "Production Data & Analytics Solutions",
            "subtitle": "Confidential project from an Analytics Engineer / Data Consultant role",
            "bullets": [
                "Developed and maintained data and analytics solutions supporting business decisions with reliable, accessible data.",
                "Automated recurring reporting and operational processes to reduce manual effort and improve delivery reliability.",
                "Improved data reliability and quality across analytics workflows, collaborating with partner areas to turn requirements into deliverables.",
            ],
        },
        {
            "title": "Data Governance & Automation in Snowflake",
            "subtitle": "Confidential project from a Data Analyst role",
            "bullets": [
                "Created and managed tables, views, and stored procedures in Snowflake while automating departmental processes.",
                "Key technologies: Snowflake, Python, dbt, SQL, data governance.",
            ],
        },
    ]

    pro_cards = []
    for pro in pro_projects:
        bullets_html = "".join(f"<li>{escape(b)}</li>" for b in pro["bullets"])
        pro_cards.append(
            f"""
            <article class="card">
                <h3 class="card-title">{escape(pro["title"])}</h3>
                <p class="card-subtitle">{escape(pro["subtitle"])}</p>
                <ul>{bullets_html}</ul>
            </article>
            """
        )
    pro_projects_html = "".join(pro_cards)

    st.html(
        f"""
        <section id="projects" class="portfolio-section" aria-labelledby="heading-projects">
            <div class="section-header">
                <h2 id="heading-projects" class="section-title">Projects</h2>
                <p class="section-description">
                    Selected public projects. Use the repository link under each project to view its source code.
                </p>
            </div>
            <div class="projects-grid">{pub_projects_html}</div>
            <h3 class="subsection-title">Selected Professional Projects</h3>
            <div class="pro-projects-grid">{pro_projects_html}</div>
        </section>
        """
    )


# Section 3: Experience
def render_experience() -> None:
    """Render the vertical timeline of professional roles."""
    experiences = [
        {
            "title": "Lead Engineer",
            "company": "Sapiens Management & Technologies",
            "period": "Nov 2025 – Present",
            "location": "Belo Horizonte, Brazil",
            "bullets": [
                "Lead data consultancy engagements across cloud platforms (AWS, dbt, Snowflake, Kubernetes), delivering data and analytics solutions for clients.",
                "Drive ML/MLOps initiatives and automation to improve delivery and reliability of data products.",
                "Own end-to-end delivery and stakeholder alignment, translating business requirements into technical execution.",
            ],
        },
        {
            "title": "Analytics Engineer / Data Consultant",
            "company": "Kraken",
            "period": "Nov 2025 – Present",
            "location": "Belo Horizonte, Brazil",
            "bullets": [
                "Develop and maintain data and analytics solutions, supporting business decisions with reliable and accessible data.",
                "Automate recurring reports and operational processes, reducing manual effort and improving delivery reliability.",
                "Improve data reliability and quality across analytics workflows, collaborating with partner areas to translate requirements into deliverables.",
            ],
        },
        {
            "title": "Data Scientist / Data Analytics",
            "company": "Banco Mercantil",
            "period": "Nov 2019 – Nov 2025",
            "location": "Belo Horizonte, Brazil",
            "bullets": [
                "Progressed from intern and fraud analyst to Data Scientist over six years within the fraud-prevention organization.",
                "Automated ~80% of recurring processes and delivered an end-to-end fraud-prevention solution.",
                "Built and maintained pipelines and models, leveraging ML, Docker, and Kubernetes to accelerate case resolution by 30%+.",
                "Monitored transactional activity with anomaly detection, and built dashboards/KPIs for fraud analytics.",
                "Applied AI/MLOps practices to production fraud-detection workflows.",
            ],
        },
        {
            "title": "Founder & Lead Engineer",
            "company": "Corporate Gestão Empresarial",
            "period": "Aug 2018 – Present",
            "location": "Greater Belo Horizonte",
            "bullets": [
                "Founder and lead engineer providing technical strategic consulting for companies.",
                "Apply AI, automation, and data to improve business processes and support decision-making.",
                "Bridge commercial stakeholders and engineering, translating business needs into technical roadmaps.",
            ],
        },
    ]

    items_html = []
    for exp in experiences:
        bullets_html = "".join(f"<li>{escape(b)}</li>" for b in exp["bullets"])
        items_html.append(
            f"""
            <div class="timeline-item" role="listitem">
                <div class="timeline-marker" aria-hidden="true"></div>
                <article class="card timeline-card">
                    <div class="timeline-header">
                        <h3 class="card-title">{escape(exp["title"])}</h3>
                        <span class="timeline-badge">{escape(exp["period"])}</span>
                    </div>
                    <p class="card-subtitle">{escape(exp["company"])} &middot; {escape(exp["location"])}</p>
                    <ul>{bullets_html}</ul>
                </article>
            </div>
            """
        )
    timeline_html = "".join(items_html)

    st.html(
        f"""
        <section id="experience" class="portfolio-section" aria-labelledby="heading-experience">
            <div class="section-header">
                <h2 id="heading-experience" class="section-title">Professional Experience</h2>
            </div>
            <div class="timeline" role="list">{timeline_html}</div>
        </section>
        """
    )


# Section 4: Education & Credentials
def render_education_credentials() -> None:
    """Render academic degrees, professional certifications, and language proficiency."""
    educations = [
        {
            "title": "Postgraduate Specialization (Lato Sensu), Machine Learning Engineering",
            "subtitle": "FIAP | 2025 – 2026",
            "bullets": [
                "Advanced study of classic machine learning and deep learning models, including supervised, unsupervised, and reinforcement learning.",
                "Hands-on implementation of scalable ML solutions in AWS cloud environments, including Hadoop and Spark platforms.",
                "Advanced techniques in NLP, computer vision, and generative AI models, including GPT-4 and Stable Diffusion.",
                "End-to-end MLOps practices, including automated data pipelines, Docker containerization, and CI/CD for model deployment.",
            ],
        },
        {
            "title": "Postgraduate Specialization (Lato Sensu), Management & Strategic Data Analysis",
            "subtitle": "Pontifícia Universidade Católica de Minas Gerais | 2022 – 2023",
            "bullets": [
                "Data-driven culture, data-governance frameworks (LGPD/GDPR), and agile project management.",
                "Advanced analytics with Python, ETL/ELT processes, and dimensional modeling for data warehouses.",
            ],
        },
        {
            "title": "Major, Business Administration",
            "subtitle": "Pontifícia Universidade Católica de Minas Gerais | Jan 2018 – Dec 2021",
            "bullets": [
                "Foundation in strategic management, finance, marketing, and organizational processes.",
            ],
        },
        {
            "title": "Distance Learning, Entrepreneurship, Business and Startups",
            "subtitle": "Fast MBA | 2020",
            "bullets": [],
        },
    ]

    edu_cards = []
    for edu in educations:
        bullets_html = "".join(f"<li>{escape(b)}</li>" for b in edu["bullets"])
        list_html = f"<ul>{bullets_html}</ul>" if bullets_html else ""
        edu_cards.append(
            f"""
            <article class="card">
                <h3 class="card-title">{escape(edu["title"])}</h3>
                <p class="card-subtitle">{escape(edu["subtitle"])}</p>
                {list_html}
            </article>
            """
        )
    edu_html = "".join(edu_cards)

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

    course_cards = "".join(
        f"""
        <div class="credential-card">
            <span class="credential-name">{escape(course)}</span>
            <span class="credential-meta">{escape(provider)}</span>
        </div>
        """
        for course, provider in courses
    )

    languages = [
        ("Portuguese", "Full Professional Proficiency / C2"),
        ("English", "Highly Proficient"),
    ]

    lang_cards = "".join(
        f"""
        <div class="language-card">
            <span class="language-name">{escape(lang)}</span>
            <span class="language-level">{escape(level)}</span>
        </div>
        """
        for lang, level in languages
    )

    st.html(
        f"""
        <section id="education-credentials" class="portfolio-section" aria-labelledby="heading-education-credentials">
            <div class="section-header">
                <h2 id="heading-education-credentials" class="section-title">Education &amp; Credentials</h2>
            </div>
            <h3 class="subsection-title">Education</h3>
            <div class="education-grid">{edu_html}</div>
            <h3 class="subsection-title">Courses &amp; Certifications</h3>
            <div class="credentials-grid">{course_cards}</div>
            <h3 class="subsection-title">Languages</h3>
            <div class="languages-grid">{lang_cards}</div>
        </section>
        """
    )


# Render all 4 continuous sections
render_summary_skills()
render_projects()
render_experience()
render_education_credentials()

# Portfolio Footer
st.html(
    """
    <footer class="portfolio-footer">
        <p>Rafael Verdi de Freitas &middot; Data Engineer / Data Science / Analytics Engineer</p>
    </footer>
    """
)
