"""Translation utilities for multilingual support."""
import reflex as rx
from ..states import WebsiteState


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
    return rx.cond(
        WebsiteState.current_language == "nl",
        translations["nl"][key],
        rx.cond(
            WebsiteState.current_language == "de",
            translations["de"][key],
            translations["en"][key]
        )
    )
