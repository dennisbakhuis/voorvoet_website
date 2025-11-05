# Blog post data model
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Any, Literal

# Type definitions for content objects
ContentType = Literal["markdown", "image", "button"]

# Type hints for content object dictionaries
ContentDict = dict[str, Any]  # Always has 'type' key with ContentType value


class BlogPost(BaseModel):
    """Represents a blog post with metadata and content"""

    # Metadata from frontmatter
    title: str
    slug: str
    summary: str
    author: Optional[str] = None  # Optional: can be None if not specified
    date: datetime
    formatted_date: str     # Pre-formatted date string in Dutch
    thumbnail: str          # Filename only (e.g., "thumbnail.jpg")
    thumbnail_alt: str

    # Content and internal data
    content: str            # Raw markdown content (after frontmatter)
    filename: str           # e.g., "001_podotherapeut_of_podoloog"
    thumbnail_url: str      # Full resolved URL to thumbnail (with fallback)
    read_time: Optional[int] = None  # Optional: estimated reading time in minutes
    content_objects: list[ContentDict] = Field(default_factory=list)  # Parsed content as dicts

    @property
    def url(self) -> str:
        """Get the URL for this blog post"""
        return f"/blog/{self.slug}/"
