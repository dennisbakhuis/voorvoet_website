"""Form textarea component with consistent styling and HTML5 validation."""

from typing import Any

import reflex as rx
from ..theme import Colors, FontSizes


def form_textarea(
    name: str = "",
    placeholder: str | rx.Var = "",
    value: str | rx.Var | None = None,
    on_change: Any | None = None,
    min_height: str = "120px",
    required: bool = False,
) -> rx.Component:
    """
    Create a styled form textarea field with HTML5 validation support.

    Parameters
    ----------
    name : str
        Name attribute for FormData collection (required).
    placeholder : str | rx.Var, optional
        Placeholder text for the textarea.
    value : str | rx.Var | None, optional
        Current value of the textarea. Only needed for controlled inputs.
    on_change : callable | None, optional
        Event handler for value changes. Only needed for controlled inputs.
    min_height : str, optional
        Minimum height of the textarea. Default is "120px".
    required : bool, optional
        Whether the field is required for HTML5 validation. Default is False.

    Returns
    -------
    rx.Component
        A styled textarea component with HTML5 validation and :user-invalid styling.
    """
    base_props: dict[str, Any] = {
        "placeholder": placeholder,
        "width": "100%",
        "min_height": min_height,
        "padding": "0.75rem",
        "border_radius": "4px",
        "border": f"1px solid {Colors.borders['light']}",
        "resize": "vertical",
        "background": "white",
        "color": Colors.text["content"],
        "font_size": FontSizes.regular,
        "line_height": "1.6",
        "style": {
            "::placeholder": {
                "color": f"{Colors.text['placeholder']}",
                "opacity": "1",
            },
            "&:focus": {
                "outline": "none",
                "border_color": f"{Colors.primary['300']}",
                "box_shadow": f"0 0 0 3px {Colors.primary['300']}40",
            },
            "&:user-invalid": {
                "border": "3px solid red",
            },
        },
    }

    if name:
        base_props["name"] = name

    if value is not None:
        base_props["value"] = value

    if on_change is not None:
        base_props["on_change"] = on_change

    if required:
        base_props["required"] = True

    return rx.el.textarea(**base_props)
