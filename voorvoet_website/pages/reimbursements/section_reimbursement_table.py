import reflex as rx
import json
from pathlib import Path

from ...theme import Colors
from ...components import section, container, section_title


def load_reimbursement_data() -> tuple[list[str], list[list[str]]]:
    """Load reimbursement data from JSON file and convert to list of lists"""
    data_path = Path(__file__).parent.parent.parent / "data" / "vergoedingen_2025.json"
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Define column headers
    columns = ["Verzekeraar", "Pakket", "Vergoeding"]

    # Convert remaining rows from dict to list format
    rows = [
        [item["verzekeraar"], item["pakket"], item["vergoeding"]]
        for item in data[1:]
    ]

    return columns, rows


def section_reimbursement_table() -> rx.Component:
    """Section displaying the reimbursement table with search functionality"""

    # Load the data
    columns, data = load_reimbursement_data()

    # Custom CSS for the data table
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

            # Data table with built-in search, sort, and pagination
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

            # Note below table
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
