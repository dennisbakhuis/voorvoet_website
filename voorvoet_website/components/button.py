# Button component based on voorvoet.nl CTA button
import reflex as rx
from ..theme import Colors


def button(
    label: str, 
    href: str | None = None, 
    on_click=None
) -> rx.Component:
    
    base_styles = {
        "border_radius": "3px",
        "font_weight": "700",
        "font_size": "24px",
        "padding_x": "0.8em",
        "padding_y": "0.1em",
        "transition": "all 0.2s ease",
        "cursor": "pointer",
        "display": "inline-flex",
        "align_items": "center",
        "justify_content": "center",
        "text_decoration": "none",
        "border": "none",
        "white_space": "nowrap",
    }
    
    base_styles.update({
        "bg": Colors.primary['300'],
        "color": Colors.text['white'],
        "box_shadow": "0 4px 12px rgba(5, 168, 162, 0.3)",
        "_hover": {
            "bg": Colors.primary['500'],
            "box_shadow": "0 6px 16px rgba(5, 168, 162, 0.4)"
        }
    })  # type: ignore
    
    button_content = rx.text(label)
    
    if href:
        return rx.link(
            button_content,
            href=href,
            **base_styles,  # type: ignore
        )
    else:
        return rx.box(
            button_content,
            on_click=on_click,
            **base_styles,  # type: ignore
        )
