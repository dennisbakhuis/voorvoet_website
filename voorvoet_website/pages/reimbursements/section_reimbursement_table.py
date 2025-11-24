"""Section displaying insurance reimbursement information in a searchable table."""
import reflex as rx
import json
from pathlib import Path

from ...theme import Colors, FontSizes
from ...components import section, container
from ...utils.translations import get_translation
from ...states import WebsiteState


TRANSLATIONS = {
    "nl": {
        "title": "Vergoedingen zorgverzekeraars",
        "intro_part1": "We willen graag allemaal weten waar we aan toe zijn. Daarom heeft de ",
        "link_text": "Nederlandse Vereniging van Podotherapeuten (NVvP)",
        "intro_part2": " een overzicht gemaakt van vergoedingen van zo goed als alle zorgpakketten van Nederlandse zorgverzekeraars. Podotherapie wordt meestal vergoed vanuit een aanvullend zorgpakket. Een verwijzing van de huisarts is meestal niet nodig.",
        "intro_part3": "Hieronder is een kleine web-applicatie met zo goed als alle zorgverzekeraars. Type boven in de zoekbalk je verzekering in en zie direct wat er voor podotherapie wordt vergoedt vanuit jouw verzekering!",
        "search_placeholder": "Typ om te zoeken...",
        "sort_asc": "Kolom oplopend sorteren",
        "sort_desc": "Kolom aflopend sorteren",
        "previous": "Vorige",
        "next": "Volgende",
        "showing": "Tonen",
        "of": "van",
        "to": "tot",
        "results": "resultaten",
        "loading": "Laden...",
        "no_records": "Geen resultaten gevonden",
        "error": "Er is een fout opgetreden bij het ophalen van de gegevens",
        "disclaimer": "De lijst wordt met grootste zorg door de NVvP samengesteld en VoorVoet - Praktijk voor podotherapie neemt deze lijst zo goed als mogelijk over. Mochten er echter toch onverhoopt onjuistheden of fouten optreden dan kunnen zowel de NVvP als VoorVoet - Praktijk voor podotherapie niet aansprakelijk worden gesteld. Aan de inhoud van deze pagina's en eventueel toegevoegde bijlagen kunnen geen rechten worden ontleend.",
    },
    "de": {
        "title": "Versicherungserstattungen",
        "intro_part1": "Wir alle möchten wissen, woran wir sind. Deshalb hat die ",
        "link_text": "Niederländische Vereinigung der Podotherapeuten (NVvP)",
        "intro_part2": " eine Übersicht über Erstattungen für fast alle Pflegepakete niederländischer Krankenversicherungen erstellt. Podotherapie wird normalerweise aus einer Zusatzversicherung erstattet. Eine Überweisung des Hausarztes ist normalerweise nicht erforderlich.",
        "intro_part3": "Unten finden Sie eine kleine Web-Anwendung mit fast allen Krankenversicherungen. Geben Sie Ihre Versicherung in die Suchleiste ein und sehen Sie direkt, was für Podotherapie aus Ihrer Versicherung erstattet wird!",
        "search_placeholder": "Zum Suchen tippen...",
        "sort_asc": "Spalte aufsteigend sortieren",
        "sort_desc": "Spalte absteigend sortieren",
        "previous": "Zurück",
        "next": "Weiter",
        "showing": "Anzeigen",
        "of": "von",
        "to": "bis",
        "results": "Ergebnisse",
        "loading": "Lädt...",
        "no_records": "Keine Ergebnisse gefunden",
        "error": "Beim Abrufen der Daten ist ein Fehler aufgetreten",
        "disclaimer": "Die Liste wird mit größter Sorgfalt von der NVvP zusammengestellt und VoorVoet - Praxis für Podotherapie übernimmt diese Liste so gut wie möglich. Sollten dennoch Ungenauigkeiten oder Fehler auftreten, können weder die NVvP noch VoorVoet - Praxis für Podotherapie haftbar gemacht werden. Aus dem Inhalt dieser Seiten und eventuell beigefügten Anhängen können keine Rechte abgeleitet werden.",
    },
    "en": {
        "title": "Insurance Reimbursements",
        "intro_part1": "We all want to know where we stand. That's why the ",
        "link_text": "Dutch Association of Podotherapists (NVvP)",
        "intro_part2": " has created an overview of reimbursements for almost all care packages from Dutch health insurers. Podotherapy is usually reimbursed from a supplementary insurance package. A referral from your GP is usually not required.",
        "intro_part3": "Below is a small web application with almost all health insurers. Type your insurance in the search bar and see directly what is reimbursed for podotherapy from your insurance!",
        "search_placeholder": "Type to search...",
        "sort_asc": "Sort column ascending",
        "sort_desc": "Sort column descending",
        "previous": "Previous",
        "next": "Next",
        "showing": "Showing",
        "of": "of",
        "to": "to",
        "results": "results",
        "loading": "Loading...",
        "no_records": "No results found",
        "error": "An error occurred while fetching the data",
        "disclaimer": "The list is compiled with the greatest care by the NVvP and VoorVoet - Practice for Podotherapy adopts this list as closely as possible. However, should inaccuracies or errors occur, neither the NVvP nor VoorVoet - Practice for Podotherapy can be held liable. No rights can be derived from the content of these pages and any attached appendices.",
    },
}


