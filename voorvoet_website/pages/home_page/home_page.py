import reflex as rx

from .section_hero import hero_section
from .section_who_is_voorvoet import section_who_is_voorvoet
from .section_order_insoles import section_order_insoles
from .section_introduction import section_introduction

from ..shared_components import footer, header, modal

from ...components import container, responsive_grid, section, button
from ...theme import PRIMARY, DARK
from ...state import WebsiteState


# -----------------------------
# SERVICES SECTION
# -----------------------------
def service_card(title: str, description: str, icon: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.html(f'<i class="fa {icon} text-3xl" style="color: {PRIMARY}"></i>'),
                display="flex",
                justify_content="center",
                align_items="center",
                width="60px",
                height="60px",
                bg="rgba(16, 185, 129, 0.1)",
                border_radius="50%",
                margin_bottom="1rem",
            ),
            rx.heading(title, size="4", color=DARK, text_align="center"),
            rx.text(
                description, 
                text_align="center", 
                color="gray.600", 
                line_height="1.6",
                font_size="14px"
            ),
            spacing="3",
            align="center",
        ),
        bg="white",
        border_radius="12px",
        padding="2rem",
        box_shadow="0 4px 6px rgba(0, 0, 0, 0.05)",
        border="1px solid #f3f4f6",
        height="100%",
        transition="all 0.3s ease",
        _hover={
            "transform": "translateY(-4px)",
            "box_shadow": "0 8px 25px rgba(0, 0, 0, 0.1)"
        }
    )


def services_section() -> rx.Component:
    return section(
        container(
            rx.vstack(
                rx.text("Onze diensten", color=PRIMARY, font_weight="600", font_size="18px"),
                rx.heading("Podotherapie diensten in Enschede", size="8", color=DARK, text_align="center"),
                rx.text(
                    "Wij bieden een breed scala aan podotherapeutische behandelingen voor al uw voetklachten.",
                    text_align="center",
                    color="gray.600",
                    max_width="600px",
                    font_size="18px",
                    line_height="1.6"
                ),
                responsive_grid(
                    service_card(
                        "Podotherapie",
                        "Professionele behandeling van voet- en loopklachten door een erkend podotherapeut.",
                        "fa-user-md"
                    ),
                    service_card(
                        "Ortheses",
                        "Speciaal vervaardigde orthopedische hulpmiddelen voor correctie en ondersteuning.",
                        "fa-shoe-prints"
                    ),
                    service_card(
                        "Nagelbeugels",
                        "Behandeling van ingegroeide nagels met behulp van nagelbeugels en andere technieken.",
                        "fa-cut"
                    ),
                    service_card(
                        "Pijnbehandeling",
                        "Gerichte behandeling van voetpijn, hielspoor en andere voetgerelateerde pijn.",
                        "fa-heart-o"
                    ),
                    service_card(
                        "Steunzolen",
                        "Op maat gemaakte steunzolen voor optimaal comfort en ondersteuning bij het lopen.",
                        "fa-building-o"
                    ),
                    service_card(
                        "Kindervoeten",
                        "Specialistische zorg voor voetklachten bij kinderen en adolescenten.",
                        "fa-child"
                    ),
                    columns=[1, 2, 3],
                    spacing="6",
                ),
                spacing="8",
                align="center",
            )
        ),
        id="services",
        bg="#f9fafb"
    )


# -----------------------------
# CONTACT SECTION
# -----------------------------
def contact_info_card(title: str, info: str, icon: str) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.html(f'<i class="fa {icon}" style="color: {PRIMARY}"></i>'),
            width="24px",
            font_size="20px"
        ),
        rx.vstack(
            rx.text(title, font_weight="600", color=DARK, font_size="16px"),
            rx.text(info, color="gray.600", font_size="14px"),
            spacing="1",
            align="start"
        ),
        spacing="4",
        align="start"
    )


