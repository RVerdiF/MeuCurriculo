"""Education, certifications and languages (verbatim from the résumé)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Education:
    id: str
    title: str
    institution: str
    period: str
    details: tuple[str, ...] = ()


@dataclass(frozen=True)
class Course:
    name: str
    provider: str
    year: str


EDUCATION: tuple[Education, ...] = (
    Education(
        id="fiap",
        title="Postgraduate Specialization (Lato Sensu), Machine Learning Engineering",
        institution="FIAP",
        period="2025 — 2026",
        details=(
            "Advanced study of classic machine learning and deep learning models, "
            "including supervised, unsupervised, and reinforcement learning.",
            "Hands-on implementation of scalable ML solutions in AWS cloud environments, "
            "including Hadoop and Spark platforms.",
            "Advanced techniques in NLP, computer vision, and generative AI models, "
            "including GPT-4 and Stable Diffusion.",
            "End-to-end MLOps practices, including automated data pipelines, Docker "
            "containerization, and CI/CD for model deployment.",
        ),
    ),
    Education(
        id="puc-mgmt",
        title=(
            "Postgraduate Specialization (Lato Sensu), Management & Strategic Data Analysis"
        ),
        institution="Pontifícia Universidade Católica de Minas Gerais",
        period="2022 — 2023",
        details=(
            "Data-driven culture, data-governance frameworks (LGPD/GDPR), and agile "
            "project management.",
            "Advanced analytics with Python, ETL/ELT processes, and dimensional modeling "
            "for data warehouses.",
        ),
    ),
    Education(
        id="puc-admin",
        title="Major, Business Administration",
        institution="Pontifícia Universidade Católica de Minas Gerais",
        period="Jan 2018 — Dec 2021",
        details=(
            "Foundation in strategic management, finance, marketing, and organizational "
            "processes.",
        ),
    ),
    Education(
        id="fast-mba",
        title="Distance Learning, Entrepreneurship, Business and Startups",
        institution="Fast MBA",
        period="2020",
    ),
)

COURSES: tuple[Course, ...] = (
    Course("AI Agents — Google", "Alura", "Sep 2025"),
    Course("Financial Markets", "Yale University", "Sep 2023"),
    Course("Análise de Dados e Power BI", "Escola Conquer", "Sep 2023"),
    Course("DBT e Snowflake", "triggo.ai", "Jun 2023"),
    Course("Data Analysis with Python", "freeCodeCamp", "Jun 2022"),
    Course("Yellow Belt — Lean Six Sigma", "FM2S Educação e Consultoria", "Jan 2022"),
    Course("Introdução à Ciência de Dados 2.0", "Data Science Academy", "Apr 2020"),
    Course("Lean Six-Sigma — White Belt Certification", "Escola EDTI", "Mar 2020"),
    Course("Transformando Ideias em Negócios", "Corporate Gestão Empresarial", "Jan 2015"),
)

LANGUAGES: tuple[tuple[str, str], ...] = (
    ("Portuguese", "Full Professional Proficiency / C2"),
    ("English", "Highly Proficient"),
)
