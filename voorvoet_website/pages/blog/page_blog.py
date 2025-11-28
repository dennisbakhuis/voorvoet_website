"""Blog page composition with all sections."""
import reflex as rx

from .section_hero import section_hero
from .section_blog_list import section_blog_list
from .section_starter import section_starter

from ..shared_sections import footer, header
from ...components import modal
from ...utils.translations import get_language_from_path


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
    language = get_language_from_path()

    return rx.fragment(
        header(language, page_key="blog"),
        section_hero(),
        section_starter(language),
        section_blog_list(language),
        footer(language),
        modal(),
    )
