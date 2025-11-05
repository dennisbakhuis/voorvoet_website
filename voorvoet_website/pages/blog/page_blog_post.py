# Individual blog post page
import reflex as rx
from ...state import BlogState
from ...theme import Colors, FontSizes
from ...components import container, section, modal, markdown_content
from ..shared_sections import footer, header
from .section_hero import section_hero
from ...config import config


def page_blog_post() -> rx.Component:
    """
    Individual blog post page
    Shows the full blog post content with title, metadata, and rendered markdown
    """
    return rx.fragment(
        header(),
        section_hero(),

        # Main section with title, content, and back link
        section(
            container(
                rx.cond(
                    BlogState.current_post,
                    rx.vstack(
                        # Title
                        rx.heading(
                            BlogState.current_post.title,  # type: ignore (rx.cond not detected by type-checker)
                            size="9",
                            color=Colors.text['heading'],
                        ),

                        # Metadata row (only shown if at least one setting is enabled)
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
                                                BlogState.current_post.read_time.to(str) + " min leestijd",  # type: ignore (rx.cond not detected by type-checker)
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

                        # Blog content with custom styling
                        markdown_content(BlogState.current_post),  # type: ignore (rx.cond not detected by type-checker)

                        # Back to blog link
                        rx.link(
                            rx.text("← Terug naar blog overzicht"),
                            href="/blog/",
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

                    # Fallback if no post were found
                    rx.text(
                        "Blogpost niet gevonden",
                        color=Colors.text['muted'],
                        font_size=FontSizes.regular,
                    ),
                ),
            ),

            padding_top="1em",
        ),

        footer(),
        modal(),
    )
