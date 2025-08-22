# Section component
import reflex as rx

from ..theme import LIGHT


def section(*children, bg=LIGHT, **styles) -> rx.Component:
    return rx.box(
        *children,
        width="100%",
        py=["48px", "64px"],
        bg=bg,
        **styles,
    )
