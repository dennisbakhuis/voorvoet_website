"""Introductory text section for the information page."""
import reflex as rx

from ...theme import Colors
from ...components import section, container, section_title, regular_text
from ...utils.translations import get_translation


TRANSLATIONS = {
    "nl": {
        "title": "Alles over podotherapie",
        "intro": "Op deze pagina vind je uitgebreide informatie over podotherapie en bij welke klachten je bij ons terecht kunt - van voet- en enkelproblemen tot knie-, heup- en rugklachten die hun oorsprong vinden in de voeten. Ook lees je hoe een behandeltraject eruitziet, van eerste consult tot behandeling en nazorg.\nAls erkende podotherapeuten nemen we de tijd voor grondige analyse en stellen we een behandelplan op maat op dat aansluit bij jouw specifieke situatie.",
    },
    "de": {
        "title": "Alles über Podotherapie",
        "intro": "Auf dieser Seite finden Sie umfassende Informationen über Podotherapie und bei welchen Beschwerden Sie zu uns kommen können - von Fuß- und Knöchelproblemen bis hin zu Knie-, Hüft- und Rückenbeschwerden, die ihren Ursprung in den Füßen haben. Sie erfahren auch, wie ein Behandlungsverlauf aussieht, vom Erstgespräch über die Behandlung bis zur Nachsorge.\nAls anerkannte Podotherapeuten nehmen wir uns Zeit für eine gründliche Analyse und erstellen einen maßgeschneiderten Behandlungsplan, der auf Ihre spezifische Situation zugeschnitten ist.",
    },
    "en": {
        "title": "Everything about podotherapy",
        "intro": "On this page you will find extensive information about podotherapy and which complaints you can come to us with - from foot and ankle problems to knee, hip and back complaints that originate in the feet. You will also read about what a treatment process looks like, from the first consultation to treatment and aftercare.\nAs certified podotherapists, we take the time for thorough analysis and create a customized treatment plan that fits your specific situation.",
    },
}


def section_starter() -> rx.Component:
    """
    Create the introductory section for the information page.

    Displays a welcoming title and introductory text explaining what information
    visitors can find on this page, including details about podiatry services,
    common complaints, and treatment processes.

    Returns
    -------
    rx.Component
        A section component with white background containing the title
        and introductory text about the information page content.
    """
    return section(
        container(
            section_title(
                get_translation(TRANSLATIONS, "title"),
            ),
            regular_text(
                get_translation(TRANSLATIONS, "intro"),
                color=Colors.text["content"],
                max_width="1200px",
            ),
        ),
        background=Colors.backgrounds["white"],
        padding_bottom="0",
    )
