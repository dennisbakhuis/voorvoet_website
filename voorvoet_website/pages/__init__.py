"""Module holding all pages for the website."""
from .home import page_home
from .blog import page_blog, page_blog_post
from .informatie import page_informatie
from .vergoedingen import page_vergoedingen
from .contact import page_contact
from .zolen_bestellen import page_zolen_bestellen

__all__ = [
    "page_home",
    "page_blog",
    "page_blog_post",
    "page_informatie",
    "page_vergoedingen",
    "page_contact",
    "page_zolen_bestellen",
]
