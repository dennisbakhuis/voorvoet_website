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
from ...utils.translations import get_language_from_path


def page_informatie() -> rx.Component:
    """
    Create the complete informatie page with all sections.

    The informatie page provides comprehensive details about podiatry services,
    including what podiatry is, who it's for, treatment processes, common
    complaints, company podiatry services, and risk foot classifications.

    Returns
    -------
    rx.Component
        A fragment containing all sections of the informatie page including
        header, hero, informational sections, footer, and modal components.
    """
    language = get_language_from_path()

    return rx.fragment(
        header(language),
        section_hero(),
        section_starter(language),
        section_what_is_podiatry(language),
        section_for_everyone(language),
        section_behandeltraject(language),
        section_veel_voorkomende_klachten(language),
        section_bedrijfspodotherapie(language),
        section_risicovoet(language),

        footer(language),
        modal(),
    )
