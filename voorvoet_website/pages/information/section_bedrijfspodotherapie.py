# Section "Bedrijfspodotherapie" on the information page
import reflex as rx
from ...components import container, section, section_title, regular_text, icon_list_item, column
from ...theme import Colors, Layout, Spacing


def section_bedrijfspodotherapie() -> rx.Component:
    # Create image column (left side)
    image_column = column(
        rx.image(
            src="/images/page_information/bedrijfs_podotherapie_pijnlijke_voeten_hielpijn_voorvoet_podotherapie_enschede.jpg",
            width="100%",
            max_width="450px",
            height="auto",
            border_radius=Layout.image_border_radius,
            box_shadow=Layout.image_box_shadow,
        ),
        size=Layout.image_column_size,
        padding_right=["0", "0", "0", "2rem"],
        display="flex",
        justify_content="center",
        align_items="center",
        margin_bottom=Spacing.image_margin_bottom,
        order=["1", "1", "1", "1"],
    )
    
    # Create text column (right side)
    text_column = column(
        section_title("Bedrijfspodotherapie via VoorVoet podotherapie Enschede", margin_bottom=Spacing.text_margin_bottom),
        regular_text(
            "Bedrijfspodotherapie is een specifieke vorm van podotherapie die gericht is op het verbeteren van de gezondheid en het welzijn van werknemers. Het richt zich op het voorkomen en behandelen van voetklachten die ontstaan zijn door de werkomgeving, zoals bijvoorbeeld door het dragen van niet goed passende werkschoenen, het lange staan op harde ondergronden en repetitieve werkzaamheden. Ook als je voor je werk veel moet staan en lopen kan dit natuurlijk klachten geven.",
            text_align="left",
            margin_bottom="1.5rem",
            color=Colors.text["content"],
        ),
        regular_text(
            "Bedrijfspodotherapie kan worden aangeboden als onderdeel van een bedrijfsgezondheidsprogramma en omvat onder meer:",
            text_align="left",
            margin_bottom="1rem",
            color=Colors.text["content"],
        ),
        rx.vstack(
            icon_list_item("fa-solid fa-circle", "Beoordeling van de werkomgeving en het werkverrichtingsproces"),
            icon_list_item("fa-solid fa-circle", "Advies over het dragen van geschikte schoenen en indien nodig het aanmeten van steunzolen welke geschikt zijn voor het werkschoeisel. Hiervoor geldt specifiek wet- en regelgeving."),
            icon_list_item("fa-solid fa-circle", "Behandeling van voetklachten"),
            icon_list_item("fa-solid fa-circle", "Oefeningen voor de voeten en het verbeteren van de houding"),
            icon_list_item("fa-solid fa-circle", "Preventie van voetproblemen door het verbeteren van de werkomgeving en werkverrichtingsproces."),
            gap="0.5rem",
            align="start",
            width="100%",
            margin_left="1.5rem",
        ),
        regular_text(
            "Bedrijfspodotherapie kan helpen bij het voorkomen en behandelen van voetklachten en verminderen van het ziekteverzuim en de kosten die daarmee gepaard gaan. Het kan ook bijdragen aan het verbeteren van de productiviteit en tevredenheid van de werknemers.",
            text_align="left",
            margin_bottom="1rem",
            margin_top="1.5rem",
            color=Colors.text["content"],
        ),
        regular_text(
            "Neem voor meer informatie vrijblijvend contact op.",
            text_align="left",
            color=Colors.text["content"],
        ),
        size=Layout.text_column_size,
        padding_left=["0", "0", "0", "2rem"],
        order=["2", "2", "2", "2"],
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
        background=Colors.backgrounds["green_light"],
        divider_color=Colors.backgrounds["white"],
        clip_top="gentle_2",
        clip_bottom="gentle_3",
        id="bedrijfspodotherapie",
    )