"""Centered image component for reusable centered image layouts."""

import reflex as rx
from typing import Optional
from ..theme import Layout


def centered_image(
    src: str, alt: Optional[str] = None, max_width: str = "500px", **props
) -> rx.Component:
    """
    Create a centered image with standard styling and shadow.

    Creates an image component with responsive width, border radius,
    and box shadow styling. The image is automatically centered and
    scaled based on its max_width constraint.

    Parameters
    ----------
    src : str
        Image source path or URL.
    alt : str | None, optional
        Alternative text for the image for accessibility. Default is None.
    max_width : str, optional
        Maximum width of the image. Default is "500px".
    **props : dict
        Additional style properties to apply to the image.
        These will override the default styles.

    Returns
    -------
    rx.Component
        A Reflex image component with centered, styled presentation.
    """
    return rx.image(
        src=src,
        alt=alt,
        width=props.get("width", "100%"),
        max_width=props.get("max_width", max_width),
        height=props.get("height", "auto"),
        border_radius=props.get("border_radius", Layout.image_border_radius),
        box_shadow=props.get("box_shadow", Layout.image_box_shadow),
        margin_y=props.get("margin_y", "2rem"),
        loading=props.get("loading", "lazy"),
    )
