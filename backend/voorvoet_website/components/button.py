# Button component
import reflex as rx
from ..theme import PRIMARY, LIGHT, ACCENT


def button(label: str, href: str | None = None, on_click=None, variant: str = "solid") -> rx.Component:
    base = dict(
        px="20px",
        py="12px",
        border_radius="9999px",
        font_weight="600",
        transition="all .2s ease",
        cursor="pointer",
        display="inline-flex",
        align_items="center",
        gap="8px",
        white_space="nowrap",
    )
    if variant == "solid":
        base.update(bg=LIGHT, color=ACCENT, _hover={"bg": PRIMARY, "color": LIGHT})  # type: ignore
    elif variant == "primary":
        base.update(bg=PRIMARY, color=LIGHT, _hover={"opacity": 0.9})  # type: ignore
    else:
        base.update(bg="transparent", border=f"1px solid {LIGHT}", color=LIGHT, _hover={"bg": LIGHT, "color": ACCENT})  # type: ignore

    element = rx.link(rx.hstack(rx.text(label),), href=href) if href else rx.box(rx.text(label))
    return rx.box(element, on_click=on_click, **base)  # type: ignore
