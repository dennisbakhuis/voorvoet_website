"""BlogPost data model definition."""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Any, Literal


ContentType = Literal["heading", "paragraph", "markdown", "image", "button", "list"]
ContentDict = dict[str, Any]

FALLBACK_DATE = datetime(2023, 2, 1)


class BlogPost(BaseModel):
    """
    Represents a blog post with metadata and content.

    Attributes
    ----------
    title : str
        The title of the blog post.
    slug : str
        URL-friendly identifier for the blog post.
    summary : str
        Brief summary or excerpt of the blog post.
    author : str
        Author name.
    date : str
        Publication date string (as stored in frontmatter).
    thumbnail : str
        Primary thumbnail image URL.
    thumbnail_alt : str
        Alt text for the thumbnail image.
    content : str
        Raw markdown content after frontmatter extraction.
    filename : str
        Original filename of the blog post source.
    thumbnail_fallback : str
        Fallback image URL (JPG or PNG).
    thumbnail_avif : str
        AVIF format image URL (empty string if not available).
    thumbnail_webp : str
        WebP format image URL (empty string if not available).
    content_objects : list[ContentDict]
        Parsed content as structured dictionaries.
    category : str
        Article category/section.
    story_number : str
        Numeric identifier for the story.
    language : str
        Language code (nl/de/en).
    """

    title: str
    slug: str
    summary: str
    author: str
    date: str
    thumbnail: str
    thumbnail_alt: str
    content: str
    filename: str
    thumbnail_fallback: str
    thumbnail_avif: str = ""
    thumbnail_webp: str = ""
    content_objects: Any = Field(default_factory=lambda: [])
    category: str
    story_number: str
    language: str

    def datetime(self) -> datetime:
        """Parse date string to datetime (YYYY-MM-DD, DD-MM-YYYY, or ISO format)."""
        try:
            return datetime.strptime(self.date, "%Y-%m-%d")
        except ValueError:
            try:
                return datetime.strptime(self.date, "%d-%m-%Y")
            except ValueError:
                try:
                    return datetime.fromisoformat(self.date)
                except ValueError:
                    print(f"Warning: Could not parse date '{self.date}'")
                    return FALLBACK_DATE

    @property
    def formatted_date(self) -> str:
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
        date_obj = self.datetime()
        return f"{date_obj.day} {months_nl[date_obj.month]} {date_obj.year}"

    @property
    def url(self) -> str:
        """Get the URL path for this blog post."""
        return f"/blog/{self.slug}/"
