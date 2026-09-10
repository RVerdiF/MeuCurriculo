"""Lab — the interactive section: architecture, technology map, queries, questions."""

from __future__ import annotations

import streamlit as st

from portfolio.components import payloads, shell


def render() -> None:
    shell.island(
        "explorer",
        payloads.explorer_payload(),
        "architecture explorer",
        "pick any stage to see its role, patterns and where it was used",
    )
    st.html('<div class="wrap" style="height:var(--space-6)"></div>')
    shell.island(
        "stackmap",
        payloads.stackmap_payload(),
        "technology map",
        "organised by responsibility, not by percentage — click a technology for evidence",
    )
    st.html('<div class="wrap" style="height:var(--space-6)"></div>')
    shell.island(
        "queryconsole",
        payloads.console_payload(),
        "query my experience",
        "fixed dataset · three supported query shapes · nothing is executed as SQL",
    )
    st.html('<div class="wrap" style="height:var(--space-6)"></div>')
    shell.island(
        "ask",
        payloads.ask_payload(),
        "ask the data",
        "deterministic lookup over the same structured data — no LLM API, no cost",
    )
