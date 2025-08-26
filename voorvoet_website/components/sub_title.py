# Sub title component
import reflex as rx
from ..theme import DARK


def sub_title(text: str, **props) -> rx.Component:
    return rx.text(
        text,
        font_size=["20px", "24px", "28px", "30px"],  # Responsive font sizes
        font_weight="700",
        color=DARK,
        **props
    )
