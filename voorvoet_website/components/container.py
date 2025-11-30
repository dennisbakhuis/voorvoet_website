"""Container component to center content and limit max width."""

import reflex as rx

from ..theme import Layout, Spacing


def container(*children, **styles) -> rx.Component:
    """
    Create a centered container with max-width constraints.

    Wraps child components in a box that centers content horizontally
    and applies consistent padding and maximum width limits.

    Parameters
    ----------
    *children : rx.Component
        Variable number of child components to render inside the container.
    **styles : dict
        Additional style properties to apply to the container.
        These will override the default styles.

    Returns
    -------
    rx.Component
        A Reflex box component with centered, max-width constrained content.
    """
    base = dict(
        width="100%",
        max_width=Layout.max_width,
        margin_x="auto",
        padding_x=Spacing.container_padding,
    )
    base.update(styles)
    return rx.box(*children, **base)  # type: ignore
