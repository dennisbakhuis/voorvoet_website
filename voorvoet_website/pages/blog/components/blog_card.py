# Blog card component for displaying blog post previews
import reflex as rx
from ....models import BlogPost
from ....theme import Colors, FontSizes, Layout
from ....config import config


def blog_card(post: BlogPost, flip: bool = False) -> rx.Component:
    """
    Display a single blog post card for the listing page in landscape layout

    Args:
        post: BlogPost object to display
        flip: If True, thumbnail is on the right; if False, thumbnail is on the left

    Returns:
        Reflex component representing the blog card
    """
    # Content area with title and summary
    content_area = rx.vstack(
        # Title
        rx.heading(
            post.title,
            size="6",
            color=Colors.text['heading'],
            margin_bottom="0.5rem",
            line_height="1.3",
        ),

        # Summary
        rx.text(
            post.summary,
            color=Colors.text['content'],
            font_size=FontSizes.regular,
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
                                color=Colors.text['muted'],
                                font_size="0.85rem",
                            ),
                            rx.text(
                                "•",
                                color=Colors.text['muted'],
                                font_size="0.85rem",
                            ),
                        ),
                    ),
                ),
                rx.cond(
                    config.blog_show_publication_date,
                    rx.text(
                        post.formatted_date,
                        color=Colors.text['muted'],
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
                                    color=Colors.text['muted'],
                                    font_size="0.85rem",
                                ),
                            ),
                            rx.text(
                                post.read_time.to(str) + " min leestijd",
                                color=Colors.text['muted'],
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
            color=Colors.primary['500'],
            font_weight="600",
            font_size=FontSizes.regular,
            margin_top="auto",
        ),

        spacing="3",
        align_items="start",
        justify_content="center",
        padding="2.5rem",
        flex="1",
    )

    # Thumbnail image - square aspect ratio with rounded corners and shadow
    thumbnail = rx.box(
        rx.image(
            src=post.thumbnail_url,
            alt=post.thumbnail_alt,
            width="100%",
            height="100%",
            object_fit="cover",
        ),
        width="250px",
        height="250px",
        flex_shrink="0",
        border_radius=Layout.image_border_radius,
        overflow="hidden",
        box_shadow=Layout.image_box_shadow,
    )

    # Build the card layout based on flip parameter
    card_content = rx.cond(
        flip,
        rx.hstack(
            content_area,
            thumbnail,
            width="100%",
            height="250px",
            spacing="0",
            align_items="center",
        ),
        rx.hstack(
            thumbnail,
            content_area,
            width="100%",
            height="250px",
            spacing="0",
            align_items="center",
        ),
    )

    return rx.link(
        rx.box(
            card_content,
            # Card styling - no border, clean look
            border_radius="8px",
            background=Colors.backgrounds['white'],
            padding="1.5rem",
            margin_y="1rem",
            transition="all 0.3s ease",
            _hover={
                "box_shadow": "0 8px 24px rgba(0, 0, 0, 0.12)",
                "transform": "translateY(-2px)",
            },
        ),
        href="/blog/" + post.slug,
        text_decoration="none",
        _hover={"text_decoration": "none"},
    )
