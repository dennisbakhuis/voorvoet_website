# Shared modal component
import reflex as rx

from ...components import button
from ...theme import LIGHT
from ...state import WebsiteState


def modal() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.box()),
        rx.dialog.content(
            rx.hstack(rx.spacer(), rx.icon_button("x", on_click=WebsiteState.close_modal), align="center"),  # type: ignore
            rx.heading(WebsiteState.modal_title, size="6", text_align="center"),
            rx.text(WebsiteState.modal_desc, mt="8px"),
            rx.text_area(
                placeholder="write...",
                value=WebsiteState.modal_input,
                on_change=WebsiteState.set_modal_input,  # type: ignore
                max_length=2000,
            ),
            rx.hstack(button("Open", href="#", variant="primary"), justify="center", mt="12px"),
            width=["90vw", "480px"],
            max_width="600px",
            bg=LIGHT,
            border_radius="12px",
        ),
        open=WebsiteState.modal_open,
        on_open_change=WebsiteState.on_modal_change,  # type: ignore
    )
