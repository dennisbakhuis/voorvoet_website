import reflex as rx

from ...theme import Colors
from ...components import section, container, section_title, regular_text


def section_starter() -> rx.Component:
    return section(
        container(
            section_title(
                "Welkom bij onze Blog",
            ),
            regular_text(
                "Hier vindt u artikelen over podotherapie, voetzorg tips en informatie over "
                "het voorkomen en behandelen van voetklachten. Onze expertise helpt u "
                "uw voeten gezond te houden.",
                color=Colors.text["content"],
                max_width="800px",
            ),
        ),
        background=Colors.backgrounds["white"],
        padding_y="3rem",
    )