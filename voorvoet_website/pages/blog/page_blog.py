import reflex as rx

from .section_hero import section_hero
from .section_blog_list import section_blog_list

from ..shared_components import footer, header, modal


def page_blog() -> rx.Component:
    return rx.fragment(
        header(),
        section_hero(),
        section_blog_list(),

        footer(),
        modal(),
    )
