"""Hero — identity, thesis, system metadata and the primary actions."""

from __future__ import annotations

import streamlit as st

from portfolio.config import esc
from portfolio.data.profile import PROFILE, RESUME_URL_PATH


def _actions() -> str:
    links = {link.id: link for link in PROFILE.links}
    return f"""
        <div class="hero-actions">
          <a class="btn btn--primary" href="#experience">
            Explore experience <span class="btn-arrow" aria-hidden="true">→</span>
          </a>
          <a class="btn" href="#projects">
            View projects <span class="btn-arrow" aria-hidden="true">→</span>
          </a>
          <a class="btn" href="{esc(RESUME_URL_PATH)}" download="Rafael_Verdi_de_Freitas_Resume.pdf">
            ↓ Download résumé
          </a>
          <a class="btn btn--ghost" href="{esc(links['linkedin'].href)}" target="_blank"
             rel="noopener noreferrer">LinkedIn ↗</a>
          <a class="btn btn--ghost" href="{esc(links['github'].href)}" target="_blank"
             rel="noopener noreferrer">GitHub ↗</a>
        </div>
    """


def _meta() -> str:
    rows = "".join(
        f"<div><span class='meta-key'>{esc(key)}</span><span class='meta-val'>{esc(value)}</span></div>"
        for key, value in PROFILE.meta
    )
    return f'<div class="hero-meta">{rows}</div>'


def _panel() -> str:
    return """
        <aside class="hero-panel" aria-label="System summary">
          <div class="hero-panel-head">
            <span>system</span>
            <span>profile.v1</span>
          </div>
          <div class="hero-panel-body">
            <div class="panel-row"><span class="k">role</span><span class="v">Data / Analytics Engineer</span></div>
            <div class="panel-row"><span class="k">domain</span><span class="v">Banking · Fraud · Digital assets</span></div>
            <div class="panel-row"><span class="k">stack</span><span class="v">dbt · Snowflake · AWS · Python</span></div>
            <div class="panel-row"><span class="k">location</span><span class="v">Brazil · GMT-3</span></div>
            <div class="panel-row"><span class="k">status</span><span class="v ok">● available</span></div>
          </div>
        </aside>
    """


def render() -> None:
    first, second = PROFILE.hero_themes
    st.html(
        f"""
        <section class="section section--flush" id="home">
          <div class="wrap">
            <div class="hero">
              <div class="hero-grid">
                <div>
                  <h1 class="hero-name">{esc(PROFILE.name)}</h1>
                  <p class="hero-role">{esc(PROFILE.role)}</p>
                  <p class="hero-thesis" aria-label="{esc(first)} {esc(second)}">
                    {esc(first)}<br><strong>{esc(second)}</strong>
                  </p>
                  {_meta()}
                  {_actions()}
                </div>
                {_panel()}
              </div>
            </div>
          </div>
        </section>
        """
    )
