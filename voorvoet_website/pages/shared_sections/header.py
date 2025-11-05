"""Header component used across all pages."""
import reflex as rx

from ...theme import Colors, FontSizes
from ...states import WebsiteState
from ...components import container, language_switcher


TRANSLATIONS = {
    "nl": {
        "home": "Home",
        "blog": "Blog",
        "informatie": "Informatie",
        "vergoedingen": "Vergoedingen",
        "contact": "Contact",
    },
    "de": {
        "home": "Home",
        "blog": "Blog",
        "informatie": "Informationen",
        "vergoedingen": "Erstattungen",
        "contact": "Kontakt",
    },
    "en": {
        "home": "Home",
        "blog": "Blog",
        "informatie": "Information",
        "vergoedingen": "Reimbursements",
        "contact": "Contact",
    },
}


def header() -> rx.Component:
    """
    Create the site-wide header with navigation and mobile menu.

    The header includes the logo, desktop navigation links, and a mobile menu
    toggle button. Navigation items are conditionally displayed based on the
    current page path to avoid showing links to the current page.

    Returns
    -------
    rx.Component
        A fragment containing the fixed header bar and mobile menu overlay.

    Notes
    -----
    The header uses Reflex state (WebsiteState) to:
    - Track the current page path for conditional nav rendering
    - Handle navigation between pages
    - Toggle the mobile menu visibility
    - Provide translated navigation labels
    """
    # Helper function to get translation based on current language
    def get_translation(key: str) -> rx.Var:
        return rx.cond(
            WebsiteState.current_language == "nl",
            TRANSLATIONS["nl"][key],
            rx.cond(
                WebsiteState.current_language == "de",
                TRANSLATIONS["de"][key],
                TRANSLATIONS["en"][key]
            )
        )

    # Helper function to check if we're on a specific page (language-aware)
    def is_not_on_page(page_suffix: str) -> rx.Var:
        """Check if current path does not match the given page."""
        if page_suffix == "":  # Home page
            # Check if we're NOT on home (path should be exactly /nl, /de, or /en)
            is_home = (
                (WebsiteState.current_page_path == "/nl") |
                (WebsiteState.current_page_path == "/de") |
                (WebsiteState.current_page_path == "/en")
            )
            return rx.cond(is_home, False, True)
        else:
            # Check if current path does NOT end with the page suffix
            return rx.cond(
                WebsiteState.current_page_path.endswith(page_suffix),
                False,
                True
            )

    nav_items = [
        rx.cond(
            is_not_on_page(""),
            rx.link(get_translation("home"), color=Colors.text["heading"], font_size=FontSizes.nav_link, font_weight="600", _hover={"color": Colors.primary["300"]}, on_click=WebsiteState.nav_to_home, cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
        rx.cond(
            is_not_on_page("/blog/"),
            rx.link(get_translation("blog"), color=Colors.text["heading"], font_size=FontSizes.nav_link, font_weight="600", _hover={"color": Colors.primary["300"]}, on_click=WebsiteState.nav_to_blog, cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
        rx.cond(
            is_not_on_page("/informatie/"),
            rx.link(get_translation("informatie"), color=Colors.text["heading"], font_size=FontSizes.nav_link, font_weight="600", _hover={"color": Colors.primary["300"]}, on_click=WebsiteState.nav_to_informatie, cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
        rx.cond(
            is_not_on_page("/reimbursements/"),
            rx.link(get_translation("vergoedingen"), color=Colors.text["heading"], font_size=FontSizes.nav_link, font_weight="600", _hover={"color": Colors.primary["300"]}, on_click=WebsiteState.nav_to_reimbursements, cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
        rx.cond(
            is_not_on_page("/contact/"),
            rx.link(get_translation("contact"), color=Colors.text["heading"], font_size=FontSizes.nav_link, font_weight="600", _hover={"color": Colors.primary["300"]}, on_click=WebsiteState.nav_to_contact, cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
    ]

    mobile_nav_items = [
        rx.cond(
            is_not_on_page(""),
            rx.link(get_translation("home"), width="100%", text_align="right", color=Colors.text["white"], py="8px", on_click=[WebsiteState.toggle_nav, WebsiteState.nav_to_home], cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
        rx.cond(
            is_not_on_page("/blog/"),
            rx.link(get_translation("blog"), width="100%", text_align="right", color=Colors.text["white"], py="8px", on_click=[WebsiteState.toggle_nav, WebsiteState.nav_to_blog], cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
        rx.cond(
            is_not_on_page("/informatie/"),
            rx.link(get_translation("informatie"), width="100%", text_align="right", color=Colors.text["white"], py="8px", on_click=[WebsiteState.toggle_nav, WebsiteState.nav_to_informatie], cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
        rx.cond(
            is_not_on_page("/reimbursements/"),
            rx.link(get_translation("vergoedingen"), width="100%", text_align="right", color=Colors.text["white"], py="8px", on_click=[WebsiteState.toggle_nav, WebsiteState.nav_to_reimbursements], cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
        rx.cond(
            is_not_on_page("/contact/"),
            rx.link(get_translation("contact"), width="100%", text_align="right", color=Colors.text["white"], py="8px", on_click=[WebsiteState.toggle_nav, WebsiteState.nav_to_contact], cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
    ]

    header_container = container(
        rx.hstack(
            rx.image(
                src="/images/shared/podotherapeut_enschede_voorvoet_praktijk_voor_podotherapie_logo.svg",
                width="300px",
                height="90px",

            ),
            rx.hstack(
                rx.hstack(*nav_items, gap="20px", display=["none", "none", "flex"]),
                language_switcher(),
                rx.box(
                    rx.icon("menu", size=28),
                    on_click=WebsiteState.toggle_nav,  # type: ignore
                    display=["inline-flex", "inline-flex", "none"],
                    color=Colors.text["heading"],
                    cursor="pointer",
                    padding="8px",
                    border_radius="4px",
                    transition="all 0.2s ease",
                    _hover={
                        "bg": Colors.primary["50"],
                        "color": Colors.primary["500"]
                    },
                ),
                align="center",
                justify="end",
                gap="12px",
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
