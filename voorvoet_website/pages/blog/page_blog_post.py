"""Individual blog post page displaying full content."""
import reflex as rx
from ...states import BlogState
from ...theme import Colors, FontSizes
from ...components import container, section, modal, markdown_content, article_schema
from ..shared_sections import footer, header
from .section_hero import section_hero
from ...config import config
from ...utils.translations import get_translation, get_language_from_path


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


def page_blog_post() -> rx.Component:
    """
    Create the individual blog post page with full content.

    Displays the complete blog post including title, metadata (author,
    date, reading time based on config), rendered markdown content,
    and a back link to the blog overview. Also includes Article structured
    data (JSON-LD) for SEO optimization.

    Returns
    -------
    rx.Component
        A fragment containing header, hero, blog post content section,
        footer, and modal components.
    """
    language = get_language_from_path()

    return rx.fragment(
        # Add Article schema for SEO (automatically handles empty state)
        article_schema(),

        header(language, page_key="blog"),
        section_hero(),

        section(
            container(
                rx.cond(
                    BlogState.current_post,
                    rx.vstack(
                        rx.heading(
                            BlogState.current_post.title,  # type: ignore (rx.cond not detected by type-checker)
                            font_size=FontSizes.section_title,
                            color=Colors.text['heading'],
                        ),

                        rx.cond(
                            config.blog_show_author | config.blog_show_publication_date | config.blog_show_reading_time,
                            rx.hstack(
                                rx.cond(
                                    config.blog_show_author,
                                    rx.cond(
                                        BlogState.current_post.author,  # type: ignore (rx.cond not detected by type-checker)
                                        rx.fragment(
                                            rx.text(
                                                BlogState.current_post.author,  # type: ignore (rx.cond not detected by type-checker)
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
                                ),
                                rx.cond(
                                    config.blog_show_publication_date,
                                    rx.text(
                                        BlogState.current_post.formatted_date,  # type: ignore (rx.cond not detected by type-checker)
                                        color=Colors.text['content'],
                                        font_size="1rem",
                                    ),
                                ),
                                rx.cond(
                                    config.blog_show_reading_time,
                                    rx.cond(
                                        BlogState.current_post.read_time,  # type: ignore (rx.cond not detected by type-checker)
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
                                                BlogState.current_post.read_time.to(str) + " " + get_translation(TRANSLATIONS, "reading_time", language),  # type: ignore (rx.cond not detected by type-checker)
                                                color=Colors.text['content'],
                                                font_size="1rem",
                                            ),
                                        ),
                                    ),
                                ),
                                spacing="2",
                                wrap="wrap",
                                margin_bottom="2rem",
                            ),
                        ),

                        markdown_content(BlogState.current_post),  # type: ignore (rx.cond not detected by type-checker)

                        rx.link(
                            rx.text(get_translation(TRANSLATIONS, "back_to_blog", language)),
                            href=f"/{BlogState.current_language}/blog/",
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
                    ),

                    rx.vstack(
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
                            href=f"/{BlogState.current_language}/blog/",
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
                    ),
                ),
            ),

            padding_top="1em",
        ),

        footer(language),
        modal(),
    )
