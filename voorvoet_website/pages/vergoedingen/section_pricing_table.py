"""Section displaying VoorVoet pricing information in a searchable table."""

import reflex as rx
import csv
from pathlib import Path

from ...theme import Colors, FontSizes
from ...components import section, container
from ...utils.get_translation import get_translation


TRANSLATIONS = {
    "nl": {
        "title": "Tarieven bij VoorVoet",
        "intro": "VoorVoet hanteert eerlijke tarieven om zorg voor iedereen toegankelijk te maken. Hieronder staat een overzicht van de kosten van alle behandelingen en hulpmiddelen. De bedragen zijn, indien nodig, inclusief BTW. De tarieven kunt u ook als ",
        "pdf_link": "PDF bestand downloaden",
        "disclaimer": "We houden deze lijst zo nauwkeurig mogelijk bij. Mochten er onverhoopt fouten optreden dan houdt VoorVoet - Praktijk voor podotherapie het recht om de prijs te corrigeren. Aan deze lijst kunnen geen rechten worden ontleend.",
    },
    "de": {
        "title": "Tarife bei VoorVoet",
        "intro": "VoorVoet wendet faire Tarife an, um die Versorgung für alle zugänglich zu machen. Unten finden Sie eine Übersicht über die Kosten aller Behandlungen und Hilfsmittel. Die Beträge verstehen sich, sofern erforderlich, inklusive MwSt. Die Tarife können Sie auch als ",
        "pdf_link": "PDF-Datei herunterladen",
        "disclaimer": "Wir halten diese Liste so genau wie möglich. Sollten dennoch Fehler auftreten, behält sich VoorVoet - Praxis für Podotherapie das Recht vor, den Preis zu korrigieren. Aus dieser Liste können keine Rechte abgeleitet werden.",
    },
    "en": {
        "title": "Rates at VoorVoet",
        "intro": "VoorVoet applies fair rates to make care accessible to everyone. Below is an overview of the costs of all treatments and aids. The amounts include VAT where applicable. You can also ",
        "pdf_link": "download the rates as a PDF file",
        "disclaimer": "We keep this list as accurate as possible. Should errors occur, VoorVoet - Practice for Podotherapy reserves the right to correct the price. No rights can be derived from this list.",
    },
}


def load_pricing_data() -> tuple[list[str], list[list[str]]]:
    """
    Load pricing data from CSV file and convert to table format.

    Reads the 2025 pricing data from the data directory and transforms
    it from CSV format to a list of lists suitable for display
    in a data table component.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")

    Returns
    -------
    tuple[list[str], list[list[str]]]
        A tuple containing:
        - Column headers as a list of strings
        - Table rows as a list of lists, where each inner list represents
          one row with [behandeling, prijs]
    """
    data_path = (
        Path(__file__).parent.parent.parent
        / "data"
        / "reimbursements"
        / "pricing_2025.csv"
    )

    with open(data_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    columns = rows[0]
    data_rows = [row for row in rows[1:] if row and row[0].strip()]

    return columns, data_rows


def section_pricing_table(language: str) -> rx.Component:
    """
    Create the pricing table section.

    Displays a comprehensive, searchable table of VoorVoet's treatment
    prices for 2025. The table includes built-in search, sort, and
    pagination functionality for easy navigation. Features alternating
    row colors (white and light green) for better readability.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")

    Returns
    -------
    rx.Component
        A section component containing a data table with pricing
        information and a note about the pricing.
    """
    columns, data = load_pricing_data()

    table_styles = {
        ".gridjs-th": {
            "background-color": f"{Colors.primary['500']} !important",
            "color": f"{Colors.text['white']} !important",
            "font-weight": "600",
            "white-space": "normal !important",
        },
        ".gridjs-th .gridjs-th-content": {
            "color": f"{Colors.text['white']} !important",
        },
        ".gridjs-th:nth-child(1)": {
            "background-color": f"{Colors.primary['500']} !important",
        },
        ".gridjs-th:nth-child(2)": {
            "background-color": f"{Colors.primary['500']} !important",
        },
        "tr:nth-of-type(even) td": {
            "background": Colors.backgrounds["white"],
        },
        "tr:nth-of-type(odd) td": {
            "background": Colors.backgrounds["green_light"],
        },
        ".gridjs-wrapper": {
            "overflow-x": "auto",
            "box-shadow": "inset -10px 0 8px -8px rgba(0,0,0,0.15)",
        },
        ".gridjs-td": {
            "white-space": "normal !important",
            "word-wrap": "break-word !important",
            "line-height": "1.4",
        },
        ".gridjs-th:nth-child(1), td:nth-child(1)": {
            "min-width": "150px",
        },
        ".gridjs-th:nth-child(2), td:nth-child(2)": {
            "min-width": "140px",
            "width": "140px",
        },
        "@media (max-width: 640px)": {
            ".gridjs-th:nth-child(1), td:nth-child(1)": {
                "min-width": "110px",
            },
        },
    }

    return section(
        container(
            rx.text(
                get_translation(TRANSLATIONS, "title", language),
                font_size=FontSizes.section_sub_title,
                font_weight="700",
                color=Colors.text["subheading"],
            ),
            rx.text(
                get_translation(TRANSLATIONS, "intro", language),
                rx.link(
                    get_translation(TRANSLATIONS, "pdf_link", language),
                    href="/documents/voorvoet_praktijk_voor_podotherapie_tarieven_2025.pdf",
                    color=Colors.text["link"],
                    text_decoration="underline",
                    is_external=True,
                ),
                ".",
                color=Colors.text["content"],
                font_size="1.125rem",
                margin_bottom="1rem",
            ),
            rx.box(
                rx.data_table(
                    data=data,
                    columns=columns,
                    search=False,
                    sort=True,
                    pagination=False,
                    resizable=False,
                ),
                width="100%",
                max_width="800px",
                margin_x="auto",
                margin_top="2rem",
                margin_bottom="2rem",
                style=table_styles,
            ),
            rx.box(
                rx.text(
                    get_translation(TRANSLATIONS, "disclaimer", language),
                    color=Colors.text["muted"],
                    font_size="16px",
                    font_style="italic",
                ),
                margin_top="1.5rem",
            ),
        ),
        background=Colors.backgrounds["white"],
        padding_y="3rem",
    )
