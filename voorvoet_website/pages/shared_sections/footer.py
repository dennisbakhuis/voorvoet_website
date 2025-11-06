"""Footer component for the entire site."""
import reflex as rx

from ...components import container, section, regular_text
from ...theme import Colors, FontSizes
from ...states import WebsiteState


TRANSLATIONS = {
    "nl": {
        "location_eeftinksweg": "Locatie Eeftinksweg",
        "location_beethovenlaan": "Locatie Beethovenlaan",
        "monday": "Maandag",
        "tuesday": "Dinsdag",
        "wednesday": "Woensdag",
        "thursday": "Donderdag",
        "friday": "Vrijdag",
        "kvk_number": "KvK nummer",
        "practice_code": "Praktijkcode",
        "bank_account": "Bankrekening",
        "credits": "Credits",
        "privacy_policy": "Privacy beleid",
        "terms_conditions": "Algemene voorwaarden",
        "made_with_love": "Gemaakt met ❤️ door Dennis",
    },
    "de": {
        "location_eeftinksweg": "Standort Eeftinksweg",
        "location_beethovenlaan": "Standort Beethovenlaan",
        "monday": "Montag",
        "tuesday": "Dienstag",
        "wednesday": "Mittwoch",
        "thursday": "Donnerstag",
        "friday": "Freitag",
        "kvk_number": "KvK Nummer",
        "practice_code": "Praxiscode",
        "bank_account": "Bankkonto",
        "credits": "Credits",
        "privacy_policy": "Datenschutzrichtlinie",
        "terms_conditions": "Allgemeine Geschäftsbedingungen",
        "made_with_love": "Mit ❤️ gemacht von Dennis",
    },
    "en": {
        "location_eeftinksweg": "Location Eeftinksweg",
        "location_beethovenlaan": "Location Beethovenlaan",
        "monday": "Monday",
        "tuesday": "Tuesday",
        "wednesday": "Wednesday",
        "thursday": "Thursday",
        "friday": "Friday",
        "kvk_number": "KvK Number",
        "practice_code": "Practice Code",
        "bank_account": "Bank Account",
        "credits": "Credits",
        "privacy_policy": "Privacy Policy",
        "terms_conditions": "Terms & Conditions",
        "made_with_love": "Made with ❤️ by Dennis",
    },
}