def contact_section() -> rx.Component:
    return section(
        container(
            responsive_grid(
                rx.vstack(
                    rx.heading("Neem contact op", size="7", color=DARK),
                    rx.text(
                        "Heeft u vragen of wilt u een afspraak maken? Neem gerust contact met ons op!",
                        color="gray.600",
                        line_height="1.6",
                        font_size="16px"
                    ),
                    rx.vstack(
                        contact_info_card(
                            "Telefoon", 
                            "+31 (0) 6 577 509 97", 
                            "fa-phone"
                        ),
                        contact_info_card(
                            "E-mail", 
                            "info@voorvoet.nl", 
                            "fa-envelope"
                        ),
                        contact_info_card(
                            "Locaties", 
                            "Eeftinksweg 13 (ma, do) • Beethovenlaan 10 (di, wo, vr)", 
                            "fa-map-marker"
                        ),
                        contact_info_card(
                            "KvK-nummer", 
                            "87984814", 
                            "fa-file-text-o"
                        ),
                        spacing="6",
                        align="start",
                        width="100%"
                    ),
                    button(
                        "Maak een afspraak",
                        on_click=WebsiteState.open_modal("Afspraak maken", "Neem contact op voor een afspraak")  # type: ignore
                    ),
                    spacing="6",
                    align="start"
                ),
                rx.box(
                    rx.html(
                        '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2443.8!2d6.8944!3d52.2215!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zNTLCsDA4JzE3LjQiTiA2wrA1MycyNy45IkU!5e0!3m2!1sen!2snl!4v1234567890" style="border:0;width:100%;height:100%;min-height:400px" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>'
                    ),
                    width="100%",
                    height="100%",
                    min_height="400px",
                    border_radius="12px",
                    overflow="hidden"
                ),
                columns=[1, 1, 2],
                spacing="8",
                align_items="center"
            )
        ),
        id="contact"
    )


# -----------------------------
# KIM BAKHUIS SECTION
# -----------------------------
def kim_section() -> rx.Component:
    return section(
        container(
            responsive_grid(
                rx.box(
                    rx.image(
                        src="/assets/images/podotherapeut_enschede_kim_bakhuis_van_voorvoet_praktijk_voor_podotherapie.jpg",
                        width="100%",
                        height="100%",
                        object_fit="cover",
                        border_radius="12px"
                    ),
                    height=["300px", "400px", "500px"]
                ),
                rx.vstack(
                    rx.text("Podotherapeut", color=PRIMARY, font_weight="600", font_size="18px"),
                    rx.heading("Kim Bakhuis", size="7", color=DARK),
                    rx.text(
                        "Ik ben Kim Bakhuis, oorspronkelijk fysiotherapeut, maar overgestapt naar de podotherapie. Sinds 2023 ben ik eigenaar van deze praktijk. Met ruim 16 jaar ervaring in de zorg help ik mensen met hun voetklachten.",
                        line_height="1.6",
                        color="gray.600",
                        font_size="16px"
                    ),
                    rx.text(
                        "Mijn passie ligt in het bieden van persoonlijke zorg en het vinden van de juiste oplossing voor elke patiënt. Ik werk graag samen met andere zorgverleners om de beste behandeling te bieden.",
                        line_height="1.6",
                        color="gray.600",
                        font_size="16px"
                    ),
                    rx.text(
                        "Naast mijn werk in de praktijk houd ik van wandelen, hardlopen, Crossfit en duiken. Deze actieve levensstijl helpt mij ook om beter te begrijpen wat sporters en actieve mensen nodig hebben.",
                        line_height="1.6",
                        color="gray.600",
                        font_size="16px"
                    ),
                    rx.vstack(
                        rx.text("Achtergrond:", font_weight="600", color=DARK),
                        rx.text("• Oorspronkelijk fysiotherapeut", color="gray.600"),
                        rx.text("• Ruim 16 jaar ervaring in de zorg", color="gray.600"),
                        rx.text("• Eigenaar praktijk sinds 2023", color="gray.600"),
                        rx.text("• Gespecialiseerd in podotherapie", color="gray.600"),
                        spacing="2",
                        align="start",
                        width="100%"
                    ),
                    spacing="6",
                    align="start"
                ),
                columns=[1, 1, 2],
                spacing="8",
                align_items="center"
            )
        ),
        id="kim",
        bg="#f9fafb"
    )


# -----------------------------
# PAGE
# -----------------------------
def home_page() -> rx.Component:
    return rx.fragment(
        header(),
        hero_section(),
        section_who_is_voorvoet(),
        section_order_insoles(),
        section_introduction(),
        services_section(),
        kim_section(),
        contact_section(),
        footer(),
        modal(),
    )
