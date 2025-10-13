import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Rafael Verdi de Freitas — Data Scientist", page_icon="📊", layout="wide")

# ---------- DATA (from CV) ----------
NAME = "Rafael Verdi de Freitas"
ROLE = "Data Scientist · Fraud Prevention · Machine Learning · BI"
LOCATION = "Belo Horizonte, MG, Brazil"
PHONE = "+55 31 99873-1255"
EMAIL = "rafaelverdifreitas@hotmail.com"

SUMMARY = (
    "Cientista de Dados com 5+ anos no setor financeiro, focado em Gestão Estratégica de Dados, "
    "Prevenção a Fraudes e Machine Learning. Experiência construindo modelos preditivos, "
    "automação com práticas DevOps/MLOps e tradução de dados em decisões de negócio."
)

SKILLS = {
    "Programação & Bancos": ["Python (5 anos)", "SQL (5 anos)"],
    "Dados & Analytics": ["Power BI (5 anos)", "ETL (5 anos)", "Snowflake", "dbt", "Microsoft Office"],
    "ML & Data Science": ["Aprendizado Supervisionado/Não Supervisionado", "Deep Learning", "Modelagem Preditiva", "NLP", "MLOps", "Governança de Dados"],
    "Plataformas & Metodologias": ["DevOps", "CI/CD", "Agile (Scrum, Kanban)", "Docker", "AWS", "Big Data (Hadoop, Spark, Kafka)"],
}

EXPERIENCES = [
    {
        "title": "Data Scientist, Fraud Prevention",
        "company": "Banco Mercantil do Brasil",
        "period": "Nov/2024 – Presente",
        "location": "Belo Horizonte, MG",
        "bullets": [
            "Orquestração de agentes autônomos de IA e pipelines MLOps para automação e escalabilidade.",
            "Desenvolvimento de algoritmos para prevenção a fraudes transacionais.",
            "Modelos preditivos de fraude com ML/AI para respostas proativas a ameaças.",
            "Gestão de projetos com práticas DevOps para acelerar entregas e confiabilidade."
        ],
    },
    {
        "title": "Data Analyst, Fraud Prevention",
        "company": "Banco Mercantil do Brasil",
        "period": "Jan/2023 – Nov/2024",
        "location": "Belo Horizonte, MG",
        "bullets": [
            "Monitoramento de KPIs e qualidade dos serviços da área.",
            "Sistema de monitoramento transacional em Python e dashboards em Power BI.",
            "Automação de processos-chave elevando eficiência e produtividade.",
            "Governança de dados no Snowflake com Python, dbt e SQL."
        ],
    },
    {
        "title": "Data Analysis & Fraud Prevention Assistant",
        "company": "Banco Mercantil do Brasil",
        "period": "Dez/2021 – Jan/2023",
        "location": "Belo Horizonte, MG",
        "bullets": [
            "Suporte às operações diárias e projetos estratégicos das equipes de dados e fraudes.",
            "Preparação, limpeza e análise preliminar de dados.",
        ],
    },
    {
        "title": "Intern",
        "company": "Banco Mercantil do Brasil",
        "period": "Nov/2019 – Nov/2021",
        "location": "Belo Horizonte, MG",
        "bullets": [
            "Experiência fundamental no setor financeiro em tarefas de dados e documentação de processos."
        ],
    },
]

EDUCATION = [
    {"course": "Pós-graduação (Especialização) — Machine Learning Engineering", "school": "FIAP", "period": "Prev. Fev/2025"},
    {"course": "Pós-graduação (Especialização) — Gestão & Análise Estratégica de Dados", "school": "PUC Minas", "period": "Ago/2022 – Out/2023"},
    {"course": "Bacharelado — Administração", "school": "PUC Minas", "period": "Fev/2018 – Dez/2021"},
]

CERTS = [
    "Financial Markets — Yale University (2023)",
    "DBT & Snowflake (2023)",
    "Data Analysis and Power BI (2023)",
    "Data Analysis with Python (2022)",
    "Lean Six Sigma — Yellow Belt (2022)",
    "Introduction to Data Science 2.0 (2020)",
    "Lean Six Sigma — White Belt (2020)",
    "Transforming Ideas into Business (2015)",
]

