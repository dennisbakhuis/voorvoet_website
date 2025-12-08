"""Blog service for loading and managing blog posts from the file system."""

from datetime import datetime
from pathlib import Path
import frontmatter
from typing import Optional

from ..models import BlogPost
from .content_parser import parse_blog_content

FALLBACK_DATE = datetime(2023, 2, 1)
_posts_cache: dict[str, list[BlogPost]] = {}


def _get_blog_content_dir() -> Path:
    """Get the path to the blog content directory."""
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent
    return project_root / "voorvoet_website" / "data" / "blog_content"


def calculate_read_time(content: str) -> int:
    """Calculate estimated reading time (200 words per minute, minimum 1 minute)."""
    words = len(content.split())
    return max(1, round(words / 200))


def _resolve_thumbnail_path(filename: str, thumbnail_filename: str) -> str:
    """Resolve thumbnail path with fallback to default image."""
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent
    thumbnail_path = f"/images/page_blog/{filename}/{thumbnail_filename}"
    file_system_path = project_root / f"assets{thumbnail_path}"

    if not file_system_path.exists():
        thumbnail_path = "/images/page_blog/default_thumbnail.jpg"

    return thumbnail_path


def _build_thumbnail_sources(thumbnail_url: str) -> list[str]:
    """Build list of thumbnail image sources with AVIF, WebP, and fallback formats."""
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent

    url_path = Path(thumbnail_url)
    base_path = str(url_path.with_suffix(""))
    asset_base = base_path.lstrip("/")

    sources = []
    if (project_root / f"assets/{asset_base}.avif").exists():
        sources.append(f"{base_path}.avif")
    if (project_root / f"assets/{asset_base}.webp").exists():
        sources.append(f"{base_path}.webp")
    sources.append(thumbnail_url)

    return sources


def _build_picture_sources(
    thumbnail_sources: list[str],
) -> tuple[list[dict[str, str]], str]:
    """
    Build picture element sources and fallback from thumbnail sources.

    Returns tuple of (sources_list, fallback_url).
    """
    mime_types = {
        ".avif": "image/avif",
        ".webp": "image/webp",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
    }

    sources = []
    fallback_src = None

    for img_path in thumbnail_sources:
        ext = img_path[img_path.rfind(".") :].lower() if "." in img_path else ""
        mime_type = mime_types.get(ext)

        if mime_type in ("image/jpeg", "image/png"):
            fallback_src = img_path
        elif mime_type:
            sources.append({"type": mime_type, "srcset": img_path})

    if not fallback_src and thumbnail_sources:
        fallback_src = thumbnail_sources[-1]

    return sources, fallback_src or ""


