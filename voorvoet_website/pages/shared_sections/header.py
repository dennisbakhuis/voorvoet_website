"""Header component used across all pages."""
import reflex as rx

from ...theme import Colors, FontSizes, Layout
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


def header(language: str) -> rx.Component:
    """
    Create the site-wide header with navigation and mobile menu.

    The header includes the logo, desktop navigation links, and a mobile menu
    toggle button. Navigation items are conditionally displayed based on the
    current page path to avoid showing links to the current page.

    Parameters
    ----------
    language : str
        The current language code (nl, de, or en).

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
    """
    def get_translation(key: str, lang: str) -> rx.Var:
        """
        Get translation for a key based on provided language.

        Parameters
        ----------
        key : str
            Translation key to look up in TRANSLATIONS dict.
        lang : str
            Language code (nl, de, or en).

        Returns
        -------
        rx.Var
            Reactive variable containing the translated text for the specified language.
        """
        return rx.cond(
            lang == "nl",
            TRANSLATIONS["nl"][key],
            rx.cond(
                lang == "de",
                TRANSLATIONS["de"][key],
                TRANSLATIONS["en"][key]
            )
        )

    def is_not_on_page(page_suffix: str) -> rx.Var:
        """
        Check if current path does not match the given page.

        Parameters
        ----------
        page_suffix : str
            Page suffix to check against current path (empty string for home page).

        Returns
        -------
        rx.Var
            Reactive variable evaluating to True if not on the specified page,
            False otherwise.
        """
        if page_suffix == "":
            is_home = (
                (WebsiteState.current_page_path == "/nl") |
                (WebsiteState.current_page_path == "/de") |
                (WebsiteState.current_page_path == "/en")
            )
            return rx.cond(is_home, False, True)
        else:
            return rx.cond(
                WebsiteState.current_page_path.endswith(page_suffix),
                False,
                True
            )

    nav_items = [
        rx.cond(
            is_not_on_page(""),
            rx.link(get_translation("home", language), color=Colors.text["heading"], font_size=FontSizes.nav_link, font_weight="600", _hover={"color": Colors.primary["300"]}, on_click=WebsiteState.nav_to_home, cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
        rx.cond(
            is_not_on_page("/blog/"),
            rx.link(get_translation("blog", language), color=Colors.text["heading"], font_size=FontSizes.nav_link, font_weight="600", _hover={"color": Colors.primary["300"]}, on_click=WebsiteState.nav_to_blog, cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
        rx.cond(
            is_not_on_page("/informatie/"),
            rx.link(get_translation("informatie", language), color=Colors.text["heading"], font_size=FontSizes.nav_link, font_weight="600", _hover={"color": Colors.primary["300"]}, on_click=WebsiteState.nav_to_informatie, cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
        rx.cond(
            is_not_on_page("/vergoedingen/"),
            rx.link(get_translation("vergoedingen", language), color=Colors.text["heading"], font_size=FontSizes.nav_link, font_weight="600", _hover={"color": Colors.primary["300"]}, on_click=WebsiteState.nav_to_vergoedingen, cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
        rx.cond(
            is_not_on_page("/contact/"),
            rx.link(get_translation("contact", language), color=Colors.text["heading"], font_size=FontSizes.nav_link, font_weight="600", _hover={"color": Colors.primary["300"]}, on_click=WebsiteState.nav_to_contact, cursor="pointer"),  #type: ignore
            rx.fragment()
        ),
    ]

    mobile_nav_items = [
        rx.cond(
            is_not_on_page(""),
            rx.box(
                rx.link(
                    get_translation("home", language),
                    color=Colors.primary["700"],
                    font_size=FontSizes.nav_link,
                    font_weight="500",
                    text_decoration="none",
                ),
                width="100%",
                padding="10px 16px",
                cursor="pointer",
                transition="all 0.2s ease",
                on_click=[WebsiteState.toggle_nav, WebsiteState.nav_to_home],  #type: ignore
                _hover={
                    "& a": {
                        "color": Colors.primary["300"],
                        "text_decoration": "underline",
                    }
                },
            ),
            rx.fragment()
        ),
        rx.cond(
            is_not_on_page("/blog/"),
            rx.box(
                rx.link(
                    get_translation("blog", language),
                    color=Colors.primary["700"],
                    font_size=FontSizes.nav_link,
                    font_weight="500",
                    text_decoration="none",
                ),
                width="100%",
                padding="10px 16px",
                cursor="pointer",
                transition="all 0.2s ease",
                on_click=[WebsiteState.toggle_nav, WebsiteState.nav_to_blog],  #type: ignore
                _hover={
                    "& a": {
                        "color": Colors.primary["300"],
                        "text_decoration": "underline",
                    }
                },
            ),
            rx.fragment()
        ),
        rx.cond(
            is_not_on_page("/informatie/"),
            rx.box(
                rx.link(
                    get_translation("informatie", language),
                    color=Colors.primary["700"],
                    font_size=FontSizes.nav_link,
                    font_weight="500",
                    text_decoration="none",
                ),
                width="100%",
                padding="10px 16px",
                cursor="pointer",
                transition="all 0.2s ease",
                on_click=[WebsiteState.toggle_nav, WebsiteState.nav_to_informatie],  #type: ignore
                _hover={
                    "& a": {
                        "color": Colors.primary["300"],
                        "text_decoration": "underline",
                    }
                },
            ),
            rx.fragment()
        ),
        rx.cond(
            is_not_on_page("/vergoedingen/"),
            rx.box(
                rx.link(
                    get_translation("vergoedingen", language),
                    color=Colors.primary["700"],
                    font_size=FontSizes.nav_link,
                    font_weight="500",
                    text_decoration="none",
                ),
                width="100%",
                padding="10px 16px",
                cursor="pointer",
                transition="all 0.2s ease",
                on_click=[WebsiteState.toggle_nav, WebsiteState.nav_to_vergoedingen],  #type: ignore
                _hover={
                    "& a": {
                        "color": Colors.primary["300"],
                        "text_decoration": "underline",
                    }
                },
            ),
            rx.fragment()
        ),
        rx.cond(
            is_not_on_page("/contact/"),
            rx.box(
                rx.link(
                    get_translation("contact", language),
                    color=Colors.primary["700"],
                    font_size=FontSizes.nav_link,
                    font_weight="500",
                    text_decoration="none",
                ),
                width="100%",
                padding="10px 16px",
                cursor="pointer",
                transition="all 0.2s ease",
                on_click=[WebsiteState.toggle_nav, WebsiteState.nav_to_contact],  #type: ignore
                _hover={
                    "& a": {
                        "color": Colors.primary["300"],
                        "text_decoration": "underline",
                    }
                },
            ),
            rx.fragment()
        ),
    ]

    header_container = container(
        rx.hstack(
            rx.image(
                src="/images/shared/podotherapeut_enschede_voorvoet_praktijk_voor_podotherapie_logo.svg",
                width=["66%", "66%", "clamp(200px, calc(200px + (100vw - 768px) * 1.22), 300px)", "300px"],
                max_width="300px",
                height="auto",
            ),
            rx.hstack(
                rx.hstack(*nav_items, gap="12px", display=["none", "none", "flex", "flex"]),
                rx.box(
                    language_switcher(language),
                    display=["none", "flex", "flex", "flex"],
                    overflow=["hidden", "visible", "visible", "visible"],
                ),
                rx.box(
                    rx.cond(
                        WebsiteState.nav_open,
                        rx.icon("x", size=28),
                        rx.icon("menu", size=28),
                    ),
                    on_click=WebsiteState.toggle_nav,  # type: ignore
                    display=Layout.mobile_only_inline_flex,
                    color=Colors.primary["700"],
                    cursor="pointer",
                    padding="8px",
                    border_radius="4px",
                    transition="color 0.2s ease",
                    _hover={
                        "color": Colors.primary["300"]
                    },
                ),
                align="center",
                justify="end",
                gap="12px",
            ),
            align="center",
            justify="between",
            width="100%",
        ),
        padding_x=["1rem", "1.5rem", "clamp(0.5rem, calc(0.5rem + (100vw - 768px) * 0.018), 2rem)", "2rem"],
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

    overlay = rx.cond(
        WebsiteState.nav_open,
        rx.box(
            position="fixed",
            top="0",
            left="0",
            right="0",
            bottom="0",
            z_index="20",
            on_click=WebsiteState.toggle_nav,  # type: ignore
        ),
        rx.fragment(),
    )

    mobile_menu = rx.cond(
        WebsiteState.nav_open,
        rx.box(
            rx.vstack(
                *mobile_nav_items,
                rx.box(
                    language_switcher(language, mobile=True),
                    width="100%",
                    display=["flex", "none", "none", "none"],
                    justify_content="flex-end",
                    padding_top="4px",
                ),
                spacing="0",
                width="100%",
            ),
            position="fixed",
            top="68px",
            right="16px",
            margin_top="8px",
            border=f"1px solid {Colors.primary['50']}",
            border_radius="8px",
            box_shadow="0 4px 12px rgba(0, 0, 0, 0.1)",
            padding="8px",
            min_width="200px",
            max_width="90%",
            z_index="21",
            style={
                "background": "rgba(255, 255, 255, 0.85)",
                "backdropFilter": "saturate(180%) blur(10px)",
                "webkitBackdropFilter": "saturate(180%) blur(10px)",
            },
        ),
        rx.box(),
    )

    return rx.fragment(overlay, bar, mobile_menu)
