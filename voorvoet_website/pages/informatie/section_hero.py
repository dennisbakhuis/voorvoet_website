"""Hero section for the information page."""

import reflex as rx

from ...theme import Colors
from ...components import section, hero_banner
from ...utils.get_translation import get_translation


TRANSLATIONS = {
    "nl": {
        "hero_image_alt": "Wandeling in het bos zonder hielpijn dankzij podotherapie",
    },
    "de": {
        "hero_image_alt": "Waldspaziergang ohne Fersenschmerzen dank Podotherapie",
    },
    "en": {
        "hero_image_alt": "Forest walk without heel pain thanks to podotherapy",
    },
}


def section_hero(language: str) -> rx.Component:
    """
    Create the information page hero section with background image.

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
            image_src_fallback="/images/page_information/podotherapie_enschede_wandeling_in_het_bos_zonder_hielpijn_voorvoet_podotherapie_enschede.jpg",
            image_src_avif="/images/page_information/podotherapie_enschede_wandeling_in_het_bos_zonder_hielpijn_voorvoet_podotherapie_enschede.avif",
            image_src_webp="/images/page_information/podotherapie_enschede_wandeling_in_het_bos_zonder_hielpijn_voorvoet_podotherapie_enschede.webp",
            alt_text=get_translation(TRANSLATIONS, "hero_image_alt", language),
            gradient="linear-gradient(270deg, rgba(255,255,255,.35) 0%, rgba(16,185,129,.35) 100%)",
            content=None,
        ),
        background_color=Colors.backgrounds["green_light"],
        padding_top="0",
        position="relative",
        height="500px",
        clip_bottom="gentle_3",
        divider_color=Colors.backgrounds["white"],
    )
