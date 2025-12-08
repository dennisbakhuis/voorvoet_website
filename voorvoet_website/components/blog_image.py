"""Blog image component for rendering images with optional captions."""

import reflex as rx
from ..theme import Colors, FontSizes, Spacing, Layout
from .responsive_image import responsive_image


def blog_image(src: str, alt: str, caption: str = "") -> rx.Component:
    """
    Create a styled image for blog content with optional caption.

    Parameters
    ----------
    src : str
        The image source URL or path (absolute or relative)
    alt : str
        Alternative text for the image (for accessibility and SEO)
    caption : str, optional
        Optional caption text to display below the image (default: "")
        Caption is displayed in italic, muted color, and centered

    Returns
    -------
    rx.Component
        A Reflex box component containing the styled image and optional caption
    """
    return rx.box(
        responsive_image(
            src=src,
            alt=alt,
            loading="lazy",
        ),
        rx.cond(
            caption != "",
            rx.text(
                caption,
                color=Colors.text["muted"],
                font_size=FontSizes.regular,
                font_style="italic",
                text_align="center",
                margin_top=Spacing.blog_caption_margin_top,
            ),
        ),
        display="block",
        margin=Spacing.blog_image_margin,
        max_width=Layout.blog_image_max_width,
        width="100%",
        style={
            "& img": {
                "display": "block",
                "margin": "0 auto",
                "max_width": "100%",
                "width": "100%",
                "height": "auto",
                "border_radius": Layout.blog_image_border_radius,
                "box_shadow": Layout.image_box_shadow,
            }
        },
    )
