"""Form select dropdown component with consistent styling."""
import reflex as rx
from ..theme import Colors


def form_select(
    items: list[str] | rx.Var,
    value: str | rx.Var,
    on_change,
    placeholder: str | rx.Var = "",
    size: str = "3",
) -> rx.Component:
    """
    Create a styled select dropdown with consistent theming.

    Parameters
    ----------
    items : list[str] | rx.Var
        List of options to display in the dropdown.
    value : str | rx.Var
        Currently selected value (bound to state).
    on_change : callable
        Event handler for value changes.
    placeholder : str | rx.Var, optional
        Placeholder text when no option is selected. Default is "".
    size : str, optional
        Size variant for the select component. Default is "3".

    Returns
    -------
    rx.Component
        A styled select dropdown component with consistent theming.
    """
    custom_css = f"""
        .rt-SelectTrigger:where(.rt-variant-surface) {{
            color: {Colors.text['content']} !important;
            background-color: white !important;
            box-shadow: inset 0 0 0 1px {Colors.borders['light']} !important;
            min-height: 50px !important;
        }}

        .rt-SelectContent {{
            background-color: white !important;
        }}

        .rt-SelectItem {{
            color: {Colors.text['content']} !important;
        }}

        .rt-SelectItem:hover {{
            background-color: {Colors.primary['300']} !important;
            color: {Colors.text['white']} !important;
        }}
    """

    return rx.fragment(
        rx.html(f"<style>{custom_css}</style>"),
        rx.select(
            items,
            value=value,
            on_change=on_change,
            placeholder=placeholder,
            size=size,
            width="100%",
            variant="surface",
        ),
    )
