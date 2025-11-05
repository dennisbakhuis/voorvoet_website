# Footer for the whole site
import reflex as rx

from ...components import container, section, regular_text
from ...theme import Colors, FontSizes


def footer() -> rx.Component:
    return section(
        container(
            # Main footer layout: 30% logo / 70% content (which splits into 50%/50%)
            rx.box(
                # Logo column (30%)
                rx.box(
                    rx.image(
                        src="/images/shared/podotherapeut_enschede_voorvoet_praktijk_voor_podotherapie_logo.svg",
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
                        regular_text(
                            "Locatie Eeftinksweg",
                            color=Colors.text["muted"],
                            font_weight="700",
                            text_decoration="underline",
                            font_size=FontSizes.regular,
                            margin_bottom="0.15rem"
                        ),
                        regular_text("Eeftinksweg 13", color=Colors.text["secondary"]),
                        regular_text("7541 WE Enschede", color=Colors.text["secondary"], margin_bottom="0.20rem"),
                        rx.box(
                            regular_text("Maandag", color=Colors.text["secondary"], display="inline-block", width="100px"),
                            regular_text("8.00 - 17.00", color=Colors.text["secondary"], display="inline-block", margin_left="10px"),
                        ),
                        rx.box(
                            regular_text("Donderdag", color=Colors.text["secondary"], display="inline-block", width="100px"),
                            regular_text("8.00 - 17.00", color=Colors.text["secondary"], display="inline-block", margin_left="10px"),
                            margin_bottom="0.15rem"
                        ),
                        # Locatie Beethovenlaan with opening hours
                        regular_text(
                            "Locatie Beethovenlaan",
                            color=Colors.text["muted"],
                            font_weight="700",
                            text_decoration="underline",
                            font_size=FontSizes.regular,
                            margin_top="1rem",
                            margin_bottom="0.15rem"
                        ),
                        regular_text("Beethovenlaan 10", color=Colors.text["secondary"]),
                        regular_text("7522 HJ Enschede", color=Colors.text["secondary"], margin_bottom="0.20rem"),
                        rx.box(
                            regular_text("Dinsdag", color=Colors.text["secondary"], display="inline-block", width="100px"),
                            regular_text("8.30 - 19.30", color=Colors.text["secondary"], display="inline-block", margin_left="10px"),
                        ),
                        rx.box(
                            regular_text("Woensdag", color=Colors.text["secondary"], display="inline-block", width="100px"),
                            regular_text("8.30 - 17.00", color=Colors.text["secondary"], display="inline-block", margin_left="10px"),
                        ),
                        rx.box(
                            regular_text("Vrijdag", color=Colors.text["secondary"], display="inline-block", width="100px"),
                            regular_text("8.00 - 13.00", color=Colors.text["secondary"], display="inline-block", margin_left="10px"),
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
                                rx.html(f'<i class="fa fa-phone" style="color: {Colors.text["secondary"]}; font-size: 20px;"/>'),
                                rx.link(
                                    "+31 (0) 6 577 509 97",
                                    href="tel:+31657750997",
                                    color=Colors.text["secondary"],
                                    font_size=FontSizes.body_accent,
                                    text_decoration="none",
                                    _hover={"text_decoration": "underline", "color": Colors.primary["700"]}
                                ),
                                spacing="2",
                                align="center",
                                justify_content=["center", "center", "flex-start", "flex-start", "flex-start"]
                            ),
                            rx.hstack(
                                rx.html(f'<i class="fa fa-envelope" style="color: {Colors.text["secondary"]}; font-size: 20px;"/>'),
                                rx.link(
                                    "info@voorvoet.nl",
                                    href="mailto:info@voorvoet.nl",
                                    color=Colors.text["secondary"],
                                    font_size=FontSizes.body_accent,
                                    text_decoration="none",
                                    _hover={"text_decoration": "underline", "color": Colors.primary["700"]}
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
                                regular_text("KvK nummer", color=Colors.text["muted"], font_weight="600", display="inline-block", width="140px"),
                                regular_text("87984814", color=Colors.text["secondary"], display="inline-block"),
                                margin_bottom="0.5rem"
                            ),
                            rx.box(
                                regular_text("Praktijkcode", color=Colors.text["muted"], font_weight="600", display="inline-block", width="140px"),
                                regular_text("26000993", color=Colors.text["secondary"], display="inline-block"),
                                margin_bottom="0.5rem"
                            ),
                            rx.box(
                                regular_text("Bankrekening", color=Colors.text["muted"], font_weight="600", display="inline-block", width="140px"),
                                regular_text("NL18 KNAB 0515 1858 84", color=Colors.text["secondary"], display="inline-block"),
                            ),
                            flex="1",
                            margin_bottom="2rem"
                        ),
                        # Links at bottom
                        rx.box(
                            rx.link("Credits", href="#", color=Colors.text["link"], text_decoration="underline", display="block", font_size=FontSizes.regular, margin_bottom="0.5rem", text_align=["center", "center", "left", "left", "left"]),
                            rx.link("Privacy beleid", href="#", color=Colors.text["link"], text_decoration="underline", display="block", font_size=FontSizes.regular, margin_bottom="0.5rem", text_align=["center", "center", "left", "left", "left"]),
                            rx.link("Algemene voorwaarden", href="#", color=Colors.text["link"], text_decoration="underline", display="block", font_size=FontSizes.regular, text_align=["center", "center", "left", "left", "left"])
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
                        rx.image(src="/images/shared/podotherapeut_enschede_nederlandse_vereniging_van_podotherapeuten_voorvoet.png", height="60px"),
                        href="https://www.podotherapie.nl/",
                        is_external=True
                    ),
                    display="flex",
                    justify_content="center",
                    flex="1",
                ),
                rx.box(
                    rx.link(
                        rx.image(src="/images/shared/podotherapeut_enschede_kwaliteit_register_paramedici_kim_bakhuis_geregistreerd.png", height="60px"),
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
                        href="https://linkedin.com/in/dennisbakhuis",
                        color=Colors.text["muted"],
                        font_size=FontSizes.regular,
                        text_align="center",
                        text_decoration="none",
                        _hover={"text_decoration": "underline", "color": Colors.primary["700"]},
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
        id="footer",
        padding_bottom="0.5rem",
        background_color=Colors.backgrounds["green_light"],
        clip_top="gentle_2",
        divider_color=Colors.backgrounds['white'],
    )
