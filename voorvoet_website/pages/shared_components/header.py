# Header used across multiple all pages
import reflex as rx

from ...theme import ACCENT, DARK, LIGHT, PRIMARY
from ...state import WebsiteState
from ...components import container


def header() -> rx.Component:
    nav_links = [
        ("Blog", "#blog"),
        ("Informatie", "#informatie"),
        ("Vergoedingen", "#vergoedingen"),
        ("Contact", "#contact"),
    ]

    def nav_items():
        return [
            rx.link(
                link,
                href=href,
                color=DARK,
                font_size="24px",
                font_weight="600",
                _hover={"color": PRIMARY},
            )
            for link, href in nav_links
        ]


    bar = rx.hstack(
        container(
            rx.hstack(
                rx.image(
                    src="/images/podotherapeut_enschede_voorvoet_praktijk_voor_podotherapie_logo.svg",
                    width="300px",
                    height="90px",
                ),
                rx.hstack(
                    rx.hstack(*nav_items(), gap="20px", display=["none", "none", "flex"]),
                    rx.icon_button(
                        "menu",
                        aria_label="menu",
                        on_click=WebsiteState.toggle_nav,  # type: ignore
                        display=["inline-flex", "inline-flex", "none"],
                        color=LIGHT,
                        bg="transparent",
                    ),
                    align="center",
                    justify="end",
                ),
                align="center",
                justify="between",
                width="100%",
            ),
            max_width="1200px",
            margin_x="auto",
            padding_x=["12px", "16px", "24px"],
        ),
        position="fixed",
        top="0",
        left="0",
        z_index="20",
        width="100%",
        style={"backdropFilter": "saturate(180%) blur(6px)"},
    )

    mobile_menu = rx.cond(
        WebsiteState.nav_open,
        rx.box(
            container(
                rx.vstack(
                    *[
                        rx.link(
                            link,
                            href=href,
                            width="100%",
                            text_align="right",
                            color=LIGHT,
                            py="8px",
                            on_click=WebsiteState.toggle_nav,  # type: ignore
                        )
                        for link, href in nav_links
                    ],
                    gap="10px",
                ),
                max_width="1200px",
                margin_x="auto",
                padding_x=["12px", "16px", "24px"],
            ),
            position="fixed",
            top="60px",
            left="0",
            width="100%",
            bg=ACCENT,
            py="16px",
            z_index="19",
        ),
        rx.box(),
    )

    return rx.fragment(bar, mobile_menu)
