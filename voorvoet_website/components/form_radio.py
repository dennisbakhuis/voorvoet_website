"""Form radio button component with consistent styling."""

from typing import Any

import reflex as rx
from typing import Literal
from ..theme import FontSizes, Colors


def form_radio(
    items: list[str | rx.Var] | rx.Var,
    value: str | rx.Var,
    on_change: Any,
    direction: Literal["column", "column-reverse", "row", "row-reverse"]
    | list[str] = "column",
    spacing: Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] = "2",
    color: str | rx.Var | None = None,
    font_size: str | rx.Var | None = None,
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
    direction : Literal["column", "column-reverse", "row", "row-reverse"] | list[str], optional
        Layout direction. Can be a single value or responsive array [mobile, sm, md, lg].
        Default is "column".
    spacing : Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], optional
        Spacing between radio buttons. Default is "2".
    color : str | rx.Var, optional
        Text color. Default is Colors.text["content"].
    font_size : str | rx.Var, optional
        Font size. Default is FontSizes.regular.

    Returns
    -------
    rx.Component
        A styled radio button group component with consistent theming.
    """
    base_style = {
        ".rt-BaseRadioRoot:where(.rt-variant-classic):where(:not(:checked), [data-state='unchecked'])::before": {
            "background_color": "transparent !important",
            "box_shadow": f"inset 0 0 0 2px {Colors.text['placeholder']} !important",
        },
        ".rt-BaseRadioRoot:where(.rt-variant-classic):where(:checked, [data-state='checked'])::before": {
            "background_color": "transparent !important",
            "box_shadow": f"inset 0 0 0 2px {Colors.text['placeholder']} !important",
        },
        ".rt-BaseRadioRoot:where(.rt-variant-classic):where(:checked, [data-state='checked'])::after": {
            "background_color": f"{Colors.primary['300']} !important",
        },
        "& .rt-Text, & label, & .rt-RadioGroupItem": {
            "font-size": f"{FontSizes.regular} !important",
        },
    }

    if isinstance(direction, list):
        responsive_style = {
            **base_style,
            "flex_direction": "column !important",
            "&.rt-RadioGroupRoot": {
                "flex_direction": "column !important",
            },
            "& > *": {
                "flex_direction": "column !important",
            },
            "@media (min-width: 768px)": {
                "flex_direction": "row !important",
                "&.rt-RadioGroupRoot": {
                    "flex_direction": "row !important",
                },
                "& > *": {
                    "flex_direction": "row !important",
                },
            },
        }

        return rx.radio(
            items,
            value=value,
            on_change=on_change,
            direction="column",
            spacing=spacing,
            font_size=font_size or FontSizes.regular,
            variant="classic",
            color=color or Colors.text["content"],
            size="3",
            style=responsive_style,
        )
    else:
        return rx.radio(
            items,
            value=value,
            on_change=on_change,
            direction=direction,
            spacing=spacing,
            font_size=font_size or FontSizes.regular,
            variant="classic",
            color=color or Colors.text["content"],
            size="3",
            style=base_style,
        )
