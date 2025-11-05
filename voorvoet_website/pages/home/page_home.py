"""Home page composition with all sections."""
import reflex as rx

from .section_hero import section_hero
from .section_who_is_voorvoet import section_who_is_voorvoet
from .section_order_insoles import section_order_insoles
from .section_introduction import section_introduction
from .section_information import section_information
from .section_locations import section_locations

from ..shared_sections import footer, header
from ...components import modal


def page_home() -> rx.Component:
    """
    Create the complete home page with all sections.

    The home page is composed of multiple sections arranged vertically:
    header, hero, about practice, ordering insoles, introduction,
    information cards, locations, footer, and modal.

    Returns
    -------
    rx.Component
        A fragment containing all sections of the home page in order.
    """
    return rx.fragment(
        header(),
        section_hero(),
        section_who_is_voorvoet(),
        section_order_insoles(),
        section_introduction(),
        section_information(),
        section_locations(),
        footer(),
        modal(),
    )
