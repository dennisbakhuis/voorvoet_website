import reflex as rx

from ..theme import Colors
from .button import button


def information_card(title: str, description: str, icon: str, bg_color="white", show_box=True, button_text="Lees meer", button_link="#") -> rx.Component:
    # Define box styling conditionally
    box_styles = {}
    if show_box:
        box_styles = {
            "bg": bg_color,
            "border_radius": "12px",
            "padding": "2rem",
            "box_shadow": "0 4px 6px rgba(0, 0, 0, 0.05)",
            "border": f"1px solid {Colors.borders['light']}",
            "transition": "all 0.3s ease",
            "_hover": {
                "transform": "translateY(-4px)",
                "box_shadow": "0 8px 25px rgba(0, 0, 0, 0.1)"
            }
        }
    else:
        box_styles = {
            "bg": "transparent",
            "padding": "2rem"
        }
    
    return rx.box(
        rx.vstack(
            rx.vstack(
                rx.box(
                    rx.html(f'<i class="fa {icon}" style="color: {Colors.text["heading"]}; font-size: 4.5rem;"></i>'),
                    display="flex",
                    justify_content="center",
                    align_items="center",
                    margin_bottom="1rem",
                ),
                rx.text(title, font_size="20px", font_weight="600", color=Colors.text["heading"], text_align="center"),
                rx.text(
                    description, 
                    text_align="center", 
                    color=Colors.text["heading"], 
                    line_height="1.6",
                    font_size="18px"
                ),
                spacing="3",
                align="center",
                flex="1",
            ),
            rx.box(
                button(button_text, href=button_link),
                display="flex",
                justify_content="center",
                width="100%",
                margin_top="1rem",
            ),
            spacing="0",
            align="center",
            height="100%",
        ),
        height="100%",
        width="100%",
        max_width="350px",
        min_width="280px",
        display="flex",
        **box_styles,  # type: ignore
    )