def load_reimbursement_data() -> tuple[list[str], list[list[str]]]:
    """
    Load reimbursement data from JSON file and convert to table format.

    Reads the 2025 reimbursement data from the data directory and transforms
    it from JSON dictionary format to a list of lists suitable for display
    in a data table component.

    Returns
    -------
    tuple[list[str], list[list[str]]]
        A tuple containing:
        - Column headers as a list of strings
        - Table rows as a list of lists, where each inner list represents
          one row with [verzekeraar, pakket, vergoeding]
    """
    data_path = Path(__file__).parent.parent.parent / "data" / "reimbursements" / "reimbursements_2025.json"
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    columns = ["Verzekeraar", "Pakket", "Vergoeding"]

    rows = [
        [item["verzekeraar"], item["pakket"], item["vergoeding"]]
        for item in data[1:]
    ]

    return columns, rows


def section_reimbursement_table() -> rx.Component:
    """
    Create the reimbursement table section.

    Displays a comprehensive, searchable table of insurance providers
    and their reimbursement amounts for podiatry services in 2025.
    The table includes built-in search, sort, and pagination functionality
    for easy navigation. Features alternating row colors (white and light
    green) for better readability.

    Returns
    -------
    rx.Component
        A section component containing a data table with insurance
        reimbursement information and a disclaimer note.
    """
    columns, data = load_reimbursement_data()

    table_styles = {
        ".gridjs-th": {
            "background-color": f"{Colors.primary['500']} !important",
            "color": f"{Colors.text['white']} !important",
            "font-weight": "600",
        },
        ".gridjs-th .gridjs-th-content": {
            "color": f"{Colors.text['white']} !important",
        },
        ".gridjs-th:nth-child(2)": {
            "background-color": f"{Colors.primary['500']} !important",
            "color": f"{Colors.text['white']} !important",
        },
        ".gridjs-th:nth-child(2) .gridjs-th-content": {
            "color": f"{Colors.text['white']} !important",
        },
        ".gridjs-th:nth-child(3)": {
            "background-color": f"{Colors.primary['500']} !important",
            "color": f"{Colors.text['white']} !important",
        },
        ".gridjs-th:nth-child(3) .gridjs-th-content": {
            "color": f"{Colors.text['white']} !important",
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
        ".gridjs-th:nth-child(1)": {
            "position": "sticky",
            "left": "0",
            "z-index": "10",
            "background-color": f"{Colors.primary['500']} !important",
            "color": f"{Colors.text['white']} !important",
        },
        ".gridjs-th:nth-child(1) .gridjs-th-content": {
            "color": f"{Colors.text['white']} !important",
        },
        "td:nth-child(1)": {
            "position": "sticky",
            "left": "0",
            "z-index": "5",
        },
        "tr:nth-of-type(even) td:nth-child(1)": {
            "background": Colors.backgrounds["white"],
        },
        "tr:nth-of-type(odd) td:nth-child(1)": {
            "background": Colors.backgrounds["green_light"],
        },
        ".gridjs-td": {
            "white-space": "normal !important",
            "word-wrap": "break-word !important",
            "line-height": "1.4",
        },
        ".gridjs-th": {
            "white-space": "normal !important",
        },
        ".gridjs-th:nth-child(1), td:nth-child(1)": {
            "min-width": "150px",
        },
        ".gridjs-th:nth-child(2), td:nth-child(2)": {
            "min-width": "120px",
        },
        ".gridjs-th:nth-child(3), td:nth-child(3)": {
            "min-width": "250px",
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
                get_translation(TRANSLATIONS, "title"),
                font_size=FontSizes.section_sub_title,
                font_weight="700",
                color=Colors.text["subheading"],
            ),
            rx.box(
                rx.text(
                    get_translation(TRANSLATIONS, "intro_part1"),
                    rx.link(
                        get_translation(TRANSLATIONS, "link_text"),
                        href="https://www.podotherapie.nl/vergoedingen/",
                        color=Colors.text["link"],
                        text_decoration="underline",
                        is_external=True,
                    ),
                    get_translation(TRANSLATIONS, "intro_part2"),
                    color=Colors.text["content"],
                    font_size="1.125rem",
                    margin_bottom="1rem",
                ),
                rx.text(
                    get_translation(TRANSLATIONS, "intro_part3"),
                    color=Colors.text["content"],
                    font_size="1.125rem",
                    margin_bottom="1rem",
                ),
            ),

            rx.box(
                rx.cond(
                    WebsiteState.current_language == "nl",
                    rx.data_table(
                        data=data,
                        columns=columns,
                        search=True,
                        sort=True,
                        pagination={"limit": 12},
                        resizable=False,
                        custom_attrs={
                            "language": {
                                "search": {"placeholder": "Typ om te zoeken..."},
                                "sort": {"sortAsc": "Kolom oplopend sorteren", "sortDesc": "Kolom aflopend sorteren"},
                                "pagination": {"previous": "Vorige", "next": "Volgende", "showing": "Tonen", "of": "van", "to": "tot", "results": "resultaten"},
                                "loading": "Laden...",
                                "noRecordsFound": "Geen resultaten gevonden",
                                "error": "Er is een fout opgetreden bij het ophalen van de gegevens"
                            }
                        },
                    ),
                    rx.cond(
                        WebsiteState.current_language == "de",
                        rx.data_table(
                            data=data,
                            columns=columns,
                            search=True,
                            sort=True,
                            pagination={"limit": 12},
                            resizable=False,
                            custom_attrs={
                                "language": {
                                    "search": {"placeholder": "Zum Suchen tippen..."},
                                    "sort": {"sortAsc": "Spalte aufsteigend sortieren", "sortDesc": "Spalte absteigend sortieren"},
                                    "pagination": {"previous": "Zurück", "next": "Weiter", "showing": "Anzeigen", "of": "von", "to": "bis", "results": "Ergebnisse"},
                                    "loading": "Lädt...",
                                    "noRecordsFound": "Keine Ergebnisse gefunden",
                                    "error": "Beim Abrufen der Daten ist ein Fehler aufgetreten"
                                }
                            },
                        ),
                        rx.data_table(
                            data=data,
                            columns=columns,
                            search=True,
                            sort=True,
                            pagination={"limit": 12},
                            resizable=False,
                            custom_attrs={
                                "language": {
                                    "search": {"placeholder": "Type to search..."},
                                    "sort": {"sortAsc": "Sort column ascending", "sortDesc": "Sort column descending"},
                                    "pagination": {"previous": "Previous", "next": "Next", "showing": "Showing", "of": "of", "to": "to", "results": "results"},
                                    "loading": "Loading...",
                                    "noRecordsFound": "No results found",
                                    "error": "An error occurred while fetching the data"
                                }
                            },
                        ),
                    ),
                ),
                width="100%",
                margin_top="2rem",
                margin_bottom="2rem",
                style=table_styles,
            ),

            rx.box(
                rx.text(
                    get_translation(TRANSLATIONS, "disclaimer"),
                    color=Colors.text["muted"],
                    font_size="16px",
                    font_style="italic",
                ),
                margin_top="1.5rem",
            ),
        ),
        background=Colors.backgrounds["white"],
        padding_y="1rem",
    )
