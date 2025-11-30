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

    Notes
    -----
    - Uses content text color from theme
    - Regular font size (18px) for readability
    - Bottom margin of 1rem for spacing between blocks
    - Links styled with brand colors (brand 500) with hover effect (brand 300)
    - Supports full markdown syntax including:
        - Headings (# ## ###)
        - Lists (ordered and unordered)
        - Code blocks (```language```)
        - Blockquotes (>)
        - Links and images
        - Bold, italic, strikethrough
        - Tables
    - Use this for content that doesn't need to be split into separate components

    Examples
    --------
    >>> blog_markdown("This is **bold** and this is *italic*.")
    >>> blog_markdown("# Heading\\n\\nParagraph text\\n\\n- List item\\n- Another item")
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
