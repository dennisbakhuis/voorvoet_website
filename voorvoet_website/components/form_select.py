"""Form select dropdown component with consistent styling."""

import reflex as rx
from reflex.event import EventType
from ..theme import Colors


def form_select(
    items: list[str] | rx.Var,
    value: str | rx.Var,
    on_change: EventType[()],
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
    return rx.select.root(
        rx.select.trigger(
            placeholder=placeholder,
            width="100%",
            color=Colors.text["content"],
            style={
                "background_color": "white",
                "min_height": "50px",
                "border": f"1px solid {Colors.borders['light']}",
                "border_radius": "4px",
            },
        ),
        rx.select.content(
            rx.foreach(
                items,
                lambda item: rx.select.item(item, value=item),
            ),
            background="white",
            color=Colors.text["content"],
        ),
        value=value,
        on_change=on_change,
        size=size,
    )
