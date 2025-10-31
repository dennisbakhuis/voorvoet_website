# Regular text component for body content
import reflex as rx
from typing import Union
from ..theme import Colors, FontSizes, Spacing


def regular_text(text: Union[str, list[str]], **props) -> rx.Component:
    # Set default values that can be overridden by props
    defaults = {
        "font_size": FontSizes.regular,
        "line_height": "1.6", 
        "color": Colors.text["heading"],
    }
    # Merge defaults with props, props take precedence
    defaults.update(props)
    
    # Handle single string - return single text component
    if isinstance(text, str):
        return rx.text(text, **defaults)  # type: ignore
    
    # Handle list of strings - create separate paragraphs
    paragraphs = []
    for i, paragraph in enumerate(text):
        # Add margin_bottom to all paragraphs except the last one
        paragraph_props = defaults.copy()
        if i < len(text) - 1:
            paragraph_props["margin_bottom"] = Spacing.text_margin_bottom
        paragraphs.append(rx.text(paragraph, **paragraph_props))
    
    return rx.box(*paragraphs)