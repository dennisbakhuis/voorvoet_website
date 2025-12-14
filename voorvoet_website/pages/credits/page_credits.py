"""Credits page composition with all sections."""

import reflex as rx

from .section_hero import section_hero
from .section_content import section_content

from ..shared_sections import footer, header
from ...components import breadcrumb_schema
from ...translations import BREADCRUMB_NAMES
from ...config import config


def page_credits(language: str = "nl") -> rx.Component:
    """
    Create the complete credits page with all sections.

    The credits page provides attribution for images, Python packages,
    and information about the website creator.

    Parameters
    ----------
    language : str
        The current language code (nl, de, or en).

    Returns
    -------
    rx.Component
        A fragment containing all sections of the credits page
        including header, hero, content, and footer components.
    """
    breadcrumb_items = [
        {
            "name": BREADCRUMB_NAMES.get(language, {}).get("home", "Home"),
            "url": f"{config.site_url}/{language}",
        },
        {
            "name": BREADCRUMB_NAMES.get(language, {}).get("credits", "Credits"),
            "url": f"{config.site_url}/{language}/credits",
        },
    ]

    return rx.fragment(
        breadcrumb_schema(breadcrumb_items),
        header(language, page_key="credits"),
        rx.box(
            section_hero(language),
            section_content(language),
            id="main-content",
            role="main",
        ),
        footer(language),
    )
