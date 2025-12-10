"""Blog card component for displaying blog post previews."""

import reflex as rx

from .responsive_image import responsive_image

from ..models import BlogPost
from ..theme import Colors, FontSizes, Layout, ImageDimensions
from ..config import config


def blog_card(
    post: BlogPost | dict, language: str = "nl", flip: bool = False
) -> rx.Component:
    """
    Display a blog post card in landscape layout with thumbnail and content.

    Parameters
    ----------
    post : BlogPost or dict
        BlogPost object or dictionary containing all post data and metadata.
    language : str
        Current language code ("nl", "de", or "en")
    flip : bool, optional
        If True, thumbnail appears on the right side; if False, on the left.
        Default is False.

    Returns
    -------
    rx.Component
        A Reflex link component wrapping the styled blog card.
    """
    if isinstance(post, dict):
        post = BlogPost(**post)

    content_area = rx.vstack(
        rx.heading(
            post.title,
            size="6",
            color=Colors.text["heading"],
            margin_top="1.0rem",
            margin_bottom="-0.2rem",
            line_height="1.3",
        ),
        rx.text(
            post.summary,
            color=Colors.text["content"],
            font_size=FontSizes.regular,
            line_height="1.6",
            margin_bottom="0.5rem",
        ),
        rx.cond(
            config.blog_show_author
            | config.blog_show_publication_date
            | config.blog_show_reading_time,
            rx.hstack(
                rx.cond(
                    config.blog_show_author,
                    rx.cond(
                        post.author,
                        rx.fragment(
                            rx.text(
                                post.author,
                                color=Colors.text["muted"],
                                font_size="0.85rem",
                            ),
                            rx.text(
                                "•",
                                color=Colors.text["muted"],
                                font_size="0.85rem",
                            ),
                        ),
                    ),
                ),
                rx.cond(
                    config.blog_show_publication_date,
                    rx.text(
                        post.formatted_date,
                        color=Colors.text["muted"],
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
                                    color=Colors.text["muted"],
                                    font_size="0.85rem",
                                ),
                            ),
                            rx.text(
                                f"{post.read_time} min leestijd",
                                color=Colors.text["muted"],
                                font_size="0.85rem",
                            ),
                        ),
                    ),
                ),
                spacing="2",
                wrap="wrap",
            ),
        ),
        rx.text(
            "Lees meer →",
            color=Colors.primary["500"],
            font_weight="600",
            font_size=FontSizes.regular,
            margin_top="auto",
        ),
        align_items="start",
        justify_content="center",
        padding_top="4",
        flex="1",
    )

    thumbnail = rx.box(
        responsive_image(
            src_fallback=post.thumbnail_fallback,
            src_avif=post.thumbnail_avif,
            src_webp=post.thumbnail_webp,
            alt=str(post.thumbnail_alt),
            dimensions=ImageDimensions.blog_thumbnail,
            width="100%",
            height="100%",
            object_fit="cover",
            object_position="center",
            loading="lazy",
        ),
        width="250px",
        height="250px",
        flex_shrink="0",
        border_radius=Layout.image_border_radius,
        overflow="hidden",
        box_shadow=Layout.image_box_shadow,
    )

    card_content = rx.cond(
        flip,
        rx.flex(
            thumbnail,
            content_area,
            width="100%",
            height="auto",
            gap=["8", "8", "1.5rem", "1.5rem"],
            align_items=["center", "center", "center", "center"],
            flex_direction=["column", "column", "row-reverse", "row-reverse"],
        ),
        rx.flex(
            thumbnail,
            content_area,
            width="100%",
            height="auto",
            gap=["8", "8", "1.5rem", "1.5rem"],
            align_items=["center", "center", "center", "center"],
            flex_direction=["column", "column", "row", "row"],
        ),
    )

    return rx.link(
        rx.box(
            card_content,
            border_radius="8px",
            background=Colors.backgrounds["white"],
            padding="1.5rem",
            margin_y="1rem",
            box_shadow="0 8px 24px rgba(0, 0, 0, 0.12)",
            transition="all 0.3s ease",
            _hover={
                "box_shadow": f"0 8px 24px {Colors.primary['300']}66",
                "transform": "translateY(-2px)",
            },
        ),
        href=f"/{language}/blog/{post.slug}/",
        text_decoration="none",
        _hover={"text_decoration": "none"},
    )
