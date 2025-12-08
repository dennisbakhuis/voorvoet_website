"""Button component based on voorvoet.nl CTA button styling."""

from typing import Any

import reflex as rx
from reflex.event import EventType
from ..theme import Colors, FontSizes


def button(
    label: str | rx.Var,
    href: str | rx.Var | None = None,
    on_click: EventType[()] | None = None,
) -> rx.Component:
    """
    Create a styled call-to-action button component.

    Creates either a link button (if href is provided) or a clickable box button
    (if on_click is provided). The button features voorvoet.nl branding with
    primary colors and hover effects.

    Parameters
    ----------
    label : str
        The text to display on the button.
    href : str | None, optional
        URL to navigate to when clicked. If provided, renders as a link.
        Default is None.
    on_click : callable, optional
        Event handler function to call when button is clicked.
        Only used when href is None. Default is None.

    Returns
    -------
    rx.Component
        A Reflex link component (if href provided) or box component
        (if on_click provided) styled as a button.
    """
    base_styles: dict[str, Any] = {
        "border_radius": "3px",
        "font_weight": "700",
        "font_size": FontSizes.button,
        "padding_x": "0.8em",
        "padding_y": "0.1em",
        "transition": "all 0.2s ease",
        "cursor": "pointer",
        "display": "inline-flex",
        "align_items": "center",
        "justify_content": "center",
        "text_decoration": "none",
        "border": "none",
        "white_space": "nowrap",
        "bg": Colors.primary["300"],
        "color": Colors.text["white"],
        "box_shadow": "0 4px 12px rgba(5, 168, 162, 0.3)",
        "_hover": {
            "bg": Colors.primary["500"],
            "box_shadow": "0 6px 16px rgba(5, 168, 162, 0.4)",
        },
    }

    button_content = rx.text(label)

    if href is not None:
        return rx.link(
            button_content,
            href=href,
            **base_styles,
        )
    else:
        return rx.box(
            button_content,
            on_click=on_click,
            **base_styles,
        )
