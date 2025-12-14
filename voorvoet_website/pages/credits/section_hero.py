"""Hero section for the credits page."""

import reflex as rx

from ...theme import Colors, ImageDimensions
from ...components import section, hero_banner
from ...utils.get_translation import get_translation


TRANSLATIONS = {
    "nl": {
        "hero_image_alt": "Credits - VoorVoet podotherapie",
    },
    "de": {
        "hero_image_alt": "Credits - VoorVoet Podotherapie",
    },
    "en": {
        "hero_image_alt": "Credits - VoorVoet Podiatry",
    },
}


def section_hero(language: str) -> rx.Component:
    """
    Create the credits page hero section with background image.

    Parameters
    ----------
    language : str
        The current language code (nl, de, or en).

    Returns
    -------
    rx.Component
        A section component containing a hero banner with background image.
    """
    return section(
        hero_banner(
            image_src_fallback="/images/page_credits/credits_hero_banner.jpg",
            image_src_avif="/images/page_credits/credits_hero_banner.avif",
            image_src_webp="/images/page_credits/credits_hero_banner.webp",
            alt_text=get_translation(TRANSLATIONS, "hero_image_alt", language),
            dimensions=ImageDimensions.hero_banner,
            gradient="linear-gradient(180deg, rgba(255,255,255,.55) 0%, rgba(16,185,129,.35) 100%)",
            content=None,
        ),
        padding_top="0",
        position="relative",
        height="400px",
        clip_bottom="gentle_2",
        divider_color=Colors.backgrounds["white"],
    )
