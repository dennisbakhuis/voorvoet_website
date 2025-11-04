# Blog card component for displaying blog post previews
import reflex as rx
from ....models import BlogPost
from ....theme import Colors, FontSizes, Layout
from ....config import config


def blog_card(post: BlogPost) -> rx.Component:
    """
    Display a single blog post card for the listing page

    Args:
        post: BlogPost object to display

    Returns:
        Reflex component representing the blog card
    """
    # Thumbnail URL is already resolved in BlogPost during loading

    return rx.link(
        rx.card(
            # Thumbnail image
            rx.image(
                src=post.thumbnail_url,
                alt=post.thumbnail_alt,
                width="100%",
                height="200px",
                object_fit="cover",
                border_radius="8px 8px 0 0",
            ),

            # Content area
            rx.vstack(
                # Title
                rx.heading(
                    post.title,
                    size="6",
                    color=Colors.text['heading'],
                    margin_bottom="0.5rem",
                    line_height="1.3",
                ),

                # Summary (truncated to 150 chars)
                rx.text(
                    post.summary,
                    color=Colors.text['content'],
                    font_size="0.95rem",
                    line_height="1.6",
                    margin_bottom="1rem",
                    overflow="hidden",
                    text_overflow="ellipsis",
                    display="-webkit-box",
                    style={
                        "-webkit-line-clamp": "3",
                        "-webkit-box-orient": "vertical",
                    },
                ),

                # Metadata row (only shown if at least one setting is enabled)
                rx.cond(
                    config.blog_show_author | config.blog_show_publication_date | config.blog_show_reading_time,
                    rx.hstack(
                        rx.cond(
                            config.blog_show_author,
                            rx.cond(
                                post.author,
                                rx.fragment(
                                    rx.text(
                                        post.author,
                                        color=Colors.text['content'],
                                        font_size="0.85rem",
                                    ),
                                    rx.text(
                                        "•",
                                        color=Colors.text['content'],
                                        font_size="0.85rem",
                                    ),
                                ),
                            ),
                        ),
                        rx.cond(
                            config.blog_show_publication_date,
                            rx.text(
                                post.formatted_date,
                                color=Colors.text['content'],
                                font_size="0.85rem",
                            ),
                        ),
                        rx.cond(
                            config.blog_show_reading_time,
                            rx.cond(
                                post.read_time,
                                rx.fragment(
                                    rx.cond(
                                        config.blog_show_publication_date,
                                        rx.text(
                                            "•",
                                            color=Colors.text['content'],
                                            font_size="0.85rem",
                                        ),
                                    ),
                                    rx.text(
                                        post.read_time.to(str) + " min leestijd",
                                        color=Colors.text['content'],
                                        font_size="0.85rem",
                                    ),
                                ),
                            ),
                        ),
                        spacing="2",
                        wrap="wrap",
                    ),
                ),

                # Read more link
                rx.text(
                    "Lees meer →",
                    color=Colors.primary['300'],
                    font_weight="600",
                    margin_top="1rem",
                ),

                spacing="3",
                align_items="start",
                padding="4",
            ),

            # Card styling
            border_radius="8px",
            box_shadow="0 4px 12px rgba(0, 0, 0, 0.1)",
            overflow="hidden",
            transition="all 0.3s ease",
            _hover={
                "box_shadow": "0 8px 20px rgba(0, 0, 0, 0.15)",
                "transform": "translateY(-4px)",
            },
        ),
        href="/blog/" + post.slug,
        text_decoration="none",
        _hover={"text_decoration": "none"},
    )
