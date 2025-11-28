"""Home page composition with all sections."""
import reflex as rx

from .section_hero import section_hero
from .section_who_is_voorvoet import section_who_is_voorvoet
from .section_order_insoles import section_order_insoles
from .section_introduction import section_introduction
from .section_information import section_information
from .section_locations import section_locations

from ..shared_sections import footer, header
from ...components import organization_schema
from ...utils.translations import get_language_from_path


def page_home() -> rx.Component:
    """
    Create the complete home page with all sections.

    Returns
    -------
    rx.Component
        A fragment containing all sections of the home page in order.
    """
    language = get_language_from_path()

    return rx.fragment(
        organization_schema(),
        header(language),
        section_hero(language),
        section_who_is_voorvoet(language),
        section_order_insoles(language),
        section_introduction(language),
        section_information(language),
        section_locations(language),
        footer(language),
    )
