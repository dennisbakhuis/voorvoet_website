"""Hero section for the blog page."""

import reflex as rx

from ...theme import Colors
from ...components import section, hero_banner
from ...utils.get_translation import get_translation


TRANSLATIONS = {
    "nl": {
        "hero_image_alt": "Gezonde blote voeten bij zwembad - sandalen met uitneembaar voetbed voor steunzolen",
    },
    "de": {
        "hero_image_alt": "Gesunde nackte Füße am Pool - Sandalen mit herausnehmbarem Fußbett für Einlagen",
    },
    "en": {
        "hero_image_alt": "Healthy bare feet by pool - sandals with removable footbed for insoles",
    },
}


def section_hero(language: str) -> rx.Component:
    """
    Create the blog page hero section with background image.

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
            image_src_fallback="/images/page_blog/voorvoet_praktijk_voor_podotherapie_Sandalen_Durea_modern_uitneembaar_voetbed_steunzolen_op_maat_gezonde_blote_voeten_bij_zwembad.jpg",
            image_src_avif="/images/page_blog/voorvoet_praktijk_voor_podotherapie_Sandalen_Durea_modern_uitneembaar_voetbed_steunzolen_op_maat_gezonde_blote_voeten_bij_zwembad.avif",
            image_src_webp="/images/page_blog/voorvoet_praktijk_voor_podotherapie_Sandalen_Durea_modern_uitneembaar_voetbed_steunzolen_op_maat_gezonde_blote_voeten_bij_zwembad.webp",
            alt_text=get_translation(TRANSLATIONS, "hero_image_alt", language),
            gradient="linear-gradient(270deg, rgba(255,255,255,.55) 0%, rgba(16,185,129,.35) 100%)",
            content=None,
        ),
        padding_top="0",
        position="relative",
        height="500px",
        clip_bottom="gentle_1",
        divider_color=Colors.backgrounds["white"],
    )
