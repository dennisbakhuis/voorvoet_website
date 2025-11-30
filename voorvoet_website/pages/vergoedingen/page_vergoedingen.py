"""Reimbursements page composition with all sections."""

import reflex as rx

from .section_hero import section_hero
from .section_starter import section_starter
from .section_reimbursement_table import section_reimbursement_table
from .section_pricing_table import section_pricing_table

from ..shared_sections import footer, header


def page_vergoedingen(language: str = "nl") -> rx.Component:
    """
    Create the complete vergoedingen page with all sections.

    The vergoedingen page provides information about insurance coverage
    and costs for podiatry services, including a comprehensive searchable
    table of insurance providers and their reimbursement amounts for 2025,
    as well as VoorVoet's pricing information.

    Returns
    -------
    rx.Component
        A fragment containing all sections of the vergoedingen page
        including header, hero, starter text, reimbursement table,
        pricing table, footer components.
    """
    return rx.fragment(
        header(language, page_key="vergoedingen"),
        section_hero(),
        section_starter(language),
        section_reimbursement_table(language),
        section_pricing_table(language),
        footer(language),
    )
