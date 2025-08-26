# Section title component for main section headings
import reflex as rx
from ..theme import DARK


def section_title(text: str, **props) -> rx.Component:
    return rx.text(
        text,
        font_size=["24px", "28px", "32px", "36px"],  # Slightly larger than sub_title
        font_weight="700",
        color=DARK,
        **props
    )