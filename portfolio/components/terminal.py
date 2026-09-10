"""Terminal — the signature interaction, mounted as a same-origin island."""

from __future__ import annotations

from portfolio.components import payloads, shell


def render() -> None:
    shell.island(
        "terminal",
        payloads.terminal_payload(),
        "interactive · portfolio cli",
        "allowlisted commands · no shell, no eval, no arbitrary execution",
    )
