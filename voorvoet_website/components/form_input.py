"""Form input component with consistent styling and error states."""
import reflex as rx
from ..theme import Colors, FontSizes


def form_input(
    placeholder: str | rx.Var,
    value: str | rx.Var,
    on_change,
    input_type: str = "text",
    on_blur=None,
    show_error: bool | rx.Var = False,
    custom_attrs: dict | None = None,
    input_mode: str | None = None,
    max_length: int | None = None,
) -> rx.Component:
    """
    Create a styled form input field with error state support.

    Parameters
    ----------
    placeholder : str | rx.Var
        Placeholder text for the input field.
    value : str | rx.Var
        Current value of the input (bound to state).
    on_change : callable
        Event handler for value changes.
    input_type : str, optional
        HTML input type (text, email, tel, etc.). Default is "text".
    on_blur : callable | None, optional
        Event handler for blur events. Default is None.
    show_error : bool | rx.Var, optional
        Whether to show error styling (red border). Default is False.
    custom_attrs : dict | None, optional
        Custom HTML attributes for the input. Default is None.
    input_mode : str | None, optional
        Input mode hint for mobile keyboards. Default is None.
    max_length : int | None, optional
        Maximum character length. Default is None.

    Returns
    -------
    rx.Component
        A styled input component with consistent theming and optional
        error state.
    """
    if isinstance(show_error, bool):
        border_value = "3px solid red" if show_error else f"1px solid {Colors.borders['light']}"
    else:
        border_value = rx.cond(
            show_error,
            "3px solid red",
            f"1px solid {Colors.borders['light']}",
        )

    base_props = {
        "placeholder": placeholder,
        "value": value,
        "on_change": on_change,
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
        },
    }

    if on_blur:
        base_props["on_blur"] = on_blur

    if input_mode:
        base_props["input_mode"] = input_mode

    if max_length:
        base_props["max_length"] = max_length

    if custom_attrs:
        base_props["custom_attrs"] = custom_attrs

    return rx.el.input(**base_props)
