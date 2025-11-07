"""Order insoles section promoting extra insole purchases."""
import reflex as rx
from ...components import container, section, image_text_section
from ...theme import Colors
from ...utils.translations import get_translation


TRANSLATIONS = {
    "nl": {
        "title": "Bestel een extra paar zolen online",
        "paragraph1": "Een extra paar steunzolen kan handig zijn om bijvoorbeeld met een ander paar schoenen te gebruiken, bijvoorbeeld in sport- of wandelschoenen. Dit scheelt niet alleen gedoe met wisselen maar verlengt ook de levensduur van de podotherapeutische zolen.",
        "paragraph2": "Wij werken samen met andere medische disciplines zoals bijvoorbeeld huisartsen, medisch pedicures en fysiotherapeuten om de beste zorg te bieden aan onze patiënten. Onze praktijk is toegankelijk voor iedereen - van kinderen tot actievelingen met blessures en ouderen met voet- of voetgerelateerde klachten.",
    },
    "de": {
        "title": "Bestellen Sie online ein zusätzliches Paar Einlagen",
        "paragraph1": "Ein zusätzliches Paar Stützeinlagen kann praktisch sein, um sie beispielsweise mit einem anderen Paar Schuhen zu verwenden, etwa in Sport- oder Wanderschuhen. Dies erspart nicht nur den Aufwand des Wechselns, sondern verlängert auch die Lebensdauer der podotherapeutischen Einlagen.",
        "paragraph2": "Wir arbeiten mit anderen medizinischen Disziplinen wie Hausärzten, medizinischen Fußpflegern und Physiotherapeuten zusammen, um unseren Patienten die beste Versorgung zu bieten. Unsere Praxis ist für jeden zugänglich - von Kindern bis zu aktiven Menschen mit Verletzungen und Senioren mit Fuß- oder fußbezogenen Beschwerden.",
    },
    "en": {
        "title": "Order an extra pair of insoles online",
        "paragraph1": "An extra pair of support insoles can be handy to use with a different pair of shoes, for example in sports or hiking shoes. This not only saves the hassle of switching but also extends the lifespan of the podotherapeutic insoles.",
        "paragraph2": "We work together with other medical disciplines such as general practitioners, medical pedicurists and physiotherapists to provide the best care to our patients. Our practice is accessible to everyone - from children to active people with injuries and elderly with foot or foot-related complaints.",
    },
}


def section_order_insoles() -> rx.Component:
    """
    Create the section for ordering extra pairs of insoles.

    This section promotes the option to order additional pairs of orthopedic
    insoles online for use with different shoes. It features an image-text
    layout with outdoor shoes imagery and explains the benefits of having
    multiple pairs and the practice's collaborative approach.

    Returns
    -------
    rx.Component
        A section component with an image-text layout on a light green
        background, displaying shoe imagery on the right and promotional
        text on the left, with a call-to-action button.
    """
    paragraphs = [
        get_translation(TRANSLATIONS, "paragraph1"),
        get_translation(TRANSLATIONS, "paragraph2")
    ]

    # Create section without button to avoid reactive variable issue with if statement
    return section(
        container(
            image_text_section(
                image_src="/images/page_home/podoloog_enschede_outdoor_schoenen_voorvoet_praktijk_voor_podotherapie.jpg",
                title=get_translation(TRANSLATIONS, "title"),
                paragraphs=paragraphs,
                image_position="right"
            )
        ),
        id="order-insoles",
        background_color=Colors.backgrounds["green_light"],
        divider_color=Colors.backgrounds["white"],
        clip_top="gentle_2",
        clip_bottom="gentle_3"
    )
