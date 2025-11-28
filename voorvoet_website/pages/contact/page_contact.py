"""Contact page composition with all sections."""
import reflex as rx

from .section_hero import section_hero
from .section_starter import section_starter
from .section_contact_form import section_contact_form

from ..shared_sections import footer, header
from ...components import toast


def page_contact(language: str="nl") -> rx.Component:
    """
    Create the complete contact page with all sections.

    The contact page is composed of: header, hero banner, starter text,
    contact form, footer, and toast notification components.

    Returns
    -------
    rx.Component
        A fragment containing all sections of the contact page in order.
    """
    return rx.fragment(
        header(language, page_key="contact"),
        section_hero(),
        section_starter(language),
        section_contact_form(language),
        footer(language),
        toast(),
    )
