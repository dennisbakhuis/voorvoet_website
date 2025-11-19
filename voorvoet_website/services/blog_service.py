"""Blog service for loading and managing blog posts from the file system.

This module handles all I/O operations for blog posts including loading markdown
files, parsing frontmatter metadata, resolving thumbnail paths, and caching loaded
posts. Content parsing is delegated to the content_parser module for clean
separation of concerns.
"""
from datetime import datetime
from pathlib import Path
import frontmatter
from typing import Optional

from ..models import BlogPost
from .content_parser import parse_blog_content
from ..utils.translations import get_current_language


_posts_cache: list[BlogPost] | None = None

FALLBACK_DATE = datetime(2023, 2, 1)


def _get_blog_content_dir() -> Path:
    """
    Get the path to the blog content directory.

    Returns
    -------
    Path
        Absolute path to the blog_content directory containing markdown files
    """
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent
    return project_root / "voorvoet_website" / "data" / "blog_content"


def calculate_read_time(content: str) -> int:
    """
    Calculate estimated reading time based on word count.

    Uses average reading speed of 200 words per minute to estimate how long
    it takes to read the blog post content.

    Parameters
    ----------
    content : str
        Markdown content text to analyze

    Returns
    -------
    int
        Estimated reading time in minutes (minimum 1)
    """
    words = len(content.split())
    minutes = max(1, round(words / 200))
    return minutes


def _resolve_thumbnail_path(filename: str, thumbnail_filename: str) -> str:
    """
    Resolve thumbnail path with fallback to default image.

    Parameters
    ----------
    filename : str
        Blog post filename without extension
    thumbnail_filename : str
        Thumbnail filename from frontmatter metadata

    Returns
    -------
    str
        Resolved absolute URL path to thumbnail image
    """
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent

    thumbnail_path = f"/images/page_blog/{filename}/{thumbnail_filename}"
    file_system_path = project_root / f"assets{thumbnail_path}"

    if not file_system_path.exists():
        thumbnail_path = "/images/page_blog/default_thumbnail.jpg"

    return thumbnail_path


def _parse_date(date_str: str, filename: str) -> datetime:
    """
    Parse date string from frontmatter with multiple format support.

    Parameters
    ----------
    date_str : str
        Date string from frontmatter metadata
    filename : str
        Blog post filename for error reporting

    Returns
    -------
    datetime
        Parsed datetime object or FALLBACK_DATE if parsing fails
    """
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        try:
            return datetime.strptime(date_str, '%d-%m-%Y')
        except ValueError:
            print(f"Warning: Could not parse date '{date_str}' in {filename}")
            return FALLBACK_DATE


def _format_date_dutch(date: datetime) -> str:
    """
    Format datetime as Dutch locale date string.

    Parameters
    ----------
    date : datetime
        Date to format

    Returns
    -------
    str
        Formatted date string like "15 maart 2024"
    """
    months_nl = {
        1: "januari", 2: "februari", 3: "maart", 4: "april",
        5: "mei", 6: "juni", 7: "juli", 8: "augustus",
        9: "september", 10: "oktober", 11: "november", 12: "december"
    }
    return f"{date.day} {months_nl[date.month]} {date.year}"


