"""Blog paragraph component for rendering paragraph text with markdown support."""

import reflex as rx
from ..theme import Colors, FontSizes, Spacing


def blog_paragraph(content: str) -> rx.Component:
    """
    Create a styled paragraph for blog content with markdown support.

    Renders paragraph text using Reflex's markdown component, allowing for
    inline formatting like bold, italic, links, and code within the paragraph.
    Provides consistent styling for all paragraph content in blog posts.

    Parameters
    ----------
    content : str
        The paragraph text content, which may include inline markdown formatting
        such as **bold**, *italic*, [links](url), and `code`

    Returns
    -------
    rx.Component
        A Reflex markdown component styled for blog paragraphs
    """
    return rx.box(
        rx.markdown(
            content,
            color=Colors.text["content"],
            font_size=FontSizes.regular,
        ),
        margin_bottom=Spacing.blog_content_margin_bottom,
        style={
            "& p": {
                "marginTop": "0",
                "marginBottom": "0",
            },
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
