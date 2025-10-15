import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit_lottie import st_lottie

# --- PAGE CONFIGURATION ---
st.set_page_config(layout="wide", page_title="Portfolio | Rafael Verdi de Freitas")

# --- HTML & JS for Vanta.js Background ---
# This block injects the necessary scripts and styles for the animated background.
vanta_html = """
<style>
#vanta-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: -1;
}
</style>
<div id="vanta-bg"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r134/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vanta@latest/dist/vanta.birds.min.js"></script>
<script>
console.log("Vanta script starting");
document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded event fired");
    try {
        VANTA.BIRDS({
          el: "#vanta-bg",
          mouseControls: true,
          touchControls: true,
          gyroControls: false,
          minHeight: 200.00,
          minWidth: 200.00,
          scale: 1.00,
          scaleMobile: 1.00,
          backgroundColor: 0x121212,
          color1: 0x4caf50,
          color2: 0x4caf50,
          colorMode: "lerp"
        });
        console.log("Vanta script executed successfully");
    } catch (e) {
        console.error("Vanta script error:", e);
    }
});
</script>
"""
st.markdown(vanta_html, unsafe_allow_html=True)

# --- Function to load local CSS file ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# --- Function to load Lottie animation from URL ---
def load_lottieurl(url: str):
    return url

# --- ASSETS ---
local_css("style.css")
lottie_animation_url = "https://assets9.lottiefiles.com/packages/lf20_v9riyrep.json"

