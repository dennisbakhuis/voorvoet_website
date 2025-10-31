# Centered image component for reusable centered image layouts
import reflex as rx
from typing import Optional
from ..theme import Layout


def centered_image(
    src: str,
    alt: Optional[str] = None,
    max_width: str = "500px",
    **props
) -> rx.Component:
    """
    Standard centered image component.
    
    Args:
        src: Image source path
        alt: Alt text for the image
        max_width: Maximum width of the image (default: 500px)
        **props: Additional props passed to the image
    """
    defaults = {
        "width": "100%",
        "max_width": max_width,
        "height": "auto",
        "border_radius": Layout.image_border_radius,
        "box_shadow": Layout.image_box_shadow,
        "margin_y": "2rem",
    }
    defaults.update(props)
    
    return rx.image(
        src=src,
        alt=alt,
        **defaults
    )