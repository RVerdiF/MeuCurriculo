"""Contact — intentionally minimal, with the résumé available two ways."""

from __future__ import annotations

from pathlib import Path

import streamlit as st

from portfolio.config import BASE_DIR, esc
from portfolio.data.profile import PROFILE, RESUME_DOWNLOAD_NAME, RESUME_LOCAL_PATH, RESUME_URL_PATH

FOCUS = (
    "Data Engineering",
    "Analytics Engineering",
    "Data Platforms",
    "AI-enabled Data Workflows",
)


def render() -> None:
    links = {link.id: link for link in PROFILE.links}
    focus = "".join(f"<div>{esc(item)}</div>" for item in FOCUS)
    contact_rows = "".join(
        f"<a class='contact-link' href='{esc(link.href)}'"
        + (" target='_blank' rel='noopener noreferrer'" if link.kind == "external" else "")
        + f">{esc(link.label)}<span class='dim'>{esc(link.value)}</span></a>"
        for link in (links["email"], links["linkedin"], links["github"])
    )
    st.html(
        f"""
        <section class="contact" id="contact">
          <div class="wrap">
            <div class="eyebrow">contact</div>
            <h2 class="contact-title">Let's build something useful.</h2>
            <div class="contact-grid">
              <div class="contact-focus">
                <div class="label">open to</div>
                {focus}
              </div>
              <div class="contact-list">
                <div class="label">direct</div>
                {contact_rows}
              </div>
              <div class="contact-list">
                <div class="label">résumé</div>
                <a class="contact-link" href="{esc(RESUME_URL_PATH)}"
                   download="{esc(RESUME_DOWNLOAD_NAME)}">PDF<span class="dim">direct download</span></a>
                <div class="dim" style="font-size:var(--text-xs)">
                  Mirror below if the direct link is blocked by your browser.
                </div>
              </div>
            </div>
          </div>
        </section>
        """
    )

    resume_path = Path(BASE_DIR) / RESUME_LOCAL_PATH
    if resume_path.is_file():
        st.download_button(
            label="Download résumé (PDF)",
            data=resume_path.read_bytes(),
            file_name=RESUME_DOWNLOAD_NAME,
            mime="application/pdf",
        )

    st.html(
        f"""
        <footer class="footer">
          <div class="wrap">
            <span>
              Built with Streamlit · content lives in structured Python modules ·
              no trackers, no external calls
            </span>
            <span>{esc(PROFILE.name)} · {esc(PROFILE.location)}</span>
          </div>
        </footer>
        """
    )