# --- PDF CV for Download ---
with open("CV.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# --- HEADER & INTRO ---
with st.container():
    col1, col2 = st.columns((3, 1))
    with col1:
        st.title("Rafael Verdi de Freitas")
        st.subheader("Data Scientist | Machine Learning Engineer | Fraud Prevention Specialist")
        st.markdown("""
        <a href="https://www.linkedin.com/in/rafael-verdi-de-freitas/" target="_blank" style="text-decoration: none; color: #4CAF50; margin-right: 15px;">LinkedIn</a> 
        <a href="https://github.com/RVerdiF" target="_blank" style="text-decoration: none; color: #4CAF50;">GitHub</a>
        """, unsafe_allow_html=True)
        st.write(" ") 
        st.download_button(label="📄 Download CV", data=PDFbyte, file_name="RafaelVerdiFreitas_CV.pdf", mime="application/octet-stream")
    with col2:
        st.image("1594050442709.jpeg", width=230)

st.markdown("---")

# --- TAB CREATION ---
tab1, tab2, tab3, tab4 = st.tabs(["Summary & Skills", "Projects", "Professional Experience", "Education & Qualifications"])

# --- TAB 1: SUMMARY & SKILLS ---
with tab1:
    col1, col2 = st.columns((2, 1))
    with col1:
        st.header("Professional Summary")
        st.write("""
        Results-driven Data Scientist with over 5 years of experience in the financial industry, specializing in Strategic Data Management, Fraud Prevention, and Machine Learning. Proven track record of developing advanced fraud detection algorithms, building predictive models, and enhancing operational efficiency through automation and DevOps practices. A collaborative team player with a strong background in Business Administration, skilled in translating complex data into actionable business insights and driving organizational success.
        """)
    with col2:
        st_lottie(load_lottieurl(lottie_animation_url), speed=1, height=250, key="initial")

    st.markdown("---")
    st.header("Technical Skills")
    skills_data = {
        'Skill': [
            'Python', 'SQL', 'Power BI', 'Predictive Modeling',
            'Snowflake', 'DBT', 'ETL Processes', 'Deep Learning',
            'Apache Spark', 'Docker', 'CI/CD', 'AWS (S3, SageMaker)', 'Kubernetes',
            'Kafka', 'Hadoop', 'NLP', 'MLOps', 'Data Governance', 'Agile', 'Generative AI'
        ],
        'Years': [
            5, 5, 5, 5,
            5, 5, 5, 3,
            2, 2, 3, 3, 1,
            2, 2, 3, 3, 4, 5, 1
        ]
    }
    df_skills = pd.DataFrame(skills_data).sort_values(by="Years", ascending=True)

    fig = px.bar(df_skills, 
                 x='Years', 
                 y='Skill', 
                 orientation='h', 
                 title='Years of Experience',
                 template='plotly_dark',
                 color='Years',
                 color_continuous_scale=px.colors.sequential.Greens_r)
    
    fig.update_layout(
        height=700,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(title='Years'),
        yaxis=dict(title=''),
        coloraxis_showscale=False,
        title_x=0.5
    )
    st.plotly_chart(fig, use_container_width=True)

# --- TAB 2: PROJECTS ---
with tab2:
    st.header("Projects")
    st.write("Here are some of my projects on GitHub. Click on a title to see the repository!")
    st.markdown("---")

    projects_data = [
        {
            "url": "https://github.com/RVerdiF/api-embrapa-tech-challenge",
            "title": "API Embrapa - Vitivinicultura",
            "readme": '''
API para extração e consulta de informações referentes à vitivinicultura, baseada em dados da Embrapa.

**Descrição**: API RESTful desenvolvida com FastAPI que fornece acesso a dados sobre vitivinicultura, extraídos do portal Vitibrasil da Embrapa.

**Categorias de Dados**:
- Produção, Comercialização, Processamento, Exportação, Importação.

**Tecnologias**:
- FastAPI, Docker, Pandas, Pydantic.

**Uso da API**:
A API está disponível em: `https://api-embrapa-tech-challenge.onrender.com/`
Documentação Swagger: `https://api-embrapa-tech-challenge.onrender.com/docs`
''',
            "deployment_url": None
        },
        {
            "url": "https://github.com/RVerdiF/TechChallenge3",
            "title": "BTC Prediction Project",
            "readme": '''
Projeto de previsão de preço do Bitcoin usando Machine Learning com arquitetura modular e dashboard interativo.

**Funcionalidades**:
- Coleta de dados do Yahoo Finance com atualização automática.
- Engenharia de features com indicadores técnicos (SMA, RSI, MACD, etc.).
- Modelo de Machine Learning com LightGBM Classifier.
- Dashboard web com autenticação de usuários, gráfico interativo, previsões e treinamento customizado.

**Arquitetura Modular**:
- `ApiHandler`: Coleta de dados.
- `AuthHandler`: Autenticação de usuários.
- `DataHandler`: Gerenciamento de banco de dados de preços e modelos.
- `ModelHandler`: Treinamento e previsão.
- `main.py`: Interface com Streamlit.

**Tecnologias**:
- Streamlit, Pandas, yfinance, scikit-learn, lightgbm, plotly.
''',
            "deployment_url": "https://techchallenge3rafaelfreitas.streamlit.app/"
        },
        {
            "url": "https://github.com/RVerdiF/PaysimViz",
            "title": "PaySim Dataset Explorer",
            "readme": '''
A Streamlit application for exploring and analyzing the PaySim synthetic financial dataset.

**Features**:
- Backend de alta performance para lidar com o grande dataset PaySim.
- Análise de estatísticas gerais, distribuição de transações, performance do `isFlaggedFraud`, e identificação de "contas mula".

**Arquitetura e Design**:
- Backend centrado em SQL (SQLite) para evitar carregar todo o dataset em memória.
- Execução paralela de queries para uma experiência de usuário mais rápida.
- Agregação de alta performance com Polars para agregações complexas.

**Tecnologias**:
- Streamlit, Polars, SQLite, Pandas.
''',
            "deployment_url": "https://rverdif-paysimviz-app-olphe6.streamlit.app/"
        },
    ]

    for project in projects_data:
        # Main title links to GitHub
        title_md = f"### [{project['title']}]({project['url']})"
        
        # Add deployment link if it exists
        if project.get("deployment_url"):
            title_md += f" | [Live App]({project['deployment_url']})"

        st.markdown(title_md, unsafe_allow_html=True)
        
        with st.expander("See details (README)"):
            st.markdown(project['readme'], unsafe_allow_html=True)
        st.markdown("---")
    
    st.markdown("##") # Add some space
    st.subheader("Key Professional Projects")
    st.markdown("""
    <div class="card">
        <p class="job-title">Autonomous AI Agents & MLOps Pipelines</p>
        <p style="font-style: italic; color: #a0a0a0;">A confidential project from my role as a Data Scientist.</p>
        <p>Designed, engineered, and orchestrated autonomous AI agents and robust MLOps pipelines to automate complex data workflows, enhancing system scalability and reliability.</p>
        <p><strong>Key Technologies:</strong> Python, AI/ML, MLOps, CI/CD, Docker, AWS</p>
    </div>
    <div class="card">
        <p class="job-title">Advanced Fraud Detection Algorithms</p>
        <p style="font-style: italic; color: #a0a0a0;">A confidential project from my role as a Data Scientist.</p>
        <p>Developed and implemented advanced algorithms for real-time transactional fraud prevention, significantly improving the integrity and security of payment systems.</p>
        <p><strong>Key Technologies:</strong> Python, Machine Learning, Predictive Modeling, Big Data (Spark/Kafka)</p>
    </div>
    <div class="card">
        <p class="job-title">Predictive Fraud Modeling</p>
        <p style="font-style: italic; color: #a0a0a0;">A confidential project from my role as a Data Scientist.</p>
        <p>Built and trained sophisticated predictive fraud models using Machine Learning and AI, enabling proactive responses to emerging and evolving security threats.</p>
        <p><strong>Key Technologies:</strong> Python, Scikit-learn, Deep Learning (TensorFlow/Keras), SQL</p>
    </div>
    <div class="card">
        <p class="job-title">Transaction Monitoring System</p>
        <p style="font-style: italic; color: #a0a0a0;">A confidential project from my role as a Data Analyst.</p>
        <p>Created and maintained a comprehensive transaction monitoring system. This involved developing a Python-based backend and dynamic Power BI dashboards to assess operational risk and optimize security.</p>
        <p><strong>Key Technologies:</strong> Python, Power BI, SQL, Statistical Analysis</p>
    </div>
    <div class="card">
        <p class="job-title">Data Governance & Automation in Snowflake</p>
        <p style="font-style: italic; color: #a0a0a0;">A confidential project from my role as a Data Analyst.</p>
        <p>Led data governance initiatives by creating and managing tables, views, and stored procedures in Snowflake. Automated key departmental processes, improving workflow efficiency and team productivity.</p>
        <p><strong>Key Technologies:</strong> Snowflake, Python, dbt, SQL, Data Governance</p>
    </div>
    """, unsafe_allow_html=True)


# --- TAB 3: PROFESSIONAL EXPERIENCE (ALL CONTENT RESTORED) ---
with tab3:
    st.header("Professional Experience")
    st.markdown("""
    <div class="card">
        <p class="job-title">Data Scientist, Fraud Prevention</p>
        <p class="company-name">Banco Mercantil do Brasil | November 2024 – Present</p>
        <ul>
            <li>Engineer and orchestrate autonomous AI agents, designing and managing robust data and MLOps pipelines to automate complex workflows and enhance scalability.</li>
            <li>Develop and implement advanced algorithms for transactional fraud prevention, ensuring the integrity and security of payment systems.</li>
            <li>Build and train predictive fraud models using machine learning and AI, enabling proactive responses to emerging threats.</li>
            <li>Lead autonomous project management using DevOps practices, accelerating solution delivery and improving system reliability.</li>
        </ul>
    </div>
    <div class="card">
        <p class="job-title">Data Analyst, Fraud Prevention</p>
        <p class="company-name">Banco Mercantil do Brasil | January 2023 – November 2024</p>
        <ul>
            <li>Monitored and analyzed key performance indicators (KPIs) to ensure the quality and effectiveness of the department's services.</li>
            <li>Developed and maintained a transaction monitoring system using Python and Power BI dashboards, applying statistical methods to assess operational risk and optimize security.</li>
            <li>Automated key departmental processes, significantly improving workflow efficiency and team productivity.</li>
            <li>Managed data governance by creating and maintaining tables, views, and procedures in Snowflake using Python, dbt, and SQL.</li>
        </ul>
    </div>
    <div class="card">
        <p class="job-title">Data Analysis & Fraud Prevention Assistant</p>
        <p class="company-name">Banco Mercantil do Brasil | December 2021 – January 2023</p>
        <ul>
            <li>Provided critical support to the data analysis and fraud prevention teams, contributing to daily operations and strategic projects.</li>
            <li>Assisted in data preparation, cleaning, and preliminary analysis to support senior analysts and data scientists.</li>
        </ul>
    </div>
    <div class="card">
        <p class="job-title">Intern</p>
        <p class="company-name">Banco Mercantil do Brasil | November 2019 – November 2021</p>
        <ul>
            <li>Gained foundational experience in the financial industry, supporting various teams with data-related tasks and process documentation.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- TAB 4: EDUCATION & QUALIFICATIONS (ALL CONTENT RESTORED) ---
with tab4:
    st.header("Education")
    st.markdown("""
    <div class="card">
        <p class="degree-title">Postgraduate Specialization, Machine Learning Engineering</p>
        <p class="university-name">FIAP | Expected February 2025</p>
        <ul>
            <li><strong>Advanced Modeling:</strong> In-depth study of Classic Machine Learning and Deep Learning models, including supervised, unsupervised, and reinforcement learning.</li>
            <li><strong>Cloud & Big Data Ecosystems:</strong> Hands-on implementation of scalable ML solutions in cloud environments (AWS), leveraging platforms like Hadoop and Spark.</li>
            <li><strong>Specialized AI Applications:</strong> Covers advanced techniques in NLP, Computer Vision, and Generative AI models (GPT-4, Stable Diffusion).</li>
            <li><strong>MLOps & Productionalization:</strong> Emphasizes end-to-end MLOps practices, including automated data pipelines, containerization with Docker, and CI/CD for model deployment.</li>
        </ul>
    </div>
    <div class="card">
        <p class="degree-title">Postgraduate Specialization, Strategic Data Management & Analysis</p>
        <p class="university-name">PUC Minas | August 2022 - October 2023</p>
        <ul>
            <li><strong>Data-Driven Strategy:</strong> Provided knowledge of data-driven culture, data governance frameworks (LGPD/GDPR), and Agile Project Management.</li>
            <li><strong>Advanced Analytics & BI:</strong> Developed skills in advanced analytics using Python, including ETL/ELT processes and dimensional modeling for Data Warehouses.</li>
        </ul>
    </div>
    <div class="card">
        <p class="degree-title">Bachelor of Business Administration</p>
        <p class="university-name">PUC Minas | February 2018 – December 2021</p>
        <ul>
            <li>Provided a strong foundation in strategic management, finance, marketing, and organizational processes.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.header("Certifications & Licenses")
    st.markdown("""
    <div class="card">
        <ul>
            <li>Financial Markets | Yale University (2023)</li>
            <li>DBT & Snowflake (2023)</li>
            <li>Data Analysis and Power BI (2023)</li>
            <li>Data Analysis with Python (2022)</li>
            <li>Certified Yellow Belt, Lean Six Sigma (2022)</li>
            <li>Introduction to Data Science 2.0 (2020)</li>
            <li>Certified White Belt, Lean Six Sigma (2020)</li>
            <li>Transforming Ideas into Business (2015)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)