"""Form button component with loading and disabled states."""

from typing import Any, Literal

import reflex as rx
from ..theme import Colors, FontSizes


def form_button(
    label: str | rx.Var,
    on_click: Any | None = None,
    is_loading: bool | rx.Var = False,
    is_disabled: bool | rx.Var = False,
    loading_text: str = "Versturen...",
    button_type: Literal["button", "submit", "reset"] = "button",
) -> rx.Component:
    """
    Create a form button with loading and disabled states.

    The button automatically displays different states:
    - Loading: Shows loading indicator with custom text
    - Disabled: Grayed out, non-interactive
    - Active: Normal interactive button with hover effects

    Parameters
    ----------
    label : str | rx.Var
        Button text to display in normal/active state.
    on_click : callable | None, optional
        Event handler function to call when button is clicked.
        Not needed for submit buttons in forms.
    is_loading : bool | rx.Var, optional
        Whether the button is in loading state. Default is False.
    is_disabled : bool | rx.Var, optional
        Whether the button is disabled. Default is False.
    loading_text : str, optional
        Text to display during loading state. Default is "Versturen...".
    button_type : Literal["button", "submit", "reset"], optional
        HTML button type. Default is "button".

    Returns
    -------
    rx.Component
        A button component that renders different states based on
        is_loading and is_disabled parameters.
    """
    loading_button = rx.el.button(
        rx.text("⏳ ", display="inline"),
        rx.text(loading_text, display="inline"),
        type="button",
        disabled=True,
        border_radius="3px",
        font_weight="700",
        font_size=FontSizes.button,
        padding="0.1em 0.8em",
        display="inline-flex",
        align_items="center",
        justify_content="center",
        text_decoration="none",
        border="none",
        white_space="nowrap",
        cursor="wait",
        background=Colors.borders["light"],
        color=Colors.text["muted"],
        opacity="0.7",
    )

    disabled_button = rx.el.button(
        label,
        type=button_type,
        disabled=True,
        border_radius="3px",
        font_weight="700",
        font_size=FontSizes.button,
        padding="0.1em 0.8em",
        display="inline-flex",
        align_items="center",
        justify_content="center",
        text_decoration="none",
        border="none",
        white_space="nowrap",
        cursor="not-allowed",
        background=Colors.borders["light"],
        color=Colors.text["muted"],
        opacity="0.6",
    )

    active_button_props: dict[str, Any] = {
        "type": button_type,
        "border_radius": "3px",
        "font_weight": "700",
        "font_size": FontSizes.button,
        "padding": "0.1em 0.8em",
        "display": "inline-flex",
        "align_items": "center",
        "justify_content": "center",
        "text_decoration": "none",
        "border": "none",
        "white_space": "nowrap",
        "cursor": "pointer",
        "transition": "all 0.2s ease",
        "background": Colors.primary["300"],
        "color": Colors.text["white"],
        "box_shadow": "0 4px 12px rgba(5, 168, 162, 0.3)",
        "style": {
            "&:hover:not(:disabled)": {
                "background": Colors.primary["500"],
                "box_shadow": "0 6px 16px rgba(5, 168, 162, 0.4)",
            },
            "&:disabled": {
                "background": Colors.borders["light"],
                "color": Colors.text["muted"],
                "opacity": "0.6",
                "cursor": "not-allowed",
                "box_shadow": "none",
            },
        },
    }

    if on_click is not None:
        active_button_props["on_click"] = on_click

    active_button = rx.el.button(label, **active_button_props)

    return rx.cond(
        is_loading,
        loading_button,
        rx.cond(
            is_disabled,
            disabled_button,
            active_button,
        ),
    )
