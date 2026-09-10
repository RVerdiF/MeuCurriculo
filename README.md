# RafaelOS — Data Systems Console

An interactive portfolio for **Rafael Verdi de Freitas** (Data Engineer / Analytics
Engineer), built with Streamlit. It is a single continuous page — navigation, hero,
metrics, a real terminal, career-as-system-history, project artefacts, an interactive
lab and contact — where the interactive pieces are same-origin embedded islands and
everything else is static HTML rendered from structured Python data.

```
streamlit run app.py
```

## What is actually in here

| Layer | Where | Notes |
|---|---|---|
| Content (single source of truth) | `portfolio/data/` | dataclasses: profile, experience, projects, stack, education, query model, architecture |
| Page shell | `portfolio/components/shell.py` | page config, stylesheet injection, navigation, section frames |
| Sections | `portfolio/components/{hero,metrics,experience,projects,lab,contact}.py` | static HTML, no reruns |
| Islands (interactive) | `portfolio/islands/*.html` | terminal, architecture explorer, technology map, query console, ask-the-data, command palette |
| Payload builders | `portfolio/components/payloads.py` | serialise the content layer into island payloads |
| Design system | `portfolio/styles/{tokens,page,islands}.css` | tokens are shared by page and islands, never duplicated |
| Verification | `qa/` | a Playwright harness that drives the real page |

### The terminal

`portfolio/islands/terminal.html` implements a small command line over the same data
that renders the page: `help`, `whoami`, `experience [company]`, `projects [id]`,
`stack [layer]`, `impact`, `contact`, `resume`, `ls`, `cat <file>`, `grep <term>`,
`open <link|project>`, `go <section>`, `clear`, plus one easter egg.

**Security model.** There is no shell anywhere. Commands are an allowlist implemented
in the browser; nothing is passed to `os.system`, `subprocess`, `eval` or `exec`, and
there is no database or LLM behind it. `grep` is a literal substring search over the
in-memory payload. The query console accepts exactly three query shapes and looks the
answer up in pre-computed tables — SQL is only ever *displayed*, never executed.
All island output is written with `textContent`, so a command can never inject markup.

### How the islands talk to the page

Streamlit renders `st.iframe(html, height="content")` as a **same-origin `srcdoc`
frame** with automatic height measurement. That is what lets the terminal scroll the
page, the palette inject its overlay into the page document, and the palette drive
other islands through their `window.rafaelPortfolio` hooks. If same-origin access is
ever unavailable, each island degrades to working inside its own frame.

## Editing the content

Nothing professional is written inside rendering code. To change what the site says,
edit the dataclasses in `portfolio/data/`:

- `profile.py` — identity, links, hero metadata, headline metrics
- `experience.py` — roles, responsibilities, delivery chains, documented impact
- `projects.py` — public projects (from `projects.md`) and confidential systems
- `stack.py` — technologies by responsibility, each with evidence pointers
- `education.py` — degrees, courses, languages
- `queries.py` — query-console presets and ask-the-data intents
- `architecture.py` — the stage-by-stage architecture explorer

**Only facts that trace back to `CV.pdf` or to the repository's own project notes are
published.** Known metrics that could not be verified (for example a fraud-loss figure
attributed to the Mercantil tenure) are deliberately absent — `portfolio/data/profile.py`
documents the rule. Add a `Metric` there only when the number has a source.

To update the downloadable résumé, replace `static/CV.pdf`. It is served through
Streamlit static serving (`server.enableStaticServing = true`) at
`app/static/CV.pdf`, and the contact section also offers a native download button as a
mirror.

## Verification

```bash
# 1. run the app
streamlit run app.py --server.port 8520

# 2. drive it in a real browser (needs: pip install playwright && playwright install chromium)
python3 qa/check.py --url http://127.0.0.1:8520/
python3 qa/screenshots.py --url http://127.0.0.1:8520/
```

`qa/check.py` boots Chromium and asserts, against the live page: every section exists;
the résumé link serves a real PDF; the terminal answers `whoami`, `help`, `grep`, `cat`,
`ls`, `stack`, refuses unknown commands and injection attempts, and survives its own
commands; the explorer, technology map, query console, ask-the-data and command palette
all respond; the palette drives other islands; navigation stays fixed while the terminal
scrolls the page; `Tab` reaches content with a visible focus ring; and desktop, laptop,
tablet and mobile viewports have no horizontal overflow (with the terminal exercised on
mobile). Screenshots land in `/tmp/portfolio-qa/shots`.

Playwright is a development-only dependency: it is not in `requirements.txt`, so it is
never installed by Streamlit Community Cloud.

## Deployment

Standard Streamlit Community Cloud layout: `app.py` is the entry point,
`requirements.txt` pins `streamlit>=1.63,<2` (needed for `st.iframe` and `st.html`), and
`.streamlit/config.toml` carries the theme and static serving. No secrets, no external
API calls, no analytics: the page renders entirely from local modules.

### Known limitation

Document metadata (`<meta name="description">`, Open Graph tags) cannot be injected —
Streamlit renders `st.html` fragments in the body and drops head-only tags. The page
title comes from `set_page_config`; the professional summary is visible content in the
hero and the résumé section. Adding real meta tags would require a custom static host
in front of the app.
