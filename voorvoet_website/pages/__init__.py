"""Module holding all pages for the website."""

from .home import page_home
from .blog import page_blog, page_blog_post
from .information import page_information
from .reimbursements import page_reimbursements
from .contact import page_contact
from .order_insoles import page_order_insoles
from .credits import page_credits
from .not_found import page_not_found

__all__ = [
    "page_home",
    "page_blog",
    "page_blog_post",
    "page_information",
    "page_reimbursements",
    "page_contact",
    "page_order_insoles",
    "page_credits",
    "page_not_found",
]
