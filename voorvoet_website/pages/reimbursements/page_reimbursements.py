import reflex as rx

from .section_hero import section_hero
from .section_starter import section_starter
from .section_reimbursement_table import section_reimbursement_table

from ..shared_sections import footer, header
from ...components import modal
from ...state import WebsiteState


def page_reimbursements() -> rx.Component:
    return rx.fragment(
        header(),
        section_hero(),
        section_starter(),
        section_reimbursement_table(),

        footer(),
        modal(),
    )
