import reflex as rx

from ...theme import Colors
from ...components import section, container, section_title, regular_text


def section_starter() -> rx.Component:
    return section(
        container(
            section_title(
                "Vergoedingen en Kosten",
            ),
            regular_text(
                "Podotherapie wordt vaak vergoed door uw zorgverzekering. Hier vindt u "
                "alle informatie over vergoedingen, kosten en wat u kunt verwachten "
                "bij uw behandeling bij VoorVoet.",
                color=Colors.text["content"],
                max_width="800px",
            ),
        ),
        background=Colors.backgrounds["white"],
        padding_y="3rem",
    )
