"""Blog page composition with all sections."""
import reflex as rx

from .section_hero import section_hero
from .section_blog_list import section_blog_list
from .section_starter import section_starter

from ..shared_sections import footer, header
from ...components import modal


def page_blog() -> rx.Component:
    """
    Create the complete blog page with all sections.

    The blog page is composed of: header, hero banner, starter text,
    blog list grid, footer, and modal components. The page title is
    dynamically set based on the current language.

    Returns
    -------
    rx.Component
        A fragment containing all sections of the blog page in order.
    """
    return rx.fragment(
        header(),
        section_hero(),
        section_starter(),
        section_blog_list(),
        footer(),
        modal(),
    )
