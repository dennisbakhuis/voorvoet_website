"""Blog markdown component for rendering mixed markdown content blocks."""

import reflex as rx
from ..theme import Colors, FontSizes, Spacing


def blog_markdown(content: str) -> rx.Component:
    """
    Create a styled markdown block for blog content.

    Renders markdown content blocks that may contain multiple elements like
    paragraphs, lists, code blocks, blockquotes, etc. Used for larger content
    sections that don't fit into specific component types.

    Parameters
    ----------
    content : str
        The markdown content to render, which may include multiple markdown
        elements such as paragraphs, headings, lists, code blocks, blockquotes,
        links, images, and inline formatting

    Returns
    -------
    rx.Component
        A Reflex markdown component styled for blog content blocks
    """
    return rx.box(
        rx.markdown(  # type: ignore[operator]  # Due to missing stubs in Relfex
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
            "& h1, & h2, & h3, & h4, & h5, & h6": {
                "marginTop": Spacing.blog_heading_margin_top,
                "marginBottom": Spacing.blog_heading_margin_bottom,
                "color": Colors.text["heading"],
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
