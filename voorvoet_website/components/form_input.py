"""Form input component with consistent styling and HTML5 validation."""

import reflex as rx
from typing import Any
from ..theme import Colors, FontSizes


def form_input(
    name: str = "",
    placeholder: str | rx.Var = "",
    value: str | rx.Var | None = None,
    on_change: Any | None = None,
    input_type: str = "text",
    on_blur: Any | None = None,
    required: bool = False,
    show_error: bool | rx.Var = False,
    custom_attrs: dict | None = None,
    input_mode: str | None = None,
    max_length: int | None = None,
    pattern: str | None = None,
) -> rx.Component:
    """
    Create a styled form input field with HTML5 validation support.

    Parameters
    ----------
    name : str
        Name attribute for FormData collection (required).
    placeholder : str | rx.Var, optional
        Placeholder text for the input field.
    value : str | rx.Var | None, optional
        Current value of the input. Only needed for controlled inputs.
    on_change : callable | None, optional
        Event handler for value changes. Only needed for controlled inputs.
    input_type : str, optional
        HTML input type (text, email, tel, etc.). Default is "text".
    on_blur : callable | None, optional
        Event handler for blur events. Default is None.
    required : bool, optional
        Whether the field is required for HTML5 validation. Default is False.
    custom_attrs : dict | None, optional
        Custom HTML attributes for the input. Default is None.
    input_mode : str | None, optional
        Input mode hint for mobile keyboards. Default is None.
    max_length : int | None, optional
        Maximum character length. Default is None.
    pattern : str | None, optional
        HTML5 pattern attribute for validation regex. Default is None.

    Returns
    -------
    rx.Component
        A styled input component with HTML5 validation and :user-invalid styling.
    """
    border_value: str | rx.Var[str]
    if isinstance(show_error, bool):
        border_value = (
            "3px solid red" if show_error else f"1px solid {Colors.borders['light']}"
        )
    else:
        border_value = rx.cond(
            show_error,
            "3px solid red",
            f"1px solid {Colors.borders['light']}",
        )

    base_props: dict[str, Any] = {
        "placeholder": placeholder,
        "width": "100%",
        "padding": "0.75rem 0.75rem",
        "height": "auto",
        "min_height": "50px",
        "border_radius": "4px",
        "font_size": FontSizes.regular,
        "background": "white",
        "color": Colors.text["content"],
        "type": input_type,
        "border": border_value,
        "style": {
            "::placeholder": {
                "color": f"{Colors.text['muted']}",
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

    if on_blur is not None:
        base_props["on_blur"] = on_blur

    if required:
        base_props["required"] = True

    if input_mode is not None:
        base_props["input_mode"] = input_mode

    if max_length is not None:
        base_props["max_length"] = max_length

    if custom_attrs is not None:
        base_props["custom_attrs"] = custom_attrs

    if pattern is not None:
        base_props["pattern"] = pattern

    return rx.el.input(**base_props)
