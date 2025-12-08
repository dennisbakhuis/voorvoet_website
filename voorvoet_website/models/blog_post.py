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
    author : str | None
        Author name, defaults to None if not specified.
    date : datetime
        Publication date and time.
    date_modified : datetime | None
        Last modification date, defaults to None (uses publication date).
    formatted_date : str
        Pre-formatted date string in Dutch locale.
    thumbnail : str
        Filename of the thumbnail image.
    thumbnail_alt : str
        Alt text for the thumbnail image.
    content : str
        Raw markdown content after frontmatter extraction.
    filename : str
        Original filename of the blog post source.
    thumbnail_url : str
        Full resolved URL to thumbnail with fallback.
    thumbnail_fallback : str
        Fallback image URL (JPG or PNG).
    thumbnail_avif : str
        AVIF format image URL (empty string if not available).
    thumbnail_webp : str
        WebP format image URL (empty string if not available).
    read_time : int | None
        Estimated reading time in minutes, defaults to None.
    content_objects : list[ContentDict]
        Parsed content as structured dictionaries.
    tags : list[str]
        Keywords/tags for the blog post for SEO and categorization.
    category : str | None
        Article category/section, defaults to None.
    url : str
        Computed URL path for the blog post (read-only property).
    """

    title: str
    slug: str
    summary: str
    author: str | None = None
    date: datetime
    date_modified: datetime | None = None
    formatted_date: str
    thumbnail: str
    thumbnail_alt: str = ""
    content: str = ""
    filename: str
    thumbnail_url: str
    thumbnail_fallback: str = ""
    thumbnail_avif: str = ""
    thumbnail_webp: str = ""
    read_time: int | None = None
    content_objects: Any = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)
    category: str | None = None
    story_number: str

    @field_validator("date", mode="before")
    @classmethod
    def parse_date(cls, v: str | datetime) -> datetime:
        """Parse date from string or datetime."""
        if isinstance(v, str):
            return datetime.fromisoformat(v)
        return v

    @field_validator("date_modified", mode="before")
    @classmethod
    def parse_date_modified(cls, v: str | datetime | None) -> datetime | None:
        """Parse date_modified from string or datetime."""
        if v is None or v == "":
            return None
        if isinstance(v, str):
            return datetime.fromisoformat(v)
        return v

    @field_validator("read_time", mode="before")
    @classmethod
    def parse_read_time(cls, v: str | int | None) -> int | None:
        """Parse read_time from string or int."""
        if v is None or v == "":
            return None
        if isinstance(v, str):
            return int(v)
        return v

    @field_validator("tags", mode="before")
    @classmethod
    def parse_tags(cls, v: str | list[str]) -> list[str]:
        """Parse tags from string or list."""
        if isinstance(v, str):
            if v == "":
                return []
            return [tag.strip() for tag in v.split(",")]
        return v

    @field_validator("thumbnail_alt", mode="before")
    @classmethod
    def ensure_thumbnail_alt(cls, v: str | None) -> str:
        """Ensure thumbnail_alt is never None."""
        if v is None or v == "":
            return ""
        return str(v)

    @property
    def url(self) -> str:
        """
        Get the URL path for this blog post.

        Returns
        -------
        str
            URL path in the format '/blog/{slug}/'.
        """
        return f"/blog/{self.slug}/"
