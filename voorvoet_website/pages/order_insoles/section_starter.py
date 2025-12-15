"""Starter section introducing the order insoles page purpose."""

import reflex as rx

from ...theme import Colors
from ...components import section, container, header, regular_text
from ...utils.get_translation import get_translation


TRANSLATIONS = {
    "nl": {
        "title": "Bestel zolen",
        "pricing_title": "Bestelt u binnen 3 maanden na uw nieuwe paar zolen een extra paar?",
        "pricing_within_3m": "Dan kan dit tegen een gereduceerd tarief van € 109,50 per paar.",
        "pricing_after_3m": "Bestelt u na 3 maanden een extra paar dan zijn de kosten € 187,50 per paar.",
        "pricing_workshoes": "Let er op dat er voor werkschoen zolen een toeslag geldt van € 25,- per paar.",
        "pricing_link": "Kijk voor alle tarieven op onze tarievenlijst.",
        "terms": "Indien mogelijk dienen wij de factuur in bij uw zorgverzekeraar. Anders zult u de factuur van ons thuis ontvangen en dient u het bedrag binnen 14 dagen aan ons over te maken. Als u op de bestelknop drukt gaat u akkoord met onze algemene voorwaarden.",
    },
    "de": {
        "title": "Einlagen bestellen",
        "pricing_title": "Bestellen Sie innerhalb von 3 Monaten nach Ihrem neuen Paar Einlagen ein zusätzliches Paar?",
        "pricing_within_3m": "Dann ist dies zu einem reduzierten Tarif von € 109,50 pro Paar möglich.",
        "pricing_after_3m": "Wenn Sie nach 3 Monaten ein zusätzliches Paar bestellen, betragen die Kosten € 187,50 pro Paar.",
        "pricing_workshoes": "Beachten Sie, dass für Arbeitsschuheinlagen ein Aufpreis von € 25,- pro Paar gilt.",
        "pricing_link": "Alle Tarife finden Sie in unserer Preisliste.",
        "terms": "Wenn möglich reichen wir die Rechnung bei Ihrer Krankenkasse ein. Andernfalls erhalten Sie die Rechnung von uns zu Hause und müssen den Betrag innerhalb von 14 Tagen an uns überweisen. Mit dem Klicken auf die Bestellschaltfläche stimmen Sie unseren Allgemeinen Geschäftsbedingungen zu.",
    },
    "en": {
        "title": "Order insoles",
        "pricing_title": "Are you ordering an extra pair within 3 months of your new pair of insoles?",
        "pricing_within_3m": "Then you can do this at a reduced rate of € 109.50 per pair.",
        "pricing_after_3m": "If you order an extra pair after 3 months, the costs are € 187.50 per pair.",
        "pricing_workshoes": "Please note that for work shoe insoles there is a surcharge of € 25.- per pair.",
        "pricing_link": "See our price list for all rates.",
        "terms": "If possible, we will submit the invoice to your health insurance company. Otherwise, you will receive the invoice from us at home and must transfer the amount to us within 14 days. By clicking the order button, you agree to our terms and conditions.",
    },
}


def section_starter(language: str) -> rx.Component:
    """
    Create the order insoles page starter section with pricing information.

    This section provides pricing information for ordering extra pairs of
    orthopedic insoles, including discounts for orders within 3 months
    and terms and conditions.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")

    Returns
    -------
    rx.Component
        A section component with centered title and pricing information
        on a white background with vertical padding.
    """
    return section(
        container(
            header(
                get_translation(TRANSLATIONS, "title", language),
                level=1,
            ),
            rx.box(
                regular_text(
                    get_translation(TRANSLATIONS, "pricing_title", language),
                    color=Colors.text["content"],
                    font_weight="700",
                    margin_bottom="0.5rem",
                ),
                regular_text(
                    get_translation(TRANSLATIONS, "pricing_within_3m", language),
                    color=Colors.text["content"],
                    margin_bottom="0.5rem",
                ),
                regular_text(
                    get_translation(TRANSLATIONS, "pricing_after_3m", language),
                    color=Colors.text["content"],
                    margin_bottom="0.5rem",
                ),
                regular_text(
                    get_translation(TRANSLATIONS, "pricing_workshoes", language),
                    color=Colors.text["content"],
                    margin_bottom="0.5rem",
                ),
                regular_text(
                    get_translation(TRANSLATIONS, "pricing_link", language),
                    color=Colors.text["content"],
                    margin_bottom="1.5rem",
                ),
                regular_text(
                    get_translation(TRANSLATIONS, "terms", language),
                    color=Colors.text["content"],
                    font_style="italic",
                ),
                margin_top="1.5rem",
            ),
        ),
        background=Colors.backgrounds["white"],
        padding_y="3rem",
    )
