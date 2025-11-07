"""Hero call-to-action box component for appointment booking."""
import reflex as rx
from ...components import button, section_sub_title, icon_list_item
from ...theme import Colors
from ...config import config
from ...utils.translations import get_translation


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


def hero_cta_box() -> rx.Component:
    """
    Create a call-to-action box for the hero section.

    The CTA box displays a title, list of benefits (no referral needed,
    quick professional help, fastest route to specialist), and a button
    to book an appointment. The box has a light green background with
    rounded corners and shadow.

    Returns
    -------
    rx.Component
        A styled box component containing the CTA content with title,
        benefit list, and appointment booking button.
    """
    return rx.box(
        rx.vstack(
            section_sub_title(get_translation(TRANSLATIONS, "cta_title"), text_align="center"),
            rx.box(
                rx.vstack(
                    icon_list_item("fa-check-square-o", get_translation(TRANSLATIONS, "no_referral")),
                    icon_list_item("fa-check-square-o", get_translation(TRANSLATIONS, "quick_help")),
                    icon_list_item("fa-check-square-o", get_translation(TRANSLATIONS, "fastest_route")),
                    spacing="3",
                    align="start",
                ),
                width="100%",
                display="flex",
                justify_content="center"
            ),
            rx.box(
                button(get_translation(TRANSLATIONS, "make_appointment"), href=config.link_plan_portal),
                width="100%",
                display="flex",
                justify_content="center"
            ),
            spacing="4",
            align="center",
        ),
        width=["95%", "28rem", "32rem", "36rem"],
        max_width=["95%", "90%", "85%", "38rem"],
        bg=Colors.backgrounds["green_light"],
        border_radius="0.75rem",
        padding=["1rem", "1.5rem", "1.75rem", "2rem"],
        box_shadow="0 6px 18px rgba(0,0,0,.12)",
        backdrop_filter="saturate(1.05) blur(1px)",
        margin_left=["auto", "auto", "auto", "auto"],
        margin_right=["auto", "20px", "20px", "20px"],
    )
