# Post content object models - Pydantic models for blog post content types
from pydantic import BaseModel, ConfigDict
from typing import Literal, Union


class PostObject(BaseModel):
    """Base class for all post content objects"""
    model_config = ConfigDict(extra='allow')

    type: str

    # Optional fields that may exist on child classes
    content: str | None = None
    src: str | None = None
    alt: str | None = None
    caption: str | None = None
    label: str | None = None
    url: str | None = None

    def to_dict(self):
        return {
            "type": self.type,
            "content": self.content,
            "src": self.src,
            "alt": self.alt,
            "label": self.label,
            "url": self.url,
        }


class PostMarkdown(PostObject):
    """Represents markdown content"""
    type: Literal["markdown"] = "markdown"
    content: str = ""


class PostImage(PostObject):
    """Represents an image with caption"""
    type: Literal["image"] = "image"
    src: str = ""
    alt: str | None = None
    caption: str | None = None


class PostButton(PostObject):
    """Represents a CTA button"""
    type: Literal["button"] = "button"
    label: str = ""
    url: str = ""


# Type alias for any content object
ContentObject = Union[PostMarkdown, PostImage, PostButton]
