"""Section explaining the podiatry treatment process."""

import reflex as rx

from ...components import container, section, image_text_section
from ...utils import get_translation


TRANSLATIONS = {
    "nl": {
        "title": "Het behandeltraject",
        "paragraph1": "We beginnen altijd met een uitgebreide intake om de klachten in kaart te brengen. Aan de hand daarvan voeren we een onderzoek uit. Dit kan bestaat veelal uit een inspectie, onderzoek van het looppatroon, een drukmeting en het testen van de functie van de voeten. Ook bekijken we het schoeisel waar je veel op loopt of waarin je juist veel klachten ervaart. Als er een therapie geïndiceerd is, dan bespreken we dat samen en bij akkoord wordt de therapie gestart. In het geval van het aanmeten van podotherapeutische zolen worden de zolen op korte termijn geleverd en vind er als je nieuw bij ons bent altijd een controle afspraak plaats. De therapie is ten allen tijde maatwerk en wordt afgestemd op de individuele situatie.",
        "image_alt": "Wandelen zonder pijn in de voeten dankzij podotherapie",
    },
    "de": {
        "title": "Der Behandlungsverlauf",
        "paragraph1": "Wir beginnen immer mit einer ausführlichen Anamnese, um die Beschwerden zu erfassen. Auf dieser Grundlage führen wir eine Untersuchung durch. Diese besteht meist aus einer Inspektion, Untersuchung des Gangmusters, einer Druckmessung und dem Testen der Fußfunktion. Wir betrachten auch das Schuhwerk, in dem Sie viel gehen oder in dem Sie besonders viele Beschwerden haben. Wenn eine Therapie indiziert ist, besprechen wir dies gemeinsam und bei Zustimmung wird die Therapie begonnen. Im Falle des Anpassens von podotherapeutischen Einlagen werden die Einlagen kurzfristig geliefert und wenn Sie neu bei uns sind, findet immer ein Kontrolltermin statt. Die Therapie ist stets maßgeschneidert und wird auf die individuelle Situation abgestimmt.",
        "image_alt": "Schmerzfrei gehen dank Podotherapie",
    },
    "en": {
        "title": "The treatment process",
        "paragraph1": "We always start with a comprehensive intake to map out the complaints. Based on that, we conduct an examination. This usually consists of an inspection, examination of the gait pattern, a pressure measurement and testing the function of the feet. We also look at the footwear you walk in a lot or in which you experience many complaints. If a therapy is indicated, we discuss this together and with approval the therapy is started. In the case of fitting podotherapeutic insoles, the insoles are delivered in the short term and if you are new to us, a follow-up appointment always takes place. The therapy is always customized and tailored to the individual situation.",
        "image_alt": "Walking without foot pain thanks to podotherapy",
    },
}


def section_behandeltraject(language: str) -> rx.Component:
    """
    Create the treatment process explanation section.

    Describes the complete treatment journey from intake to follow-up,
    including examination procedures (inspection, gait analysis, pressure
    measurements), treatment planning, insole fitting, and follow-up care.
    Emphasizes the personalized approach to each patient.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")

    Returns
    -------
    rx.Component
        A section component with an image-text layout explaining the
        step-by-step treatment process at the practice.
    """
    paragraphs = [get_translation(TRANSLATIONS, "paragraph1", language)]

    return section(
        container(
            image_text_section(
                image_fallback="/images/page_information/wandelen_zonder_pijn_in_de_voeten_voorvoet_podotherapie_enschede.jpg",
                image_avif="/images/page_information/wandelen_zonder_pijn_in_de_voeten_voorvoet_podotherapie_enschede.avif",
                image_webp="/images/page_information/wandelen_zonder_pijn_in_de_voeten_voorvoet_podotherapie_enschede.webp",
                image_alt=get_translation(TRANSLATIONS, "image_alt", language),
                title=get_translation(TRANSLATIONS, "title", language),
                paragraphs=paragraphs,
                image_position="left",
                image_max_width="450px",
            ),
        ),
        padding_bottom="2rem",
        id="het-behandeltraject",
    )
