"""Hero section for the contact page."""

import reflex as rx

from ...theme import Colors
from ...components import section, hero_banner
from ...utils.get_translation import get_translation


TRANSLATIONS = {
    "nl": {
        "hero_image_alt": "Voetklachten en zere voeten - neem contact op met VoorVoet",
    },
    "de": {
        "hero_image_alt": "Fußbeschwerden und schmerzende Füße - kontaktieren Sie VoorVoet",
    },
    "en": {
        "hero_image_alt": "Foot complaints and sore feet - contact VoorVoet",
    },
}


def section_hero(language: str) -> rx.Component:
    """
    Create the contact page hero section with background image.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")

    Returns
    -------
    rx.Component
        A section component containing a hero banner with only the
        background image and gradient overlay.
    """
    return section(
        hero_banner(
            image_src=[
                "/images/page_contact/voetklachten_enschede_zere_voeten_voorvoet_contact.avif",
                "/images/page_contact/voetklachten_enschede_zere_voeten_voorvoet_contact.webp",
                "/images/page_contact/voetklachten_enschede_zere_voeten_voorvoet_contact.jpg",
            ],
            alt_text=get_translation(TRANSLATIONS, "hero_image_alt", language),
            gradient="linear-gradient(270deg, rgba(255,255,255,.55) 0%, rgba(16,185,129,.35) 100%)",
            content=None,
        ),
        padding_top="0",
        position="relative",
        height="500px",
        clip_bottom="gentle_2",
        divider_color=Colors.backgrounds["white"],
    )
