# Section "Introduction" on the home page
import reflex as rx
from ...components import container, section, image_text_section


def section_introduction() -> rx.Component:
    paragraphs = [
        "Mijn naam is Kim Bakhuis, podotherapeut en eigenaar van VoorVoet. In 2004 studeerde ik af als fysiotherapeut en na 3 jaar kwam ik in aanraking met podotherapie. Dit vak sprak me zo aan dat ik besloot me te laten omscholen. Inmiddels heb ik ruim 16 jaar werkervaring opgedaan in dit mooie vak. De laatste jaren kriebelde het en heb ik besloten om in 2023 mijn eigen praktijk op te zetten.",
        "Door mijn vooropleiding, verschillende scholingen en jarenlange ervaring heb ik een brede kijk op voet- en voetgerelateerde problemen. Het is belangrijk om me goed in te kunnen leven en mijn uiterste best te doen om je zo goed mogelijk te helpen met jouw hulpvraag. Dat kan in de vorm van advies, behandeling en waar nodig de vervaardiging van ortheses, nagelbeugels of steunzolen. Vanuit mijn praktische instelling werk ik graag samen met andere disciplines om het beste resultaat voor jou te boeken. Privé ben ik een erg actief persoon die houdt van wandelen, hardlopen en Crossfit. Daarnaast daag ik mijzelf graag uit door (grot)duiken en speleo tripjes."
    ]
    
    return section(
        container(
            image_text_section(
                image_src="/images/podotherapeut_enschede_kim_bakhuis_loopt_op_strand_voorvoet_praktijk_voor_podotherapie.jpg",
                title="Even voorstellen",
                paragraphs=paragraphs,
                image_position="left"
            )
        ),
        id="introduction"
    )
