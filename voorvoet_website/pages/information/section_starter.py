"""Introductory text section for the information page."""
import reflex as rx

from ...theme import Colors
from ...components import section, container, section_title, regular_text


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
                "Alles over podotherapie",
            ),
            regular_text("""\
Op deze pagina vind je uitgebreide informatie over podotherapie en bij welke klachten je bij ons terecht kunt - van voet- en enkelproblemen tot knie-, heup- en rugklachten die hun oorsprong vinden in de voeten. Ook lees je hoe een behandeltraject eruitziet, van eerste consult tot behandeling en nazorg.
Als erkende podotherapeuten nemen we de tijd voor grondige analyse en stellen we een behandelplan op maat op dat aansluit bij jouw specifieke situatie.
""",
                color=Colors.text["content"],
                max_width="1200px",
            ),
        ),
        background=Colors.backgrounds["white"],
        padding_bottom="0",
    )
