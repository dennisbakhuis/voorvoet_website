"""Regular text component for body content."""
import reflex as rx
from typing import Union
from ..theme import Colors, FontSizes, Spacing


def regular_text(text: Union[str, list[str]], **props) -> rx.Component:
    """
    Create regular body text with consistent styling.

    Creates text components with standard font size, line height, and color.
    Supports both single text strings and lists of paragraphs with
    automatic spacing between paragraphs.

    Parameters
    ----------
    text : str | list[str]
        Single text string or list of paragraph strings.
        When a list is provided, each string becomes a separate paragraph
        with automatic spacing between them.
    **props : dict
        Additional style properties to apply to the text.
        These will override the default styles (font_size, line_height, color).

    Returns
    -------
    rx.Component
        A Reflex text component (for single string) or box component
        (for list of paragraphs) with standard body text styling.

    Notes
    -----
    When passing a list, all paragraphs except the last one automatically
    receive margin_bottom spacing. The last paragraph has no bottom margin
    unless specified in props.
    """
    defaults = {
        "font_size": FontSizes.regular,
        "line_height": "1.6",
        "color": Colors.text["heading"],
    }
    defaults.update(props)

    if isinstance(text, str):
        return rx.text(text, **defaults)  # type: ignore

    paragraphs = []
    for i, paragraph in enumerate(text):
        paragraph_props = defaults.copy()
        if i < len(text) - 1:
            paragraph_props["margin_bottom"] = Spacing.text_margin_bottom
        paragraphs.append(rx.text(paragraph, **paragraph_props))

    return rx.box(*paragraphs)