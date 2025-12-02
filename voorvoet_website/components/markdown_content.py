"""Markdown content component for rendering parsed blog post content.

This module provides the main rendering logic for blog post content by
dynamically selecting the appropriate blog component based on content type.
All actual rendering is delegated to specialized blog components for
maintainability and reusability.
"""

import reflex as rx
from ..models import BlogPost
from .blog_heading import blog_header
from .blog_paragraph import blog_paragraph
from .blog_markdown import blog_markdown
from .blog_image import blog_image
from .blog_list import blog_list
from .button import button


def render_content_object(obj) -> rx.Component:
    """
    Render a single content object based on its type.

    Dynamically renders different content types (heading, paragraph, markdown,
    image, button, list) from parsed blog post content objects. Used with
    rx.foreach for dynamic rendering of content lists with proper type checking
    and conditional rendering.

    Parameters
    ----------
    obj : dict
        Dictionary containing content object data with keys:
        - type : str - Content type identifier
        - For type="heading": level (int), content (str)
        - For type="paragraph": content (str)
        - For type="markdown": content (str)
        - For type="image": src (str), alt (str), caption (str, optional)
        - For type="button": label (str), url (str)
        - For type="list": ordered (bool), items (list[str])

    Returns
    -------
    rx.Component
        A Reflex component appropriate for the content type with consistent
        styling from the site theme

    Notes
    -----
    - Headings use dynamic font sizes based on level (h1-h6)
    - Paragraphs use standard content text styling
    - Markdown blocks support full markdown rendering
    - Images are centered with optional captions and responsive sizing
    - Buttons use primary color scheme with hover effects
    - Lists support both ordered (numbered) and unordered (bulleted) formats
    """
    return rx.cond(
        obj["type"] == "heading",
        _render_heading(obj),
        rx.cond(
            obj["type"] == "paragraph",
            _render_paragraph(obj),
            rx.cond(
                obj["type"] == "markdown",
                _render_markdown(obj),
                rx.cond(
                    obj["type"] == "image",
                    _render_image(obj),
                    rx.cond(
                        obj["type"] == "button",
                        _render_button(obj),
                        rx.cond(
                            obj["type"] == "list",
                            _render_list(obj),
                        ),
                    ),
                ),
            ),
        ),
    )


def _render_heading(obj) -> rx.Component:
    """
    Render a heading content object using blog_header component.

    Parameters
    ----------
    obj : dict
        Heading object with 'level' (1-6) and 'content' keys

    Returns
    -------
    rx.Component
        Styled heading component via blog_header
    """
    return blog_header(obj["content"], obj["level"])


def _render_paragraph(obj) -> rx.Component:
    """
    Render a paragraph content object using blog_paragraph component.

    Parameters
    ----------
    obj : dict
        Paragraph object with 'content' key containing text/markdown

    Returns
    -------
    rx.Component
        Styled paragraph via blog_paragraph
    """
    return blog_paragraph(obj["content"])


def _render_markdown(obj) -> rx.Component:
    """
    Render a markdown content object using blog_markdown component.

    Parameters
    ----------
    obj : dict
        Markdown object with 'content' key

    Returns
    -------
    rx.Component
        Styled markdown via blog_markdown
    """
    return blog_markdown(obj["content"])


def _render_image(obj) -> rx.Component:
    """
    Render an image content object using blog_image component.

    Parameters
    ----------
    obj : dict
        Image object with 'src', 'alt', and optional 'caption' keys

    Returns
    -------
    rx.Component
        Styled image via blog_image
    """
    return blog_image(obj["src"], obj.get("alt", ""), obj.get("caption", ""))


def _render_button(obj) -> rx.Component:
    """
    Render a button content object using button component.

    Parameters
    ----------
    obj : dict
        Button object with 'label' and 'url' keys

    Returns
    -------
    rx.Component
        Styled button via button component, centered horizontally
    """
    return rx.box(
        button(label=obj["label"], href=obj["url"]),
        display="flex",
        justify_content="center",
        width="100%",
        margin_y="1.5rem",
    )


def _render_list(obj) -> rx.Component:
    """
    Render a list content object using blog_list component.

    Parameters
    ----------
    obj : dict
        List object with 'markdown' key containing list in markdown format

    Returns
    -------
    rx.Component
        Styled list via blog_list
    """
    return blog_list(obj.get("markdown", ""))


def markdown_content(post: BlogPost) -> rx.Component:
    """
    Render complete blog post content from parsed content objects.

    Iterates through the blog post's content_objects list and renders each
    object using the appropriate component type. Provides the main content
    display for individual blog post pages.

    Parameters
    ----------
    post : BlogPost
        BlogPost object with parsed content_objects list

    Returns
    -------
    rx.Component
        A Reflex box component containing all rendered content elements in
        order with consistent styling and spacing

    Notes
    -----
    Content objects are rendered dynamically using rx.foreach with the
    render_content_object function, allowing for flexible content structure
    and easy addition of new content types.
    """
    return rx.box(
        rx.foreach(
            post.content_objects,
            render_content_object,
        ),
        width="100%",
    )
