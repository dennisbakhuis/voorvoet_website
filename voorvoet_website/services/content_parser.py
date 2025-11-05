"""Content parser for blog posts - transforms markdown into structured content objects.

This module provides markdown parsing functionality that converts raw markdown
text into a structured list of content objects suitable for dynamic rendering
in blog post pages. Uses mistletoe for proper AST-based markdown parsing instead
of regex, enabling support for various content types including headings,
paragraphs, images, buttons, and lists.
"""
import re
from typing import Any
from pathlib import Path
import mistletoe
from mistletoe import Document
from mistletoe.block_token import Heading, Paragraph, List as MarkdownList, BlockToken
from mistletoe.span_token import RawText, Image, Link


def parse_blog_content(
    markdown_content: str,
    filename: str,
) -> list[dict[str, Any]]:
    """
    Parse markdown content into structured content dictionaries for rendering.

    Transforms raw markdown text into a list of content objects representing
    different content types (headings, paragraphs, images, buttons, lists).
    Handles image path resolution with fallbacks and custom button syntax.
    Uses mistletoe for proper Abstract Syntax Tree (AST) based parsing.

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

    Notes
    -----
    - Image paths are resolved relative to /images/page_blog/{filename}/
    - Non-existent images fall back to default_image_filler.jpg
    - Custom button syntax: !button[label](url) is converted to button objects
    - Empty content blocks are filtered out
    - Lists can be ordered (numbered) or unordered (bullet points)
    """
    # Get project root for image path validation
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent

    # Preprocess: Convert custom !button syntax to a marker we can detect
    button_pattern = r'!button\[([^\]]+)\]\(([^)]+)\)'
    button_placeholder = "BUTTON_PLACEHOLDER_{index}"

    buttons = []
    button_index = 0

    def replace_button(match):
        nonlocal button_index
        buttons.append({
            'label': match.group(1),
            'url': match.group(2),
        })
        placeholder = button_placeholder.format(index=button_index)
        button_index += 1
        return placeholder

    processed_content = re.sub(button_pattern, replace_button, markdown_content)

    # Parse markdown using mistletoe
    doc = Document(processed_content)

    content_objects: list[dict[str, Any]] = []

    for child in doc.children:
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
        content = _render_span_tokens(token.children, filename, buttons, project_root)
        if content.strip():
            return {
                'type': 'heading',
                'level': token.level,
                'content': content,
            }

    elif isinstance(token, Paragraph):
        content = _render_span_tokens(token.children, filename, buttons, project_root)

        # Check if this paragraph contains a button placeholder
        button_match = re.match(r'^BUTTON_PLACEHOLDER_(\d+)$', content.strip())
        if button_match:
            button_index = int(button_match.group(1))
            if button_index < len(buttons):
                return {
                    'type': 'button',
                    'label': buttons[button_index]['label'],
                    'url': buttons[button_index]['url'],
                }

        # Check if this paragraph is just an image
        if len(token.children) == 1 and isinstance(token.children[0], Image):
            image = token.children[0]
            return _process_image(image, filename, project_root)

        # Regular paragraph
        if content.strip():
            return {
                'type': 'paragraph',
                'content': content,
            }

    elif isinstance(token, MarkdownList):
        items = []
        for item in token.children:
            item_content = _render_span_tokens(item.children, filename, buttons, project_root)
            if item_content.strip():
                items.append(item_content)

        if items:
            is_ordered = token.start is not None
            if is_ordered:
                markdown_list = '\n'.join([f"{i+1}. {item}" for i, item in enumerate(items)])
            else:
                markdown_list = '\n'.join([f"- {item}" for item in items])

            return {
                'type': 'list',
                'ordered': is_ordered,
                'items': items,
                'markdown': markdown_list,
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
    src = image.src
    alt = _render_span_tokens(image.children, filename, [], project_root) if image.children else ""

    # Resolve relative image paths
    if not (src.startswith('http://') or src.startswith('https://') or src.startswith('/')):
        resolved_path = f"/images/page_blog/{filename}/{src}"
        file_system_path = project_root / f"assets{resolved_path}"

        # Check if image exists, otherwise use default fallback
        if not file_system_path.exists():
            resolved_path = "/images/page_blog/default_image_filler.jpg"

        src = resolved_path

    return {
        'type': 'image',
        'src': src,
        'alt': alt,
        'caption': alt,  # Use alt text as caption
    }


def _render_span_tokens(
    tokens: list,
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
            # Images in paragraphs - keep markdown format for now
            alt = _render_span_tokens(token.children, filename, buttons, project_root) if token.children else ""
            result.append(f"![{alt}]({token.src})")
        elif isinstance(token, Link):
            text = _render_span_tokens(token.children, filename, buttons, project_root) if token.children else ""
            result.append(f"[{text}]({token.target})")
        elif hasattr(token, 'children'):
            # Recursive for nested tokens
            result.append(_render_span_tokens(token.children, filename, buttons, project_root))
        else:
            # Fallback: try to get content attribute
            result.append(getattr(token, 'content', str(token)))

    return ''.join(result)
