"""Information card component for displaying service or feature information."""
import reflex as rx
from typing import Union

from ..theme import Colors, FontSizes, Layout
from .button import button
from .fa_icon import fa_icon


def information_card(title: Union[str, rx.Var], description: Union[str, rx.Var], icon: str, bg_color="white", show_box=True, button_text: Union[str, rx.Var] = "Lees meer", button_link: Union[str, rx.Var] = "#") -> rx.Component:
    """
    Create an information card with icon, title, description, and button.

    Creates a styled card component with a FontAwesome icon, title text,
    description text, and a call-to-action button. The card can be rendered
    with or without a visible box border and shadow, and includes hover effects.

    Parameters
    ----------
    title : str
        Card title text.
    description : str
        Card description text explaining the service or feature.
    icon : str
        FontAwesome icon class name (e.g., "fa-heart", "fa-star").
    bg_color : str, optional
        Background color for the card. Default is "white".
    show_box : bool, optional
        Whether to show the card box border and shadow. If False,
        renders with transparent background. Default is True.
    button_text : str, optional
        Text for the call-to-action button. Default is "Lees meer".
    button_link : str, optional
        URL for the call-to-action button. Default is "#".

    Returns
    -------
    rx.Component
        A Reflex box component styled as an information card.
    """
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
                    fa_icon(icon, color=Colors.text["heading"], size="4.5rem"),
                    display="flex",
                    justify_content="center",
                    align_items="center",
                    margin_bottom="1rem",
                ),
                rx.text(title, font_size=FontSizes.card_title, font_weight="600", color=Colors.text["heading"], text_align="center"),
                rx.text(
                    description, 
                    text_align="center", 
                    color=Colors.text["heading"], 
                    line_height="1.6",
                    font_size=FontSizes.regular
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
        max_width=Layout.card_max_width,
        min_width=Layout.card_min_width,
        display="flex",
        **box_styles,  # type: ignore
    )
