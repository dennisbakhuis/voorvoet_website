"""Hero section for the blog page."""
import reflex as rx

from ...theme import Colors
from ...components import section, hero_banner


def section_hero() -> rx.Component:
    """
    Create the blog page hero section with background image.

    The hero section displays a full-width background image with a gradient
    overlay, without any text content overlay.

    Returns
    -------
    rx.Component
        A section component containing a hero banner with only the
        background image and gradient overlay.
    """
    return section(
        hero_banner(
            image_src="/images/page_blog/voorvoet_praktijk_voor_podotherapie_Sandalen_Durea_modern_uitneembaar_voetbed_steunzolen_op_maat_gezonde_blote_voeten_bij_zwembad.jpg",
            gradient="linear-gradient(270deg, rgba(255,255,255,.55) 0%, rgba(16,185,129,.35) 100%)",
            content=None,
        ),
        padding_top="0",
        position="relative",
        height="500px",
        clip_bottom="gentle_1",
        divider_color=Colors.backgrounds['white']
    )
