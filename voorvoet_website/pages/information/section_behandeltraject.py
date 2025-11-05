"""Section explaining the podiatry treatment process."""
import reflex as rx
from ...components import container, section, image_text_section


def section_behandeltraject() -> rx.Component:
    """
    Create the treatment process explanation section.

    Describes the complete treatment journey from intake to follow-up,
    including examination procedures (inspection, gait analysis, pressure
    measurements), treatment planning, insole fitting, and follow-up care.
    Emphasizes the personalized approach to each patient.

    Returns
    -------
    rx.Component
        A section component with an image-text layout explaining the
        step-by-step treatment process at the practice.
    """
    paragraphs = [
        "We beginnen altijd met een uitgebreide intake om de klachten in kaart te brengen. Aan de hand daarvan voeren we een onderzoek uit. Dit kan bestaat veelal uit een inspectie, onderzoek van het looppatroon, een drukmeting en het testen van de functie van de voeten. Ook bekijken we het schoeisel waar je veel op loopt of waarin je juist veel klachten ervaart. Als er een therapie geïndiceerd is, dan bespreken we dat samen en bij akkoord wordt de therapie gestart. In het geval van het aanmeten van podotherapeutische zolen worden de zolen op korte termijn geleverd en vind er als je nieuw bij ons bent altijd een controle afspraak plaats. De therapie is ten allen tijde maatwerk en wordt afgestemd op de individuele situatie."
    ]
    
    return section(
        container(
            image_text_section(
                image_src="/images/page_information/wandelen_zonder_pijn_in_de_voeten_voorvoet_podotherapie_enschede.jpg",
                title="Het behandeltraject",
                paragraphs=paragraphs,
                image_position="left",
                image_max_width="450px",
            ),
        ),
        padding_bottom="2rem",
        id="het-behandeltraject"
    )