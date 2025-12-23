"""Order insoles page composition with all sections."""

import reflex as rx

from .section_hero import section_hero
from .section_starter import section_starter
from .section_order_form import section_order_form

from ..shared_sections import footer, header
from ...components import toast, breadcrumb_schema
from ...translations import BREADCRUMB_NAMES
from ...config import config
from ...models.pricing import PricingData


def page_order_insoles(language: str, pricing: PricingData) -> rx.Component:
    """
    Create the complete order insoles page with all sections.

    The order insoles page is composed of: header, hero banner, starter text,
    order form, footer, and toast notification components.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")
    pricing : PricingData
        Pricing data loaded at app startup

    Returns
    -------
    rx.Component
        A fragment containing all sections of the order insoles page in order.
    """
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
        rx.box(
            section_hero(language),
            section_starter(language, pricing),
            section_order_form(language),
            id="main-content",
            role="main",
        ),
        footer(language),
        toast(),
    )
