import reflex as rx

from .section_hero import section_hero
from .section_starter import section_starter
from .section_contact_form import section_contact_form

from ..shared_sections import footer, header
from ...components import toast, modal
from ...state import WebsiteState


def page_contact() -> rx.Component:
    return rx.fragment(
        header(),
        section_hero(),
        section_contact_form(),

        footer(),
        modal(),
        toast(),
    )
