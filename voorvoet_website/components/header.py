"""Standard header component for all semantic heading levels h1-h6."""

from typing import Union
import reflex as rx
from ..theme import Colors, FontSizes


def header(text: Union[str, rx.Var], level: int = 2, **props) -> rx.Component:
    """
    Create a semantic heading with standardized styling.

    Renders a heading element (h1-h6) with theme-consistent responsive sizing.
    This is the standard component for all headings across the site.

    Parameters
    ----------
    text : str | rx.Var
        The heading text to display. Can be a string or reactive variable.
    level : int, optional
        Heading level from 1 to 6 (default: 2).
        - Level 1: Hero/page title [2.5rem, 4rem, 5rem, 6rem]
        - Level 2: Section title [1.5rem, 1.75rem, 2rem, 2.25rem]
        - Level 3: Subsection title [1.25rem, 1.5rem, 1.75rem, 1.875rem]
        - Level 4-6: Minor headings [1.125rem, 1.25rem, 1.375rem, 1.5rem]
    **props : dict
        Additional style properties to apply to the heading.
        These will override the default styles.

    Returns
    -------
    rx.Component
        A Reflex heading component with semantic HTML and theme styling.

    Examples
    --------
    >>> header("Main Page Title", level=1)  # <h1> with hero styling
    >>> header("Section Title", level=2)     # <h2> with section styling
    >>> header("Subsection", level=3)        # <h3> with subsection styling
    """
    # Map levels to theme font sizes
    font_size_map = {
        1: FontSizes.hero_title,
        2: FontSizes.section_title,
        3: FontSizes.section_sub_title,
        4: ["1.125rem", "1.25rem", "1.375rem", "1.5rem"],
        5: ["1rem", "1.125rem", "1.25rem", "1.375rem"],
        6: ["1rem", "1.125rem", "1.25rem", "1.25rem"],
    }

    # Get font size for the specified level, default to level 2 if invalid
    font_size = font_size_map.get(level, FontSizes.section_title)

    # Set default styles that can be overridden by props
    default_styles = {
        "font_size": font_size,
        "font_weight": "700",
        "color": Colors.text["heading"],
    }

    # Merge defaults with props, with props taking precedence
    merged_styles = {**default_styles, **props}

    return rx.heading(
        text,
        as_=f"h{level}",
        **merged_styles,
    )
