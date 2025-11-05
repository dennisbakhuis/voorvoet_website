"""Modal dialog component for user input and interactions."""
import reflex as rx

from .button import button
from ..theme import Colors
from ..states import WebsiteState


def modal() -> rx.Component:
    """
    Create a modal dialog component with input capabilities.

    This component renders a dialog that can be opened/closed through the
    WebsiteState. It includes a title, description, text area input, and
    action buttons.

    Returns
    -------
    rx.Component
        A Reflex dialog component with input field and controls.

    Notes
    -----
    The modal state is managed through WebsiteState properties:
    - modal_open: Controls visibility
    - modal_title: Dialog heading text
    - modal_desc: Dialog description text
    - modal_input: Text area value
    """
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
            rx.hstack(button("Open", href="#"), justify="center", mt="12px"),
            width=["90vw", "480px"],
            max_width="600px",
            bg=Colors.backgrounds["white"],
            border_radius="12px",
        ),
        open=WebsiteState.modal_open,
        on_open_change=WebsiteState.on_modal_change,  # type: ignore
    )
