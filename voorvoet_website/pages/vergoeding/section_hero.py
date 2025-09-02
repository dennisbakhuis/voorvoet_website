# Hero section for the home page
import reflex as rx

from ...theme import Colors
from ...components import section


def section_hero() -> rx.Component:
    return section(
        # Background images
        rx.image(
            src="/images/podotherapie_enschede_wandeling_in_het_bos_zonder_hielpijn_voorvoet_podotherapie_enschede.jpg",
            object_fit="cover",
            position="absolute",
            inset="0",
            width="100%",
            height="100%",
            filter="brightness(1.05) saturate(1.06)",
        ),
        rx.box(
            position="absolute",
            inset="0",
            bg="linear-gradient(270deg, rgba(255,255,255,.55) 0%, rgba(16,185,129,.35) 100%)",
            mix_blend_mode="screen",
            pointer_events="none",
        ),      
        padding_top="0",
        height="500px",
        position="relative",
        overflow="hidden",
        clip_bottom="gentle_1",
        divider_color=Colors.backgrounds['white']
    )
