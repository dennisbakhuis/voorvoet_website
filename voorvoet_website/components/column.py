# Enhanced column component for flexible layout with responsive helpers
import reflex as rx
from typing import Union, List, Optional

from ..theme import responsive_padding, Layout, Spacing


def column(
    *children, 
    size: Optional[Union[str, List[str]]] = None,
    spacing_direction: Optional[str] = None,  # "left", "right", "both", "none"
    responsive_spacing: Optional[List[str]] = None,  # Custom spacing array
    **props
) -> rx.Component:
    """
    Enhanced column component with responsive spacing helpers
    
    Args:
        *children: Child components
        size: Column size (single value or responsive array)
        spacing_direction: Direction for responsive padding ("left", "right", "both", "none")
        responsive_spacing: Custom responsive spacing array
        **props: Additional props passed to rx.box
    """
    
    flex_props = {}
    
    # Handle size (existing logic)
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