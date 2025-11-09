"""Starter section introducing the contact page purpose."""
import reflex as rx

from ...theme import Colors
from ...components import section, container, section_title, regular_text
from ...utils.translations import get_translation


TRANSLATIONS = {
    "nl": {
        "title": "Contact",
        "description": "Heb je een vraag stel hem dan via onderstaand formulier. Je kunt antwoord krijgen via email of  een terugbelverzoek sturen.",
    },
    "de": {
        "title": "Kontakt",
        "description": "Haben Sie eine Frage, stellen Sie sie über das untenstehende Formular. Sie können eine Antwort per E-Mail erhalten oder einen Rückrufwunsch senden.",
    },
    "en": {
        "title": "Contact",
        "description": "If you have a question, please ask it using the form below. You can receive an answer via email or send a callback request.",
    },
}


def section_starter() -> rx.Component:
    """
    Create the contact page starter section with introductory text.

    This section provides a brief introduction to the contact page,
    explaining that visitors can ask questions about podotherapy or
    schedule an appointment through the contact form or provided
    contact details.

    Returns
    -------
    rx.Component
        A section component with centered title and descriptive text
        on a white background with vertical padding.
    """
    return section(
        container(
            section_title(
                get_translation(TRANSLATIONS, "title"),
            ),
            regular_text(
                get_translation(TRANSLATIONS, "description"),
                color=Colors.text["content"],
            ),
        ),
        background=Colors.backgrounds["white"],
        padding_y="3rem",
    )
