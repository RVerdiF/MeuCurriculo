import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit_lottie import st_lottie

# --- PAGE CONFIGURATION ---
st.set_page_config(layout="wide", page_title="Portfolio | Rafael Verdi de Freitas")

# --- Function to load local CSS file ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# --- Function to load Lottie animation from URL ---
def load_lottieurl(url: str):
    # The st_lottie function can directly handle URLs.
    return url

# --- ASSETS ---
local_css("style.css") # Load the custom CSS
lottie_animation_url = "https://assets9.lottiefiles.com/packages/lf20_v9riyrep.json"

# --- PDF CV for Download ---
# Make sure you have a file named 'CV.pdf' in the same folder
with open("CV.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# --- HEADER & INTRO ---
with st.container():
    # col1, col2 = st.columns((3, 1))
    # with col1:
    st.title("Rafael Verdi de Freitas")
    st.subheader("Data Scientist | Machine Learning Engineer | Fraud Prevention Specialist")
    # --- Social Links with improved styling ---
    st.markdown("""
    <a href="https://www.linkedin.com/in/rafael-verdi/" target="_blank" style="text-decoration: none; color: #4CAF50; margin-right: 15px;">LinkedIn</a> 
    <a href="https://github.com/rafaelvverdi" target="_blank" style="text-decoration: none; color: #4CAF50;">GitHub</a>
    """, unsafe_allow_html=True)
    st.write(" ") # Adding a little space
    st.download_button(
        label="📄 Download CV",
        data=PDFbyte,
        file_name="RafaelVerdiFreitas_CV.pdf",
        mime="application/octet-stream",
    )
    # with col2:
    #     # Make sure you have a file named 'profile_pic.png'
    #     st.image("profile_pic.png", width=230)

st.markdown("---")

# --- TAB CREATION ---
tab1, tab2, tab3 = st.tabs([
    "Summary & Skills", 
    "Professional Experience", 
    "Education & Qualifications"
])

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

    # --- Interactive Skills Chart ---
    skills_data = {
        'Skill': [
            'Python', 'SQL', 'Power BI', 'Predictive Modeling', 
            'Snowflake', 'DBT', 'ETL Processes', 'Deep Learning', 
            'Apache Spark', 'Docker', 'CI/CD', 'AWS (S3, SageMaker)', 'Kubernetes'
        ],
        'Proficiency': [
            95, 90, 90, 85, 
            85, 85, 85, 80, 
            80, 75, 75, 70, 70
        ]
    }
    df_skills = pd.DataFrame(skills_data)
    
    fig = px.bar(df_skills.sort_values(by="Proficiency"), x='Proficiency', y='Skill', orientation='h', title='Skill Proficiency', color='Proficiency',
                 color_continuous_scale='Greens', text='Proficiency')
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font=dict(color='#E0E0E0'),
                      xaxis=dict(showgrid=False, range=[0, 100]), yaxis=dict(showgrid=False), title_x=0.5)
    fig.update_traces(texttemplate='%{text}%', textposition='inside')
    st.plotly_chart(fig, use_container_width=True)

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
        </ul>
    </div>
    <div class="card">
        <p class="job-title">Data Analyst, Fraud Prevention</p>
        <p class="company-name">Banco Mercantil do Brasil | January 2023 – November 2024</p>
        <ul>
            <li>Monitored and analyzed key performance indicators (KPIs) to ensure the quality and effectiveness of the department's services.</li>
            <li>Developed and maintained a transaction monitoring system using Python and Power BI dashboards.</li>
            <li>Managed data governance by creating and maintaining tables, views, and procedures in Snowflake using Python, dbt, and SQL.</li>
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
            <li><strong>Advanced Modeling:</strong> In-depth study of ML and Deep Learning models, including supervised, unsupervised, and reinforcement learning.</li>
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