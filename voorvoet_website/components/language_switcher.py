"""Language switcher component with flag icons and popup selector."""
import reflex as rx
from ..theme import Colors
from ..states import WebsiteState


def language_option(flag_emoji: str, language_name: str, language_code: str) -> rx.Component:
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

    Returns
    -------
    rx.Component
        A clickable language option with flag and name
    """
    return rx.box(
        rx.hstack(
            rx.text(
                flag_emoji,
                font_size="1.5rem",
            ),
            rx.text(
                language_name,
                font_size="0.95rem",
                font_weight="500",
                color=Colors.text["heading"],
            ),
            spacing="3",
            align="center",
        ),
        padding="10px 16px",
        cursor="pointer",
        border_radius="6px",
        transition="all 0.2s ease",
        _hover={
            "bg": Colors.primary["50"],
        },
        on_click=lambda: WebsiteState.set_language(language_code),  # type: ignore
        width="100%",
    )


def language_switcher() -> rx.Component:
    """
    Create the language switcher component with popup selector.

    Displays the current language flag and opens a popup menu when clicked.
    The popup shows all available languages with their flags and names.

    Returns
    -------
    rx.Component
        A language switcher button with popup menu overlay
    """
    # Map language codes to flag emojis and names
    language_info = {
        "nl": {"flag": "🇳🇱", "name": "Nederlands"},
        "de": {"flag": "🇩🇪", "name": "Deutsch"},
        "en": {"flag": "🇬🇧", "name": "English"},
    }

    # Current language display button
    current_flag = rx.cond(
        WebsiteState.current_language == "nl",
        "🇳🇱",
        rx.cond(
            WebsiteState.current_language == "de",
            "🇩🇪",
            "🇬🇧"
        )
    )

    trigger_button = rx.box(
        rx.hstack(
            rx.text(
                current_flag,
                font_size="1.5rem",
                transition="transform 0.2s ease",
            ),
            rx.icon(
                "chevron-down",
                size=16,
                color=Colors.text["heading"],
            ),
            spacing="2",
            align="center",
        ),
        padding="8px 12px",
        border_radius="6px",
        cursor="pointer",
        _hover={
            "& *": {
                "transform": "scale(1.1)",
            }
        },
        on_click=WebsiteState.toggle_language_selector,  # type: ignore
    )

    # Popup menu with all language options
    popup_menu = rx.cond(
        WebsiteState.language_selector_open,
        rx.box(
            rx.vstack(
                language_option(
                    flag_emoji=language_info["nl"]["flag"],
                    language_name=language_info["nl"]["name"],
                    language_code="nl"
                ),
                language_option(
                    flag_emoji=language_info["de"]["flag"],
                    language_name=language_info["de"]["name"],
                    language_code="de"
                ),
                language_option(
                    flag_emoji=language_info["en"]["flag"],
                    language_name=language_info["en"]["name"],
                    language_code="en"
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
            z_index="30",
            style={
                "background": "rgba(255, 255, 255, 0.50)",
                "backdropFilter": "saturate(180%) blur(6px)",
                "webkitBackdropFilter": "saturate(180%) blur(6px)",
            },
        ),
        rx.fragment(),
    )

    # Overlay to close popup when clicking outside
    overlay = rx.cond(
        WebsiteState.language_selector_open,
        rx.box(
            position="fixed",
            top="0",
            left="0",
            right="0",
            bottom="0",
            z_index="29",
            on_click=WebsiteState.toggle_language_selector,  # type: ignore
        ),
        rx.fragment(),
    )

    return rx.fragment(
        overlay,
        rx.box(
            trigger_button,
            popup_menu,
            position="relative",
        ),
    )
