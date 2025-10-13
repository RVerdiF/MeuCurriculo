import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(layout="wide", page_title="CV - Rafael Verdi de Freitas")

# --- HEADER ---
# This section remains visible across all tabs
st.title("Rafael Verdi de Freitas")
st.write("Belo Horizonte, MG, Brazil | +55 31 998731255 | rafaelverdifreitas@hotmail.com")
st.markdown("---")

# --- TAB CREATION ---
# We have 3 main tabs for a consolidated view
tab1, tab2, tab3 = st.tabs([
    "Summary & Skills", 
    "Professional Experience", 
    "Education & Qualifications"
])

# --- TAB 1: SUMMARY & SKILLS ---
with tab1:
    # Professional Summary Section
    st.header("Professional Summary")
    st.write("""
    Results-driven Data Scientist with over 5 years of experience in the financial industry,
    specializing in Strategic Data Management, Fraud Prevention, and Machine Learning. Proven
    track record of developing advanced fraud detection algorithms, building predictive models, and
    enhancing operational efficiency through automation and DevOps practices. A collaborative team
    player with a strong background in Business Administration, skilled in translating complex data
    into actionable business insights and driving organizational success.
    """)
    
    st.markdown("---") # Visual separator

    # Technical Skills Section
    st.header("Technical Skills")
    skills = {
        "Programming & Databases": "Python (5 years), SQL (5 years)",
        "Data & Analytics Tools": "Power BI (5 years), ETL (5 years), Snowflake, dbt, Microsoft Office Suite (5 years)",
        "ML & Data Science": "Machine Learning (Supervised & Unsupervised), Deep Learning, Predictive Modeling, NLP, MLOps, Data Governance",
        "Platforms & Methodologies": "DevOps, CI/CD, Agile (Scrum, Kanban), Docker, AWS, Big Data (Hadoop, Spark, Kafka)"
    }
    for category, skill_list in skills.items():
        st.subheader(category)
        st.write(skill_list)

# --- TAB 2: PROFESSIONAL EXPERIENCE ---
with tab2:
    st.header("Professional Experience")
    st.subheader("Data Scientist, Fraud Prevention | Banco Mercantil do Brasil")
    st.write("November 2024 – Present")
    st.markdown("""
    - Engineer and orchestrate autonomous AI agents, designing and managing robust data and MLOps pipelines to automate complex workflows and enhance scalability.
    - Develop and implement advanced algorithms for transactional fraud prevention, ensuring the integrity and security of payment systems.
    - Build and train predictive fraud models using machine learning and AI, enabling proactive responses to emerging threats.
    - Lead autonomous project management using DevOps practices, accelerating solution delivery and improving system reliability.
    """)

    st.subheader("Data Analyst, Fraud Prevention | Banco Mercantil do Brasil")
    st.write("January 2023 – November 2024")
    st.markdown("""
    - Monitored and analyzed key performance indicators (KPIs) to ensure the quality and effectiveness of the department's services.
    - Developed and maintained a transaction monitoring system using Python and Power BI dashboards, applying statistical methods to assess operational risk and optimize security.
    - Automated key departmental processes, significantly improving workflow efficiency and team productivity.
    - Managed data governance by creating and maintaining tables, views, and procedures in Snowflake using Python, dbt, and SQL.
    """)
    
    st.subheader("Data Analysis & Fraud Prevention Assistant | Banco Mercantil do Brasil")
    st.write("December 2021 – January 2023")
    st.markdown("""
    - Provided critical support to the data analysis and fraud prevention teams, contributing to daily operations and strategic projects.
    - Assisted in data preparation, cleaning, and preliminary analysis to support senior analysts and data scientists.
    """)
    
    st.subheader("Intern | Banco Mercantil do Brasil")
    st.write("November 2019 – November 2021")
    st.markdown("""
    - Gained foundational experience in the financial industry, supporting various teams with data-related tasks and process documentation.
    """)

# --- TAB 3: EDUCATION & QUALIFICATIONS ---
with tab3:
    # Education Section with enhanced descriptions
    st.header("Education")
    st.subheader("Postgraduate Specialization, Machine Learning Engineering | FIAP")
    st.write("Expected February 2025")
    st.markdown("""
    - **Advanced Modeling:** In-depth study and application of classic Machine Learning and Deep Learning models, including supervised (e.g., regressions, classifications), unsupervised (e.g., clustering, dimensionality reduction), and reinforcement learning algorithms.
    - **Cloud & Big Data Ecosystems:** Hands-on implementation of scalable ML solutions in both on-premise and cloud environments (AWS, Azure, GCP), leveraging Big Data platforms like Hadoop and Spark for distributed data processing.
    - **Specialized AI Applications:** Covers advanced techniques in Natural Language Processing (NLP), Computer Vision, and the architecture of Generative AI models such as GPT-4 and Stable Diffusion.
    - **MLOps & Productionalization:** Emphasizes end-to-end MLOps practices, including automated data pipeline construction, model containerization with Docker, CI/CD for continuous model training and deployment, and API development for serving models in both batch and real-time scenarios.
    """)

    st.subheader("Postgraduate Specialization, Strategic Data Management & Analysis | PUC Minas")
    st.write("August 2022 - October 2023")
    st.markdown("""
    - **Data-Driven Strategy:** Provided comprehensive knowledge of fostering a data-driven culture, implementing robust data governance frameworks (LGPD/GDPR), and applying Agile Project Management (Scrum, Kanban) to data-centric projects.
    - **Advanced Analytics & BI:** Developed skills in advanced analytics using Python, including complex ETL/ELT processes and dimensional modeling for the design and creation of enterprise-level Data Warehouses, Data Marts, and OLAP applications.
    - **Corporate Intelligence:** Coursework included applied statistics, corporate intelligence, and data visualization techniques to transform raw data into actionable insights through interactive dashboards and strategic storytelling.
    """)

    st.subheader("Bachelor of Business Administration | PUC Minas")
    st.write("February 2018 – December 2021")
    st.markdown("""
    - Provided a strong foundation in strategic management, finance, marketing, and organizational processes, enabling a comprehensive understanding of how to apply data-driven solutions to solve complex business challenges.
    """)
    
    st.markdown("---") # Visual separator

    # Certifications & Licenses Section
    st.header("Certifications & Licenses")
    certifications = [
        "Financial Markets | Yale University (2023)",
        "DBT & Snowflake (2023)",
        "Data Analysis and Power BI (2023)",
        "Data Analysis with Python (2022)",
        "Certified Yellow Belt, Lean Six Sigma (2022)",
        "Introduction to Data Science 2.0 (2020)",
        "Certified White Belt, Lean Six Sigma (2020)",
        "Transforming Ideas into Business (2015)"
    ]
    for cert in certifications:
        st.write(f"- {cert}")

    st.markdown("---") # Visual separator

    # Languages Section
    st.header("Languages")
    st.write("- Portuguese: Native")
    st.write("- English: Advanced")