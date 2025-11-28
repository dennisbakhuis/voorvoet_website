"""BlogPost data model definition."""
from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional, Any, Literal, Union


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
    date: Union[datetime, str]
    date_modified: Optional[Union[datetime, str]] = None
    formatted_date: str
    thumbnail: str
    thumbnail_alt: str = ""
    content: str = ""
    filename: str
    thumbnail_url: str
    read_time: Optional[Union[int, str]] = None
    content_objects: Any = Field(default_factory=list)
    tags: Union[list[str], str] = Field(default_factory=list)
    category: Optional[str] = None

    @field_validator('date', mode='before')
    @classmethod
    def parse_date(cls, v):
        """Parse date from string or datetime."""
        if isinstance(v, str):
            return datetime.fromisoformat(v)
        return v

    @field_validator('date_modified', mode='before')
    @classmethod
    def parse_date_modified(cls, v):
        """Parse date_modified from string or datetime."""
        if v is None or v == "":
            return None
        if isinstance(v, str):
            return datetime.fromisoformat(v)
        return v

    @field_validator('read_time', mode='before')
    @classmethod
    def parse_read_time(cls, v):
        """Parse read_time from string or int."""
        if v is None or v == "":
            return None
        if isinstance(v, str):
            return int(v)
        return v

    @field_validator('tags', mode='before')
    @classmethod
    def parse_tags(cls, v):
        """Parse tags from string or list."""
        if isinstance(v, str):
            if v == "":
                return []
            return [tag.strip() for tag in v.split(',')]
        return v

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