def parse_blog_post(file_path: Path) -> Optional[BlogPost]:
    """
    Parse a single blog post markdown file into a BlogPost object.

    Reads the markdown file, extracts frontmatter metadata, resolves asset paths,
    and delegates content parsing to the content_parser module. Handles errors
    gracefully and returns None if parsing fails.

    Parameters
    ----------
    file_path : Path
        Absolute path to the markdown file to parse

    Returns
    -------
    Optional[BlogPost]
        BlogPost object with all metadata and parsed content, or None if
        parsing fails due to invalid file format or I/O errors

    Notes
    -----
    - Expects frontmatter with fields: title, slug, summary, date, author (optional),
      thumbnail (optional), thumbnail_alt (optional), read_time (optional)
    - Falls back to calculated read time if not specified in frontmatter
    - Resolves thumbnail paths with fallback to default images
    - Content parsing is handled by content_parser.parse_blog_content()
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)

        metadata = post.metadata
        content = post.content
        filename = file_path.stem
        if '.' in filename:
            filename = filename.rsplit('.', 1)[0]

        date_str = str(metadata.get('date', ''))
        date = _parse_date(date_str, filename)
        formatted_date = _format_date_dutch(date)

        try:
            read_time = int(str(metadata.get('read_time', "")))
            if read_time <= 0:
                raise ValueError("Invalid read_time value")
        except (ValueError, TypeError):
            read_time = calculate_read_time(content)

        author = metadata.get('author')
        thumbnail_filename = metadata.get('thumbnail', 'thumbnail.jpg')
        thumbnail_url = _resolve_thumbnail_path(filename, thumbnail_filename)

        content_objects = parse_blog_content(content, filename)

        blog_post = BlogPost(
            title=str(metadata.get('title', 'Untitled')),
            slug=str(metadata.get('slug', filename)),
            summary=str(metadata.get('summary', '')),
            author=str(author) if author else None,
            date=date,
            formatted_date=formatted_date,
            thumbnail=str(thumbnail_filename),
            thumbnail_alt=str(metadata.get('thumbnail_alt', '')),
            content=content,
            filename=filename,
            thumbnail_url=thumbnail_url,
            read_time=read_time,
            content_objects=content_objects,
        )

        return blog_post

    except Exception as e:
        print(f"Error parsing blog post {file_path}: {e}")
        return None


def load_all_posts(force_reload: bool = False, language: Optional[str] = None) -> list[BlogPost]:
    """
    Load all blog posts from the blog_content directory for a specific language.

    Scans the blog content directory for markdown files matching the current language
    and parses each one into BlogPost objects. Results are cached for performance unless
    force_reload is specified.

    Parameters
    ----------
    force_reload : bool, optional
        If True, bypass cache and reload all posts from disk (default: False)
    language : Optional[str], optional
        Language code to load posts for (e.g., "nl", "en", "de").
        If None, uses the current language from get_current_language()

    Returns
    -------
    list[BlogPost]
        List of BlogPost objects sorted by date in descending order (newest first)
        for the specified language

    Notes
    -----
    - Posts are cached globally after first load
    - Only .{language}.md files in the blog_content directory are processed
    - Invalid or malformed posts are skipped with warnings
    - Falls back to Dutch (nl) if the requested language is not available
    """
    global _posts_cache

    if _posts_cache is not None and not force_reload:
        return _posts_cache

    if language is None:
        language = get_current_language()

    posts = []
    blog_dir = _get_blog_content_dir()

    if not blog_dir.exists():
        print(f"Warning: Blog content directory not found: {blog_dir}")
        return []

    pattern = f"*.{language}.md"
    for file_path in blog_dir.glob(pattern):
        post = parse_blog_post(file_path)
        if post:
            posts.append(post)

    posts.sort(key=lambda p: p.date, reverse=True)

    _posts_cache = posts

    return posts


def get_post_by_slug(slug: str, language: Optional[str] = None) -> Optional[BlogPost]:
    """
    Get a single blog post by its URL slug for a specific language.

    Parameters
    ----------
    slug : str
        The URL-friendly slug identifier for the post
    language : Optional[str], optional
        Language code to load the post for (e.g., "nl", "en", "de").
        If None, uses the current language from get_current_language()

    Returns
    -------
    Optional[BlogPost]
        BlogPost object matching the slug in the specified language, or None if not found
    """
    if language is None:
        language = get_current_language()

    all_posts = load_all_posts(language=language)

    for post in all_posts:
        if post.slug == slug:
            return post

    return None


def clear_cache():
    """
    Clear the posts cache.

    Useful during development when blog content changes and needs to be reloaded
    without restarting the application.
    """
    global _posts_cache
    _posts_cache = None
