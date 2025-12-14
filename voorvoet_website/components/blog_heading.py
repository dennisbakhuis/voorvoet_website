"""Blog header component with blog-specific styling overrides."""

import reflex as rx
from ..theme import Spacing
from .header import header


def blog_header(text: str | rx.Var, level: int = 2) -> rx.Component:
    """
    Create a blog-styled heading with appropriate spacing.

    Wraps the standard header component with blog-specific margin spacing.
    Uses the base header component for semantic HTML and consistent sizing,
    but adds blog-appropriate vertical spacing.

    Parameters
    ----------
    text : str | rx.Var
        The text content of the heading.
    level : int, optional
        Heading level from 1 to 6 (default: 2).

    Returns
    -------
    rx.Component
        A Reflex heading component with blog-specific spacing.
    """
    return header(
        text,
        level=level,
        margin_top=Spacing.blog_heading_margin_top,
        margin_bottom=Spacing.blog_heading_margin_bottom,
    )
