"""Standard header component for all semantic heading levels h1-h6."""

from typing import Union
import reflex as rx
from ..theme import Colors, FontSizes


def header(text: Union[str, rx.Var], level: int = 2, **props) -> rx.Component:
    """
    Create a semantic heading with standardized styling.

    Parameters
    ----------
    text : str | rx.Var
        The heading text to display. Can be a string or reactive variable.
    level : int, optional
        Heading level from 1 to 6 (default: 2); sizes are set in theme.py.
    **props : dict
        Additional style properties to apply to the heading.
        These will override the default styles.

    Returns
    -------
    rx.Component
        A Reflex heading component with semantic HTML and theme styling.
    """
    font_size_map = {
        1: FontSizes.heading_h1,
        2: FontSizes.heading_h2,
        3: FontSizes.heading_h3,
        4: FontSizes.heading_h4,
        5: FontSizes.heading_h5,
        6: FontSizes.heading_h6,
    }

    font_size = font_size_map.get(level, FontSizes.section_title)

    default_styles = {
        "font_size": font_size,
        "font_weight": "700",
        "margin_bottom": "1rem",
        "color": Colors.text["heading"],
    }

    merged_styles = {**default_styles, **props}

    return rx.heading(
        text,
        as_=f"h{level}",
        **merged_styles,
    )
