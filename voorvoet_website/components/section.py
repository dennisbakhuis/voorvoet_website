# Section component
import reflex as rx

from ..theme import Colors, Spacing


def section(*children, alternate_bg=False, **styles) -> rx.Component:
    bg_color = Colors.backgrounds["green_light"] if alternate_bg else Colors.backgrounds["white"]
    
    # Set default padding that can be overridden
    defaults = {
        "width": "100%",
        "padding_top": Spacing.section_vertical,
        "padding_bottom": Spacing.section_vertical, 
        "bg": bg_color,
    }
    # Merge defaults with styles, styles take precedence
    defaults.update(styles)
    
    return rx.box(*children, **defaults)