def footer() -> rx.Component:
    """
    Create the site-wide footer with practice information and links.

    The footer displays comprehensive practice information including:
    - Logo
    - Two location addresses with opening hours
    - Contact information (phone and email)
    - Business details (KvK, practice code, bank account)
    - Professional affiliations (logos)
    - Legal links (privacy policy, terms)
    - Copyright notice

    Returns
    -------
    rx.Component
        A section component containing the complete footer layout with
        responsive design for mobile, tablet, and desktop viewports.

    Notes
    -----
    The footer uses a responsive layout that:
    - Stacks vertically on mobile devices
    - Transitions to side-by-side layout on larger screens
    - Includes gentle wave clip-path styling at the top
    """
    # Helper function to get translation based on current language
    def get_translation(key: str) -> rx.Var:
        return rx.cond(
            WebsiteState.current_language == "nl",
            TRANSLATIONS["nl"][key],
            rx.cond(
                WebsiteState.current_language == "de",
                TRANSLATIONS["de"][key],
                TRANSLATIONS["en"][key]
            )
        )

    return section(
        container(
            rx.box(
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
                rx.box(
                    rx.box(
                        regular_text(
                            get_translation("location_eeftinksweg"),
                            color=Colors.text["muted"],
                            font_weight="700",
                            text_decoration="underline",
                            font_size=FontSizes.regular,
                            margin_bottom="0.15rem"
                        ),
                        regular_text("Eeftinksweg 13", color=Colors.text["secondary"]),
                        regular_text("7541 WE Enschede", color=Colors.text["secondary"], margin_bottom="0.20rem"),
                        rx.box(
                            regular_text(get_translation("monday"), color=Colors.text["secondary"], display="inline-block", width="100px"),
                            regular_text("8.00 - 17.00", color=Colors.text["secondary"], display="inline-block", margin_left="10px"),
                        ),
                        rx.box(
                            regular_text(get_translation("thursday"), color=Colors.text["secondary"], display="inline-block", width="100px"),
                            regular_text("8.00 - 17.00", color=Colors.text["secondary"], display="inline-block", margin_left="10px"),
                            margin_bottom="0.15rem"
                        ),
                        regular_text(
                            get_translation("location_beethovenlaan"),
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
                            regular_text(get_translation("tuesday"), color=Colors.text["secondary"], display="inline-block", width="100px"),
                            regular_text("8.30 - 19.30", color=Colors.text["secondary"], display="inline-block", margin_left="10px"),
                        ),
                        rx.box(
                            regular_text(get_translation("wednesday"), color=Colors.text["secondary"], display="inline-block", width="100px"),
                            regular_text("8.30 - 17.00", color=Colors.text["secondary"], display="inline-block", margin_left="10px"),
                        ),
                        rx.box(
                            regular_text(get_translation("friday"), color=Colors.text["secondary"], display="inline-block", width="100px"),
                            regular_text("8.00 - 13.00", color=Colors.text["secondary"], display="inline-block", margin_left="10px"),
                        ),
                        flex="1",
                        text_align=["center", "center", "left", "left", "left"],
                        margin_bottom=["2rem", "2rem", "0", "0", "0"],
                        padding_x=["20px", "20px", "20px", "20px", "20px"],
                    ),
                    rx.box(
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
                        rx.box(
                            rx.box(
                                regular_text(get_translation("kvk_number"), color=Colors.text["muted"], font_weight="600", display="inline-block", width="140px"),
                                regular_text("87984814", color=Colors.text["secondary"], display="inline-block"),
                                margin_bottom="0.5rem"
                            ),
                            rx.box(
                                regular_text(get_translation("practice_code"), color=Colors.text["muted"], font_weight="600", display="inline-block", width="140px"),
                                regular_text("26000993", color=Colors.text["secondary"], display="inline-block"),
                                margin_bottom="0.5rem"
                            ),
                            rx.box(
                                regular_text(get_translation("bank_account"), color=Colors.text["muted"], font_weight="600", display="inline-block", width="140px"),
                                regular_text("NL18 KNAB 0515 1858 84", color=Colors.text["secondary"], display="inline-block"),
                            ),
                            flex="1",
                            margin_bottom="2rem"
                        ),
                        rx.box(
                            rx.link(get_translation("credits"), href="#", color=Colors.text["link"], text_decoration="underline", display="block", font_size=FontSizes.regular, margin_bottom="0.5rem", text_align=["center", "center", "left", "left", "left"]),
                            rx.link(get_translation("privacy_policy"), href="#", color=Colors.text["link"], text_decoration="underline", display="block", font_size=FontSizes.regular, margin_bottom="0.5rem", text_align=["center", "center", "left", "left", "left"]),
                            rx.link(get_translation("terms_conditions"), href="#", color=Colors.text["link"], text_decoration="underline", display="block", font_size=FontSizes.regular, text_align=["center", "center", "left", "left", "left"])
                        ),
                        display="flex",
                        flex_direction="column",
                        flex="1",
                        text_align=["center", "center", "left", "left", "left"]
                    ),
                    display=["block", "block", "flex", "flex", "flex"],
                    gap=["0", "0", "2rem", "2rem", "2rem"],
                    flex=["none", "none", "none", "0 0 70%", "0 0 70%"]
                ),
                display=["block", "block", "block", "flex", "flex"],
                gap=["0", "0", "0", "2rem", "2rem"],
                align_items=["center", "center", "center", "flex-start", "flex-start"],
                text_align=["center", "center", "center", "left", "left"]
            ),
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
                        rx.text("© ", get_translation("made_with_love")),
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