PDF_NAME = "curriculum_rafael_verdi_de_freitas.pdf"  # coloque o PDF com este nome na raiz do projeto

# ---------- UI HELPERS ----------
def section_header(title, subtitle=None):
    st.markdown(f"## {title}")
    if subtitle:
        st.caption(subtitle)

def skill_badges(items):
    # simples badges com markdown
    st.markdown("".join([f"<span class='badge'>{item}</span>" for item in items]), unsafe_allow_html=True)

def show_pdf(pdf_path: Path):
    try:
        data = pdf_path.read_bytes()
        st.download_button("Baixar CV (PDF)", data=data, file_name="Rafael_Verde_de_Freitas_CV.pdf", mime="application/pdf")
        # preview inline
        import base64
        base64_pdf = base64.b64encode(data).decode("utf-8")
        st.markdown(f"<iframe src='data:application/pdf;base64,{base64_pdf}' width='100%' height='700' type='application/pdf'></iframe>", unsafe_allow_html=True)
    except Exception as e:
        st.warning(f"Não foi possível abrir o PDF ({e}). Verifique se o arquivo existe.")

# ---------- SIDEBAR NAV ----------
st.sidebar.title("Navegação")
page = st.sidebar.radio(
    "Ir para",
    ["Início", "Experiência", "Habilidades", "Educação", "Certificações", "Contato", "Currículo (PDF)"],
    index=0,
)

# ---------- TOP BAR ----------
col1, col2 = st.columns([3, 2], vertical_alignment="center")
with col1:
    st.markdown(f"# {NAME}")
    st.write(ROLE)
    st.write(LOCATION)
with col2:
    st.write("")
    st.write("")
    st.markdown(f"**E-mail:** [{EMAIL}](mailto:{EMAIL})  \n**Telefone:** {PHONE}")

st.divider()

# ---------- PAGES ----------
if page == "Início":
    section_header("Sobre", "Resumo profissional")
    st.write(SUMMARY)
    st.info("Disponível para projetos remotos em Ciência de Dados, Engenharia de Dados, BI e MLOps.")

elif page == "Experiência":
    section_header("Experiência Profissional")
    for exp in EXPERIENCES:
        with st.container(border=True):
            st.markdown(f"**{exp['title']}** · {exp['company']}  \n{exp['period']} · {exp['location']}")
            for b in exp["bullets"]:
                st.markdown(f"- {b}")

elif page == "Habilidades":
    section_header("Habilidades Técnicas")
    for group, items in SKILLS.items():
        with st.container(border=True):
            st.markdown(f"**{group}**")
            skill_badges(items)

elif page == "Educação":
    section_header("Formação Acadêmica")
    for ed in EDUCATION:
        with st.container(border=True):
            st.markdown(f"**{ed['course']}**  \n{ed['school']} · {ed['period']}")

elif page == "Certificações":
    section_header("Certificações & Licenças")
    for c in CERTS:
        st.markdown(f"- {c}")

elif page == "Contato":
    section_header("Contato")
    st.markdown(f"- 📧 E-mail: [{EMAIL}](mailto:{EMAIL})")
    st.markdown(f"- 📍 Localização: {LOCATION}")
    st.markdown(f"- 📱 Telefone/WhatsApp: {PHONE}")
    st.success("Fale comigo para discutirmos como posso ajudar o seu time a gerar valor com dados.")

elif page == "Currículo (PDF)":
    section_header("Currículo (PDF)")
    pdf_path = Path(PDF_NAME)
    if pdf_path.exists():
        show_pdf(pdf_path)
    else:
        st.warning(f"Coloque o arquivo **{PDF_NAME}** na mesma pasta deste aplicativo para habilitar o download e a visualização.")

# ---------- STYLES ----------
st.markdown(
    """
    <style>
    .badge {
        display:inline-block; padding:6px 10px; margin:4px; border-radius:999px;
        background:rgba(0,0,0,0.07); font-size:0.9rem;
    }
    </style>
    """, unsafe_allow_html=True
)
