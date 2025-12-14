"""Introductory text section for the blog page."""

import reflex as rx

from ...theme import Colors
from ...components import section, container, header, regular_text
from ...utils.get_translation import get_translation


TRANSLATIONS = {
    "nl": {
        "title": "Stap voor stap naar gezonde voeten: alles over podotherapie",
        "intro_text": "Op deze pagina kun je allerlei interessante stukken vinden over voetgezondheid en podotherapie, samen met andere verwante onderwerpen. Hier delen we handige tips en nuttige inzichten om je voeten gelukkig en gezond te houden. Of het nu gaat om het vinden van de juiste schoenen, het begrijpen van podotherapie, of gewoon het leren waarderen van je voeten, we hebben allerlei leuke en informatieve artikelen om je te helpen. Neem gerust een kijkje en ontdek hoe je je voeten het beste kunt verzorgen!",
    },
    "de": {
        "title": "Schritt für Schritt zu gesunden Füßen: alles über Podotherapie",
        "intro_text": "Auf dieser Seite finden Sie verschiedene interessante Artikel über Fußgesundheit und Podotherapie sowie andere verwandte Themen. Hier teilen wir praktische Tipps und nützliche Einblicke, um Ihre Füße glücklich und gesund zu halten. Ob es darum geht, die richtigen Schuhe zu finden, Podotherapie zu verstehen oder einfach Ihre Füße zu schätzen zu lernen, wir haben verschiedene interessante und informative Artikel, die Ihnen helfen. Schauen Sie sich gerne um und entdecken Sie, wie Sie Ihre Füße am besten pflegen können!",
    },
    "en": {
        "title": "Step by step to healthy feet: all about podiatry",
        "intro_text": "On this page you can find various interesting articles about foot health and podiatry, along with other related topics. Here we share practical tips and useful insights to keep your feet happy and healthy. Whether it's finding the right shoes, understanding podiatry, or simply learning to appreciate your feet, we have various interesting and informative articles to help you. Feel free to take a look and discover how to best care for your feet!",
    },
}


def section_starter(language: str) -> rx.Component:
    """
    Create the introductory section for the blog page.

    Displays a welcoming title and introductory text explaining the purpose
    of the blog and what type of content visitors can expect to find.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")

    Returns
    -------
    rx.Component
        A section component with white background containing the title
        and introductory text about foot health and podiatry topics.
    """
    return section(
        container(
            header(
                get_translation(TRANSLATIONS, "title", language),
                level=1,
                margin_bottom=10,
            ),
            regular_text(
                get_translation(TRANSLATIONS, "intro_text", language),
                color=Colors.text["content"],
            ),
        ),
        background=Colors.backgrounds["white"],
        padding=0,
        padding_top=10,
    )
