"""Translation utilities for multilingual support."""
import reflex as rx
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..states import WebsiteState


def get_current_language() -> str:
    """
    Get the current language from WebsiteState.

    This function is used by the blog service to determine which language
    files to load. It uses a deferred import to avoid circular dependencies.

    Returns
    -------
    str
        The current language code ("nl", "de", or "en"), defaults to "nl"
    """
    from ..states import WebsiteState

    try:
        state = rx.State()  # type: ignore
        if hasattr(state, 'current_language'):
            return state.current_language  # type: ignore
    except Exception:
        pass

    return "nl"


def get_translation(translations: dict, key: str) -> rx.Var:
    """
    Get translated text based on current language.

    This helper function uses Reflex's rx.cond to conditionally return
    the appropriate translation based on the current language state.

    Parameters
    ----------
    translations : dict
        Translation dictionary with language codes as keys ("nl", "de", "en")
        and translation strings as values for the specified key.
        Example structure: {"nl": {"key": "text"}, "de": {"key": "text"}, "en": {"key": "text"}}
    key : str
        The translation key to look up in each language dictionary.

    Returns
    -------
    rx.Var
        A reactive variable that evaluates to the correct translation
        based on WebsiteState.current_language.

    Examples
    --------
    >>> TRANSLATIONS = {
    ...     "nl": {"greeting": "Hallo"},
    ...     "de": {"greeting": "Hallo"},
    ...     "en": {"greeting": "Hello"}
    ... }
    >>> get_translation(TRANSLATIONS, "greeting")
    """
    from ..states import WebsiteState

    return rx.cond(
        WebsiteState.current_language == "nl",
        translations["nl"][key],
        rx.cond(
            WebsiteState.current_language == "de",
            translations["de"][key],
            translations["en"][key]
        )
    )
