"""Blog heading component for rendering headings with dynamic levels."""

import reflex as rx
from ..theme import Colors, FontSizes, Spacing


def blog_heading(content: str, level: int = 2) -> rx.Component:
    """
    Create a styled heading for blog content with dynamic level support.

    Renders a heading element (h1-h3) with appropriate responsive sizing based
    on the level parameter. Provides consistent styling for heading levels used
    in blog posts. Only supports levels 1-3 as these are the most commonly used
    in blog content.

    Parameters
    ----------
    content : str
        The text content of the heading
    level : int, optional
        Heading level from 1 to 3, where 1 is largest (default: 2)
        - Level 1: Responsive [1.5rem, 1.75rem, 2rem, 2.25rem] (matches section_title)
        - Level 2: Responsive [1.375rem, 1.5rem, 1.75rem, 1.875rem]
        - Level 3: Responsive [1.25rem, 1.375rem, 1.5rem, 1.625rem]

    Returns
    -------
    rx.Component
        A Reflex heading component with theme-consistent responsive styling

    Notes
    -----
    - All headings use the heading color from theme
    - Responsive font sizes that scale with viewport width
    - Consistent margin spacing from theme (2rem top, 1rem bottom)
    - Font weight is always 700 (bold)
    - Level parameter is used dynamically with rx.cond for Reflex compatibility
    - H1 matches section_title size for consistency across the site

    Examples
    --------
    >>> blog_heading("Introduction", level=1)  # Main title (largest)
    >>> blog_heading("Key Points", level=2)    # Section heading
    >>> blog_heading("Details", level=3)       # Subsection heading
    """
    return rx.heading(
        content,
        as_=f"h{level}",
        font_size=rx.cond(
            level == 1,
            FontSizes.blog_heading_h1,
            rx.cond(level == 2, FontSizes.blog_heading_h2, FontSizes.blog_heading_h3),
        ),
        color=Colors.text["heading"],
        margin_top=Spacing.blog_heading_margin_top,
        margin_bottom=Spacing.blog_heading_margin_bottom,
        font_weight="700",
    )
