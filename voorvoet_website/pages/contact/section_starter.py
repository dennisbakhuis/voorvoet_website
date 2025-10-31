import reflex as rx

from ...theme import Colors
from ...components import section, container, section_title, regular_text


def section_starter() -> rx.Component:
    return section(
        container(
            section_title(
                "Contact & Afspraken",
            ),
            regular_text(
                "Heeft u vragen over podotherapie of wilt u een afspraak maken? "
                "We staan klaar om u te helpen. Neem contact op via onderstaande "
                "gegevens of plan direct een afspraak in.",
                color=Colors.text["content"],
                max_width="800px",
            ),
        ),
        background=Colors.backgrounds["white"],
        padding_y="3rem",
    )