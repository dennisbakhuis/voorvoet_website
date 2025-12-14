"""Individual blog post page displaying full content."""

import reflex as rx
from typing import Any

from ...models import BlogPostDict
from ...theme import Colors, FontSizes, Spacing
from ...components import (
    container,
    section,
    article_schema,
    breadcrumb_schema,
    blog_header,
    blog_paragraph,
    blog_markdown,
    blog_image,
    blog_list,
    button,
)
from ..shared_sections import footer, header
from ...config import config
from ...utils import get_translation
from ...translations import BREADCRUMB_NAMES

from .section_hero import section_hero


TRANSLATIONS = {
    "nl": {
        "back_to_blog": "← Terug naar blog overzicht",
    },
    "de": {
        "back_to_blog": "← Zurück zur Blog-Übersicht",
    },
    "en": {
        "back_to_blog": "← Back to blog overview",
    },
}


def _build_content_component(obj: dict[str, Any]) -> rx.Component:
    """Build a single content component from a content object dict at compile time."""
    content_type = obj.get("type", "")

    if content_type == "heading":
        return blog_header(obj.get("content", ""), obj.get("level", 2))
    elif content_type == "paragraph":
        return blog_paragraph(obj.get("content", ""))
    elif content_type == "markdown":
        return blog_markdown(obj.get("content", ""))
    elif content_type == "image":
        return blog_image(
            src_fallback=obj.get("src_fallback", ""),
            alt=obj.get("alt", ""),
            src_avif=obj.get("src_avif", ""),
            src_webp=obj.get("src_webp", ""),
            caption=obj.get("caption", ""),
        )
    elif content_type == "button":
        return rx.box(
            button(label=obj.get("label", ""), href=obj.get("url", "")),
            display="flex",
            justify_content="center",
            width="100%",
            margin_y="1.5rem",
        )
    elif content_type == "list":
        return blog_list(obj.get("markdown", ""))
    else:
        return rx.box()


def page_blog_post(
    post: BlogPostDict,
    language: str = "nl",
) -> rx.Component:
    """
    Create the individual blog post page with full content.

    Parameters
    ----------
    post : BlogPostDict
        Blog post data as dictionary.
    language : str
        Current language code ("nl", "de", or "en")

    Returns
    -------
    rx.Component
        A fragment containing header, hero, blog post content section,
        footer.
    """
    title_val = post.get("title", "")
    author_val = post.get("author", "") or ""
    formatted_date_val = post.get("formatted_date", "")
    content_objects_val = post.get("content_objects", [])

    content_components = [_build_content_component(obj) for obj in content_objects_val]

    metadata_components = []
    if config.blog_show_author and author_val:
        metadata_components.append(
            rx.text(author_val, color=Colors.text["content"], font_size="1rem")
        )
        metadata_components.append(
            rx.text("•", color=Colors.text["content"], font_size="1rem")
        )

    if config.blog_show_publication_date:
        metadata_components.append(
            rx.text(formatted_date_val, color=Colors.text["content"], font_size="1rem")
        )

    page_components: list[rx.Component] = [
        rx.heading(
            title_val,
            as_="h1",
            font_size=FontSizes.section_title,
            color=Colors.text["heading"],
            margin_bottom=Spacing.blog_heading_margin_bottom,
        )
    ]

    if metadata_components:
        page_components.append(
            rx.hstack(
                *metadata_components,
                spacing="2",
                wrap="wrap",
                margin_bottom="2rem",
            )
        )

    page_components.extend(content_components)

    page_components.append(
        rx.link(
            rx.text(get_translation(TRANSLATIONS, "back_to_blog", language)),
            href=f"/{language}/blog/",
            color=Colors.primary["500"],
            font_size=FontSizes.regular,
            font_weight="600",
            text_decoration="none",
            margin_top="3rem",
            _hover={
                "text_decoration": "underline",
            },
        )
    )

    content_component = rx.vstack(
        *page_components,
        spacing="0",
        align_items="start",
        width="100%",
    )

    article_schema_component = article_schema(post, language)

    breadcrumb_items = [
        {
            "name": BREADCRUMB_NAMES.get(language, {}).get("home", "Home"),
            "url": f"{config.site_url}/{language}",
        },
        {
            "name": BREADCRUMB_NAMES.get(language, {}).get("blog", "Blog"),
            "url": f"{config.site_url}/{language}/blog/",
        },
        {
            "name": title_val,
            "url": f"{config.site_url}/{language}/blog/{post.get('slug', '')}/",
        },
    ]
    breadcrumb_schema_component = breadcrumb_schema(breadcrumb_items)

    return rx.fragment(
        article_schema_component,
        breadcrumb_schema_component,
        header(language, page_key="blog"),
        rx.box(
            section_hero(language),
            section(
                container(
                    content_component,
                ),
                padding_top="1em",
                padding_bottom="2em",
            ),
            id="main-content",
            role="main",
        ),
        footer(language),
    )
