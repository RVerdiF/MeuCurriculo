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

## Descrição

Este projeto consiste em uma API RESTful desenvolvida com FastAPI que fornece acesso a dados sobre vitivinicultura. A API extrai dados do portal Vitibrasil da Embrapa e os disponibiliza em formato JSON através de endpoints estruturados.

## Fluxograma geral do Projeto

![Fluxograma da API Embrapa](assets/fluxograma_api.png)

## Diagrama de sequencia do Projeto

![Diagrama de sequencia da API Embrapa](assets/diagrama_de_sequencia.png)

## Categorias de Dados

A API fornece informações sobre:

- **Produção**: Dados sobre a produção de uvas e derivados
- **Comercialização**: Informações sobre a comercialização de produtos vitivinícolas
- **Processamento**: Dados sobre o processamento de uvas (viníferas, americanas, mesa e outros)
- **Exportação**: Estatísticas de exportação (vinhos de mesa, espumantes, uvas frescas e sucos)
- **Importação**: Estatísticas de importação (vinhos de mesa, espumantes, uvas frescas, passas e sucos)

## Tecnologias Utilizadas

- **FastAPI**: Framework web para construção de APIs
- **Docker**: Containerização da aplicação
- **Pandas**: Manipulação e análise de dados
- **Pydantic**: Validação de dados
- **PyYAML**: Processamento de arquivos YAML para configuração

## Requisitos

- Docker e Docker Compose
- Python 3.10+ (para desenvolvimento local)

## Instalação e Execução

### Usando Docker (Recomendado)

1. Clone o repositório:
   ```
   git clone <url-do-repositorio>
   cd embrapa-api
   ```

2. Crie um arquivo `.env` baseado no `.env.example`:
   ```
   cp .env.example .env
   ```

3. Para ambiente de desenvolvimento (com hot-reload):
   ```
   ./start-dev.bat
   ```
   ou
   ```
   docker-compose -f docker-compose.dev.yml up --build
   ```

4. Para ambiente de produção:
   ```
   ./start-prod.bat
   ```
   ou
   ```
   docker-compose up --build
   ```

### Instalação Local (Desenvolvimento)

1. Clone o repositório:
   ```
   git clone <url-do-repositorio>
   cd embrapa-api
   ```

2. Execute o script de instalação e inicialização:
   ```
   main.bat
   ```

   O script irá automaticamente criar um ambiente virtual, instalar as dependências necessárias e iniciar a aplicação.

## Uso da API

A API está disponível em:
- Produção: `https://api-embrapa-tech-challenge.onrender.com/`
- Desenvolvimento local: `http://localhost:8000`


### Documentação Swagger

Acesse a documentação interativa da API em:
- `http://localhost:8000/docs`
- `https://api-embrapa-tech-challenge.onrender.com/docs`

### Endpoints Principais

- **GET /v1/producao**: Retorna dados de produção
- **GET /v1/comercializacao**: Retorna dados de comercialização
- **GET /v1/processamento**: Retorna dados de processamento
- **GET /v1/exportacao**: Retorna dados de exportação
- **GET /v1/importacao**: Retorna dados de importação

### Exemplos de Filtros

Cada categoria possui endpoints para filtrar dados:

- **Por categoria**: `/v1/producao/categoria/{categoria}`
- **Por produto**: `/v1/producao/produto/{produto}`
- **Por ano**: `/v1/producao/ano/{ano}`
- **Por quantidade mínima**: `/v1/producao/quantidade/min/{quantidade}`
- **Por quantidade máxima**: `/v1/producao/quantidade/max/{quantidade}`
- **Filtros combinados**: `/v1/producao/filter?categoria=X&produto=Y&ano=2022`

## Estrutura do Projeto

```
./
├── app/
│   ├── models/            # Modelos de dados Pydantic
│   ├── routers/           # Rotas da API
│   ├── scrapping/         # Módulos para extração de dados
│   └── utils/             # Funções utilitárias
├── docker-compose.dev.yml # Configuração Docker para desenvolvimento
├── docker-compose.yml     # Configuração Docker para produção
├── Dockerfile             # Definição da imagem Docker
├── main.bat               # Script para execução local em Windows
├── main.py                # Ponto de entrada da aplicação
├── start-dev.bat          # Script para iniciar ambiente de desenvolvimento
├── start-prod.bat         # Script para iniciar ambiente de produção
├── requirements.txt       # Dependências do projeto
└── README.md              # Este arquivo
```

