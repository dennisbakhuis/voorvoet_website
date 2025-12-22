"""Starter section introducing the order insoles page purpose."""

import reflex as rx

from ...theme import Colors
from ...components import section, container, header, regular_text
from ...utils import get_translation
from ...models.pricing import PricingData
from ...services.pricing_service import get_price_formatted


def section_starter(language: str, pricing: PricingData) -> rx.Component:
    """
    Create the order insoles page starter section with pricing information.

    This section provides pricing information for ordering extra pairs of
    orthopedic insoles with prices loaded from the centralized pricing data.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")
    pricing : PricingData
        Pricing data loaded at app startup

    Returns
    -------
    rx.Component
        A section component with centered title and pricing information
        on a white background with vertical padding.
    """
    price_extra = get_price_formatted(pricing, "Podotherapeutische zolen extra paar")
    price_workshoes = get_price_formatted(
        pricing, "Podotherapeutische zolen extra paar voor werkschoenen"
    )

    translations = {
        "nl": {
            "title": "Bestel zolen",
            "pricing_info": f"Extra paar podotherapeutische zolen: {price_extra} per paar.",
            "pricing_workshoes": f"Extra paar voor werkschoenen: {price_workshoes} per paar.",
            "pricing_link": "Kijk voor alle tarieven op onze tarievenlijst.",
            "terms": "Indien mogelijk dienen wij de factuur in bij uw zorgverzekeraar. Anders zult u de factuur van ons thuis ontvangen en dient u het bedrag binnen 14 dagen aan ons over te maken. Als u op de bestelknop drukt gaat u akkoord met onze algemene voorwaarden.",
        },
        "de": {
            "title": "Einlagen bestellen",
            "pricing_info": f"Zusätzliches Paar podotherapeutische Einlagen: {price_extra} pro Paar.",
            "pricing_workshoes": f"Zusätzliches Paar für Arbeitsschuhe: {price_workshoes} pro Paar.",
            "pricing_link": "Alle Tarife finden Sie in unserer Preisliste.",
            "terms": "Wenn möglich reichen wir die Rechnung bei Ihrer Krankenkasse ein. Andernfalls erhalten Sie die Rechnung von uns zu Hause und müssen den Betrag innerhalb von 14 Tagen an uns überweisen. Mit dem Klicken auf die Bestellschaltfläche stimmen Sie unseren Allgemeinen Geschäftsbedingungen zu.",
        },
        "en": {
            "title": "Order insoles",
            "pricing_info": f"Extra pair of podotherapeutic insoles: {price_extra} per pair.",
            "pricing_workshoes": f"Extra pair for work shoes: {price_workshoes} per pair.",
            "pricing_link": "See our price list for all rates.",
            "terms": "If possible, we will submit the invoice to your health insurance company. Otherwise, you will receive the invoice from us at home and must transfer the amount to us within 14 days. By clicking the order button, you agree to our terms and conditions.",
        },
    }

    return section(
        container(
            header(
                get_translation(translations, "title", language),
                level=1,
            ),
            rx.box(
                regular_text(
                    get_translation(translations, "pricing_info", language),
                    color=Colors.text["content"],
                    margin_bottom="0.5rem",
                ),
                regular_text(
                    get_translation(translations, "pricing_workshoes", language),
                    color=Colors.text["content"],
                    margin_bottom="0.5rem",
                ),
                regular_text(
                    get_translation(translations, "pricing_link", language),
                    color=Colors.text["content"],
                    margin_bottom="1.5rem",
                ),
                regular_text(
                    get_translation(translations, "terms", language),
                    color=Colors.text["content"],
                    font_style="italic",
                ),
                margin_top="1.5rem",
            ),
        ),
        background=Colors.backgrounds["white"],
        padding_y="3rem",
    )
