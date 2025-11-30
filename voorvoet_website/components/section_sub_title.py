"""Section sub title component for subsection headings."""

import reflex as rx
from ..theme import Colors, FontSizes


def section_sub_title(text: str, **props) -> rx.Component:
    """
    Create a section subtitle with medium, bold styling.

    Creates a text component with styling appropriate for subsection
    headings. Uses medium font size and bold weight with subheading color.

    Parameters
    ----------
    text : str
        The subtitle text to display.
    **props : dict
        Additional style properties to apply to the subtitle.
        These will override the default styles (font_size, font_weight, color).

    Returns
    -------
    rx.Component
        A Reflex text component styled as a section subtitle.
    """
    return rx.text(
        text,
        font_size=FontSizes.section_sub_title,
        font_weight="700",
        color=Colors.text["subheading"],
        **props,
    )
