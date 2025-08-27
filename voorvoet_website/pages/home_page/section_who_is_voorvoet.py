# Section "Who is Voorvoet?" on the home page  
import reflex as rx
from ...components import container, section, image_text_section


def section_who_is_voorvoet() -> rx.Component:
    paragraphs = [
        "Wij zijn een kleinschalige praktijk in de buurt van de Zuiderval. Wij geloven sterk in de kracht van een persoonlijke benadering voor een succesvolle behandeling. Onze praktijk is uitgerust met de nieuwste technologieën en methoden, waardoor wij in staat zijn om een goede en specifieke diagnose te stellen en een behandelplan op maat aan te bieden, zodat jij weer goed vooruit kunt!",
        "Wij werken samen met andere medische disciplines zoals bijvoorbeeld huisartsen, medisch pedicures en fysiotherapeuten om de beste zorg te bieden aan onze patiënten. Onze praktijk is toegankelijk voor iedereen - van kinderen tot actievelingen met blessures en ouderen met voet- of voetgerelateerde klachten."
    ]
    
    return section(
        container(
            image_text_section(
                image_src="/images/podotherapeut_enschede_kim_bakhuis_van_voorvoet_praktijk_voor_podotherapie.jpg",
                title="Podotherapeut Enschede",
                paragraphs=paragraphs,
                image_position="left"
            )
        ),
        id="who-is-voorvoet"
    )