## Fonte dos Dados

Os dados são extraídos do portal Vitibrasil da Embrapa:
- [http://vitibrasil.cnpuv.embrapa.br/](http://vitibrasil.cnpuv.embrapa.br/)

## Deploy em Máquina Virtual

### Pré-requisitos
- Uma máquina virtual com Linux
- Docker e Docker Compose instalados
- Acesso SSH à máquina virtual

### Passo a Passo Simplificado

1. **Conecte-se à VM e instale Docker**:
   ```bash
   ssh usuario@endereco-da-vm
   sudo apt update && sudo apt install -y docker.io docker-compose
   sudo systemctl enable docker && sudo systemctl start docker
   ```

2. **Clone e execute a aplicação**:
   ```bash
   git clone <url-do-repositorio> && cd embrapa-api
   cp .env.example .env
   docker-compose up -d
   ```

3. **Configure um proxy reverso (opcional)**:
   ```bash
   sudo apt install -y nginx
   sudo nano /etc/nginx/sites-available/embrapa-api
   # Adicione a configuração básica do Nginx
   sudo ln -s /etc/nginx/sites-available/embrapa-api /etc/nginx/sites-enabled/
   sudo systemctl restart nginx
   ```

## Exemplo de Uso para Machine Learning

### Caso de Uso: Previsão de Produção de Uvas

Este exemplo conceitual demonstra como utilizar os dados da API para criar um modelo preditivo de machine learning:

#### Fluxo de Trabalho

1. **Coleta de Dados**: Utilize o endpoint `/producao/filter?categoria=VINHO_DE_MESA&produto=TINTO` para obter dados históricos de produção de vinho tinto.

2. **Preparação dos Dados**: 
   - Converta os dados para formato numérico
   - Crie features adicionais como produção do ano anterior e variação percentual
   - Codifique variáveis categóricas
   - Divida os dados em conjuntos de treino e teste

3. **Treinamento do Modelo**:
   - Utilize um algoritmo como Random Forest Regressor
   - Treine o modelo com dados históricos
   - Avalie o desempenho usando métricas como MSE e R²

4. **Visualização e Análise**:
   - Identifique as features mais importantes para a previsão
   - Compare valores reais vs. previstos
   - Analise tendências por região e tipo de produto

5. **Previsões Futuras**:
   - Utilize o modelo treinado para prever a produção do próximo ano
   - Gere previsões por estado e produto
   - Crie relatórios para auxiliar no planejamento da produção

Este fluxo de trabalho permite que produtores e empresas do setor vitivinícola utilizem os dados históricos disponibilizados pela API para tomar decisões baseadas em dados e antecipar tendências de mercado.
''',
            "deployment_url": None
        },
        {
            "url": "https://github.com/RVerdiF/TechChallenge3",
            "title": "BTC Prediction Project",
            "readme": '''
Projeto de previsão de preço do Bitcoin usando Machine Learning com arquitetura modular e dashboard interativo.

## Estrutura do Projeto

```
/Tech_Challenge_3
├── .devcontainer/              # Configurações do Dev Container
├── .git/                       # Repositório Git
├── .venv/                      # Ambiente virtual Python
├── src/
│   ├── ApiHandler/
│   │   └── data_api.py         # Coleta de dados via yfinance
│   ├── AuthHandler/
│   │   └── auth.py             # Gerenciamento de autenticação de usuários
│   ├── BacktestHandler/
│   │   └── backtesting.py      # Lógica para backtesting de estratégias
│   ├── DataHandler/
│   │   ├── data_handler.py     # Gerenciamento do DB de preços (btc_prices.db)
│   │   ├── model_db_handler.py # Gerenciamento do DB de modelos (models.db)
│   │   └── feature_engineering.py # Criação de features
│   ├── LogHandler/
│   │   └── log_config.py       # Configuração de logs
│   ├── ModelHandler/
│   │   ├── train_model.py      # Treinamento do modelo
│   │   └── predict.py          # Previsões
│   ├── Orchestration/
│   │   ├── run_project.py      # Script de configuração inicial (obsoleto)
│   │   └── update_scheduler.py # Lógica para atualização diária de dados
│   ├── __init__.py             # Inicializador do pacote src
│   └── config.py               # Configurações do projeto (paths)
├── .gitignore                  # Arquivos ignorados pelo Git
├── main.py                     # Interface Streamlit
├── requirements.txt            # Dependências do projeto
└── README.md                   # Documentação
```

**Observações:**
- Os bancos de dados `btc_prices.db`, `users.db` e `models.db` são criados dinamicamente no diretório `src/DataHandler/`.
- Os diretórios `__pycache__` são criados automaticamente pelo Python.

## Instalação

1. Clone o repositório
2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate    # Windows
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso

**Para iniciar o dashboard interativo:**
```bash
streamlit run main.py
```
A aplicação irá iniciar e apresentar uma tela de login. Você pode criar um novo usuário e, após o login, o dashboard será exibido. A primeira carga de dados é feita automaticamente em segundo plano.

## Funcionalidades

### Coleta de Dados
- **Fonte**: Yahoo Finance (yfinance)
- **Atualização Automática**: Os dados são atualizados diariamente em segundo plano para incluir o dia mais recente.
- **Armazenamento**: SQLite local (`btc_prices.db`).

### Engenharia de Features
- **Indicadores Técnicos**: SMA, RSI, EMA, MACD, Bandas de Bollinger, Oscilador Estocástico.
- **Target**: Classificação binária (Alta/Queda do próximo dia).

### Modelo de Machine Learning
- **Algoritmo**: LightGBM Classifier
- **Validação**: Time Series Split (3 folds)
- **Métricas**: Accuracy e F1-Score
- **Armazenamento**: O modelo treinado, métricas e parâmetros são salvos em um banco de dados SQLite, associados à conta do usuário.

### Dashboard Web
- **Autenticação**: Sistema de login e registro de usuários.
- **Atualização Automática**: Os dados de preço são atualizados diariamente em background.
- **Gráfico interativo**: Histórico de preços com Plotly, com seleção de período.
- **Previsões**: Botão para gerar previsão do próximo dia com a confiança do modelo do usuário.
- **Treinamento Customizado**: Interface para ajustar parâmetros de features e do modelo, e treinar um novo modelo para o usuário logado. Os parâmetros são salvos no banco de dados para futuras sessões.
- **Backtesting**: Página para simular uma estratégia de trading baseada no modelo treinado.

## Fluxos da Aplicação

(Os diagramas de fluxo fornecem uma visão geral da lógica da aplicação. Note que o armazenamento, antes baseado em arquivos, agora é centralizado em bancos de dados SQLite.)

### Fluxo Principal
![Fluxo Principal da Aplicação](imgs/Main%20Application%20Flow.jpg)

### Fluxo de Atualização de Dados (Dashboard)
![Fluxo de Atualização de Dados](imgs/Data%20Update%20Flow%20(Dashboard).jpg)

### Fluxo de Predição (Dashboard)
![Fluxo de Predição](imgs/Prediction%20Flow%20(Dashboard).jpg)

### Fluxo de Treinamento (Configurações)
![Fluxo de Treinamento](imgs/Training%20Flow%20(Settings).jpg)

### Fluxo de Backtesting
![Fluxo de Backtesting](imgs/Backtesting%20Flow%20(Backtesting).jpg)

## Arquitetura Modular

### `main.py`
- Interface principal com Streamlit. Gerencia a navegação, estado da sessão e inicialização de tarefas em segundo plano (atualização de dados).

### `src/`
- **`ApiHandler/`**: Coleta de dados externos.
- **`AuthHandler/`**: Gerencia a autenticação de usuários em seu próprio banco de dados (`users.db`).
- **`BacktestHandler/`**: Contém a lógica para executar a simulação de backtesting.
- **`DataHandler/`**:
  - `data_handler.py`: Gerencia o banco de dados de preços (`btc_prices.db`) e metadados (ex: data da última atualização).
  - `model_db_handler.py`: Gerencia o banco de dados de modelos e configurações dos usuários (`models.db`).
  - `feature_engineering.py`: Funções para calcular indicadores técnicos.
- **`LogHandler/`**: Configuração centralizada do logger.
- **`ModelHandler/`**:
  - `train_model.py`: Pipeline de treinamento que salva o modelo e métricas no banco de dados via `model_db_handler`.
  - `predict.py`: Carrega um modelo do banco de dados para fazer previsões.
- **`Orchestration/`**:
  - `update_scheduler.py`: Contém a lógica da tarefa em segundo plano que verifica e dispara a atualização diária dos dados.

## Dependências

- **pandas**: Manipulação de dados
- **yfinance**: API do Yahoo Finance
- **scikit-learn**: Métricas e validação
- **lightgbm**: Algoritmo de ML
- **joblib**: Serialização do modelo
- **streamlit**: Interface web
- **plotly**: Visualizações interativas

## Notas Técnicas

- **Multi-usuário**: A arquitetura suporta múltiplos usuários, onde cada um pode treinar, salvar e usar seu próprio modelo e configurações, persistidos em um banco de dados.
- **Tarefas em Segundo Plano**: A atualização diária de dados é executada em uma thread separada, garantindo que a interface do usuário não seja bloqueada.
''',
            "deployment_url": "https://techchallenge3rafaelfreitas.streamlit.app/"
        },
        {
            "url": "https://github.com/RVerdiF/PaysimViz",
            "title": "PaySim Dataset Explorer",
            "readme": '''
A Streamlit application for exploring and analyzing the PaySim synthetic financial dataset. This tool provides insights into transaction patterns, fraud detection, and data anomalies.

## Features

- **Efficient, High-Performance Backend:** Designed to handle the large PaySim dataset without crashing. The app uses a query-based architecture, parallel data loading, and the high-performance Polars data analysis library to ensure stability and speed.
- **Data-Aware Loading:** The app checks if the dataset exists. If not, it presents a simple one-click download button that securely uses your Kaggle credentials from Streamlit's secrets.
- **Home Page:** General statistics about the dataset, including null value analysis, negative value checks, and zero-amount transaction reports, all generated through efficient, direct-to-database queries.
- **Data Exploration:** In-depth analysis of the dataset, including:
    - Transaction distribution over time (Hourly, Daily, Weekly).
    - Transaction type overview (Pie chart and summary table).
    - Analysis of the `isFlaggedFraud` feature's performance.
    - Insights into transaction amounts and descriptive statistics.
    - "Mule account" identification and analysis, powered by Polars for high-performance aggregation.
    - Analysis of balance-draining fraudulent transactions.

## Architecture and Design

This application has been refactored for high performance and memory safety to handle the multi-gigabyte PaySim dataset.

- **SQL-Centric Backend:** Instead of loading the entire dataset into memory, the application leverages a **SQLite** database backend. Each chart and analysis on the UI is powered by a specific, targeted SQL query that only pulls the necessary aggregated data.
- **Parallel Execution:** To ensure a fast and responsive user experience, all independent database queries on a given page are executed in **parallel** using a `concurrent.futures.ThreadPoolExecutor`.
- **High-Performance Aggregation with Polars:** For complex aggregations that are not suitable for SQL (like the "Top Mule Accounts Overview"), the application uses the **Polars** library. It employs a memory-safe streaming strategy: data is queried from the database in chunks, processed, and aggregated without ever holding the complete intermediate dataset in memory.

## Dataset

This application uses the PaySim dataset from Kaggle. You can find more information here: [PaySim Synthetic Dataset](https://www.kaggle.com/datasets/ealaxi/paysim1/data)

## Getting Started

### 1. Prerequisites

- Python 3.8+
- A Kaggle account and an API token.

### 2. Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd KrakenInterview
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Kaggle API Credentials:**
    - Create a file at `.streamlit/secrets.toml`.
    - Add your Kaggle username and API key to this file in the following format:
      ```toml
      [kaggle]
      username = "YOUR_KAGGLE_USERNAME"
      key = "YOUR_KAGGLE_KEY"
      ```

### 3. Usage

1.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

2.  **Download the Dataset:**
    - On the first launch, the app will display a "Download Dataset" button.
    - Click this button to automatically download the data from Kaggle and set up the local SQLite database. This process is memory-safe and handles the large CSV in chunks.
    - After the download is complete, the app will proceed to the main data explorer.

## Project Structure
```
├── .gitignore
├── app.py              # Main Streamlit application file
├── LICENSE
├── requirements.txt    # Python dependencies
├── .streamlit/
│   └── secrets.toml    # Streamlit secrets for Kaggle credentials
├── dl/                 # Directory for downloaded data
└── src/
    ├── DataBase/       # Stores the final SQLite database
    ├── DataHandler/    # Modules for handling data (loading, downloading)
    ├── LogHandler/     # Module for logging setup
    ├── notebooks/      # Jupyter notebooks for exploration
    └── Utils/          # Utility scripts (e.g., SQL queries)
```
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