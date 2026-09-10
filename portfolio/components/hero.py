"""Hero: who this is, what they build, and the two actions that matter."""

from __future__ import annotations

import streamlit as st

from portfolio.config import esc
from portfolio.data.profile import PROFILE, RESUME_DOWNLOAD_NAME, RESUME_URL_PATH


def _meta() -> str:
    rows = "".join(
        f"<div><span class='meta-key'>{esc(key)}</span><span class='meta-val'>{esc(value)}</span></div>"
        for key, value in PROFILE.meta
    )
    return f'<div class="hero-meta">{rows}</div>'


def _actions() -> str:
    links = {link.id: link for link in PROFILE.links}
    return f"""
        <div class="hero-actions">
          <a class="btn btn--primary" href="#projects">
            View my work <span class="btn-arrow" aria-hidden="true">→</span>
          </a>
          <a class="btn" href="{esc(RESUME_URL_PATH)}" download="{esc(RESUME_DOWNLOAD_NAME)}">
            ↓ Download résumé
          </a>
        </div>
        <div class="hero-links">
          <a href="{esc(links['linkedin'].href)}" target="_blank" rel="noopener noreferrer">
            LinkedIn ↗<span class="dim">{esc(links['linkedin'].value)}</span>
          </a>
          <a href="{esc(links['github'].href)}" target="_blank" rel="noopener noreferrer">
            GitHub ↗<span class="dim">{esc(links['github'].value)}</span>
          </a>
        </div>
    """


def render() -> None:
    first, second = PROFILE.hero_themes
    st.html(
        f"""
        <section class="section section--flush" id="home">
          <div class="wrap">
            <div class="hero">
              <h1 class="hero-name">{esc(PROFILE.name)}</h1>
              <p class="hero-role">{esc(PROFILE.role)}</p>
              <p class="hero-thesis" aria-label="{esc(first)} {esc(second)}">
                {esc(first)}<br><strong>{esc(second)}</strong>
              </p>
              {_meta()}
              {_actions()}
            </div>
          </div>
        </section>
        """
    )
