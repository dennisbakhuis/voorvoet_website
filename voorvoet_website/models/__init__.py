"""Models module containing the data structures."""

from .phone_number import PhoneNumber
from .email_address import EmailAddress
from .contact_form import ContactForm
from .blog_post import BlogPostDict, ContentType, ContentDict

__all__ = [
    "PhoneNumber",
    "EmailAddress",
    "ContactForm",
    "BlogPostDict",
    "ContentType",
    "ContentDict",
]
