import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(layout="wide", page_title="Portfolio | Rafael Verdi de Freitas")

# --- Function to load local CSS file ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the custom CSS
local_css("style.css")

# --- HEADER ---
st.title("Rafael Verdi de Freitas")
st.write("Belo Horizonte, MG, Brazil | +55 31 998731255 | rafaelverdifreitas@hotmail.com")
st.markdown("---")

# --- TAB CREATION ---
tab1, tab2, tab3 = st.tabs([
    "Summary & Skills", 
    "Professional Experience", 
    "Education & Qualifications"
])

# --- TAB 1: SUMMARY & SKILLS ---
with tab1:
    st.header("Professional Summary")
    st.write("""
    Results-driven Data Scientist with over 5 years of experience in the financial industry,
    specializing in Strategic Data Management, Fraud Prevention, and Machine Learning. Proven
    track record of developing advanced fraud detection algorithms, building predictive models, and
    enhancing operational efficiency through automation and DevOps practices. A collaborative team
    player with a strong background in Business Administration, skilled in translating complex data
    into actionable business insights and driving organizational success.
    """)
    st.markdown("---")
    st.header("Technical Skills")
    st.markdown("""
    <div class="card">
        <p class="job-title">Programming & Databases</p>
        <p>Python (5 years), SQL (5 years)</p>
    </div>
    <div class="card">
        <p class="job-title">Data & Analytics Tools</p>
        <p>Power BI (5 years), ETL (5 years), Snowflake, dbt, Microsoft Office Suite (5 years)</p>
    </div>
    <div class="card">
        <p class="job-title">ML & Data Science</p>
        <p>Machine Learning (Supervised & Unsupervised), Deep Learning, Predictive Modeling, NLP, MLOps, Data Governance</p>
    </div>
    <div class="card">
        <p class="job-title">Platforms & Methodologies</p>
        <p>DevOps, CI/CD, Agile (Scrum, Kanban), Docker, AWS, Big Data (Hadoop, Spark, Kafka)</p>
    </div>
    """, unsafe_allow_html=True)

# --- TAB 2: PROFESSIONAL EXPERIENCE ---
with tab2:
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
    """, unsafe_allow_html=True)

# --- TAB 3: EDUCATION & QUALIFICATIONS ---
with tab3:
    st.header("Education")
    st.markdown("""
    <div class="card">
        <p class="degree-title">Postgraduate Specialization, Machine Learning Engineering</p>
        <p class="university-name">FIAP | Expected February 2025</p>
        <ul>
            <li><strong>Advanced Modeling:</strong> In-depth study of classic Machine Learning and Deep Learning models, including supervised, unsupervised, and reinforcement learning.</li>
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
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    
    st.header("Languages")
    st.markdown("""
    <div class="card">
        <p><strong>Portuguese:</strong> Native</p>
        <p><strong>English:</strong> Advanced</p>
    </div>
    """, unsafe_allow_html=True)