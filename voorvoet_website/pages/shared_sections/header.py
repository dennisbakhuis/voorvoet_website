"""Header component used across all pages."""

import reflex as rx

from ...theme import Colors, FontSizes, Layout
from ...states import WebsiteState
from ...components import container, language_switcher
from ...translations import ROUTE_MAPPINGS
from ...utils import get_translation


TRANSLATIONS = {
    "nl": {
        "home": "Home",
        "blog": "Blog",
        "informatie": "Informatie",
        "vergoedingen": "Vergoedingen",
        "contact": "Contact",
        "logo_alt": "VoorVoet Praktijk voor Podotherapie logo",
        "skip_to_content": "Spring naar hoofdinhoud",
    },
    "de": {
        "home": "Home",
        "blog": "Blog",
        "informatie": "Informationen",
        "vergoedingen": "Erstattungen",
        "contact": "Kontakt",
        "logo_alt": "VoorVoet Praktijk voor Podotherapie Logo",
        "skip_to_content": "Zum Hauptinhalt springen",
    },
    "en": {
        "home": "Home",
        "blog": "Blog",
        "informatie": "Information",
        "vergoedingen": "Reimbursements",
        "contact": "Contact",
        "logo_alt": "VoorVoet Praktijk voor Podotherapie logo",
        "skip_to_content": "Skip to main content",
    },
}


