# Icon list item component for CTA boxes and lists
import reflex as rx
from ..theme import Colors, FontSizes


def icon_list_item(icon: str, text: str, **props) -> rx.Component:
    return rx.hstack(
        rx.html(f'<i class="fa {icon}" style="color: {Colors.text["content"]}; font-size: 8px; margin-top: 6px;"/>'),
        rx.text(
            text,
            font_size=FontSizes.regular,
            color=Colors.text["content"],
            line_height="1.6"
        ),
        spacing="3",
        align="start",
        **props
    )