"""Icon list item component for CTA boxes and lists."""

import reflex as rx
from typing import Any
from ..theme import Colors, FontSizes
from .fa_icon import fa_icon


def icon_list_item(icon: str, text: str, **props: Any) -> rx.Component:
    """
    Create a list item with a FontAwesome icon and text.

    Creates a horizontal stack with a FontAwesome icon on the left
    and text content on the right. The icon is aligned to the top
    to handle multi-line text properly.

    Parameters
    ----------
    icon : str
        FontAwesome icon class name (e.g., "fa-check", "fa-star").
    text : str
        Text content to display next to the icon.
    **props : dict
        Additional style properties to apply to the hstack container.
        These will override the default styles.

    Returns
    -------
    rx.Component
        A Reflex hstack component with icon and text.
    """
    return rx.hstack(
        fa_icon(
            icon,
            color=Colors.text["content"],
            margin_top="10px",
        ),
        rx.text(
            text,
            font_size=FontSizes.regular,
            color=Colors.text["content"],
            line_height="1.6",
        ),
        spacing="3",
        align="start",
        **props,
    )
