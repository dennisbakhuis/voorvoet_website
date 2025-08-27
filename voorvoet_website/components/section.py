# Section component
import reflex as rx

from ..theme import Colors


def section(*children, alternate_bg=False, **styles) -> rx.Component:
    bg_color = Colors.backgrounds["green_light"] if alternate_bg else Colors.backgrounds["white"]
    
    # Set default padding that can be overridden
    defaults = {
        "width": "100%",
        "padding_top": "5rem",
        "padding_bottom": "5rem", 
        "bg": bg_color,
    }
    # Merge defaults with styles, styles take precedence
    defaults.update(styles)
    
    return rx.box(*children, **defaults)
