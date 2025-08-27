# Sectino "Who is Voorvoet?" on the home page
import reflex as rx
from ...components import column, container, regular_text, section, section_title


def section_who_is_voorvoet() -> rx.Component:
    return section(
        container(
            rx.box(
                column(
                    rx.image(
                        src="/images/podotherapeut_enschede_kim_bakhuis_van_voorvoet_praktijk_voor_podotherapie.jpg", 
                        width="100%",
                        max_width="333px",
                        height="auto",
                        border_radius="4px",
                        box_shadow="0 4px 12px rgba(0, 0, 0, 0.15)",
                    ),
                    padding_right=["0", "0", "0", "2rem"],
                    display="flex",
                    justify_content="center",
                    align_items="center",
                    margin_bottom="2rem",
                    size=["100%", "100%", "100%", "40%", "40%"],
                ),
                column(
                    section_title("Podotherapeut Enschede", margin_bottom="1rem"),
                    regular_text("Wij zijn een kleinschalige praktijk in de buurt van de Zuiderval. Wij geloven sterk in de kracht van een persoonlijke benadering voor een succesvolle behandeling. Onze praktijk is uitgerust met de nieuwste technologieën en methoden, waardoor wij in staat zijn om een goede en specifieke diagnose te stellen en een behandelplan op maat aan te bieden, zodat jij weer goed vooruit kunt!", 
                               text_align="left", 
                               margin_bottom="1rem"),
                    regular_text("Wij werken samen met andere medische disciplines zoals bijvoorbeeld huisartsen, medisch pedicures en fysiotherapeuten om de beste zorg te bieden aan onze patiënten. Onze praktijk is toegankelijk voor iedereen - van kinderen tot actievelingen met blessures en ouderen met voet- of voetgerelateerde klachten.", 
                               text_align="left"),
                    padding_left=["0", "0", "0", "2rem"],
                    size=["100%", "100%", "100%", "60%", "60%"],
                ),
                display=["block", "block", "block", "flex"],
                gap="1.0rem",
                align_items="center"
            )
        ),
        id="about"
    )
