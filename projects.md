https://github.com/RVerdiF/api-embrapa-tech-challenge

# API Embrapa - Vitivinicultura

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

---

https://github.com/RVerdiF/TechChallenge3

# BTC Prediction Project

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

---

https://github.com/RVerdiF/PaysimViz

# PaySim Dataset Explorer

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