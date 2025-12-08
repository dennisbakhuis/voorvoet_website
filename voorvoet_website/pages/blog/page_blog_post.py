"""Individual blog post page displaying full content."""

import reflex as rx
from typing import Any
from ...models import BlogPost
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
from .section_hero import section_hero
from ...config import config
from ...utils.get_translation import get_translation
from ...translations import BREADCRUMB_NAMES


TRANSLATIONS = {
    "nl": {
        "reading_time": "min leestijd",
        "back_to_blog": "← Terug naar blog overzicht",
        "post_not_found": "Blogpost niet gevonden",
        "translation_not_available": "Helaas is deze blogpost nog niet beschikbaar in het Nederlands. Schakel naar een andere taal om de inhoud te lezen.",
    },
    "de": {
        "reading_time": "Min. Lesezeit",
        "back_to_blog": "← Zurück zur Blog-Übersicht",
        "post_not_found": "Blogbeitrag nicht gefunden",
        "translation_not_available": "Leider ist dieser Blogbeitrag noch nicht auf Deutsch verfügbar. Wechseln Sie zu einer anderen Sprache, um den Inhalt zu lesen.",
    },
    "en": {
        "reading_time": "min read",
        "back_to_blog": "← Back to blog overview",
        "post_not_found": "Blog post not found",
        "translation_not_available": "Unfortunately, this blog post is not yet available in English. Switch to another language to read the content.",
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


def _build_content_components(
    content_objects: list[dict[str, Any]],
) -> list[rx.Component]:
    """Build all content components from content_objects list at compile time."""
    return [_build_content_component(obj) for obj in content_objects]


def page_blog_post(language: str = "nl", post: dict | None = None) -> rx.Component:
    """
    Create the individual blog post page with full content.

    Displays the complete blog post including title, metadata (author,
    date, reading time based on config), rendered markdown content,
    and a back link to the blog overview. Also includes Article structured
    data (JSON-LD) for SEO optimization.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")
    post : dict | None
        Blog post data as dictionary. If None, shows post not found message.

    Returns
    -------
    rx.Component
        A fragment containing header, hero, blog post content section,
        footer.
    """
    if post:
        title_val = post.get("title", "")
        author_val = post.get("author", "") or ""
        formatted_date_val = post.get("formatted_date", "")
        read_time_val = str(post.get("read_time", "")) if post.get("read_time") else ""
        content_objects_val = post.get("content_objects", [])

        content_components = _build_content_components(content_objects_val)

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
                rx.text(
                    formatted_date_val, color=Colors.text["content"], font_size="1rem"
                )
            )

        if config.blog_show_reading_time and read_time_val:
            if metadata_components:
                metadata_components.append(
                    rx.text("•", color=Colors.text["content"], font_size="1rem")
                )
            metadata_components.append(
                rx.text(
                    read_time_val
                    + " "
                    + get_translation(TRANSLATIONS, "reading_time", language),
                    color=Colors.text["content"],
                    font_size="1rem",
                )
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

        try:
            blog_post_obj = BlogPost(**post)
            article_schema_component = article_schema(blog_post_obj, language)
        except Exception:
            article_schema_component = rx.fragment()

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
    else:
        content_component = rx.vstack(
            rx.text(
                get_translation(TRANSLATIONS, "post_not_found", language),
                color=Colors.text["muted"],
                font_size=FontSizes.regular,
            ),
            rx.text(
                get_translation(TRANSLATIONS, "translation_not_available", language),
                color=Colors.text["content"],
                font_size=FontSizes.regular,
                text_align="center",
            ),
            rx.link(
                rx.text(get_translation(TRANSLATIONS, "back_to_blog", language)),
                href=f"/{language}/blog/",
                color=Colors.primary["500"],
                font_size=FontSizes.regular,
                font_weight="600",
                text_decoration="none",
                margin_top="1rem",
                _hover={
                    "text_decoration": "underline",
                },
            ),
            spacing="3",
            align_items="center",
            width="100%",
            padding="2rem",
        )
        article_schema_component = rx.fragment()
        breadcrumb_schema_component = rx.fragment()

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
