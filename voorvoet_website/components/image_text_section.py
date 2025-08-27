# Reusable image-text section component to eliminate layout duplication
import reflex as rx
from typing import Optional, Union

from ..theme import Colors, FontSizes, Layout, Spacing, responsive_padding
from .column import column
from .section_title import section_title
from .regular_text import regular_text
from .button import button


def image_text_section(
    image_src: str,
    title: str,
    paragraphs: Union[str, list[str]],
    image_position: str = "left",  # "left" or "right"
    button_text: Optional[str] = None,
    button_link: Optional[str] = None,
    **section_props
) -> rx.Component:
    """
    Generic image-text layout component that eliminates duplication across sections.
    
    Args:
        image_src: Path to the image
        title: Section title
        paragraphs: Single paragraph string or list of paragraph strings
        image_position: "left" or "right" - where to position the image
        button_text: Optional button text
        button_link: Optional button link
        **section_props: Additional props passed to the container
    """
    
    # Handle single paragraph or multiple paragraphs
    if isinstance(paragraphs, str):
        paragraph_list = [paragraphs]
    else:
        paragraph_list = paragraphs
    
    # Create image column
    image_column = column(
        rx.image(
            src=image_src,
            width="100%",
            max_width=Layout.image_max_width,
            height="auto",
            border_radius=Layout.image_border_radius,
            box_shadow=Layout.image_box_shadow,
        ),
        size=Layout.image_column_size,
        padding_right=responsive_padding("right") if image_position == "left" else ["0", "0", "0", "0"],
        padding_left=responsive_padding("left") if image_position == "right" else ["0", "0", "0", "0"],
        display="flex",
        justify_content="center",
        align_items="center",
        margin_bottom=Spacing.image_margin_bottom,
    )
    
    # Create text content
    text_content = [
        section_title(title, margin_bottom=Spacing.text_margin_bottom)
    ]
    
    # Add paragraphs
    for i, paragraph in enumerate(paragraph_list):
        margin_bottom = Spacing.text_margin_bottom if i < len(paragraph_list) - 1 else "0"
        text_content.append(
            regular_text(
                paragraph,
                text_align="left",
                margin_bottom=margin_bottom
            )
        )
    
    # Add button if provided
    if button_text and button_link:
        text_content.append(
            rx.box(
                button(button_text, href=button_link),
                margin_top=Spacing.button_margin_top
            )
        )
    
    # Create text column  
    text_column = column(
        *text_content,
        size=Layout.text_column_size,
        padding_left=responsive_padding("left") if image_position == "left" else ["0", "0", "0", "0"],
        padding_right=responsive_padding("right") if image_position == "right" else ["0", "0", "0", "0"],
    )
    
    # Order columns based on image position
    if image_position == "left":
        columns = [image_column, text_column]
    else:
        columns = [text_column, image_column]
    
    # Create the responsive layout
    return rx.box(
        *columns,
        display=Layout.responsive_flex,
        gap=Spacing.section_gap,
        align_items="center",
        **section_props
    )