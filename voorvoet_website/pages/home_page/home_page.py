import reflex as rx

from .section_hero import section_hero
from .section_who_is_voorvoet import section_who_is_voorvoet
from .section_order_insoles import section_order_insoles
from .section_introduction import section_introduction
from .section_information import section_information
from .section_locations import section_locations

from ..shared_components import footer, header, modal


def home_page() -> rx.Component:
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
