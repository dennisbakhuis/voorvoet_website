"""BlogPost data model definition."""

from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Any, Literal


ContentType = Literal["heading", "paragraph", "markdown", "image", "button", "list"]
ContentDict = dict[str, Any]


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
    date : datetime
        Publication date and time.
    formatted_date : str
        Pre-formatted date string in locale format.
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
    url : str
        Computed URL path for the blog post (read-only property).
    """

    title: str
    slug: str
    summary: str
    author: str
    date: datetime
    formatted_date: str
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

    @field_validator("date", mode="before")
    @classmethod
    def parse_date(cls, v: str | datetime) -> datetime:
        """Parse date from string or datetime."""
        if isinstance(v, str):
            return datetime.fromisoformat(v)
        return v

    @property
    def url(self) -> str:
        """Get the URL path for this blog post."""
        return f"/blog/{self.slug}/"
