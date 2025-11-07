"""Hero section for the home page with title, subtitle, and CTA."""
import reflex as rx
from ...theme import Colors
from ...components import container, section, hero_banner
from ...utils.translations import get_translation
from .section_hero_cta import hero_cta_box


TRANSLATIONS = {
    "nl": {
        "hero_title": "Voetklachten?",
        "hero_subtitle": "Loop er niet mee door!",
    },
    "de": {
        "hero_title": "Fußbeschwerden?",
        "hero_subtitle": "Laufen Sie nicht damit weiter!",
    },
    "en": {
        "hero_title": "Foot complaints?",
        "hero_subtitle": "Don't walk with them!",
    },
}


def section_hero() -> rx.Component:
    """
    Create the home page hero section with tagline and call-to-action.

    The hero section displays a full-width background image with a gradient
    overlay, featuring the main tagline "Voetklachten? Loop er niet mee door!"
    and a call-to-action box for booking appointments.

    Returns
    -------
    rx.Component
        A section component containing the hero banner with overlaid content
        including the main heading, subtitle, and CTA box positioned at the
        bottom of the hero area.
    """

    hero_content = container(
        rx.box(
            rx.vstack(
                rx.text(
                    get_translation(TRANSLATIONS, "hero_title"),
                    color=Colors.primary["300"],
                    font_weight="900",
                    text_align="center",
                    line_height="1.05",
                    font_size=["3rem", "4rem", "5rem", "6rem"],
                ),
                rx.text(
                    get_translation(TRANSLATIONS, "hero_subtitle"),
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
        ),
        rx.box(
            hero_cta_box(),
            grid_row="2",
            padding_x=["1rem", "0"],
            padding_bottom=["0.5rem", "0.75rem", "1rem", "1rem", "1rem"],
            margin_bottom=["4rem","4rem","4rem","4rem","4rem"]
        ),
        position="relative",
        z_index="2",
        display="grid",
        grid_template_rows="1fr auto",
        height="100%",
    )

    return section(
        hero_banner(
            image_src="/images/page_home/podotherapeut_enschede_voeten_in_bed_podotherapie_helpt.jpeg",
            gradient="linear-gradient(180deg, rgba(255,255,255,.55) 0%, rgba(16,185,129,.35) 100%)",
            content=hero_content,
        ),
        padding_top="0",
        padding_bottom=["3rem", "3rem", "3rem", "3rem"],
        position="relative",
        min_height=["calc(56dvh + 6rem)", "calc(62dvh + 6rem)", "calc(69dvh + 6rem)", "calc(74dvh + 6rem)"],
        clip_bottom="gentle_1",
        divider_color=Colors.backgrounds['white']
    )
