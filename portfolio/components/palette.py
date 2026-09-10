"""Command palette (Ctrl/Cmd + K) — mounted as a same-origin island."""

from __future__ import annotations

from portfolio.components import payloads, shell


def render() -> None:
    shell.island(
        "palette",
        payloads.palette_payload(),
        "command palette",
        "Ctrl / Cmd + K, also on the search button in the header",
    )
