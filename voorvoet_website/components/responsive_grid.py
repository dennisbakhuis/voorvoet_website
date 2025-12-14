"""Responsive Grid component."""

from typing import Any
import reflex as rx


def responsive_grid(
    *children: rx.Component,
    columns: list[int] = [1, 1, 2],
    spacing: str = "8",
    **props: Any,
) -> rx.Component:
    """
    Create a responsive grid that adapts to different screen sizes.

    Creates a grid layout that automatically adjusts the number of columns
    based on breakpoints. Uses Reflex's breakpoint system to define
    different column counts for different screen sizes.

    Parameters
    ----------
    *children : rx.Component
        Variable number of child components to place in the grid.
    columns : list[int], optional
        Number of columns for each breakpoint in order: initial, sm, md, lg, xl, 2xl.
        Only the first N values are used where N is the length of the list.
        Default is [1, 1, 2] (1 column for initial/sm, 2 columns for md).
    spacing : str, optional
        Gap spacing between grid items. Default is "8".
    **props : dict
        Additional style properties to apply to the grid.
        These will override the default props.

    Returns
    -------
    rx.Component
        A Reflex grid component with responsive column configuration.

    Notes
    -----
    Breakpoint labels are: initial, sm, md, lg, xl, 2xl.
    Only the first len(columns) breakpoints are configured.
    """
    labels = ["initial", "sm", "md", "lg", "xl", "2xl"]
    bp: dict[str, Any] = {
        labels[i]: str(c) for i, c in enumerate(columns) if i < len(labels)
    }
    cols = rx.breakpoints(**bp)
    props = dict(columns=cols, gap=spacing)
    props.update(props)
    return rx.grid(*children, **props)
