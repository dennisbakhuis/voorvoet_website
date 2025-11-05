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

    Notes
    -----
    - Uses content text color from theme for readability
    - Regular font size (18px) for comfortable reading
    - Bottom margin of 1rem for proper paragraph spacing
    - Supports full inline markdown syntax
    - Renders as a markdown component to preserve formatting

    Examples
    --------
    >>> blog_paragraph("This is a simple paragraph.")
    >>> blog_paragraph("This paragraph has **bold** and *italic* text.")
    >>> blog_paragraph("Visit [our website](https://example.com) for more info.")
    """
    return rx.markdown(
        content,
        color=Colors.text['content'],
        font_size=FontSizes.regular,
        margin_bottom=Spacing.blog_content_margin_bottom,
    )
