# Section "Veel voorkomende klachten" on the information page
import reflex as rx
from typing import Optional
from ...components import container, section, section_title, regular_text, icon_list_item, column
from ...theme import Colors, Layout, Spacing, responsive_padding


def section_veel_voorkomende_klachten() -> rx.Component:
    # Create image column
    image_column = column(
        rx.image(
            src="/images/page_information/anatomie-voet-hielpijn_voorvoet_podotherapie_enschede.jpg",
            width="100%",
            max_width="450px",
            height="auto",
            border_radius=Layout.image_border_radius,
            box_shadow=Layout.image_box_shadow,
        ),
        size=Layout.image_column_size,
        display="flex",
        justify_content="center",
        align_items="center",
        margin_bottom=Spacing.image_margin_bottom,
        order=["1", "1", "1", "2"],
    )
    
    # Create text column with title, paragraph, and bullet list
    text_column = column(
        section_title("Veel voorkomende klachten", margin_bottom=Spacing.text_margin_bottom),
        regular_text(
            "Hieronder staat een algemene lijst van klachten die veel voorkomen in de praktijk. Neem bij twijfel of vragen gerust contact op.",
            text_align="left",
            margin_bottom="1.5rem",
            color=Colors.text["content"],
        ),
        rx.vstack(
            icon_list_item("fa-solid fa-circle", "Pijn in de voeten, hielpijn, voorvoetklachten, enkelklachten, peesontstekingen, overmatige eeltvorming of likdoorns, ingegroeide teennagels."),
            icon_list_item("fa-solid fa-circle", "Voetafwijkingen zoals platvoeten, holvoeten, doorgezakte (voor)voeten, hamer- of klauwtenen."),
            icon_list_item("fa-solid fa-circle", "Pijn in de onderbenen, knieën, heupen of rug die veroorzaakt wordt door problemen met de voeten of een afwijkende voetstand."),
            icon_list_item("fa-solid fa-circle", "Vermoeide of pijnlijke voeten en/of benen na lang staan of lopen."),
            icon_list_item("fa-solid fa-circle", "Peesontstekingen en verrekkingen."),
            icon_list_item("fa-solid fa-circle", "Klachten als gevolg van diabetes, reuma of andere aandoeningen die invloed hebben op de voeten."),
            icon_list_item("fa-solid fa-circle", "Pijn of ongemak tijdens het lopen of sporten."),
            gap="0.5rem",
            align="start",
            width="100%",
            margin_left="1.5rem",
        ),
        size=Layout.text_column_size,
        order=["2", "2", "2", "1"],
        display="flex",
        flex_direction="column",
        justify_content="center",
    )
    
    return section(
        container(
            rx.box(
                image_column,
                text_column,
                display=Layout.responsive_flex,
                gap=Spacing.section_gap,
                align_items="center",
            )
        ),
        padding_top="2rem",
        id="veel-voorkomende-klachten"
    )