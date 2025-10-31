import reflex as rx

from .section_hero import section_hero
from .section_starter import section_starter
from .section_what_is_podiatry import section_what_is_podiatry
from .section_for_everyone import section_for_everyone
from .section_behandeltraject import section_behandeltraject
from .section_veel_voorkomende_klachten import section_veel_voorkomende_klachten
from .section_bedrijfspodotherapie import section_bedrijfspodotherapie
from .section_risicovoet import section_risicovoet

from ..shared_components import footer, header, modal


def page_information() -> rx.Component:
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