def _parse_date(date_str: str, filename: str) -> datetime:
    """Parse date string from frontmatter (YYYY-MM-DD or DD-MM-YYYY)."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        try:
            return datetime.strptime(date_str, "%d-%m-%Y")
        except ValueError:
            print(f"Warning: Could not parse date '{date_str}' in {filename}")
            return FALLBACK_DATE


def _format_date_dutch(date: datetime) -> str:
    """Format datetime as Dutch locale date string (e.g., '15 maart 2024')."""
    months_nl = {
        1: "januari",
        2: "februari",
        3: "maart",
        4: "april",
        5: "mei",
        6: "juni",
        7: "juli",
        8: "augustus",
        9: "september",
        10: "oktober",
        11: "november",
        12: "december",
    }
    return f"{date.day} {months_nl[date.month]} {date.year}"


def parse_blog_post(file_path: Path) -> Optional[BlogPost]:
    """Parse a single blog post markdown file into a BlogPost object."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            post = frontmatter.load(f)

        metadata = post.metadata
        content = post.content
        filename = file_path.stem
        if "." in filename:
            filename = filename.rsplit(".", 1)[0]

        story_number = filename.split("_")[0]

        date_str = str(metadata.get("date", ""))
        date = _parse_date(date_str, filename)
        formatted_date = _format_date_dutch(date)

        date_modified = None
        if "date_modified" in metadata:
            date_modified_str = str(metadata.get("date_modified", ""))
            date_modified = _parse_date(date_modified_str, filename)

        try:
            read_time = int(str(metadata.get("read_time", "")))
            if read_time <= 0:
                raise ValueError("Invalid read_time value")
        except (ValueError, TypeError):
            read_time = calculate_read_time(content)

        author = metadata.get("author")
        thumbnail_filename: str = str(metadata.get("thumbnail", "thumbnail.jpg"))
        thumbnail_url = _resolve_thumbnail_path(filename, thumbnail_filename)
        thumbnail_sources = _build_thumbnail_sources(thumbnail_url)
        thumbnail_picture_sources, thumbnail_fallback = _build_picture_sources(
            thumbnail_sources
        )

        tags_raw = metadata.get("tags", [])
        if isinstance(tags_raw, list):
            tags = [str(tag).strip() for tag in tags_raw]
        elif isinstance(tags_raw, str):
            tags = [tag.strip() for tag in tags_raw.split(",") if tag.strip()]
        else:
            tags = []

        category = metadata.get("category")

        content_objects = parse_blog_content(content, filename)

        blog_post = BlogPost(
            title=str(metadata.get("title", "Untitled")),
            slug=str(metadata.get("slug", filename)),
            summary=str(metadata.get("summary", "")),
            author=str(author) if author else None,
            date=date,
            date_modified=date_modified,
            formatted_date=formatted_date,
            thumbnail=str(thumbnail_filename),
            thumbnail_alt=str(metadata.get("thumbnail_alt", "")),
            content=content,
            filename=filename,
            thumbnail_url=thumbnail_url,
            thumbnail_sources=thumbnail_sources,
            thumbnail_picture_sources=thumbnail_picture_sources,
            thumbnail_fallback=thumbnail_fallback,
            read_time=read_time,
            content_objects=content_objects,
            tags=tags,
            category=str(category) if category else None,
            story_number=story_number,
        )

        return blog_post

    except Exception as e:
        print(f"Error parsing blog post {file_path}: {e}")
        return None


def load_all_posts(
    force_reload: bool = False, language: Optional[str] = None
) -> list[BlogPost]:
    """Load all blog posts for a specific language, sorted by date (newest first)."""
    global _posts_cache

    if language is None:
        language = "nl"

    if language in _posts_cache and not force_reload:
        return _posts_cache[language]

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
    _posts_cache[language] = posts

    return posts


def load_all_blog_posts_dict() -> dict[str, list[dict]]:
    """Load all blog posts for all languages as dictionaries."""
    languages = ["nl", "en", "de"]
    result: dict[str, list[dict]] = {}

    for lang in languages:
        posts = load_all_posts(force_reload=False, language=lang)
        result[lang] = []

        for post in posts:
            post_dict = {
                "title": post.title,
                "slug": post.slug,
                "summary": post.summary,
                "author": post.author or "",
                "date": post.date.isoformat(),
                "date_modified": post.date_modified.isoformat()
                if post.date_modified
                else "",
                "formatted_date": post.formatted_date,
                "thumbnail": post.thumbnail,
                "thumbnail_alt": post.thumbnail_alt or "",
                "thumbnail_url": post.thumbnail_url,
                "thumbnail_sources": post.thumbnail_sources,
                "thumbnail_picture_sources": post.thumbnail_picture_sources,
                "thumbnail_fallback": post.thumbnail_fallback,
                "read_time": str(post.read_time) if post.read_time else "",
                "category": post.category or "",
                "tags": ",".join(post.tags),
                "filename": post.filename,
                "url": post.url,
                "content": post.content,
                "content_objects": post.content_objects,
                "story_number": post.story_number,
            }
            result[lang].append(post_dict)

    return result
