# Regular text component for body content
import reflex as rx
from ..theme import DARK


def regular_text(text: str, **props) -> rx.Component:
    return rx.text(
        text,
        font_size="18px",  # Slightly bigger than standard 16px
        line_height="1.6",
        color=DARK,
        **props
    )