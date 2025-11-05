"""Enhanced column component for flexible layout with responsive helpers."""
import reflex as rx
from typing import Union, List, Optional

from ..theme import responsive_padding, Layout, Spacing


def column(
    *children,
    size: Optional[Union[str, List[str]]] = None,
    spacing_direction: Optional[str] = None,
    responsive_spacing: Optional[List[str]] = None,
    **props
) -> rx.Component:
    """
    Create a flexible column with responsive sizing and spacing.

    Creates a column component with support for responsive width sizing,
    flexible padding based on direction, and custom spacing arrays.
    Handles both single values and breakpoint arrays for full responsive control.

    Parameters
    ----------
    *children : rx.Component
        Variable number of child components to render inside the column.
    size : str | list[str] | None, optional
        Column size as single value (e.g., "50%") or responsive array
        (e.g., ["100%", "50%", "33%"]) for different breakpoints.
        Default is None, which sets width to 100% with flex: 1.
    spacing_direction : str | None, optional
        Direction for responsive padding. Valid values are "left", "right",
        "both", or "none". Default is None (no spacing applied).
    responsive_spacing : list[str] | None, optional
        Custom responsive spacing array to override default padding values.
        Applied based on spacing_direction. Default is None.
    **props : dict
        Additional style properties to apply to the column.
        These will override the computed styles.

    Returns
    -------
    rx.Component
        A Reflex box component configured as a flexible column.
    """

    flex_props = {}

    if size:
        if isinstance(size, list):
            # Responsive sizing: convert each breakpoint size to flex values
            flex_values = []
            width_values = []
            for s in size:
                if s == "100%":
                    flex_values.append("1")
                    width_values.append("100%")
                else:
                    flex_values.append(f"0 0 {s}")
                    width_values.append(s)
            flex_props["flex"] = flex_values
            flex_props["width"] = width_values
        else:
            # Single size value
            flex_props["flex"] = f"0 0 {size}"
            flex_props["width"] = size
    else:
        flex_props["width"] = "100%"
        flex_props["flex"] = "1"
    
    # Handle responsive spacing
    if spacing_direction and not responsive_spacing:
        if spacing_direction == "left":
            flex_props["padding_left"] = responsive_padding("left")
        elif spacing_direction == "right":
            flex_props["padding_right"] = responsive_padding("right")
        elif spacing_direction == "both":
            flex_props["padding_left"] = responsive_padding("left")
            flex_props["padding_right"] = responsive_padding("right")
        # "none" or invalid values: no padding applied
    
    # Handle custom responsive spacing
    if responsive_spacing:
        if spacing_direction == "left":
            flex_props["padding_left"] = responsive_spacing
        elif spacing_direction == "right":
            flex_props["padding_right"] = responsive_spacing
    
    return rx.box(
        *children,
        **flex_props,
        **props
    )