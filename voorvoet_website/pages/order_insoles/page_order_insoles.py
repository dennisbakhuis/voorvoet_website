"""Order insoles page composition with all sections."""
import reflex as rx

from .section_hero import section_hero
from .section_starter import section_starter
from .section_order_form import section_order_form

from ..shared_sections import footer, header
from ...components import toast


def page_order_insoles() -> rx.Component:
    """
    Create the complete order insoles page with all sections.

    The order insoles page is composed of: header, hero banner, starter text,
    order form, footer, and toast notification components.

    Returns
    -------
    rx.Component
        A fragment containing all sections of the order insoles page in order.
    """
    return rx.fragment(
        header(),
        section_hero(),
        section_starter(),
        section_order_form(),
        footer(),
        toast(),
    )
