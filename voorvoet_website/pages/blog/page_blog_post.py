"""Individual blog post page displaying full content."""
import reflex as rx
from typing import Optional
from ...models import BlogPost
from ...theme import Colors, FontSizes
from ...components import container, section, markdown_content, article_schema
from ..shared_sections import footer, header
from .section_hero import section_hero
from ...config import config
from ...utils.get_translation import get_translation


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


def page_blog_post(language: str="nl", post: Optional[dict] = None) -> rx.Component:
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
    post : Optional[dict]
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
        content_val = post.get("content", "")

        content_component = rx.vstack(
            rx.heading(
                title_val,
                font_size=FontSizes.section_title,
                color=Colors.text['heading'],
            ),

            rx.cond(
                config.blog_show_author | config.blog_show_publication_date | config.blog_show_reading_time,
                rx.hstack(
                    rx.cond(
                        config.blog_show_author & (author_val != ""),
                        rx.fragment(
                            rx.text(
                                author_val,
                                color=Colors.text['content'],
                                font_size="1rem",
                            ),
                            rx.text(
                                "•",
                                color=Colors.text['content'],
                                font_size="1rem",
                            ),
                        ),
                    ),
                    rx.cond(
                        config.blog_show_publication_date,
                        rx.text(
                            formatted_date_val,
                            color=Colors.text['content'],
                            font_size="1rem",
                        ),
                    ),
                    rx.cond(
                        config.blog_show_reading_time & (read_time_val != ""),
                        rx.fragment(
                            rx.cond(
                                config.blog_show_publication_date,
                                rx.text(
                                    "•",
                                    color=Colors.text['content'],
                                    font_size="1rem",
                                ),
                            ),
                            rx.text(
                                read_time_val + " " + get_translation(TRANSLATIONS, "reading_time", language),
                                color=Colors.text['content'],
                                font_size="1rem",
                            ),
                        ),
                    ),
                    spacing="2",
                    wrap="wrap",
                    margin_bottom="2rem",
                ),
            ),

            rx.markdown(content_val),

            rx.link(
                rx.text(get_translation(TRANSLATIONS, "back_to_blog", language)),
                href=f"/{language}/blog/",
                color=Colors.primary['500'],
                font_size=FontSizes.regular,
                font_weight="600",
                text_decoration="none",
                margin_top="3rem",
                _hover={
                    "text_decoration": "underline",
                },
            ),

            spacing="3",
            align_items="start",
            width="100%",
        )

        blog_post_obj = BlogPost(**post)
        schema_component = article_schema(blog_post_obj, language)
    else:
        content_component = rx.vstack(
            rx.text(
                get_translation(TRANSLATIONS, "post_not_found", language),
                color=Colors.text['muted'],
                font_size=FontSizes.regular,
            ),
            rx.text(
                get_translation(TRANSLATIONS, "translation_not_available", language),
                color=Colors.text['content'],
                font_size=FontSizes.regular,
                text_align="center",
            ),
            rx.link(
                rx.text(get_translation(TRANSLATIONS, "back_to_blog", language)),
                href=f"/{language}/blog/",
                color=Colors.primary['500'],
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
        schema_component = rx.fragment()

    return rx.fragment(
        schema_component,
        header(language, page_key="blog"),
        section_hero(),
        section(
            container(
                content_component,
            ),
            padding_top="1em",
        ),
        footer(language),
    )
