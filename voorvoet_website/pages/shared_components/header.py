# Header used across multiple all pages
import reflex as rx

from ...theme import Colors
from ...state import WebsiteState
from ...components import container


def header() -> rx.Component:
    nav_links = [
        ("Blog", "#about"),
        ("Informatie", "#services"),
        ("Vergoedingen", "#kim"),
        ("Contact", "#contact"),
    ]

    def nav_items():
        return [
            rx.link(
                link,
                href=href,
                color=Colors.text["heading"],
                font_size="24px",
                font_weight="600",
                _hover={"color": Colors.primary["300"]},
            )
            for link, href in nav_links
        ]

    # Create the main header container with max width constraint
    header_container = container(
        rx.hstack(
            # Logo on the left side
            rx.image(
                src="/images/podotherapeut_enschede_voorvoet_praktijk_voor_podotherapie_logo.svg",
                width="300px",
                height="90px",
                
            ),
            # Navigation items on the right side
            rx.hstack(
                rx.hstack(*nav_items(), gap="20px", display=["none", "none", "flex"]),
                rx.icon_button(
                    "menu",
                    aria_label="menu",
                    on_click=WebsiteState.toggle_nav,  # type: ignore
                    display=["inline-flex", "inline-flex", "none"],
                    color=Colors.text["heading"],
                    bg="transparent",
                    size="4",  # Twice as big (default is "2")
                ),
                align="center",
                justify="end",
            ),
            align="center",
            justify="between",
            width="100%",
            padding_right="12px",
        ),
    )

    # Create the fixed header bar
    bar = rx.box(
        header_container,
        position="fixed",
        top="0",
        left="0",
        z_index="20",
        width="100%",
        style={"backdropFilter": "saturate(180%) blur(6px)"},
    )

    # Create mobile menu
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
                            color=Colors.text["white"],
                            py="8px",
                            on_click=WebsiteState.toggle_nav,  # type: ignore
                        )
                        for link, href in nav_links
                    ],
                    gap="10px",
                ),
                padding_x=["12px", "16px", "24px"],
            ),
            position="fixed",
            top="60px",
            left="0",
            width="100%",
            bg=Colors.text["heading"],
            py="16px",
            z_index="19",
        ),
        rx.box(),
    )

    return rx.fragment(bar, mobile_menu)
