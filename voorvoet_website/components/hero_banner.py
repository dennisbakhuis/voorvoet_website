"""Hero banner component with background image and optional content overlay."""

import reflex as rx
from .responsive_image import responsive_image


def hero_banner(
    image_src_fallback: str,
    alt_text: str,
    image_src_avif: str = "",
    image_src_webp: str = "",
    gradient: str = "linear-gradient(180deg, rgba(255,255,255,.55) 0%, rgba(16,185,129,.35) 100%)",
    content: rx.Component | None = None,
) -> rx.Component:
    """
    Create a hero banner with background image and optional overlay content.

    Parameters
    ----------
    image_src_fallback : str
        Path to the fallback background image (JPG or PNG).
    alt_text : str
        Alt text for the background image for accessibility and SEO.
    image_src_avif : str, optional
        Path to the AVIF format image (empty string if not available).
    image_src_webp : str, optional
        Path to the WebP format image (empty string if not available).
    gradient : str, optional
        CSS gradient overlay applied over the image.
        Default is a white-to-green gradient with screen blend mode.
    content : rx.Component | None, optional
        Optional content to overlay on the hero banner.
        If None, only the image and gradient are displayed.
        Default is None.

    Returns
    -------
    rx.Component
        An absolutely positioned box that fills its parent container,
        containing the background image, gradient overlay, and optional content.
    """
    children = [
        responsive_image(
            src_fallback=image_src_fallback,
            src_avif=image_src_avif,
            src_webp=image_src_webp,
            alt=alt_text,
            object_fit="cover",
            position="absolute",
            inset="0",
            width="100%",
            height="100%",
            filter="brightness(1.05) saturate(1.06)",
            loading="eager",
        ),
        rx.box(
            position="absolute",
            inset="0",
            bg=gradient,
            mix_blend_mode="screen",
            pointer_events="none",
        ),
    ]

    if content is not None:
        children.append(content)

    return rx.box(
        *children,
        position="absolute",
        inset="0",
        height="100%",
        width="100%",
        overflow="hidden",
    )
