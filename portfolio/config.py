"""Paths, asset loading and safe payload helpers shared by the components."""

from __future__ import annotations

import json
from functools import lru_cache
from html import escape
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent.parent
STYLES_DIR = BASE_DIR / "portfolio" / "styles"
ISLANDS_DIR = BASE_DIR / "portfolio" / "islands"

# Sections rendered as anchors in the single-page layout. Navigation and the
# terminal both read this list, so it stays consistent.
SECTIONS: tuple[tuple[str, str], ...] = (
    ("home", "Home"),
    ("metrics", "Metrics"),
    ("terminal", "Console"),
    ("experience", "Experience"),
    ("projects", "Projects"),
    ("stack", "Stack"),
    ("contact", "Contact"),
)

NAV_SECTIONS: tuple[tuple[str, str], ...] = (
    ("home", "Home"),
    ("experience", "Experience"),
    ("projects", "Projects"),
    ("stack", "Stack"),
    ("contact", "Contact"),
)


@lru_cache(maxsize=32)
def _read_cached(path_str: str, mtime: float) -> str:
    """Read a text asset, keyed by modification time."""
    return Path(path_str).read_text(encoding="utf-8")


def read_text(path: Path) -> str:
    """Read a text asset, cached until the file changes.

    The mtime is part of the cache key, so editing the stylesheet or an island
    template shows up on the next render instead of waiting for a restart.
    """
    return _read_cached(str(path), path.stat().st_mtime)


def stylesheet() -> str:
    """Design system for the page: tokens + page rules (Streamlit chrome, sections)."""
    return read_text(STYLES_DIR / "tokens.css") + read_text(STYLES_DIR / "page.css")


def island_stylesheet() -> str:
    """Design system for an island: tokens + island component rules.

    Islands never load the page-only rules, which keeps ~20 KB of CSS out of
    each of the six embedded frames.
    """
    return read_text(STYLES_DIR / "tokens.css") + read_text(STYLES_DIR / "islands.css")


def island_template(name: str) -> str:
    """Load an island template (HTML + CSS + JS, rendered inside st.iframe)."""
    return read_text(ISLANDS_DIR / f"{name}.html")


def to_script_json(payload: Any) -> str:
    """Serialise a payload for embedding inside a <script> block.

    ``</`` is escaped so a string in the payload can never close the script tag
    and inject markup. Only trusted, locally defined portfolio data is passed
    here — never user input.
    """
    serialised = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    return serialised.replace("</", "<\\/").replace("<!--", "<\\!--")


def render_island(template: str, *, data: dict[str, Any]) -> str:
    """Fill an island template with the island stylesheet and its data payload."""
    html = template.replace("/*__STYLES__*/", island_stylesheet())
    return html.replace("/*__PAYLOAD__*/", to_script_json(data))


def esc(value: object) -> str:
    """HTML-escape any dynamic string crossing into markup."""
    return escape(str(value), quote=True)
