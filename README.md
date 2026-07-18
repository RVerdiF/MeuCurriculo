# Rafael Verdi de Freitas — Résumé

An accessible professional résumé website built with [Streamlit](https://streamlit.io/).

## Run locally

```bash
git clone https://github.com/RVerdiF/MeuCurriculo.git
cd MeuCurriculo

uv venv .venv
uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/streamlit run app.py
```

The application entry point is `app.py`. Its downloadable résumé is `CV.pdf`, and its Streamlit theme configuration is in `.streamlit/config.toml`.

## Deployment

The repository follows Streamlit's standard deployment layout (`app.py`, `requirements.txt`, and `.streamlit/config.toml`). It contains no versioned CI workflow or provider-specific deployment manifest. To deploy it through Streamlit Community Cloud, connect this repository and select `app.py` as the entry point.