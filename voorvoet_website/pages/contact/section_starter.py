"""Starter section introducing the contact page purpose."""
import reflex as rx

from ...theme import Colors
from ...components import section, container, section_title, regular_text


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
                "Contact & Afspraken",
            ),
            regular_text(
                "Heeft u vragen over podotherapie of wilt u een afspraak maken? "
                "We staan klaar om u te helpen. Neem contact op via onderstaande "
                "gegevens of plan direct een afspraak in.",
                color=Colors.text["content"],
                max_width="800px",
            ),
        ),
        background=Colors.backgrounds["white"],
        padding_y="3rem",
    )
