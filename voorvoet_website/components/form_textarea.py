"""Form textarea component with consistent styling."""

import reflex as rx
from ..theme import Colors, FontSizes


def form_textarea(
    placeholder: str | rx.Var,
    value: str | rx.Var,
    on_change,
    min_height: str = "120px",
) -> rx.Component:
    """
    Create a styled form textarea field.

    Parameters
    ----------
    placeholder : str | rx.Var
        Placeholder text for the textarea.
    value : str
        Current value of the textarea (bound to state).
    on_change : callable
        Event handler for value changes.
    min_height : str, optional
        Minimum height of the textarea. Default is "120px".

    Returns
    -------
    rx.Component
        A styled textarea component with consistent theming.

    Examples
    --------
    >>> form_textarea(
    ...     "Enter description...",
    ...     value=state.description,
    ...     on_change=state.set_description
    ... )
    """
    return rx.el.textarea(
        placeholder=placeholder,
        value=value,
        on_change=on_change,
        width="100%",
        min_height=min_height,
        padding="0.75rem",
        border_radius="4px",
        border=f"1px solid {Colors.borders['light']}",
        resize="vertical",
        background="white",
        color=Colors.text["content"],
        font_size=FontSizes.regular,
        line_height="1.6",
        style={
            "::placeholder": {
                "color": f"{Colors.text['placeholder']}",
                "opacity": "1",
            },
            "&:focus": {
                "outline": "none",
                "border_color": f"{Colors.primary['300']}",
                "box_shadow": f"0 0 0 3px {Colors.primary['300']}40",
            },
        },
    )
