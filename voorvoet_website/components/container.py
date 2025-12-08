"""Container component to center content and limit max width."""

from typing import Any

import reflex as rx

from ..theme import Layout, Spacing


def container(*children, **props) -> rx.Component:
    """
    Create a centered container with max-width constraints.

    Wraps child components in a box that centers content horizontally
    and applies consistent padding and maximum width limits.

    Parameters
    ----------
    *children : rx.Component
        Variable number of child components to render inside the container.
    **props : dict
        Additional style properties to apply to the container.
        These will override the default props.

    Returns
    -------
    rx.Component
        A Reflex box component with centered, max-width constrained content.
    """
    base: dict[str, Any] = {
        "width": "100%",
        "max_width": Layout.max_width,
        "margin_x": "auto",
        "padding_x": Spacing.container_padding,
    }
    base.update(props)

    return rx.box(
        *children,
        **base,
    )
