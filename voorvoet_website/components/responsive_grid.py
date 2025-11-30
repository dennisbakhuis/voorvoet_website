"""Responsive Grid component."""

import reflex as rx


def responsive_grid(
    *children, columns=[1, 1, 2], spacing="8", **styles
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
    **styles : dict
        Additional style properties to apply to the grid.
        These will override the default styles.

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
    bp = {labels[i]: str(c) for i, c in enumerate(columns) if i < len(labels)}
    cols = rx.breakpoints(**bp)  # type: ignore
    props = dict(columns=cols, gap=spacing)
    props.update(styles)
    return rx.grid(*children, **props)  # type: ignore
