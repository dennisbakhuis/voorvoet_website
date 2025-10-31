# Section "What is podiatry" on the information page
import reflex as rx
from ...components import container, section, image_text_section


def section_what_is_podiatry() -> rx.Component:
    paragraphs = [
        "Podotherapie richt zicht op het onderzoeken en behandelen van klachten in de onderste extremiteit. Denk hierbij aan voetklachten, maar ook klachten in knieën, heupen of de lage rug. Ervaar je pijnklachten? De podotherapeut doet onderzoek de oorzaak van je pijnklachten en zoekt vervolgens naar de best passende oplossing. Dat kan een op maat gemaakte zool zijn, maar ook schoenadvies, oefeningen, een orthese, nagelbeugel of een tijdelijke behandeling zoals taping of het aanleggen van vilt. Kort gezegd, voor bijna alle klachten die voet- of voetstand gerelateerd zijn, kijkt de podotherapeut naar een passende oplossing."
    ]
    
    return section(
        container(
            image_text_section(
                image_src="/images/page_information/skelet_botjes_voet_voorvoet_praktijk_voor_podotherapie_enschede.jpg",
                title="Wat is podotherapie nou eigenlijk?",
                paragraphs=paragraphs,
                image_position="right",
                image_max_width="450px",
            )
        ),
        id="what-is-podiatry"
    )