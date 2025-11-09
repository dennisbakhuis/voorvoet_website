"""Reimbursements page composition with all sections."""
import reflex as rx

from .section_hero import section_hero
from .section_starter import section_starter
from .section_reimbursement_table import section_reimbursement_table
from .section_pricing_table import section_pricing_table

from ..shared_sections import footer, header
from ...components import modal
from ...states import WebsiteState


def page_reimbursements() -> rx.Component:
    """
    Create the complete reimbursements page with all sections.

    The reimbursements page provides information about insurance coverage
    and costs for podiatry services, including a comprehensive searchable
    table of insurance providers and their reimbursement amounts for 2025,
    as well as VoorVoet's pricing information.

    Returns
    -------
    rx.Component
        A fragment containing all sections of the reimbursements page
        including header, hero, starter text, reimbursement table,
        pricing table, footer, and modal components.
    """
    return rx.fragment(
        header(),
        section_hero(),
        section_starter(),
        section_reimbursement_table(),
        section_pricing_table(),

        footer(),
        modal(),
    )
