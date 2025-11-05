# Markdown content component - renders parsed blog content objects
import reflex as rx
from ....theme import Colors, FontSizes
from ....models import BlogPost


def render_content_object(obj) -> rx.Component:
    """
    Render a single content object based on its type
    Used with rx.foreach for dynamic rendering

    Args:
        obj: Dictionary with keys: type, content, src, alt, caption, label, url
    """
    return rx.cond(
        obj["type"] == "markdown",
        rx.markdown(
            obj["content"],
            color=Colors.text['content'],
            font_size=FontSizes.regular,
        ),
        rx.cond(
            obj["type"] == "image",
            rx.box(
                rx.image(
                    src=obj["src"],
                    alt=obj["alt"],
                    loading="lazy",
                ),
                rx.cond(
                    obj["caption"],
                    rx.text(
                        obj["caption"],
                        color=Colors.text['muted'],
                        font_size=FontSizes.regular,
                        font_style="italic",
                        text_align="center",
                        margin_top="0.5rem",
                    ),
                ),
                display="block",
                margin="2rem auto",
                max_width="800px",
                width="100%",
                style={
                    "& img": {
                        "display": "block",
                        "margin": "0 auto",
                        "max_width": "100%",
                        "width": "100%",
                        "height": "auto",
                        "border_radius": "8px",
                        "box_shadow": "0 4px 12px rgba(0, 0, 0, 0.15)",
                    }
                }
            ),
            rx.cond(
                obj["type"] == "button",
                rx.box(
                    rx.link(
                        rx.text(obj["label"]),
                        href=obj["url"],
                        border_radius="3px",
                        font_weight="700",
                        font_size=FontSizes.regular,
                        padding_x="0.8em",
                        padding_y="0.1em",
                        transition="all 0.2s ease",
                        cursor="pointer",
                        display="inline-flex",
                        align_items="center",
                        justify_content="center",
                        text_decoration="none",
                        border="none",
                        white_space="nowrap",
                        bg=Colors.primary['300'],
                        color=Colors.text['white'],
                        box_shadow="0 4px 12px rgba(5, 168, 162, 0.3)",
                        _hover={
                            "bg": Colors.primary['500'],
                            "box_shadow": "0 6px 16px rgba(5, 168, 162, 0.4)"
                        },
                    ),
                    display="flex",
                    justify_content="center",
                    margin="2rem 0",
                ),
            ),
        ),
    )


def markdown_content(post: BlogPost) -> rx.Component:
    """
    Render blog post content from parsed content objects

    Args:
        post: BlogPost object with parsed content_objects

    Returns:
        Reflex component with rendered content
    """
    return rx.box(
        rx.foreach(
            post.content_objects,
            render_content_object,
        ),
        width="100%",
    )