def header(language: str, page_key: str | None = None) -> rx.Component:
    """
    Create the site-wide header with navigation and mobile menu.

    Parameters
    ----------
    language : str
        The current language code (nl, de, or en).
    page_key : str, optional
        The current page identifier ('home', 'blog', 'informatie', 'vergoedingen', 'contact').
        When provided, the navigation link for that page will be hidden.

    Returns
    -------
    rx.Component
        A fragment containing the fixed header bar and mobile menu overlay.
    """

    nav_items = [
        rx.cond(
            page_key != "home",
            rx.link(
                get_translation(TRANSLATIONS, "home", language),
                href=ROUTE_MAPPINGS[language]["home"],
                color=Colors.text["heading"],
                font_size=FontSizes.nav_link,
                font_weight="600",
                _hover={"color": Colors.primary["300"]},
            ),
            rx.fragment(),
        ),
        rx.cond(
            page_key != "blog",
            rx.link(
                get_translation(TRANSLATIONS, "blog", language),
                href=ROUTE_MAPPINGS[language]["blog"],
                color=Colors.text["heading"],
                font_size=FontSizes.nav_link,
                font_weight="600",
                _hover={"color": Colors.primary["300"]},
            ),
            rx.fragment(),
        ),
        rx.cond(
            page_key != "information",
            rx.link(
                get_translation(TRANSLATIONS, "informatie", language),
                href=ROUTE_MAPPINGS[language]["information"],
                color=Colors.text["heading"],
                font_size=FontSizes.nav_link,
                font_weight="600",
                _hover={"color": Colors.primary["300"]},
            ),
            rx.fragment(),
        ),
        rx.cond(
            page_key != "reimbursements",
            rx.link(
                get_translation(TRANSLATIONS, "vergoedingen", language),
                href=ROUTE_MAPPINGS[language]["reimbursements"],
                color=Colors.text["heading"],
                font_size=FontSizes.nav_link,
                font_weight="600",
                _hover={"color": Colors.primary["300"]},
            ),
            rx.fragment(),
        ),
        rx.cond(
            page_key != "contact",
            rx.link(
                get_translation(TRANSLATIONS, "contact", language),
                href=ROUTE_MAPPINGS[language]["contact"],
                color=Colors.text["heading"],
                font_size=FontSizes.nav_link,
                font_weight="600",
                _hover={"color": Colors.primary["300"]},
            ),
            rx.fragment(),
        ),
    ]

    mobile_nav_items = [
        rx.cond(
            page_key != "home",
            rx.link(
                get_translation(TRANSLATIONS, "home", language),
                href=ROUTE_MAPPINGS[language]["home"],
                color=Colors.primary["700"],
                font_size=FontSizes.nav_link,
                font_weight="500",
                text_decoration="none",
                width="100%",
                padding="10px 16px",
                cursor="pointer",
                transition="all 0.2s ease",
                on_click=WebsiteState.toggle_nav,
                _hover={
                    "color": Colors.primary["300"],
                    "text_decoration": "underline",
                },
            ),
            rx.fragment(),
        ),
        rx.cond(
            page_key != "blog",
            rx.link(
                get_translation(TRANSLATIONS, "blog", language),
                href=ROUTE_MAPPINGS[language]["blog"],
                color=Colors.primary["700"],
                font_size=FontSizes.nav_link,
                font_weight="500",
                text_decoration="none",
                width="100%",
                padding="10px 16px",
                cursor="pointer",
                transition="all 0.2s ease",
                on_click=WebsiteState.toggle_nav,
                _hover={
                    "color": Colors.primary["300"],
                    "text_decoration": "underline",
                },
            ),
            rx.fragment(),
        ),
        rx.cond(
            page_key != "information",
            rx.link(
                get_translation(TRANSLATIONS, "informatie", language),
                href=ROUTE_MAPPINGS[language]["information"],
                color=Colors.primary["700"],
                font_size=FontSizes.nav_link,
                font_weight="500",
                text_decoration="none",
                width="100%",
                padding="10px 16px",
                cursor="pointer",
                transition="all 0.2s ease",
                on_click=WebsiteState.toggle_nav,
                _hover={
                    "color": Colors.primary["300"],
                    "text_decoration": "underline",
                },
            ),
            rx.fragment(),
        ),
        rx.cond(
            page_key != "reimbursements",
            rx.link(
                get_translation(TRANSLATIONS, "vergoedingen", language),
                href=ROUTE_MAPPINGS[language]["reimbursements"],
                color=Colors.primary["700"],
                font_size=FontSizes.nav_link,
                font_weight="500",
                text_decoration="none",
                width="100%",
                padding="10px 16px",
                cursor="pointer",
                transition="all 0.2s ease",
                on_click=WebsiteState.toggle_nav,
                _hover={
                    "color": Colors.primary["300"],
                    "text_decoration": "underline",
                },
            ),
            rx.fragment(),
        ),
        rx.cond(
            page_key != "contact",
            rx.link(
                get_translation(TRANSLATIONS, "contact", language),
                href=ROUTE_MAPPINGS[language]["contact"],
                color=Colors.primary["700"],
                font_size=FontSizes.nav_link,
                font_weight="500",
                text_decoration="none",
                width="100%",
                padding="10px 16px",
                cursor="pointer",
                transition="all 0.2s ease",
                on_click=WebsiteState.toggle_nav,
                _hover={
                    "color": Colors.primary["300"],
                    "text_decoration": "underline",
                },
            ),
            rx.fragment(),
        ),
    ]

    header_container = container(
        rx.hstack(
            rx.image(
                src="/images/shared/podotherapeut_enschede_voorvoet_praktijk_voor_podotherapie_logo.svg",
                alt=get_translation(TRANSLATIONS, "logo_alt", language),
                width=[
                    "66%",
                    "66%",
                    "clamp(200px, calc(200px + (100vw - 768px) * 1.22), 300px)",
                    "300px",
                ],
                max_width="300px",
                height="auto",
            ),
            rx.hstack(
                rx.hstack(
                    *nav_items,
                    role="navigation",
                    aria_label="Main",
                    gap="12px",
                    display=["none", "none", "flex", "flex"],
                ),
                rx.box(
                    language_switcher(language, page_key or "home"),
                    display=["none", "flex", "flex", "flex"],
                    overflow=["hidden", "visible", "visible", "visible"],
                ),
                rx.box(
                    rx.cond(
                        WebsiteState.nav_open,
                        rx.icon("x", size=28),  # type: ignore[operator]
                        rx.icon("menu", size=28),  # type: ignore[operator]
                    ),
                    on_click=WebsiteState.toggle_nav,
                    display=Layout.mobile_only_inline_flex,
                    color=Colors.primary["700"],
                    cursor="pointer",
                    padding="8px",
                    border_radius="4px",
                    transition="color 0.2s ease",
                    _hover={"color": Colors.primary["300"]},
                ),
                align="center",
                justify="end",
                gap="12px",
            ),
            align="center",
            justify="between",
            width="100%",
        ),
        padding_x=[
            "1rem",
            "1.5rem",
            "clamp(0.5rem, calc(0.5rem + (100vw - 768px) * 0.018), 2rem)",
            "2rem",
        ],
    )

    bar = rx.box(
        header_container,
        role="banner",
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
            on_click=WebsiteState.toggle_nav,
        ),
        rx.fragment(),
    )

    mobile_menu = rx.cond(
        WebsiteState.nav_open,
        rx.box(
            rx.vstack(
                *mobile_nav_items,
                rx.box(
                    language_switcher(language, page_key or "home", mobile=True),
                    width="100%",
                    display=["flex", "none", "none", "none"],
                    justify_content="flex-end",
                    padding_top="4px",
                ),
                role="navigation",
                aria_label="Mobile menu",
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

    skip_link = rx.link(
        get_translation(TRANSLATIONS, "skip_to_content", language),
        href="#main-content",
        position="fixed",
        top="0",
        left="0",
        z_index="30",
        padding="0.75rem 1rem",
        background_color=Colors.primary["700"],
        color="white",
        font_weight="600",
        border_radius="0 0 4px 0",
        text_decoration="none",
        transform="translateY(-100%)",
        _focus={
            "transform": "translateY(0)",
            "outline": f"2px solid {Colors.primary['300']}",
            "outline_offset": "2px",
        },
        transition="transform 0.2s ease-in-out",
    )

    return rx.fragment(skip_link, overlay, bar, mobile_menu)
