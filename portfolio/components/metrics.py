"""System metrics — documented numbers only, each with its source."""

from __future__ import annotations

import streamlit as st

from portfolio.config import esc
from portfolio.data.profile import METRICS


def render() -> None:
    cards = "".join(
        f"""
        <div class="metric">
          <div class="metric-label">{esc(metric.label)}</div>
          <div class="metric-value">{esc(metric.value)}</div>
          <div class="metric-context">{esc(metric.context)}</div>
          <div class="metric-source">source · {esc(metric.source)}</div>
        </div>
        """
        for metric in METRICS
    )
    st.html(
        f"""
        <div class="wrap">
          <div class="metrics-grid">{cards}</div>
          <p class="section-sub" style="margin-top:1rem;font-size:var(--text-sm)">
            Only numbers stated in the résumé appear here. Anything I cannot trace to a
            role, a project or the shipped CV is left out on purpose. A metric without a
            source is just a claim.
          </p>
        </div>
        """
    )
