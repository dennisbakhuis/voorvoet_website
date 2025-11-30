"""Blog page composition with all sections."""

import reflex as rx

from .section_hero import section_hero
from .section_blog_list import section_blog_list
from .section_starter import section_starter

from ..shared_sections import footer, header
from ...components import breadcrumb_schema
from ...translations import BREADCRUMB_NAMES
from ...config import config


def page_blog(language: str = "nl", posts: list = []) -> rx.Component:
    """
    Create the complete blog page with all sections.

    The blog page is composed of: header, hero banner, starter text,
    blog list grid, footer. The page title is
    dynamically set based on the current language.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")
    posts : list
        List of blog post dictionaries to display for the given language

    Returns
    -------
    rx.Component
        A fragment containing all sections of the blog page in order.
    """
    breadcrumb_items = [
        {
            "name": BREADCRUMB_NAMES.get(language, {}).get("home", "Home"),
            "url": f"{config.site_url}/{language}",
        },
        {
            "name": BREADCRUMB_NAMES.get(language, {}).get("blog", "Blog"),
            "url": f"{config.site_url}/{language}/blog/",
        },
    ]

    return rx.fragment(
        breadcrumb_schema(breadcrumb_items),
        header(language, page_key="blog"),
        section_hero(),
        section_starter(language),
        section_blog_list(language, posts),
        footer(language),
    )
