# Regular text component for body content
import reflex as rx
from ..theme import Colors, FontSizes


def regular_text(text: str, **props) -> rx.Component:
    # Set default values that can be overridden by props
    defaults = {
        "font_size": FontSizes.regular,
        "line_height": "1.6", 
        "color": Colors.text["heading"],
    }
    # Merge defaults with props, props take precedence
    defaults.update(props)
    
    return rx.text(text, **defaults)