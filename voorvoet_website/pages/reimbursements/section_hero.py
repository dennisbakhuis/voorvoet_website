"""Hero section for the reimbursements page."""

import reflex as rx

from ...theme import Colors, ImageDimensions
from ...components import section, hero_banner
from ...utils import get_translation


TRANSLATIONS = {
    "nl": {
        "hero_image_alt": "Hielpijn, hielspoor en plantaire fasciitis behandeling",
    },
    "de": {
        "hero_image_alt": "Fersenschmerzen, Fersensporn und Plantarfasziitis Behandlung",
    },
    "en": {
        "hero_image_alt": "Heel pain, heel spur and plantar fasciitis treatment",
    },
}


def section_hero(language: str) -> rx.Component:
    """
    Create the reimbursements page hero section with background image.

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
            image_src_fallback="/images/page_reimbursements/Hielpijn_hielspoor_plantaire_fasciits_tarieven.jpg",
            image_src_avif="/images/page_reimbursements/Hielpijn_hielspoor_plantaire_fasciits_tarieven.avif",
            image_src_webp="/images/page_reimbursements/Hielpijn_hielspoor_plantaire_fasciits_tarieven.webp",
            alt_text=get_translation(TRANSLATIONS, "hero_image_alt", language),
            dimensions=ImageDimensions.hero_banner,
            gradient="linear-gradient(270deg, rgba(255,255,255,.55) 0%, rgba(16,185,129,.35) 100%)",
            content=None,
        ),
        padding_top="0",
        position="relative",
        height="500px",
        clip_bottom="gentle_1",
        divider_color=Colors.backgrounds["white"],
    )
