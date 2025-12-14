"""Content parser for blog posts - transforms markdown into structured content objects."""

import re
from typing import Any
from pathlib import Path
from mistletoe.block_token import (
    Document,
    Heading,
    Paragraph,
    List as MarkdownList,
    BlockToken,
)
from mistletoe.span_token import RawText, Image, Link


def parse_blog_content(
    markdown_content: str,
    filename: str,
) -> list[dict[str, Any]]:
    """
    Parse markdown content into structured content dictionaries for rendering.

    Parameters
    ----------
    markdown_content : str
        Raw markdown content from blog post file (after frontmatter extraction)
    filename : str
        Blog post filename without extension (e.g., "001_podotherapeut_of_podoloog")
        Used for resolving relative image paths to absolute URLs

    Returns
    -------
    list[dict[str, Any]]
        List of content dictionaries, each with a 'type' key and type-specific data:
        - heading: {'type': 'heading', 'level': int (1-6), 'content': str}
        - paragraph: {'type': 'paragraph', 'content': str}
        - image: {'type': 'image', 'src': str, 'alt': str, 'caption': str}
        - button: {'type': 'button', 'label': str, 'url': str}
        - list: {'type': 'list', 'ordered': bool, 'items': list[str]}
    """
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent

    button_pattern = r"!button\[([^\]]+)\]\(([^)]+)\)"
    button_placeholder = "BUTTON_PLACEHOLDER_{index}"

    buttons = []
    button_index = 0

    def replace_button(match: re.Match[str]) -> str:
        nonlocal button_index
        buttons.append(
            {
                "label": match.group(1),
                "url": match.group(2),
            }
        )
        placeholder = button_placeholder.format(index=button_index)
        button_index += 1
        return placeholder

    processed_content = re.sub(button_pattern, replace_button, markdown_content)

    doc = Document(processed_content)

    content_objects: list[dict[str, Any]] = []

    children = doc.children if doc.children is not None else []
    for child in children:
        if isinstance(child, BlockToken):
            obj = _process_block_token(child, filename, buttons, project_root)
            if obj:
                content_objects.append(obj)

    return content_objects


def _process_block_token(
    token: BlockToken,
    filename: str,
    buttons: list[dict[str, str]],
    project_root: Path,
) -> dict[str, Any] | None:
    """
    Process a single mistletoe block token into a content object.

    Parameters
    ----------
    token : BlockToken
        Mistletoe AST block token to process
    filename : str
        Blog post filename for image path resolution
    buttons : list[dict[str, str]]
        List of extracted button objects with label and url
    project_root : Path
        Project root path for image file validation

    Returns
    -------
    dict[str, Any] | None
        Content object dictionary or None if token should be skipped
    """
    if isinstance(token, Heading):
        children = token.children if token.children is not None else []
        content = _render_span_tokens(children, filename, buttons, project_root)
        if content.strip():
            return {
                "type": "heading",
                "level": token.level,
                "content": content,
            }

    elif isinstance(token, Paragraph):
        children = token.children if token.children is not None else []
        content = _render_span_tokens(children, filename, buttons, project_root)

        button_match = re.match(r"^BUTTON_PLACEHOLDER_(\d+)$", content.strip())
        if button_match:
            button_index = int(button_match.group(1))
            if button_index < len(buttons):
                return {
                    "type": "button",
                    "label": buttons[button_index]["label"],
                    "url": buttons[button_index]["url"],
                }

        children_list = list(children)
        if len(children_list) == 1 and isinstance(children_list[0], Image):
            image = children_list[0]
            return _process_image(image, filename, project_root)

        if content.strip():
            return {
                "type": "paragraph",
                "content": content,
            }

    elif isinstance(token, MarkdownList):
        items = []
        list_children = token.children if token.children is not None else []
        for item in list_children:
            if hasattr(item, "children"):
                item_children = item.children if item.children is not None else []
                item_content = _render_span_tokens(
                    item_children, filename, buttons, project_root
                )
                if item_content.strip():
                    items.append(item_content)

        if items:
            is_ordered = token.start is not None
            if is_ordered:
                markdown_list = "\n".join(
                    [f"{i + 1}. {item}" for i, item in enumerate(items)]
                )
            else:
                markdown_list = "\n".join([f"- {item}" for item in items])

            return {
                "type": "list",
                "ordered": is_ordered,
                "items": items,
                "markdown": markdown_list,
            }

    return None


def _process_image(image: Image, filename: str, project_root: Path) -> dict[str, Any]:
    """
    Process an image token into an image content object with path resolution.

    Parameters
    ----------
    image : Image
        Mistletoe Image span token
    filename : str
        Blog post filename for path resolution
    project_root : Path
        Project root for file validation

    Returns
    -------
    dict[str, Any]
        Image content object with src, alt, and caption
    """
    src_fallback = image.src
    src_avif = ""
    src_webp = ""

    image_children = image.children if image.children is not None else []
    alt = (
        _render_span_tokens(image_children, filename, [], project_root)
        if image_children
        else ""
    )

    if not (
        src_fallback.startswith("http://")
        or src_fallback.startswith("https://")
        or src_fallback.startswith("/")
    ):
        resolved_path = f"/images/page_blog/{filename}/{src_fallback}"
        file_system_path = project_root / f"assets{resolved_path}"

        if not file_system_path.exists():
            resolved_path = "/images/page_blog/default_image_filler.jpg"

        src_fallback = resolved_path

        base_path = (
            src_fallback.rsplit(".", 1)[0] if "." in src_fallback else src_fallback
        )
        asset_base = base_path.lstrip("/")
        if (project_root / f"assets/{asset_base}.avif").exists():
            src_avif = f"{base_path}.avif"
        if (project_root / f"assets/{asset_base}.webp").exists():
            src_webp = f"{base_path}.webp"

    return {
        "type": "image",
        "src_fallback": src_fallback,
        "src_avif": src_avif,
        "src_webp": src_webp,
        "alt": alt,
        "caption": alt,
    }


def _render_span_tokens(
    tokens: Any,
    filename: str,
    buttons: list[dict[str, str]],
    project_root: Path,
) -> str:
    """
    Render mistletoe span tokens back to text/markdown.

    Parameters
    ----------
    tokens : list
        List of mistletoe span tokens
    filename : str
        Blog post filename (for potential nested image handling)
    buttons : list[dict[str, str]]
        Button objects list
    project_root : Path
        Project root path

    Returns
    -------
    str
        Rendered text content from span tokens
    """
    result = []

    for token in tokens:
        if isinstance(token, RawText):
            result.append(token.content)
        elif isinstance(token, Image):
            img_children = token.children if token.children is not None else []
            alt = (
                _render_span_tokens(img_children, filename, buttons, project_root)
                if img_children
                else ""
            )
            result.append(f"![{alt}]({token.src})")
        elif isinstance(token, Link):
            link_children = token.children if token.children is not None else []
            text = (
                _render_span_tokens(link_children, filename, buttons, project_root)
                if link_children
                else ""
            )
            result.append(f"[{text}]({token.target})")
        elif hasattr(token, "children"):
            nested_children = token.children if token.children is not None else []
            result.append(
                _render_span_tokens(nested_children, filename, buttons, project_root)
            )
        else:
            result.append(getattr(token, "content", str(token)))

    return "".join(result)
