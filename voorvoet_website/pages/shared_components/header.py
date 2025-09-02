# Header used across multiple all pages
import reflex as rx

from ...theme import Colors, FontSizes
from ...state import WebsiteState
from ...components import container


def header() -> rx.Component:
    nav_items = [
        rx.cond(
            WebsiteState.current_page_path != "/",
            rx.link("Home", color=Colors.text["heading"], font_size=FontSizes.nav_link, font_weight="600", _hover={"color": Colors.primary["300"]}, on_click=WebsiteState.nav_to_home, cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
        rx.cond(
            WebsiteState.current_page_path != "/blog/",
            rx.link("Blog", color=Colors.text["heading"], font_size=FontSizes.nav_link, font_weight="600", _hover={"color": Colors.primary["300"]}, on_click=WebsiteState.nav_to_blog, cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
        rx.cond(
            WebsiteState.current_page_path != "/informatie/",
            rx.link("Informatie", color=Colors.text["heading"], font_size=FontSizes.nav_link, font_weight="600", _hover={"color": Colors.primary["300"]}, on_click=WebsiteState.nav_to_informatie, cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
        rx.cond(
            WebsiteState.current_page_path != "/vergoeding/",
            rx.link("Vergoedingen", color=Colors.text["heading"], font_size=FontSizes.nav_link, font_weight="600", _hover={"color": Colors.primary["300"]}, on_click=WebsiteState.nav_to_vergoeding, cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
        rx.cond(
            WebsiteState.current_page_path != "/contact/",
            rx.link("Contact", color=Colors.text["heading"], font_size=FontSizes.nav_link, font_weight="600", _hover={"color": Colors.primary["300"]}, on_click=WebsiteState.nav_to_contact, cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
    ]
    
    mobile_nav_items = [
        rx.cond(
            WebsiteState.current_page_path != "/",
            rx.link("Home", width="100%", text_align="right", color=Colors.text["white"], py="8px", on_click=[WebsiteState.toggle_nav, WebsiteState.nav_to_home], cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
        rx.cond(
            WebsiteState.current_page_path != "/blog/",
            rx.link("Blog", width="100%", text_align="right", color=Colors.text["white"], py="8px", on_click=[WebsiteState.toggle_nav, WebsiteState.nav_to_blog], cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
        rx.cond(
            WebsiteState.current_page_path != "/informatie/",
            rx.link("Informatie", width="100%", text_align="right", color=Colors.text["white"], py="8px", on_click=[WebsiteState.toggle_nav, WebsiteState.nav_to_informatie], cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
        rx.cond(
            WebsiteState.current_page_path != "/vergoeding/",
            rx.link("Vergoedingen", width="100%", text_align="right", color=Colors.text["white"], py="8px", on_click=[WebsiteState.toggle_nav, WebsiteState.nav_to_vergoeding], cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
        rx.cond(
            WebsiteState.current_page_path != "/contact/",
            rx.link("Contact", width="100%", text_align="right", color=Colors.text["white"], py="8px", on_click=[WebsiteState.toggle_nav, WebsiteState.nav_to_contact], cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
    ]

    header_container = container(
        rx.hstack(
            rx.image(
                src="/images/podotherapeut_enschede_voorvoet_praktijk_voor_podotherapie_logo.svg",
                width="300px",
                height="90px",
                
            ),
            rx.hstack(
                rx.hstack(*nav_items, gap="20px", display=["none", "none", "flex"]),
                rx.icon_button(
                    "menu",
                    aria_label="menu",
                    on_click=WebsiteState.toggle_nav,  # type: ignore
                    display=["inline-flex", "inline-flex", "none"],
                    color=Colors.text["heading"],
                    bg="transparent",
                    size="4",
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

    bar = rx.box(
        header_container,
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
                    *mobile_nav_items,
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
