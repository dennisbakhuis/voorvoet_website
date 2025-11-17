"""Form radio button component with consistent styling."""
import reflex as rx
from typing import List, Union, Literal
from ..theme import FontSizes, Colors


def form_radio(
    items: Union[List[Union[str, rx.Var]], rx.Var],
    value: Union[str, rx.Var],
    on_change,
    direction: Literal["column", "column-reverse", "row", "row-reverse"] = "column",
    spacing: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] = "2",
) -> rx.Component:
    """
    Create a styled radio button group with consistent theming.

    Parameters
    ----------
    items : list[str | rx.Var] | rx.Var
        List of radio button options to display.
    value : str | rx.Var
        Currently selected value (bound to state).
    on_change : callable
        Event handler for value changes.
    direction : Literal["column", "column-reverse", "row", "row-reverse"], optional
        Layout direction. Default is "column".
    spacing : Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], optional
        Spacing between radio buttons. Default is "2".

    Returns
    -------
    rx.Component
        A styled radio button group component with consistent theming.
    """
    return rx.radio(
        items,
        value=value,
        on_change=on_change,
        direction=direction,
        spacing=spacing,
        font_size=FontSizes.regular,
        variant="classic",
        color=Colors.text["content"],
        style={
            # Unselected radio buttons
            ".rt-BaseRadioRoot:where(.rt-variant-classic):where(:not(:checked), [data-state='unchecked'])::before": {
                "background_color": "transparent !important",
                "box_shadow": f"inset 0 0 0 2px {Colors.text["placeholder"]} !important",
            },
            # Selected radio buttons
            ".rt-BaseRadioRoot:where(.rt-variant-classic):where(:checked, [data-state='checked'])::before": {
                "background_color": "transparent !important",
                "box_shadow": f"inset 0 0 0 2px {Colors.text["placeholder"]} !important",
            },
            # Indicator dot
            ".rt-BaseRadioRoot:where(.rt-variant-classic):where(:checked, [data-state='checked'])::after": {
                "background_color": f"{Colors.primary['300']} !important",
            },
        },
    )
