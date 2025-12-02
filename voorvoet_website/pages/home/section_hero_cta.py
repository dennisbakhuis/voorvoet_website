"""Hero call-to-action box component for appointment booking."""

import reflex as rx
from ...components import button, header, icon_list_item
from ...theme import Colors, Layout, Spacing
from ...config import config
from ...utils.get_translation import get_translation


TRANSLATIONS = {
    "nl": {
        "cta_title": "Maak direct digitaal een afspraak!",
        "no_referral": "Geen verwijzing nodig!",
        "quick_help": "Snel geholpen door een professional.",
        "fastest_route": "Snelste weg naar de specialist!",
        "make_appointment": "Maak een afspraak",
    },
    "de": {
        "cta_title": "Vereinbaren Sie sofort online einen Termin!",
        "no_referral": "Keine Überweisung erforderlich!",
        "quick_help": "Schnelle Hilfe durch einen Fachmann.",
        "fastest_route": "Schnellster Weg zum Spezialisten!",
        "make_appointment": "Termin vereinbaren",
    },
    "en": {
        "cta_title": "Make an appointment online right away!",
        "no_referral": "No referral needed!",
        "quick_help": "Quick help from a professional.",
        "fastest_route": "Fastest route to the specialist!",
        "make_appointment": "Make an appointment",
    },
}


def hero_cta_box(language: str) -> rx.Component:
    """
    Create a call-to-action box for the hero section.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")

    Returns
    -------
    rx.Component
        A styled box component containing the CTA content with title,
        benefit list, and appointment booking button.
    """
    return rx.box(
        rx.vstack(
            header(
                get_translation(TRANSLATIONS, "cta_title", language),
                level=3,
                text_align="center",
            ),
            rx.box(
                rx.vstack(
                    icon_list_item(
                        "fa-check-square-o",
                        get_translation(TRANSLATIONS, "no_referral", language),
                    ),
                    icon_list_item(
                        "fa-check-square-o",
                        get_translation(TRANSLATIONS, "quick_help", language),
                    ),
                    icon_list_item(
                        "fa-check-square-o",
                        get_translation(TRANSLATIONS, "fastest_route", language),
                    ),
                    spacing="3",
                    align="start",
                ),
                width="100%",
                display="flex",
                justify_content="center",
            ),
            rx.box(
                button(
                    get_translation(TRANSLATIONS, "make_appointment", language),
                    href=config.link_plan_portal,
                ),
                width="100%",
                display="flex",
                justify_content="center",
            ),
            spacing="4",
            align="center",
        ),
        width=Layout.hero_cta_width,
        max_width=Layout.hero_cta_max_width,
        bg=Colors.backgrounds["green_light"],
        border_radius="0.75rem",
        padding=Spacing.hero_cta_padding,
        box_shadow="0 6px 18px rgba(0,0,0,.12)",
        backdrop_filter="saturate(1.05) blur(1px)",
        margin_left=["auto", "auto", "auto", "auto"],
        margin_right=["auto", "auto", "1.25rem", "1.25rem"],
    )
