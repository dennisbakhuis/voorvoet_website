# Container component to center content and limit max width
import reflex as rx

from ..theme import Layout, Spacing


def container(*children, **styles) -> rx.Component:
    base = dict(
        width="100%",
        max_width=Layout.max_width,
        margin_x="auto",
        padding_x=Spacing.container_padding,
    )
    base.update(styles)
    return rx.box(*children, **base)  # type: ignore
