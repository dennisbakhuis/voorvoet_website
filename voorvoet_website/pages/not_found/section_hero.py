"""Hero section for the 404 not found page."""

import reflex as rx

from ...theme import Colors, ImageDimensions
from ...components import section, hero_banner


TRANSLATIONS = {
    "nl": {
        "hero_image_alt": "Pagina niet gevonden - VoorVoet podotherapie",
    },
}


def section_hero() -> rx.Component:
    """
    Create the 404 page hero section with background image.

    Returns
    -------
    rx.Component
        A section component containing a hero banner with background image.
    """
    return section(
        hero_banner(
            image_src_fallback="/images/page_not_found/404_not_found_voorvoet.jpg",
            image_src_avif="/images/page_not_found/404_not_found_voorvoet.avif",
            image_src_webp="/images/page_not_found/404_not_found_voorvoet.webp",
            alt_text=TRANSLATIONS["nl"]["hero_image_alt"],
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
