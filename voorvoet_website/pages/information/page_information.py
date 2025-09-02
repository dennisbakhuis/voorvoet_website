import reflex as rx

from .section_hero import section_hero

from ..shared_components import footer, header, modal


def page_information() -> rx.Component:
    return rx.fragment(
        header(),
        section_hero(),

        footer(),
        modal(),
    )
