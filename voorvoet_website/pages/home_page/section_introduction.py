# Sectino "Who is Voorvoet?" on the home page
import reflex as rx
from ...components import column, container, regular_text, section, section_title


def section_introduction() -> rx.Component:
    return section(
        container(
            rx.box(
                column(
                    rx.image(
                        src="/images/podotherapeut_enschede_kim_bakhuis_loopt_op_strand_voorvoet_praktijk_voor_podotherapie.jpg", 
                        width="333px",
                        height="auto",
                        border_radius="4px",
                        box_shadow="0 4px 12px rgba(0, 0, 0, 0.15)",
                    ),
                    padding_right=["0", "0", "0", "2rem"],
                    display="flex",
                    justify_content="center",
                    align_items="center",
                    margin_bottom="2rem"
                ),
                column(
                    section_title("Even voorstellen", margin_bottom="1rem"),
                    regular_text("Mijn naam is Kim Bakhuis, podotherapeut en eigenaar van VoorVoet. In 2004 studeerde ik af als fysiotherapeut en na 3 jaar kwam ik in aanraking met podotherapie. Dit vak sprak me zo aan dat ik besloot me te laten omscholen. Inmiddels heb ik ruim 16 jaar werkervaring opgedaan in dit mooie vak. De laatste jaren kriebelde het en heb ik besloten om in 2023 mijn eigen praktijk op te zetten.", 
                               text_align="left", 
                               margin_bottom="1rem"),
                    regular_text("Door mijn vooropleiding, verschillende scholingen en jarenlange ervaring heb ik een brede kijk op voet- en voetgerelateerde problemen. Het is belangrijk om me goed in te kunnen leven en mijn uiterste best te doen om je zo goed mogelijk te helpen met jouw hulpvraag. Dat kan in de vorm van advies, behandeling en waar nodig de vervaardiging van ortheses, nagelbeugels of steunzolen. Vanuit mijn praktische instelling werk ik graag samen met andere disciplines om het beste resultaat voor jou te boeken. Privé ben ik een erg actief persoon die houdt van wandelen, hardlopen en Crossfit. Daarnaast daag ik mijzelf graag uit door (grot)duiken en speleo tripjes.", 
                               text_align="left"),
                    padding_left=["0", "0", "0", "2rem"],
                    # padding_right="2rem",
                    # margin_bottom=["2rem", "2rem", "2rem", "0"]
                ),
                display=["block", "block", "block", "flex"],
                gap="1.0rem",
                align_items="center",
                max_width="1200px",
                margin_x="auto",
                width="100%",
                padding_x=["2rem", "2rem", "2rem", "2rem", "2rem"]
            )
        ),
        id="about",
        bg="white",
        padding_y="5em"
    )
