"""Blog list component for rendering ordered and unordered lists."""
import reflex as rx
from ..theme import Colors, FontSizes, Spacing


def blog_list(markdown: str) -> rx.Component:
    """
    Create a styled list for blog content from markdown format.

    Renders list content (both ordered and unordered) by converting it back
    to markdown format and rendering as a markdown block. This approach is
    used because Reflex does not support nested rx.foreach operations, which
    would be needed to dynamically render list items within a foreach loop.

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

    Notes
    -----
    - Uses content text color from theme for readability
    - Regular font size (18px) for comfortable reading
    - Bottom margin of 1rem for spacing between content blocks
    - Supports both ordered (numbered) and unordered (bulleted) lists
    - Supports nested lists if properly formatted in markdown
    - List items can contain inline markdown (bold, italic, links, code)
    - Rendered as markdown due to Reflex limitation with nested foreach

    Technical Note
    --------------
    This component exists because Reflex cannot nest rx.foreach calls.
    The ideal approach would be to use rx.foreach to iterate over list items,
    but this causes compilation errors. Instead, we keep the list in markdown
    format and let Reflex's markdown renderer handle it.

    Examples
    --------
    >>> blog_list("- First item\\n- Second item\\n- Third item")
    >>> blog_list("1. First step\\n2. Second step\\n3. Third step")
    >>> blog_list("- Item with **bold** text\\n- Item with [link](url)")
    """
    return rx.markdown(
        markdown,
        color=Colors.text['content'],
        font_size=FontSizes.regular,
        margin_bottom=Spacing.blog_content_margin_bottom,
    )
