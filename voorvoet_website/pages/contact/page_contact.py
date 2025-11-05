"""Contact page composition with all sections."""
import reflex as rx

from .section_hero import section_hero
from .section_starter import section_starter
from .section_contact_form import section_contact_form

from ..shared_sections import footer, header
from ...components import toast, modal
from ...state import WebsiteState


def page_contact() -> rx.Component:
    """
    Create the complete contact page with all sections.

    The contact page is composed of: header, hero banner, starter text,
    contact form, footer, modal, and toast notification components.

    Returns
    -------
    rx.Component
        A fragment containing all sections of the contact page in order.
    """
    return rx.fragment(
        header(),
        section_hero(),
        section_contact_form(),

        footer(),
        modal(),
        toast(),
    )
