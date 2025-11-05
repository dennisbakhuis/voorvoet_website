"""Introductory text section for the blog page."""
import reflex as rx

from ...theme import Colors
from ...components import section, container, section_title, regular_text


def section_starter() -> rx.Component:
    """
    Create the introductory section for the blog page.

    Displays a welcoming title and introductory text explaining the purpose
    of the blog and what type of content visitors can expect to find.

    Returns
    -------
    rx.Component
        A section component with white background containing the title
        and introductory text about foot health and podiatry topics.
    """
    return section(
        container(
            section_title(
                "Stap voor stap naar gezonde voeten: alles over podotherapie",
                margin_bottom=10,
            ),
            regular_text(
                "Op deze pagina kun je allerlei interessante stukken vinden over voetgezondheid en podotherapie, samen met andere verwante onderwerpen. Hier delen we handige tips en nuttige inzichten om je voeten gelukkig en gezond te houden. Of het nu gaat om het vinden van de juiste schoenen, het begrijpen van podotherapie, of gewoon het leren waarderen van je voeten, we hebben allerlei leuke en informatieve artikelen om je te helpen. Neem gerust een kijkje en ontdek hoe je je voeten het beste kunt verzorgen!",
                color=Colors.text["content"],
            ),
        ),
        background=Colors.backgrounds["white"],
        padding=0,
        padding_top=10,
    )
