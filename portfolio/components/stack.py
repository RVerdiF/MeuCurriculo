"""Core stack: fourteen technologies by responsibility, each with a reference."""

from __future__ import annotations

from portfolio.components import payloads, shell


def render() -> None:
    shell.island(
        "corestack",
        payloads.corestack_payload(),
        "core stack",
        "grouped by what it is for. Click a technology to see where it was used",
    )
