"""Order insoles page composition with all sections."""

import reflex as rx

from .section_hero import section_hero
from .section_starter import section_starter
from .section_order_form import section_order_form

from ..shared_sections import footer, header
from ...components import toast, breadcrumb_schema
from ...translations import BREADCRUMB_NAMES
from ...config import config


def page_zolen_bestellen(language: str = "nl") -> rx.Component:
    """
    Create the complete zolen bestellen page with all sections.

    The zolen bestellen page is composed of: header, hero banner, starter text,
    order form, footer, and toast notification components.

    Returns
    -------
    rx.Component
        A fragment containing all sections of the zolen bestellen page in order.
    """
    # Build breadcrumb items
    breadcrumb_items = [
        {
            "name": BREADCRUMB_NAMES.get(language, {}).get("home", "Home"),
            "url": f"{config.site_url}/{language}",
        },
        {
            "name": BREADCRUMB_NAMES.get(language, {}).get(
                "order_insoles", "Order Insoles"
            ),
            "url": f"{config.site_url}/{language}/zolen-bestellen"
            if language == "nl"
            else f"{config.site_url}/{language}/einlagen-bestellen"
            if language == "de"
            else f"{config.site_url}/{language}/order-insoles",
        },
    ]

    return rx.fragment(
        breadcrumb_schema(breadcrumb_items),
        header(language, page_key="order_insoles"),
        section_hero(),
        section_starter(language),
        section_order_form(language),
        footer(language),
        toast(),
    )
