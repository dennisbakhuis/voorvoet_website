"""Reusable image-text section component to eliminate layout duplication."""

import reflex as rx
from typing import Any
from collections.abc import Sequence

from ..theme import Layout, Spacing
from .header import header
from .regular_text import regular_text
from .button import button
from .responsive_image import responsive_image


def image_text_section(
    image_fallback: str,
    image_alt: str,
    title: str | rx.Var,
    paragraphs: str | rx.Var | Sequence[str | rx.Var],
    image_avif: str = "",
    image_webp: str = "",
    dimensions: dict[str, str] | None = None,
    image_position: str = "left",
    button_text: str | rx.Var | None = None,
    button_link: str | rx.Var | None = None,
    image_max_width: str | None = None,
    **section_props: Any,
) -> rx.Component:
    """
    Create a responsive section with image and text content.

    Creates a flexible two-column layout with an image on one side and
    text content (title, paragraphs, optional button) on the other.
    The layout automatically stacks on mobile and displays side-by-side
    on larger screens. Image position can be controlled via parameter.

    Parameters
    ----------
    image_fallback : str
        Path to the fallback image (JPG or PNG).
    image_alt : str
        Alt text for the image for accessibility and SEO.
    title : str | rx.Var
        Section title text.
    paragraphs : str | rx.Var | Sequence[str | rx.Var]
        Single paragraph string or sequence of paragraph strings.
        Multiple paragraphs are automatically spaced.
        Can be reactive variables from translations.
    image_avif : str, optional
        Path to the AVIF format image (empty string if not available).
    image_webp : str, optional
        Path to the WebP format image (empty string if not available).
    dimensions : dict[str, str], optional
        Image dimensions dict with 'width' and 'height' keys (e.g., ImageDimensions.content_portrait)
        Sets HTML attributes for aspect ratio to prevent CLS.
    image_position : str, optional
        Position of image relative to text: "left" or "right".
        Default is "left".
    button_text : str | rx.Var | None, optional
        Text for optional call-to-action button. Default is None.
    button_link : str | rx.Var | None, optional
        URL for optional call-to-action button. Default is None.
    image_max_width : str | None, optional
        Override for image maximum width. If None, uses Layout.image_max_width.
        Default is None.
    **section_props : dict
        Additional style properties to apply to the section container.
        These will override the default styles.

    Returns
    -------
    rx.Component
        A Reflex box component containing the image-text layout.

    Notes
    -----
    Both button_text and button_link must be provided for the button to appear.
    """

    paragraph_list: list[str | rx.Var]
    if isinstance(paragraphs, (str, rx.Var)):
        paragraph_list = [paragraphs]
    else:
        paragraph_list = list(paragraphs)

    image_element = responsive_image(
        src_fallback=image_fallback,
        src_avif=image_avif,
        src_webp=image_webp,
        alt=image_alt,
        dimensions=dimensions,
        width="100%",
        max_width=image_max_width or Layout.image_max_width,
        height="auto",
        border_radius=Layout.image_border_radius,
        box_shadow=Layout.image_box_shadow,
        loading="lazy",
    )

    image_column = rx.box(
        image_element,
        width=["100%", "100%", "35%", "35%"],
        flex=["1", "1", "0 0 auto", "0 0 auto"],
        display="flex",
        justify_content="center",
        align_items="center",
        margin_bottom=Spacing.image_margin_bottom,
        order=["1", "1", "1", "1"]
        if image_position == "left"
        else ["1", "1", "2", "2"],
    )

    text_content = [header(title, level=2, margin_bottom=Spacing.text_margin_bottom)]

    for i, paragraph in enumerate(paragraph_list):
        margin_bottom = (
            Spacing.text_margin_bottom if i < len(paragraph_list) - 1 else "0"
        )
        text_content.append(
            regular_text(paragraph, text_align="left", margin_bottom=margin_bottom)
        )

    if button_text and button_link:
        text_content.append(
            rx.box(
                button(button_text, href=button_link),
                margin_top=Spacing.button_margin_top,
                text_align="center",
            )
        )

    text_column = rx.box(
        *text_content,
        width=["100%", "100%", "auto", "auto"],
        flex=["1", "1", "1", "1"],
        order=["2", "2", "2", "2"]
        if image_position == "left"
        else ["2", "2", "1", "1"],
        display="flex",
        flex_direction="column",
        justify_content="center",
    )

    columns = [image_column, text_column]

    return rx.box(
        *columns,
        display=Layout.responsive_flex,
        gap=Spacing.section_gap,
        align_items="center",
        **section_props,
    )
