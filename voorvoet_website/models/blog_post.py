"""BlogPost data model definition."""
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Any, Literal


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
    author : Optional[str]
        Author name, defaults to None if not specified.
    date : datetime
        Publication date and time.
    date_modified : Optional[datetime]
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
    read_time : Optional[int]
        Estimated reading time in minutes, defaults to None.
    content_objects : list[ContentDict]
        Parsed content as structured dictionaries.
    tags : list[str]
        Keywords/tags for the blog post for SEO and categorization.
    category : Optional[str]
        Article category/section, defaults to None.
    url : str
        Computed URL path for the blog post (read-only property).
    """

    title: str
    slug: str
    summary: str
    author: Optional[str] = None
    date: datetime
    date_modified: Optional[datetime] = None
    formatted_date: str
    thumbnail: str
    thumbnail_alt: str
    content: str
    filename: str
    thumbnail_url: str
    read_time: Optional[int] = None
    content_objects: list[ContentDict] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)
    category: Optional[str] = None

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
