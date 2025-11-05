"""Information page composition with all sections."""
import reflex as rx

from .section_hero import section_hero
from .section_starter import section_starter
from .section_what_is_podiatry import section_what_is_podiatry
from .section_for_everyone import section_for_everyone
from .section_behandeltraject import section_behandeltraject
from .section_veel_voorkomende_klachten import section_veel_voorkomende_klachten
from .section_bedrijfspodotherapie import section_bedrijfspodotherapie
from .section_risicovoet import section_risicovoet

from ..shared_sections import footer, header
from ...components import modal


def page_information() -> rx.Component:
    """
    Create the complete information page with all sections.

    The information page provides comprehensive details about podiatry services,
    including what podiatry is, who it's for, treatment processes, common
    complaints, company podiatry services, and risk foot classifications.

    Returns
    -------
    rx.Component
        A fragment containing all sections of the information page including
        header, hero, informational sections, footer, and modal components.
    """
    return rx.fragment(
        header(),
        section_hero(),
        section_starter(),
        section_what_is_podiatry(),
        section_for_everyone(),
        section_behandeltraject(),
        section_veel_voorkomende_klachten(),
        section_bedrijfspodotherapie(),
        section_risicovoet(),

        footer(),
        modal(),
    )
