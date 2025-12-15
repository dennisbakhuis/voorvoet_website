"""Who is VoorVoet section introducing the practice."""

import reflex as rx
from ...components import container, section, image_text_section
from ...utils import get_translation


TRANSLATIONS = {
    "nl": {
        "title": "Podotherapeut Enschede",
        "paragraph1": "Wij zijn een kleinschalige praktijk in de buurt van de Zuiderval. Wij geloven sterk in de kracht van een persoonlijke benadering voor een succesvolle behandeling. Onze praktijk is uitgerust met de nieuwste technologieën en methoden, waardoor wij in staat zijn om een goede en specifieke diagnose te stellen en een behandelplan op maat aan te bieden, zodat jij weer goed vooruit kunt!",
        "paragraph2": "Wij werken samen met andere medische disciplines zoals bijvoorbeeld huisartsen, medisch pedicures en fysiotherapeuten om de beste zorg te bieden aan onze patiënten. Onze praktijk is toegankelijk voor iedereen - van kinderen tot actievelingen met blessures en ouderen met voet- of voetgerelateerde klachten.",
        "image_alt": "Kim Bakhuis, podotherapeut van VoorVoet Praktijk voor Podotherapie in Enschede",
    },
    "de": {
        "title": "Podotherapeut Enschede",
        "paragraph1": "Wir sind eine kleinformatige Praxis in der Nähe des Zuiderval. Wir glauben fest an die Kraft eines persönlichen Ansatzes für eine erfolgreiche Behandlung. Unsere Praxis ist mit den neuesten Technologien und Methoden ausgestattet, wodurch wir in der Lage sind, eine gute und spezifische Diagnose zu stellen und einen maßgeschneiderten Behandlungsplan anzubieten, damit Sie wieder gut vorankommen!",
        "paragraph2": "Wir arbeiten mit anderen medizinischen Disziplinen wie Hausärzten, medizinischen Fußpflegern und Physiotherapeuten zusammen, um unseren Patienten die beste Versorgung zu bieten. Unsere Praxis ist für jeden zugänglich - von Kindern bis zu aktiven Menschen mit Verletzungen und Senioren mit Fuß- oder fußbezogenen Beschwerden.",
        "image_alt": "Kim Bakhuis, Podotherapeutin von VoorVoet Praktijk voor Podotherapie in Enschede",
    },
    "en": {
        "title": "Podotherapist Enschede",
        "paragraph1": "We are a small-scale practice near the Zuiderval. We strongly believe in the power of a personal approach for successful treatment. Our practice is equipped with the latest technologies and methods, enabling us to make a good and specific diagnosis and offer a customized treatment plan, so you can move forward well again!",
        "paragraph2": "We work together with other medical disciplines such as general practitioners, medical pedicurists and physiotherapists to provide the best care to our patients. Our practice is accessible to everyone - from children to active people with injuries and elderly with foot or foot-related complaints.",
        "image_alt": "Kim Bakhuis, podotherapist at VoorVoet Praktijk voor Podotherapie in Enschede",
    },
}


def section_who_is_voorvoet(language: str) -> rx.Component:
    """
    Create the 'Who is VoorVoet' section introducing the practice.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")

    Returns
    -------
    rx.Component
        A section component with an image-text layout displaying the
        practice owner's photo on the left and practice introduction text
        on the right.
    """
    paragraphs = [
        get_translation(TRANSLATIONS, "paragraph1", language),
        get_translation(TRANSLATIONS, "paragraph2", language),
    ]

    return section(
        container(
            image_text_section(
                image_fallback="/images/page_home/podotherapeut_enschede_kim_bakhuis_van_voorvoet_praktijk_voor_podotherapie.jpg",
                image_avif="/images/page_home/podotherapeut_enschede_kim_bakhuis_van_voorvoet_praktijk_voor_podotherapie.avif",
                image_webp="/images/page_home/podotherapeut_enschede_kim_bakhuis_van_voorvoet_praktijk_voor_podotherapie.webp",
                image_alt=get_translation(TRANSLATIONS, "image_alt", language),
                title=get_translation(TRANSLATIONS, "title", language),
                paragraphs=paragraphs,
                image_position="left",
            )
        ),
        id="who-is-voorvoet",
    )
