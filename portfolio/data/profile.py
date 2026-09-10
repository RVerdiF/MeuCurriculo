"""Identity, contact channels, verified headline metrics and résumé summary."""

from __future__ import annotations

from dataclasses import dataclass, field

RESUME_FILE = "CV.pdf"
# Two paths on purpose: the URL Streamlit serves the PDF at (static serving),
# and the file on disk that the mirror button reads.
RESUME_URL_PATH = "app/static/CV.pdf"
RESUME_LOCAL_PATH = "static/CV.pdf"
RESUME_DOWNLOAD_NAME = "Rafael_Verdi_de_Freitas_Resume.pdf"


@dataclass(frozen=True)
class Link:
    """An outbound link with an explicit, human-readable destination."""

    id: str
    label: str
    value: str
    href: str
    kind: str = "external"  # external | mail | download


@dataclass(frozen=True)
class Metric:
    """A headline number that is traceable to the shipped résumé.

    `source` documents where the number comes from, so an unverifiable figure
    can never silently appear on the page.
    """

    id: str
    label: str
    value: str
    context: str
    source: str


@dataclass(frozen=True)
class Profile:
    name: str
    short_name: str
    terminal_user: str
    terminal_host: str
    role: str
    subtitle: str
    location: str
    availability: str
    summary: str
    years_experience: str
    status: str
    meta: tuple[tuple[str, str], ...]
    hero_themes: tuple[str, ...]
    links: tuple[Link, ...] = field(default_factory=tuple)

    @property
    def email(self) -> str:
        return next(link.value for link in self.links if link.id == "email")

    @property
    def resume_link(self) -> Link:
        return next(link for link in self.links if link.id == "resume")


SUMMARY = (
    "6+ years of data engineering for banks and digital-asset platforms: cloud data "
    "platforms, automated pipelines, fraud prevention and analytics. The work sits "
    "mostly in data engineering, automation, MLOps, fraud analytics and data quality."
)

PROFILE = Profile(
    name="Rafael Verdi de Freitas",
    short_name="Rafael Freitas",
    terminal_user="rafael",
    terminal_host="portfolio",
    role="Data Engineer / Analytics Engineer",
    subtitle="Data Engineer · Analytics Engineer",
    location="Belo Horizonte, Brazil",
    availability="Remote — Americas time zones",
    summary=SUMMARY,
    years_experience="6+",
    status="available",
    meta=(
        ("STATUS", "available"),
        ("LOCATION", "Brazil · GMT-3"),
        ("EXPERIENCE", "6+ years"),
        ("FOCUS", "Data · Analytics · AI"),
    ),
    hero_themes=(
        "Building data systems,",
        "analytics platforms and AI workflows.",
    ),
    links=(
        Link(
            id="email",
            label="Email",
            value="rafaelverdifreitas@hotmail.com",
            href="mailto:rafaelverdifreitas@hotmail.com",
            kind="mail",
        ),
        Link(
            id="linkedin",
            label="LinkedIn",
            value="linkedin.com/in/rafael-verdi-de-freitas",
            href="https://www.linkedin.com/in/rafael-verdi-de-freitas/",
        ),
        Link(
            id="github",
            label="GitHub",
            value="github.com/RVerdiF",
            href="https://github.com/RVerdiF",
        ),
        Link(
            id="resume",
            label="Résumé",
            value=RESUME_FILE,
            href=RESUME_FILE,
            kind="download",
        ),
    ),
)


# Only metrics stated in the shipped résumé are listed here. Anything that
# cannot be traced to the résumé or the repository is deliberately omitted.
METRICS: tuple[Metric, ...] = (
    Metric(
        id="experience",
        label="EXPERIENCE",
        value="6+ yrs",
        context="Data platforms, analytics and fraud-prevention systems",
        source="Résumé summary",
    ),
    Metric(
        id="automation",
        label="AUTOMATION_RATE",
        value="~80%",
        context="Recurring operational processes automated",
        source="Banco Mercantil · Data Scientist / Data Analytics",
    ),
    Metric(
        id="resolution",
        label="RESOLUTION_TIME",
        value="30%+",
        context="Faster case resolution after pipelines and models shipped",
        source="Banco Mercantil · fraud-prevention workflow",
    ),
    Metric(
        id="operating_since",
        label="INDEPENDENT_WORK",
        value="2018",
        context="Founder and lead engineer, technical consulting",
        source="Corporate Gestão Empresarial",
    ),
)
