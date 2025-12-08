"""Hero section for the order insoles page."""

import reflex as rx

from ...theme import Colors
from ...components import section, hero_banner
from ...utils.get_translation import get_translation


TRANSLATIONS = {
    "nl": {
        "hero_image_alt": "Wandelschoenen met podotherapeutische steunzolen",
    },
    "de": {
        "hero_image_alt": "Wanderschuhe mit podotherapeutischen Einlagen",
    },
    "en": {
        "hero_image_alt": "Hiking shoes with podotherapeutic insoles",
    },
}


def section_hero(language: str) -> rx.Component:
    """
    Create the order insoles page hero section with background image.

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
            image_src_fallback="/images/page_order_insoles/hiking_shoes.jpg",
            image_src_avif="/images/page_order_insoles/hiking_shoes.avif",
            image_src_webp="/images/page_order_insoles/hiking_shoes.webp",
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
