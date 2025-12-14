"""Contact page composition with all sections."""

import reflex as rx

from .section_hero import section_hero
from .section_starter import section_starter
from .section_contact_form import section_contact_form

from ..shared_sections import footer, header
from ...components import toast, breadcrumb_schema
from ...translations import BREADCRUMB_NAMES
from ...config import config


def page_contact(language: str = "nl") -> rx.Component:
    """
    Create the complete contact page with all sections.

    The contact page is composed of: header, hero banner, starter text,
    contact form, footer, and toast notification components.

    Returns
    -------
    rx.Component
        A fragment containing all sections of the contact page in order.
    """
    breadcrumb_items = [
        {
            "name": BREADCRUMB_NAMES.get(language, {}).get("home", "Home"),
            "url": f"{config.site_url}/{language}",
        },
        {
            "name": BREADCRUMB_NAMES.get(language, {}).get("contact", "Contact"),
            "url": f"{config.site_url}/{language}/contact"
            if language != "de"
            else f"{config.site_url}/{language}/kontakt",
        },
    ]

    return rx.fragment(
        breadcrumb_schema(breadcrumb_items),
        header(language, page_key="contact"),
        rx.box(
            section_hero(language),
            section_starter(language),
            section_contact_form(language),
            id="main-content",
            role="main",
        ),
        footer(language),
        toast(),
    )
