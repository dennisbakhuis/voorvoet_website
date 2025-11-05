"""Hero banner component with background image and optional content overlay."""
import reflex as rx
from ..theme import Colors


def hero_banner(
    image_src: str,
    gradient: str = "linear-gradient(180deg, rgba(255,255,255,.55) 0%, rgba(16,185,129,.35) 100%)",
    content: rx.Component | None = None,
) -> rx.Component:
    """
    Create a hero banner with background image and optional overlay content.

    The hero banner displays a full-width background image with an optional
    gradient overlay and custom content. It absolutely positions itself to fill
    its parent container (typically a section with height and clip_bottom set).

    Important: The parent section should set the height, not this component.
    This allows the banner to properly extend to edges for clip path effects.

    Parameters
    ----------
    image_src : str
        Path to the background image.
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

    Examples
    --------
    Simple hero banner (parent section controls height):
        >>> section(
        ...     hero_banner(image_src="/images/hero.jpg"),
        ...     height="500px",
        ...     clip_bottom="gentle_1"
        ... )

    Hero banner with custom content:
        >>> section(
        ...     hero_banner(
        ...         image_src="/images/hero.jpg",
        ...         content=rx.text("Welcome", font_size="3rem")
        ...     ),
        ...     height=["70vh", "80vh"],
        ...     clip_bottom="gentle_1"
        ... )
    """
    children = [
        rx.image(
            src=image_src,
            object_fit="cover",
            position="absolute",
            inset="0",
            width="100%",
            height="100%",
            filter="brightness(1.05) saturate(1.06)",
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
