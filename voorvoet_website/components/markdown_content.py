"""Markdown content component for rendering parsed blog post content."""
import reflex as rx
from ..theme import Colors, FontSizes
from ..models import BlogPost


def render_content_object(obj) -> rx.Component:
    """
    Render a single content object based on its type.

    Dynamically renders different content types (markdown, image, button)
    from parsed blog post content objects. Used with rx.foreach for
    dynamic rendering of content lists.

    Parameters
    ----------
    obj : dict
        Dictionary containing content object data with keys:
        - type : str - Content type ("markdown", "image", or "button")
        - content : str - Markdown text content (for type="markdown")
        - src : str - Image source URL (for type="image")
        - alt : str - Image alt text (for type="image")
        - caption : str - Image caption (for type="image", optional)
        - label : str - Button text (for type="button")
        - url : str - Button link URL (for type="button")

    Returns
    -------
    rx.Component
        A Reflex component appropriate for the content type:
        - Markdown component for text content
        - Styled image box with optional caption
        - Styled button/link component

    Notes
    -----
    - Images are displayed centered with rounded corners and shadow
    - Buttons use the primary color scheme from theme
    - All styling is consistent with the site theme
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
    Render complete blog post content from parsed content objects.

    Iterates through the blog post's content_objects list and renders
    each object using the appropriate component type.

    Parameters
    ----------
    post : BlogPost
        BlogPost object with parsed content_objects list.

    Returns
    -------
    rx.Component
        A Reflex box component containing all rendered content elements.

    Notes
    -----
    Content objects are rendered in order using rx.foreach with the
    render_content_object function.
    """
    return rx.box(
        rx.foreach(
            post.content_objects,
            render_content_object,
        ),
        width="100%",
    )
