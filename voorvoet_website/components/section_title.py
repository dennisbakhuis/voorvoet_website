"""Section title component for main section headings."""

from typing import Union
import reflex as rx
from ..theme import Colors, FontSizes


def section_title(text: Union[str, rx.Var], **props) -> rx.Component:
    """
    Create a section title with large, bold styling.

    Creates a text component with styling appropriate for main section
    headings. Uses large font size and bold weight for prominence.

    Parameters
    ----------
    text : str
        The title text to display.
    **props : dict
        Additional style properties to apply to the title.
        These will override the default styles (font_size, font_weight, color).

    Returns
    -------
    rx.Component
        A Reflex text component styled as a section title.
    """
    return rx.text(
        text,
        font_size=FontSizes.section_title,
        font_weight="700",
        color=Colors.text["heading"],
        **props,
    )
