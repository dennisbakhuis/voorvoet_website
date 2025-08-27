# Section "Order insoles" on the home page
import reflex as rx
from ...components import container, section, image_text_section


def section_order_insoles() -> rx.Component:
    paragraphs = [
        "Een extra paar steunzolen kan handig zijn om bijvoorbeeld met een ander paar schoenen te gebruiken, bijvoorbeeld in sport- of wandelschoenen. Dit scheelt niet alleen gedoe met wisselen maar verlengt ook de levensduur van de podotherapeutische zolen.",
        "Wij werken samen met andere medische disciplines zoals bijvoorbeeld huisartsen, medisch pedicures en fysiotherapeuten om de beste zorg te bieden aan onze patiënten. Onze praktijk is toegankelijk voor iedereen - van kinderen tot actievelingen met blessures en ouderen met voet- of voetgerelateerde klachten."
    ]
    
    return section(
        container(
            image_text_section(
                image_src="/images/podoloog_enschede_outdoor_schoenen_voorvoet_praktijk_voor_podotherapie.jpg",
                title="Bestel een extra paar zolen online",
                paragraphs=paragraphs,
                image_position="right",
                button_text="Extra paar bestellen",
                button_link=""
            )
        ),
        id="about",
        alternate_bg=True
    )
