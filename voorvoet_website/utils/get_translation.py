"""Translation utilities for multilingual support."""


def get_translation(
    translations: dict[str, dict[str, str]], key: str, language="nl"
) -> str:
    """
    Get translated text based on specified language.

    Parameters
    ----------
    translations : dict
        Translation dictionary with structure {"nl": {"key": "text"}, "de": {"key": "text"}, ...}
    key : str
        The translation key to look up
    language : str, optional
        Language code (e.g., "nl", "de", "en"). Defaults to "nl"

    Returns
    -------
    str
        Translated text for the specified language, or "<language_or_does_not_exist>" if not found
    """
    return translations.get(language, {}).get(key, "<language_or_does_not_exist>")
