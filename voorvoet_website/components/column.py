# Column component for flexible layout
import reflex as rx


def column(*children, **props) -> rx.Component:
    return rx.box(
        *children,
        width="100%",
        flex="1",
        **props
    )