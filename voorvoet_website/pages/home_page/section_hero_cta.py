# Hero CTA box component
import reflex as rx
from ...components import button, section_sub_title, icon_list_item
from ...theme import Colors


def hero_cta_box() -> rx.Component:
    return rx.box(
        rx.vstack(
            section_sub_title("Direct digitaal een afspraak maken!", text_align="center"),
            rx.box(
                rx.vstack(
                    icon_list_item("fa-check-square-o", "Geen verwijzing nodig!"),
                    icon_list_item("fa-check-square-o", "Snel geholpen door een professional."),
                    icon_list_item("fa-check-square-o", "Snelste weg naar de specialist!"),
                    spacing="3",
                    align="start",
                ),
                width="100%",
                display="flex",
                justify_content="center"
            ),
            rx.box(
                button("Maak een afspraak", href="#afspraak"),
                width="100%",
                display="flex",
                justify_content="center"
            ),
            spacing="4",
            align="center",
        ),
        width=["95%", "28rem", "32rem", "36rem"],
        max_width=["95%", "90%", "85%", "38rem"],
        bg=Colors.backgrounds["green_light"],
        border_radius="0.75rem",
        padding=["1rem", "1.5rem", "1.75rem", "2rem"],
        box_shadow="0 6px 18px rgba(0,0,0,.12)",
        backdrop_filter="saturate(1.05) blur(1px)",
        margin_left=["auto", "auto", "auto", "auto"],
        margin_right=["auto", "20px", "20px", "20px"],
    )