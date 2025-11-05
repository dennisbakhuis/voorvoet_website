"""Section displaying insurance reimbursement information in a searchable table."""
import reflex as rx
import json
from pathlib import Path

from ...theme import Colors
from ...components import section, container, section_title


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
        "tr:nth-of-type(even) td": {
            "background": Colors.backgrounds["white"],
        },
        "tr:nth-of-type(odd) td": {
            "background": Colors.backgrounds["green_light"],
        },
    }

    return section(
        container(
            section_title("Overzicht Vergoedingen 2025"),

            rx.box(
                rx.data_table(
                    data=data,
                    columns=columns,
                    search=True,
                    sort=True,
                    pagination=True,
                    resizable=True,
                ),
                width="100%",
                margin_top="2rem",
                margin_bottom="2rem",
                style=table_styles,
            ),

            rx.box(
                rx.text(
                    "Let op: Deze informatie is indicatief. Controleer altijd de exacte voorwaarden bij uw zorgverzekeraar.",
                    color=Colors.text["muted"],
                    font_size="16px",
                    font_style="italic",
                ),
                margin_top="1.5rem",
            ),
        ),
        background=Colors.backgrounds["white"],
        padding_y="4rem",
    )
