# Section title component for main section headings
import reflex as rx
from ..theme import Colors, FontSizes


def section_title(text: str, **props) -> rx.Component:
    return rx.text(
        text,
        font_size=FontSizes.section_title,
        font_weight="700",
        color=Colors.text["heading"],
        **props
    )