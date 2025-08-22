# Container component to center content and limit max width
import reflex as rx


def container(*children, **styles) -> rx.Component:
    base = dict(
        width="100%",
        max_width="1200px",
        margin_x="auto",
        padding_x=["5%", "5%", "10%"],
    )
    base.update(styles)
    return rx.box(*children, **base)  # type: ignore
