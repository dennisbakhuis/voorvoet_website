"""Introductory text section for the reimbursements page."""

import reflex as rx

from ...theme import Colors
from ...components import section, container, header, regular_text
from ...utils import get_translation


TRANSLATIONS = {
    "nl": {
        "title": "Vergoedingen en tarieven 2025",
        "intro": "Op deze pagina is een overzicht te vinden van de mogelijke vergoedingen van zorgverzekeraars en de tarieven die VoorVoet - Praktijk voor podotherapie hanteert.",
    },
    "de": {
        "title": "Erstattungen und Tarife 2025",
        "intro": "Auf dieser Seite finden Sie eine Übersicht über die möglichen Erstattungen von Krankenversicherungen und die Tarife, die VoorVoet - Praxis für Podotherapie anwendet.",
    },
    "en": {
        "title": "Reimbursements and Rates 2025",
        "intro": "On this page you can find an overview of possible reimbursements from health insurers and the rates that VoorVoet - Practice for Podotherapy applies.",
    },
}


def section_starter(language: str) -> rx.Component:
    """
    Create the introductory section for the reimbursements page.

    Displays a welcoming title and introductory text explaining that
    podiatry is often covered by health insurance and directing visitors
    to the comprehensive information below about reimbursements, costs,
    and what to expect during treatment.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")

    Returns
    -------
    rx.Component
        A section component with white background containing the title
        and introductory text about insurance coverage and costs.
    """
    return section(
        container(
            header(
                get_translation(TRANSLATIONS, "title", language),
                level=1,
                margin_bottom="1rem",
            ),
            regular_text(
                get_translation(TRANSLATIONS, "intro", language),
                color=Colors.text["content"],
            ),
        ),
        background=Colors.backgrounds["white"],
        padding_y="2rem",
    )
