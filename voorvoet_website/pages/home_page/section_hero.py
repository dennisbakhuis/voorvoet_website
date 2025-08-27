# Hero section for the home page
import reflex as rx
from ...theme import Colors
from ...components import container, section
from .section_hero_cta import hero_cta_box


def section_hero() -> rx.Component:
    return section(
        # Background images
        rx.image(
            src="/images/podotherapeut_enschede_voeten_in_bed_podotherapie_helpt.jpeg",
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
            bg="linear-gradient(180deg, rgba(255,255,255,.55) 0%, rgba(16,185,129,.35) 100%)",
            mix_blend_mode="screen",
            pointer_events="none",
        ),
        rx.box(
            position="absolute",
            inset="0",
            bg="linear-gradient(180deg, rgba(0,0,0,.08) 0%, rgba(0,0,0,.22) 100%)",
            pointer_events="none",
        ),
        # Content container
        container(
            rx.box(
                rx.vstack(
                    rx.text(
                        "Voetklachten?",
                        color=Colors.primary["300"],
                        font_weight="900",
                        text_align="center",
                        line_height="1.05",
                        font_size=["3rem", "4rem", "5rem", "6rem"],
                    ),
                    rx.text(
                        "Loop er niet mee door!",
                        color=Colors.text["heading"],
                        text_align="center",
                        opacity="0.95",
                        font_weight="600",
                        line_height="1.15",
                        font_size=["2rem", "2.25rem", "2.7rem", "3rem"],
                    ),
                    spacing="2",
                    align="center",
                ),
                display="flex",
                align_items="center",
                justify_content="center",
                height="100%",
                grid_row="1",
                z_index=1,
            ),
            rx.box(
                hero_cta_box(),
                grid_row="2",
                padding_x=["1rem", "0"],
                padding_bottom=["1rem", "1.25rem", "1.5rem", "1.75rem", "2rem"],
            ),
            # GRID + sizing
            position="relative",
            display="grid",
            grid_template_rows="1fr auto",
            height=["70dvh", "78dvh", "86dvh", "92dvh"],
            max_height=["640px", "720px", "840px", "920px"],
            min_height="520px",
        ),
        # Section styling
        padding_top="0",
        padding_bottom="0",  # Override default section padding for hero
        position="relative",
        overflow="hidden"
    )
