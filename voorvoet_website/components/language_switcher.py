"""Language switcher component with flag icons and popup selector."""
import reflex as rx
from ..theme import Colors
from ..states import WebsiteState


def get_language_url(target_lang: str):
    """
    Build URL for switching to a different language.

    Parameters
    ----------
    target_lang : str
        Target language code ("nl", "de", or "en")

    Returns
    -------
    Var
        URL with the language prefix replaced (as a reactive Var)
    """
    current_path = rx.State.router.page.path

    # Extract base path (remove language prefix) using rx.cond
    base_path = rx.cond(
        current_path.startswith("/nl"),
        rx.cond(current_path.length() > 3, current_path[3:], "/"),
        rx.cond(
            current_path.startswith("/de"),
            rx.cond(current_path.length() > 3, current_path[3:], "/"),
            rx.cond(
                current_path.startswith("/en"),
                rx.cond(current_path.length() > 3, current_path[3:], "/"),
                current_path
            )
        )
    )

    # Build new URL with target language
    return rx.cond(
        base_path == "/",
        f"/{target_lang}",
        f"/{target_lang}" + base_path
    )


def language_option(flag_emoji: str, language_name: str, language_code: str, toggle_handler) -> rx.Component:
    """
    Create a single language option in the selector.

    Parameters
    ----------
    flag_emoji : str
        Flag emoji for the language (e.g., "🇳🇱", "🇩🇪", "🇬🇧")
    language_name : str
        Full name of the language (e.g., "Nederlands", "Deutsch", "English")
    language_code : str
        ISO language code (e.g., "nl", "de", "en")
    toggle_handler : callable
        Function to close the language selector menu

    Returns
    -------
    rx.Component
        A clickable language option with flag and name
    """
    return rx.link(
        rx.hstack(
            rx.text(
                flag_emoji,
                font_size="1.5rem",
                transition="transform 0.2s ease",
                class_name="flag-emoji",
            ),
            rx.text(
                language_name,
                font_size="0.95rem",
                font_weight="500",
                color=Colors.primary["700"],
                text_decoration="none",
                class_name="language-name",
            ),
            spacing="3",
            align="center",
        ),
        href=get_language_url(language_code),
        padding="10px 16px",
        cursor="pointer",
        transition="all 0.2s ease",
        on_click=toggle_handler,  # type: ignore
        _hover={
            "& .flag-emoji": {
                "transform": "scale(1.2)",
            },
            "& .language-name": {
                "color": Colors.primary["300"],
                "text_decoration": "underline",
            }
        },
        width="100%",
        text_decoration="none",
    )


def language_switcher(language: str, mobile: bool = False) -> rx.Component:
    """
    Create the language switcher component with popup selector.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")
    mobile : bool
        Whether this is the mobile version (in hamburger menu) or header version

    Returns
    -------
    rx.Component
        A language switcher button with popup menu overlay
    """
    language_info = {
        "nl": {"flag": "🇳🇱", "name": "Nederlands"},
        "de": {"flag": "🇩🇪", "name": "Deutsch"},
        "en": {"flag": "🇬🇧", "name": "English"},
    }

    current_flag = language_info.get(language, language_info["nl"])["flag"]

    selector_open_state = WebsiteState.language_selector_mobile_open if mobile else WebsiteState.language_selector_open
    toggle_handler = WebsiteState.toggle_language_selector_mobile if mobile else WebsiteState.toggle_language_selector

    trigger_button = rx.box(
        rx.box(
            rx.text(
                current_flag,
                font_size="1.5rem",
                transition="transform 0.2s ease",
                class_name="flag-text",
            ),
            rx.icon(
                "chevron-down",
                size=12,
                color=Colors.text["heading"],
                transition="transform 0.2s ease",
                position="absolute",
                bottom="-2px",
                left="50%",
                style={
                    "transform": rx.cond(
                        selector_open_state,
                        "translateX(-50%) rotate(180deg)",
                        "translateX(-50%) rotate(0deg)"
                    )
                },
            ),
            position="relative",
            display="inline-flex",
            align_items="center",
            justify_content="center",
        ),
        padding="8px 12px",
        border_radius="6px",
        cursor="pointer",
        _hover={
            "& .flag-text": {
                "transform": "scale(1.1)",
            }
        },
        on_click=toggle_handler,  # type: ignore
    )

    popup_menu = rx.cond(
        selector_open_state,
        rx.box(
            rx.vstack(
                language_option(
                    flag_emoji=language_info["nl"]["flag"],
                    language_name=language_info["nl"]["name"],
                    language_code="nl",
                    toggle_handler=toggle_handler
                ),
                language_option(
                    flag_emoji=language_info["de"]["flag"],
                    language_name=language_info["de"]["name"],
                    language_code="de",
                    toggle_handler=toggle_handler
                ),
                language_option(
                    flag_emoji=language_info["en"]["flag"],
                    language_name=language_info["en"]["name"],
                    language_code="en",
                    toggle_handler=toggle_handler
                ),
                spacing="0",
                width="100%",
            ),
            position="absolute",
            top="100%",
            right="0",
            margin_top="8px",
            border=f"1px solid {Colors.primary['50']}",
            border_radius="8px",
            box_shadow="0 4px 12px rgba(0, 0, 0, 0.1)",
            padding="8px",
            min_width="180px",
            z_index="1",
            style={
                "background": "rgba(255, 255, 255, 0.95)",
                "backdropFilter": "saturate(180%) blur(10px)",
                "webkitBackdropFilter": "saturate(180%) blur(10px)",
            },
        ),
        rx.fragment(),
    )

    return rx.box(
        trigger_button,
        popup_menu,
        position="relative",
    )
