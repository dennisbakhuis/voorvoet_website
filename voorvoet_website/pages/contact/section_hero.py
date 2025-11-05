"""Hero section for the contact page."""
import reflex as rx

from ...theme import Colors
from ...components import section, hero_banner


def section_hero() -> rx.Component:
    """
    Create the contact page hero section with background image.

    The hero section displays a full-width background image with a gradient
    overlay, without any text content overlay. Features an image of sore feet.

    Returns
    -------
    rx.Component
        A section component containing a hero banner with only the
        background image and gradient overlay.
    """
    return section(
        hero_banner(
            image_src="/images/page_contact/voetklachten_enschede_zere_voeten_voorvoet_contact.jpg",
            gradient="linear-gradient(270deg, rgba(255,255,255,.55) 0%, rgba(16,185,129,.35) 100%)",
            content=None,
        ),
        padding_top="0",
        position="relative",
        height="500px",
        clip_bottom="gentle_2",
        divider_color=Colors.backgrounds['white']
    )
