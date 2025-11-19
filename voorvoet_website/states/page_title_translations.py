"""Translation strings for multi-language support.

This module contains all translatable strings used throughout the application,
organized by category. Each translation is a dictionary with language codes
(nl, de, en) as keys.
"""

PAGE_TITLES = {
    "home": {
        "nl": "VoorVoet - Praktijk voor Podotherapie",
        "de": "VoorVoet - Praxis für Podologie",
        "en": "VoorVoet - Podiatry Practice"
    },
    "blog": {
        "nl": "VoorVoet - Blog",
        "de": "VoorVoet - Blog",
        "en": "VoorVoet - Blog"
    },
    "information": {
        "nl": "VoorVoet - Informatie",
        "de": "VoorVoet - Informationen",
        "en": "VoorVoet - Information"
    },
    "reimbursements": {
        "nl": "VoorVoet - Vergoedingen",
        "de": "VoorVoet - Erstattungen",
        "en": "VoorVoet - Reimbursements"
    },
    "contact": {
        "nl": "VoorVoet - Contact",
        "de": "VoorVoet - Kontakt",
        "en": "VoorVoet - Contact"
    }
}


def get_page_title(page_key: str, language: str = "nl") -> str:
    """
    Get the page title for a specific page and language.

    Parameters
    ----------
    page_key : str
        The key identifying the page (e.g., "home", "blog", "contact")
    language : str, optional
        The language code ("nl", "de", "en"), defaults to "nl"

    Returns
    -------
    str
        The page title in the requested language, or Dutch if language not found
    """
    return PAGE_TITLES.get(page_key, {}).get(language, PAGE_TITLES.get(page_key, {}).get("nl", "VoorVoet"))
