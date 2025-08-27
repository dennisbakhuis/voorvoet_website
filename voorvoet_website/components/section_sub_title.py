# Sub title component
import reflex as rx
from ..theme import Colors


def section_sub_title(text: str, **props) -> rx.Component:
    return rx.text(
        text,
        font_size=["20px", "24px", "28px", "30px"],
        font_weight="700",
        color=Colors.text["subheading"],
        **props
    )
