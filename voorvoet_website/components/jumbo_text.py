"""Jumbo text component for extra-large display text."""

from typing import Union
import reflex as rx
from ..theme import Colors


def jumbo_text(text: Union[str, rx.Var], **props) -> rx.Component:
    """
    Create extra-large display text for hero sections.

    Parameters
    ----------
    text : str | rx.Var
        The text to display. Can be a string or reactive variable.
    **props : dict
        Additional style properties to apply.
        These will override the default styles.

    Returns
    -------
    rx.Component
        A styled text component with jumbo sizing.
    """
    default_styles = {
        "font_size": ["2.5rem", "4rem", "5rem", "6rem"],
        "font_weight": "900",
        "color": Colors.primary["300"],
        "line_height": "1.05",
    }

    merged_styles = {**default_styles, **props}

    return rx.text(
        text,
        **merged_styles,
    )
