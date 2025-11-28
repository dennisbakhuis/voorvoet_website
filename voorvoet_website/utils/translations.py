"""Translation utilities for multilingual support."""
import reflex as rx
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..states import WebsiteState


def get_language_from_path():
    """
    Extract language code from the current URL path.

    This function returns WebsiteState.current_language which is a reactive
    state variable that resolves to the language code from the URL path at runtime.

    Returns
    -------
    Var
        A reactive variable that evaluates to the language code ("nl", "de", or "en")
    """
    from ..states import WebsiteState

    return WebsiteState.current_language


def get_current_language() -> str:
    """
    Get the current language from WebsiteState.

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


def get_translation(translations: dict, key: str, language=None) -> rx.Var | str:
    """
    Get translated text based on specified or current language.

    Parameters
    ----------
    translations : dict
        Translation dictionary with structure {"nl": {"key": "text"}, ...}
    key : str
        The translation key to look up
    language : str | Var | None, optional
        If provided as a string, returns translation for that language as a string.
        If provided as a Var, returns a reactive variable that resolves based on that Var.
        If None, returns a reactive variable based on WebsiteState.current_language

    Returns
    -------
    rx.Var | str
        String if language is a string, reactive Var otherwise
    """
    if isinstance(language, str):
        return translations.get(language, translations["nl"])[key]

    from ..states import WebsiteState

    lang_var = language if language is not None else WebsiteState.current_language

    return rx.cond(
        lang_var == "nl",
        translations["nl"][key],
        rx.cond(
            lang_var == "de",
            translations["de"][key],
            translations["en"][key]
        )
    )
