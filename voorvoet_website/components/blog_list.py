"""Blog list component for rendering ordered and unordered lists."""

import reflex as rx
from ..theme import Colors, FontSizes, Spacing


def blog_list(markdown: str) -> rx.Component:
    """
    Create a styled list for blog content from markdown format.

    Parameters
    ----------
    markdown : str
        The list content in markdown format, either:
        - Unordered list: lines starting with "- " or "* "
        - Ordered list: lines starting with "1. ", "2. ", etc.
        Can include inline markdown formatting within list items

    Returns
    -------
    rx.Component
        A Reflex markdown component that renders the list with proper styling
    """
    return rx.box(
        rx.markdown(  # type: ignore[operator]  # Due to missing stubs in Relfex
            markdown,
            color=Colors.text["content"],
            font_size=FontSizes.regular,
        ),
        margin_bottom=Spacing.blog_content_margin_bottom,
        style={
            "& a": {
                "color": f"{Colors.primary['300']} !important",
                "textDecoration": "underline",
                "transition": "color 0.2s ease",
            },
            "& a:hover": {
                "color": f"{Colors.primary['700']} !important",
            },
        },
    )
