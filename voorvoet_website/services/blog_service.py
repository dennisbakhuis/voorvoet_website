# Blog service for loading and managing blog posts
import re
from datetime import datetime
from pathlib import Path
import frontmatter
from typing import Optional

from ..models import BlogPost
from .content_parser import parse_markdown_content


# Cache for loaded posts
_posts_cache: list[BlogPost] | None = None

FALLBACK_DATE = datetime(2023, 2, 1)  # Start date of VoorVoet


def _get_blog_content_dir() -> Path:
    """Get the path to the blog content directory"""
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent
    return project_root / "voorvoet_website" / "blog_content"


def calculate_read_time(content: str) -> int:
    """
    Calculate estimated reading time based on word count

    Args:
        content: Markdown content

    Returns:
        Estimated reading time in minutes (minimum 1)
    """
    # Average reading speed: 200 words per minute
    words = len(content.split())
    minutes = max(1, round(words / 200))
    return minutes


def preprocess_markdown_images(content: str, filename: str) -> str:
    """
    Preprocess markdown content to resolve relative image paths to absolute paths
    and convert custom button syntax

    Args:
        content: Raw markdown content
        filename: Blog post filename (e.g., "001_podotherapeut_of_podoloog")

    Returns:
        Markdown content with resolved image paths and button syntax converted
    """
    # Get project root for file checking
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent

    def replace_image(match):
        alt_text = match.group(1)  # Group 1 is the alt text
        image_path = match.group(2)  # Group 2 is the image path

        # Skip if already an absolute URL
        if image_path.startswith('http://') or image_path.startswith('https://') or image_path.startswith('/'):
            return match.group(0)

        # Build the resolved path
        resolved_path = f"/images/page_blog/{filename}/{image_path}"
        file_system_path = project_root / f"assets{resolved_path}"

        # Check if image exists, otherwise use default fallback
        if not file_system_path.exists():
            resolved_path = "/images/page_blog/default_image_filler.jpg"

        return f"![{alt_text}]({resolved_path})"

    # Replace markdown image syntax: ![alt text](image_path)
    # But preserve !button syntax
    processed_content = re.sub(r'!(?!button\[)\[([^\]]*)\]\(([^)]+)\)', replace_image, content)

    # Convert !button[text](url) to a special HTML marker that we can process later
    # This will be handled by the markdown_content component
    button_pattern = r'!button\[([^\]]+)\]\(([^)]+)\)'
    processed_content = re.sub(button_pattern, r'<div class="blog-button" data-label="\1" data-url="\2"></div>', processed_content)

    return processed_content


def parse_blog_post(file_path: Path) -> Optional[BlogPost]:
    """
    Parse a single blog post markdown file

    Args:
        file_path: Path to the markdown file

    Returns:
        BlogPost object or None if parsing fails
    """
    try:
        # Read and parse frontmatter
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)

        # Extract metadata
        metadata = post.metadata
        content = post.content

        # Get filename without extension (e.g., "001_podotherapeut_of_podoloog")
        filename = file_path.stem

        # Parse date
        date_str = str(metadata.get('date', ''))
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            # Try alternative format
            try:
                date = datetime.strptime(date_str, '%d-%m-%Y')
            except ValueError:
                print(f"Warning: Could not parse date '{date_str}' in {filename}")
                date = FALLBACK_DATE

        # Format date in Dutch
        months_nl = {
            1: "januari", 2: "februari", 3: "maart", 4: "april",
            5: "mei", 6: "juni", 7: "juli", 8: "augustus",
            9: "september", 10: "oktober", 11: "november", 12: "december"
        }
        formatted_date = f"{date.day} {months_nl[date.month]} {date.year}"

        # Calculate reading time (optional - only if not specified in metadata)
        try:
            read_time = int(str(metadata.get('read_time', "")))
            if read_time <= 0:
                raise ValueError("Blog post read_time not set correctly")
        except:
            read_time = calculate_read_time(content)

        # Get author (optional)
        author = metadata.get('author')  # Can be None

        # Get thumbnail filename
        thumbnail_filename = metadata.get('thumbnail', 'thumbnail.jpg')

        # Resolve thumbnail URL with fallback
        # Get project root for file checking
        current_file = Path(__file__)
        project_root = current_file.parent.parent.parent

        thumbnail_path = f"/images/page_blog/{filename}/{thumbnail_filename}"
        file_system_path = project_root / f"assets{thumbnail_path}"

        # Check if thumbnail exists, otherwise use default
        if not file_system_path.exists():
            thumbnail_path = "/images/page_blog/default_thumbnail.jpg"

        # Preprocess markdown content to resolve image paths
        processed_content = preprocess_markdown_images(content, filename)

        # Parse content into dictionaries
        content_objects = parse_markdown_content(processed_content)

        # Create BlogPost object
        blog_post = BlogPost(
            title=str(metadata.get('title', 'Untitled')),
            slug=str(metadata.get('slug', filename)),
            summary=str(metadata.get('summary', '')),
            author=str(author),
            date=date,
            formatted_date=formatted_date,
            thumbnail=str(thumbnail_filename),
            thumbnail_alt=str(metadata.get('thumbnail_alt', '')),
            content=processed_content,
            filename=filename,
            thumbnail_url=thumbnail_path,
            read_time=read_time,
            content_objects=content_objects,
        )

        return blog_post

    except Exception as e:
        print(f"Error parsing blog post {file_path}: {e}")
        return None


def load_all_posts(force_reload: bool = False) -> list[BlogPost]:
    """
    Load all blog posts from the blog_content directory

    Args:
        force_reload: If True, bypass cache and reload from disk

    Returns:
        List of BlogPost objects, sorted by date (newest first)
    """
    global _posts_cache

    # Return cached posts if available
    if _posts_cache is not None and not force_reload:
        return _posts_cache

    posts = []
    blog_dir = _get_blog_content_dir()

    if not blog_dir.exists():
        print(f"Warning: Blog content directory not found: {blog_dir}")
        return []

    # Scan directory for .md files
    for file_path in blog_dir.glob("*.md"):
        post = parse_blog_post(file_path)
        if post:
            posts.append(post)

    # Sort by date (newest first)
    posts.sort(key=lambda p: p.date, reverse=True)

    # Cache the results
    _posts_cache = posts

    return posts


def get_post_by_slug(slug: str) -> Optional[BlogPost]:
    """
    Get a single blog post by its slug

    Args:
        slug: The URL slug of the post

    Returns:
        BlogPost object or None if not found
    """
    all_posts = load_all_posts()

    for post in all_posts:
        if post.slug == slug:
            return post

    return None


def clear_cache():
    """Clear the posts cache (useful for development)"""
    global _posts_cache
    _posts_cache = None
