"""Form button component with loading and disabled states."""
import reflex as rx
from ..theme import Colors, FontSizes


def form_button(
    label: str | rx.Var,
    on_click,
    is_loading: bool | rx.Var = False,
    is_disabled: bool | rx.Var = False,
    loading_text: str = "Versturen...",
) -> rx.Component:
    """
    Create a form submit button with loading and disabled states.

    The button automatically displays different states:
    - Loading: Shows loading indicator with custom text
    - Disabled: Grayed out, non-interactive
    - Active: Normal interactive button with hover effects

    Parameters
    ----------
    label : str | rx.Var
        Button text to display in normal/active state.
    on_click : callable
        Event handler function to call when button is clicked.
    is_loading : bool | rx.Var, optional
        Whether the button is in loading state. Default is False.
    is_disabled : bool | rx.Var, optional
        Whether the button is disabled. Default is False.
    loading_text : str, optional
        Text to display during loading state. Default is "Versturen...".

    Returns
    -------
    rx.Component
        A button component that renders different states based on
        is_loading and is_disabled parameters.

    Examples
    --------
    >>> form_button(
    ...     "Submit",
    ...     on_click=state.submit,
    ...     is_loading=state.submitting,
    ...     is_disabled=state.form_invalid
    ... )
    """
    base_styles = {
        "border_radius": "3px",
        "font_weight": "700",
        "font_size": FontSizes.button,
        "padding_x": "0.8em",
        "padding_y": "0.1em",
        "display": "inline-flex",
        "align_items": "center",
        "justify_content": "center",
        "text_decoration": "none",
        "border": "none",
        "white_space": "nowrap",
    }

    # Loading state
    loading_button = rx.box(
        rx.html("⏳ "),
        rx.text(loading_text, display="inline"),
        **base_styles,
        cursor="wait",
        bg=Colors.borders["light"],
        color=Colors.text["muted"],
        opacity="0.7",
    )

    # Disabled state
    disabled_button = rx.box(
        rx.text(label),
        **base_styles,
        cursor="not-allowed",
        bg=Colors.borders["light"],
        color=Colors.text["muted"],
        opacity="0.6",
    )

    # Active state (using the existing button component styling)
    active_button = rx.box(
        rx.text(label),
        on_click=on_click,
        **base_styles,
        cursor="pointer",
        transition="all 0.2s ease",
        bg=Colors.primary['300'],
        color=Colors.text['white'],
        box_shadow="0 4px 12px rgba(5, 168, 162, 0.3)",
        _hover={
            "bg": Colors.primary['500'],
            "box_shadow": "0 6px 16px rgba(5, 168, 162, 0.4)"
        }
    )

    # Return conditional rendering based on state
    return rx.cond(
        is_loading,
        loading_button,
        rx.cond(
            is_disabled,
            disabled_button,
            active_button,
        ),
    )
