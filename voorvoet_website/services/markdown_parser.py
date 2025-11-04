# Custom markdown parser for blog posts
import re
import os
from typing import Any
import reflex as rx
from mistletoe import Document
from mistletoe.block_token import Heading, Paragraph, List, ListItem
from mistletoe.span_token import RawText, Link, Image, Strong, Emphasis, LineBreak

from ..theme import Colors, FontSizes
from ..components import button


def resolve_image_path(post_filename: str, image_name: str, is_thumbnail: bool = False) -> str:
    """
    Resolve image path with fallback to default images

    Args:
        post_filename: The blog post filename without extension (e.g., "001_podotherapeut_of_podoloog")
        image_name: The image filename (e.g., "thumbnail.jpg" or "image.jpg")
        is_thumbnail: Whether this is a thumbnail image

    Returns:
        The resolved image path, or default fallback path if not found
    """
    # Handle extension in image_name if not present
    if not any(image_name.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp']):
        image_name = f"{image_name}.jpg"

    # Construct expected path
    expected_path = f"/images/page_blog/{post_filename}/{image_name}"
    file_system_path = f"assets{expected_path}"

    # Check if file exists
    if os.path.exists(file_system_path):
        return expected_path

    # Fallback to defaults
    if is_thumbnail:
        return "/images/page_blog/default_thumbnail.jpg"
    else:
        return "/images/page_blog/default_image_filler.jpg"


def parse_custom_markdown(content: str) -> str:
    """
    Pre-process custom markdown syntax before parsing

    Handles:
    - !button[text](url) → Custom marker for button component
    - [!text](url) → External link marker

    Returns:
        Processed markdown content
    """
    # Replace !button[text](url) with a custom marker we can detect later
    # We'll use a special format that won't be parsed as normal markdown
    content = re.sub(
        r'!button\[([^\]]+)\]\(([^\)]+)\)',
        r'__BUTTON__\1__URL__\2__ENDBUTTON__',
        content
    )

    # Mark external links with a special marker
    # [!text](url) → __EXTERNAL__[text](url)
    content = re.sub(
        r'\[!([^\]]+)\]',
        r'[__EXTERNAL__\1]',
        content
    )

    return content


def render_inline_content(token: Any) -> list[rx.Component | str]:
    """
    Render inline content (text, links, bold, italic, etc.)

    Args:
        token: Mistletoe span token

    Returns:
        List of Reflex components or strings
    """
    if isinstance(token, RawText):
        return [token.content]

    elif isinstance(token, Strong):
        # Bold text
        children = []
        for child in token.children:
            children.extend(render_inline_content(child))
        return [rx.text.strong(*children)]

    elif isinstance(token, Emphasis):
        # Italic text
        children = []
        for child in token.children:
            children.extend(render_inline_content(child))
        return [rx.text.em(*children)]

    elif isinstance(token, Link):
        # Link - check if it's an external link
        link_text = []
        is_external = False

        for child in token.children:
            content = render_inline_content(child)
            for item in content:
                if isinstance(item, str) and "__EXTERNAL__" in item:
                    is_external = True
                    item = item.replace("__EXTERNAL__", "")
                link_text.append(item)

        # Auto-detect external links if not marked
        target = token.target
        if not is_external and (target.startswith("http://") or target.startswith("https://")):
            # Check if it's not our own domain
            if "voorvoet.nl" not in target:
                is_external = True

        return [rx.link(
            *link_text,
            href=target,
            color=Colors.text['link'],
            text_decoration="underline",
            is_external=is_external,
        )]

    elif isinstance(token, LineBreak):
        return [rx.text(" ")]

    else:
        # Fallback for unknown tokens
        if hasattr(token, 'children'):
            result = []
            for child in token.children:
                result.extend(render_inline_content(child))
            return result
        return [str(token)]


def parse_markdown_to_components(content: str, post_filename: str) -> list[rx.Component]:
    """
    Parse markdown content and convert to Reflex components

    Args:
        content: Raw markdown content
        post_filename: Filename of the blog post (without extension)

    Returns:
        List of Reflex components
    """
    components = []

    # Pre-process custom syntax
    content = parse_custom_markdown(content)

    # Check for custom buttons before parsing
    button_parts = content.split("__BUTTON__")

    if len(button_parts) > 1:
        # Has buttons - need to process in chunks
        for i, part in enumerate(button_parts):
            if i == 0:
                # First part - regular markdown
                if part.strip():
                    components.extend(_parse_markdown_block(part, post_filename))
            else:
                # Extract button info
                if "__ENDBUTTON__" in part:
                    button_text, rest = part.split("__URL__", 1)
                    button_url, remaining = rest.split("__ENDBUTTON__", 1)

                    # Add button
                    components.append(
                        button(label=button_text.strip(), href=button_url.strip())
                    )

                    # Parse remaining markdown
                    if remaining.strip():
                        components.extend(_parse_markdown_block(remaining, post_filename))
    else:
        # No buttons - parse normally
        components.extend(_parse_markdown_block(content, post_filename))

    return components


def _parse_markdown_block(content: str, post_filename: str) -> list[rx.Component]:
    """Parse a block of markdown content"""
    components = []

    # Parse markdown with mistletoe
    doc = Document(content)

    for token in doc.children:
        component = _render_block_token(token, post_filename)
        if component:
            components.append(component)

    return components


def _render_block_token(token: Any, post_filename: str) -> rx.Component | None:
    """
    Render a block-level token to a Reflex component

    Args:
        token: Mistletoe block token
        post_filename: Filename for image path resolution

    Returns:
        Reflex component or None
    """
    if isinstance(token, Heading):
        # Heading
        level = token.level
        children = []
        for child in token.children:
            children.extend(render_inline_content(child))

        # Map heading levels to sizes (Reflex uses 1-9 scale)
        size_map = {
            1: "8",
            2: "7",
            3: "6",
            4: "5",
            5: "4",
            6: "3",
        }

        return rx.heading(
            *children,
            size=size_map.get(level, "5"),
            color=Colors.text['heading'],
            margin_top="2rem" if level == 1 else "1.5rem",
            margin_bottom="1rem",
        )

    elif isinstance(token, Paragraph):
        # Paragraph - check for images
        children = []
        has_image = False
        image_component = None

        for child in token.children:
            if isinstance(child, Image):
                has_image = True
                # Extract alt text (also used as caption)
                alt_text = ""
                for alt_child in child.children:
                    if isinstance(alt_child, RawText):
                        alt_text += alt_child.content

                # Resolve image path
                image_src = resolve_image_path(post_filename, child.src)

                # Create image with caption
                image_component = rx.vstack(
                    rx.image(
                        src=image_src,
                        alt=alt_text,
                        max_width="100%",
                        border_radius="4px",
                        box_shadow="0 4px 12px rgba(0, 0, 0, 0.15)",
                    ),
                    rx.text(
                        alt_text,
                        font_size="0.9rem",
                        color=Colors.text['muted'],
                        font_style="italic",
                        margin_top="0.5rem",
                    ) if alt_text else None,
                    align_items="center",
                    spacing="0.5rem",
                    margin_y="2rem",
                )
            else:
                children.extend(render_inline_content(child))

        # If paragraph contains an image, return just the image
        if has_image:
            return image_component

        # Regular paragraph
        if children:
            return rx.text(
                *children,
                font_size=FontSizes.regular,
                color=Colors.text['content'],
                line_height="1.7",
                margin_bottom="1rem",
            )

    elif isinstance(token, List):
        # List (ordered or unordered)
        items = []
        for item in token.children:
            if isinstance(item, ListItem):
                item_content = []
                for child in item.children:
                    if isinstance(child, Paragraph):
                        for span in child.children:
                            item_content.extend(render_inline_content(span))
                    else:
                        item_content.extend(render_inline_content(child))

                items.append(rx.list.item(*item_content))

        if token.start is not None:
            # Ordered list
            return rx.list.ordered(
                *items,
                margin_bottom="1rem",
                margin_left="1.5rem",
            )
        else:
            # Unordered list
            return rx.list.unordered(
                *items,
                margin_bottom="1rem",
                margin_left="1.5rem",
            )

    return None
