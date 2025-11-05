# Content parser for blog posts - parses markdown into structured content dictionaries
import re
from typing import Any


def parse_markdown_content(markdown_content: str) -> list[dict[str, Any]]:
    """
    Parse markdown content into structured content dictionaries

    This extracts images and buttons as separate objects, keeping all other
    markdown content together in a single markdown object.

    Args:
        markdown_content: Preprocessed markdown content with resolved image paths

    Returns:
        List of content dictionaries with 'type' key (markdown, image, or button)
    """
    content_objects: list[dict[str, Any]] = []

    # Find all images and buttons with their positions
    image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    button_pattern = r'<div class="blog-button" data-label="([^"]+)" data-url="([^"]+)"></div>'

    # Collect all special elements (images and buttons) with their positions
    special_elements = []

    # Find all images
    for match in re.finditer(image_pattern, markdown_content):
        special_elements.append({
            'type': 'image',
            'start': match.start(),
            'end': match.end(),
            'src': match.group(2),
            'alt': match.group(1),
            'caption': match.group(1),
        })

    # Find all buttons
    for match in re.finditer(button_pattern, markdown_content):
        special_elements.append({
            'type': 'button',
            'start': match.start(),
            'end': match.end(),
            'label': match.group(1),
            'url': match.group(2),
        })

    # Sort by position
    special_elements.sort(key=lambda x: x['start'])

    # Extract markdown content and special elements in order
    current_pos = 0

    for element in special_elements:
        # Add markdown content before this element (if any)
        if current_pos < element['start']:
            markdown_text = markdown_content[current_pos:element['start']].strip()
            if markdown_text:
                content_objects.append({
                    'type': 'markdown',
                    'content': markdown_text,
                })

        # Add the special element (image or button) - already in dict format
        if element['type'] == 'image':
            content_objects.append({
                'type': 'image',
                'src': element['src'],
                'alt': element['alt'],
                'caption': element['caption'],
            })
        elif element['type'] == 'button':
            content_objects.append({
                'type': 'button',
                'label': element['label'],
                'url': element['url'],
            })

        current_pos = element['end']

    # Add any remaining markdown content after the last element
    if current_pos < len(markdown_content):
        markdown_text = markdown_content[current_pos:].strip()
        if markdown_text:
            content_objects.append({
                'type': 'markdown',
                'content': markdown_text,
            })

    # If no special elements were found, add all content as markdown
    if not content_objects and markdown_content.strip():
        content_objects.append({
            'type': 'markdown',
            'content': markdown_content.strip(),
        })

    return content_objects
