# Footer for the whole site
import reflex as rx

from ...components import container, section
from ...theme import FOOTER_BG


def footer() -> rx.Component:
    return section(
        container(
            # Main footer layout: 30% logo / 70% content (which splits into 50%/50%)
            rx.box(
                # Logo column (30%)
                rx.box(
                    rx.image(
                        src="images/podotherapeut_enschede_voorvoet_praktijk_voor_podotherapie_logo.svg", 
                        alt="VoorVoet - Praktijk voor podotherapie",
                        width="100%",
                        max_width="300px",
                        margin_top="-25px"
                    ),
                    display="flex",
                    justify_content=["center", "center", "center", "center", "flex-start"],
                    flex=["none", "none", "none", "0 0 30%", "0 0 30%"],
                    margin_bottom=["2rem", "2rem", "2rem", "0", "0"]
                ),
                # Content area (70% - splits into 50%/50%)
                rx.box(
                    # Location column
                    rx.box(
                        # Locatie Eeftinksweg with opening hours
                        rx.text(
                            "Locatie Eeftinksweg",
                            color="#666",
                            font_weight="600",
                            text_decoration="underline",
                            font_size="20px",
                            margin_bottom="0.15rem"
                        ),
                        rx.text("Eeftinksweg 13", color="#4a4a4a", font_size="20px"),
                        rx.text("7541 WE Enschede", color="#4a4a4a", font_size="20px", margin_bottom="0.15rem"),
                        rx.box(
                            rx.text("Maandag", color="#4a4a4a", display="inline-block", width="100px", font_size="20px"),
                            rx.text("8.00 - 17.00", color="#4a4a4a", display="inline-block", font_size="20px", margin_left="10px"),
                        ),
                        rx.box(
                            rx.text("Donderdag", color="#4a4a4a", display="inline-block", width="100px", font_size="20px"),
                            rx.text("8.00 - 17.00", color="#4a4a4a", display="inline-block", font_size="20px", margin_left="10px"),
                            margin_bottom="0.15rem"
                        ),
                        # Locatie Beethovenlaan with opening hours
                        rx.text(
                            "Locatie Beethovenlaan",
                            color="#666",
                            font_weight="600",
                            text_decoration="underline",
                            font_size="20px",
                            margin_top="1rem",
                            margin_bottom="0.15rem"
                        ),
                        rx.text("Beethovenlaan 10", color="#4a4a4a", font_size="20px"),
                        rx.text("7522 HJ Enschede", color="#4a4a4a", font_size="20px", margin_bottom="0.15rem"),
                        rx.box(
                            rx.text("Dinsdag", color="#4a4a4a", display="inline-block", width="100px", font_size="20px"),
                            rx.text("8.30 - 19.30", color="#4a4a4a", display="inline-block", font_size="20px", margin_left="10px"),
                        ),
                        rx.box(
                            rx.text("Woensdag", color="#4a4a4a", display="inline-block", width="100px", font_size="20px"),
                            rx.text("8.30 - 17.00", color="#4a4a4a", display="inline-block", font_size="20px", margin_left="10px"),
                        ),
                        rx.box(
                            rx.text("Vrijdag", color="#4a4a4a", display="inline-block", width="100px", font_size="20px"),
                            rx.text("8.00 - 13.00", color="#4a4a4a", display="inline-block", font_size="20px", margin_left="10px"),
                        ),
                        flex="1",
                        text_align=["center", "center", "left", "left", "left"],
                        margin_bottom=["2rem", "2rem", "0", "0", "0"],
                        padding_x=["20px", "20px", "20px", "20px", "20px"],
                    ),
                    # Contact, Company & Links column
                    rx.box(
                        # Contact info
                        rx.box(
                            rx.hstack(
                                rx.html('<i class="fa fa-phone" style="color: #4a4a4a; font-size: 20px;"/>'),
                                rx.link(
                                    "+31 (0) 6 577 509 97",
                                    href="tel:+31657750997",
                                    color="#4a4a4a",
                                    font_size="22px",
                                    text_decoration="none",
                                    _hover={"text_decoration": "underline", "color": "#047857"}
                                ),
                                spacing="2",
                                align="center",
                                justify_content=["center", "center", "flex-start", "flex-start", "flex-start"]
                            ),
                            rx.hstack(
                                rx.html('<i class="fa fa-envelope" style="color: #4a4a4a; font-size: 20px;"/>'),
                                rx.link(
                                    "info@voorvoet.nl",
                                    href="mailto:info@voorvoet.nl",
                                    color="#4a4a4a",
                                    font_size="22px",
                                    text_decoration="none",
                                    _hover={"text_decoration": "underline", "color": "#047857"}
                                ),
                                spacing="2",
                                align="center",
                                justify_content=["center", "center", "flex-start", "flex-start", "flex-start"]
                            ),
                            spacing="1rem",
                            margin_bottom="2rem"
                        ),
                        # Business details
                        rx.box(
                            rx.box(
                                rx.text("KvK nummer", color="#666", font_weight="600", display="inline-block", width="140px", font_size="20px"),
                                rx.text("87984814", color="#4a4a4a", display="inline-block", font_size="20px"),
                                margin_bottom="0.5rem"
                            ),
                            rx.box(
                                rx.text("Praktijkcode", color="#666", font_weight="600", display="inline-block", width="140px", font_size="20px"),
                                rx.text("26000993", color="#4a4a4a", display="inline-block", font_size="20px"),
                                margin_bottom="0.5rem"
                            ),
                            rx.box(
                                rx.text("Bankrekening", color="#666", font_weight="600", display="inline-block", width="140px", font_size="20px"),
                                rx.text("NL18 KNAB 0515 1858 84", color="#4a4a4a", display="inline-block", font_size="20px"),
                            ),
                            flex="1",
                            margin_bottom="2rem"
                        ),
                        # Links at bottom
                        rx.box(
                            rx.link("Credits", href="#", color="#3b82f6", text_decoration="underline", display="block", font_size="20px", margin_bottom="0.5rem", text_align=["center", "center", "left", "left", "left"]),
                            rx.link("Privacy beleid", href="#", color="#3b82f6", text_decoration="underline", display="block", font_size="20px", margin_bottom="0.5rem", text_align=["center", "center", "left", "left", "left"]),
                            rx.link("Algemene voorwaarden", href="#", color="#3b82f6", text_decoration="underline", display="block", font_size="20px", text_align=["center", "center", "left", "left", "left"])
                        ),
                        display="flex",
                        flex_direction="column",
                        flex="1",
                        text_align=["center", "center", "left", "left", "left"]
                    ),
                    # Content area layout: stacked on mobile/small tablet, side-by-side from tablet+
                    display=["block", "block", "flex", "flex", "flex"],
                    gap=["0", "0", "2rem", "2rem", "2rem"],
                    flex=["none", "none", "none", "0 0 70%", "0 0 70%"]
                ),
                # Main container layout: stacked on mobile/small tablet/tablet, side-by-side on desktop+
                display=["block", "block", "block", "flex", "flex"],
                gap=["0", "0", "0", "2rem", "2rem"],
                align_items=["center", "center", "center", "flex-start", "flex-start"],
                text_align=["center", "center", "center", "left", "left"]
            ),
            # Bottom section with logos and copyright
            rx.box(
                rx.box(
                    rx.link(
                        rx.image(src="images/podotherapeut_enschede_nederlandse_vereniging_van_podotherapeuten_voorvoet.png", height="60px"),
                        href="https://www.podotherapie.nl/",
                        is_external=True
                    ),
                    display="flex",
                    justify_content="center",
                    flex="1",
                ),
                rx.box(
                    rx.link(
                        rx.image(src="images/podotherapeut_enschede_kwaliteit_register_paramedici_kim_bakhuis_geregistreerd.png", height="60px"),
                        href="https://www.kwaliteitsregisterparamedici.nl/kwaliteitsregister/paramedici/33997",
                        is_external=True
                    ),
                    display="flex",
                    justify_content="center",
                    flex="1",
                    margin_top=["1rem", "1rem", "0", "0", "0"],
                ),
                rx.box(
                    rx.link(
                        "© Made with ❤️ by Dennis",
                        href="https://linkedin.com/in/dennisbakuis",
                        color="#666",
                        font_size="20px",
                        text_align="center",
                        text_decoration="none",
                        _hover={"text_decoration": "underline", "color": "#047857"},
                        is_external=True,
                        margin_top=["1rem", "1rem", "0", "0", "0"],

                    ),
                    display="flex",
                    justify_content="center",
                    align_items="center",
                    flex="1",
                ),
                display=["block", "block", "flex"],
                align_items="center",
                margin_top="1rem",
                padding_top="1rem"
            )
        ),
        bg=FOOTER_BG,
        id="footer",
        padding_top="4rem",
        padding_bottom="1.5rem"
    )
