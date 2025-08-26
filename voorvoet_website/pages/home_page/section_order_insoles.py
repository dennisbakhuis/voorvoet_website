# Section "Order insoles" on the home page
import reflex as rx
from ...components import button, column, container, regular_text, section, section_title


def section_order_insoles() -> rx.Component:
    return section(
        container(
            rx.box(
                column(
                    rx.image(
                        src="/images/podoloog_enschede_outdoor_schoenen_voorvoet_praktijk_voor_podotherapie.jpg", 
                        width="333px",
                        height="auto",
                        border_radius="4px",
                        box_shadow="0 4px 12px rgba(0, 0, 0, 0.15)",
                    ),
                    size=["100%", "100%", "100%", "40%"],
                    padding_left=["0", "0", "0", "2rem"],
                    display="flex",
                    justify_content="center",
                    align_items="center",
                    margin_bottom="2rem",
                ),
                column(
                    section_title("Bestel een extra paar zolen online", margin_bottom="1rem"),
                    regular_text("Een extra paar steunzolen kan handig zijn om bijvoorbeeld met een ander paar schoenen te gebruiken, bijvoorbeeld in sport- of wandelschoenen. Dit scheelt niet alleen gedoe met wisselen maar verlengt ook de levensduur van de podotherapeutische zolen.", 
                               text_align="left", 
                               margin_bottom="1rem"),
                    regular_text("Wij werken samen met andere medische disciplines zoals bijvoorbeeld huisartsen, medisch pedicures en fysiotherapeuten om de beste zorg te bieden aan onze patiënten. Onze praktijk is toegankelijk voor iedereen - van kinderen tot actievelingen met blessures en ouderen met voet- of voetgerelateerde klachten.", 
                               text_align="left", 
                               margin_bottom="1.5rem"),
                    button("Extra paar bestellen", href=""),
                    size=["100%", "100%", "100%", "60%"],
                    padding_right=["0", "0", "0", "2rem"],
                ),
                display=["block", "block", "block", "flex"],
                flex_direction=["column", "column", "column", "row-reverse"],
                gap="1.0rem",
                align_items="center",
                max_width="1200px",
                margin_x="auto",
                width="100%",
                padding_x=["2rem", "2rem", "2rem", "2rem", "2rem"]
            )
        ),
        id="about",
        bg="#dcedec",
        padding_y="5em"
    )
