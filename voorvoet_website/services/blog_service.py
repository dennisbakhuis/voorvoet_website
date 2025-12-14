"""Blog service for loading and managing blog posts from the file system."""

from pathlib import Path
import frontmatter

from ..models.blog_post import BlogPostDict, parse_datetime, format_date
from .content_parser import parse_blog_content

_posts_cache: dict[str, list[BlogPostDict]] = {}


def _get_blog_content_dir() -> Path:
    """Get the path to the blog content directory."""
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent
    return project_root / "voorvoet_website" / "data" / "blog_content"


def _resolve_thumbnail_path(filename: str, thumbnail_filename: str) -> str:
    """Resolve thumbnail path with fallback to default image."""
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent
    thumbnail_path = f"/images/page_blog/{filename}/{thumbnail_filename}"
    file_system_path = project_root / f"assets{thumbnail_path}"

    if not file_system_path.exists():
        thumbnail_path = "/images/page_blog/default_thumbnail.jpg"

    return thumbnail_path


def _build_thumbnail_paths(
    thumbnail_url: str,
) -> tuple[str, str, str]:
    """
    Build thumbnail paths for fallback, AVIF, and WebP formats.

    Returns tuple of (fallback, avif, webp). Empty string if format doesn't exist.
    """
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent

    url_path = Path(thumbnail_url)
    base_path = str(url_path.with_suffix(""))
    asset_base = base_path.lstrip("/")

    avif_path = ""
    if (project_root / f"assets/{asset_base}.avif").exists():
        avif_path = f"{base_path}.avif"

    webp_path = ""
    if (project_root / f"assets/{asset_base}.webp").exists():
        webp_path = f"{base_path}.webp"

    return thumbnail_url, avif_path, webp_path


def parse_blog_post(file_path: Path) -> BlogPostDict | None:
    """Parse a single blog post markdown file into a BlogPostDict."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            metadata_raw, content = frontmatter.parse(f.read())
        metadata = {str(key): str(value) for key, value in metadata_raw.items()}

        filename, language = (part for part in file_path.stem.rsplit(".", 1))
        story_number = filename.split("_")[0]
        slug = metadata.get("slug", filename)

        thumbnail_filename = metadata.get("thumbnail", "thumbnail.jpg")
        thumbnail_url = _resolve_thumbnail_path(filename, thumbnail_filename)
        thumbnail_fallback, thumbnail_avif, thumbnail_webp = _build_thumbnail_paths(
            thumbnail_url
        )

        content_objects = parse_blog_content(content, filename)

        date_str = metadata.get("date", "2023-02-01")
        dt_obj = parse_datetime(date_str)
        formatted_date = format_date(date_str, language)
        datetime_iso = dt_obj.isoformat()

        url = f"/blog/{slug}/"

        blog_post: BlogPostDict = {
            "title": metadata.get("title", ""),
            "slug": slug,
            "summary": metadata.get("summary", ""),
            "author": metadata.get("author", ""),
            "date": date_str,
            "formatted_date": formatted_date,
            "datetime_iso": datetime_iso,
            "thumbnail_alt": metadata.get("thumbnail_alt", ""),
            "thumbnail_fallback": thumbnail_fallback,
            "thumbnail_avif": thumbnail_avif,
            "thumbnail_webp": thumbnail_webp,
            "content": content,
            "content_objects": content_objects,
            "category": metadata.get("category", ""),
            "filename": filename,
            "story_number": story_number,
            "language": language,
            "url": url,
        }

        return blog_post

    except Exception as e:
        raise ValueError(f"Failed to parse blog post {file_path}: {e}") from e


def load_all_posts(
    force_reload: bool = False,
    language: str | None = None,
) -> list[BlogPostDict]:
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

    posts.sort(key=lambda p: p["datetime_iso"], reverse=True)
    _posts_cache[language] = posts

    return posts


def load_all_blog_posts_dict() -> dict[str, list[BlogPostDict]]:
    """Load all blog posts for all languages as BlogPostDict dictionaries."""
    languages = ["nl", "en", "de"]
    result: dict[str, list[BlogPostDict]] = {}

    for lang in languages:
        result[lang] = load_all_posts(force_reload=False, language=lang)

    return result
