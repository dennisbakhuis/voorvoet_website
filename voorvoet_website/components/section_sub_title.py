# Sub title component
import reflex as rx
from ..theme import Colors, FontSizes


def section_sub_title(text: str, **props) -> rx.Component:
    return rx.text(
        text,
        font_size=FontSizes.section_sub_title,
        font_weight="700",
        color=Colors.text["subheading"],
        **props
    )
