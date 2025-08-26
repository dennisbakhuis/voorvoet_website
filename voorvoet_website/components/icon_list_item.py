# Icon list item component for CTA boxes and lists
import reflex as rx
from ..theme import PRIMARY


def icon_list_item(icon: str, text: str, **props) -> rx.Component:
    return rx.hstack(
        rx.html(f'<i class="fa {icon}" style="color: {PRIMARY}; font-size: clamp(18px, 4vw, 27px);"/>'),
        rx.text(
            text,
            font_size=["16px", "18px", "22px", "24px"],  # Responsive font sizes
            font_weight="500",
            color="#374151",  # Gray-700 for readable text
            line_height="1.5"
        ),
        spacing="3",
        align="start",
        **props
    )