"""Section listing common foot and related complaints."""
import reflex as rx
from ...components import container, section, section_title, regular_text, icon_list_item, column
from ...theme import Colors, Layout, Spacing
from ...utils.get_translation import get_translation


TRANSLATIONS = {
    "nl": {
        "title": "Veel voorkomende klachten",
        "intro": "Hieronder staat een algemene lijst van klachten die veel voorkomen in de praktijk. Neem bij twijfel of vragen gerust contact op.",
        "item1": "Pijn in de voeten, hielpijn, voorvoetklachten, enkelklachten, peesontstekingen, overmatige eeltvorming of likdoorns, ingegroeide teennagels.",
        "item2": "Voetafwijkingen zoals platvoeten, holvoeten, doorgezakte (voor)voeten, hamer- of klauwtenen.",
        "item3": "Pijn in de onderbenen, knieën, heupen of rug die veroorzaakt wordt door problemen met de voeten of een afwijkende voetstand.",
        "item4": "Vermoeide of pijnlijke voeten en/of benen na lang staan of lopen.",
        "item5": "Peesontstekingen en verrekkingen.",
        "item6": "Klachten als gevolg van diabetes, reuma of andere aandoeningen die invloed hebben op de voeten.",
        "item7": "Pijn of ongemak tijdens het lopen of sporten.",
    },
    "de": {
        "title": "Häufige Beschwerden",
        "intro": "Unten finden Sie eine allgemeine Liste von Beschwerden, die in der Praxis häufig vorkommen. Nehmen Sie bei Zweifeln oder Fragen gerne Kontakt auf.",
        "item1": "Schmerzen in den Füßen, Fersenschmerzen, Vorfußbeschwerden, Knöchelbeschwerden, Sehnenentzündungen, übermäßige Hornhautbildung oder Hühneraugen, eingewachsene Zehennägel.",
        "item2": "Fußfehlstellungen wie Plattfüße, Hohlfüße, abgesackte (Vor-)Füße, Hammer- oder Krallenzehen.",
        "item3": "Schmerzen in den Unterschenkeln, Knien, Hüften oder im Rücken, die durch Fußprobleme oder eine abweichende Fußstellung verursacht werden.",
        "item4": "Müde oder schmerzende Füße und/oder Beine nach langem Stehen oder Gehen.",
        "item5": "Sehnenentzündungen und Zerrungen.",
        "item6": "Beschwerden als Folge von Diabetes, Rheuma oder anderen Erkrankungen, die die Füße beeinflussen.",
        "item7": "Schmerzen oder Unbehagen beim Gehen oder Sport.",
    },
    "en": {
        "title": "Common complaints",
        "intro": "Below is a general list of complaints that are common in practice. Please feel free to contact us if you have any doubts or questions.",
        "item1": "Pain in the feet, heel pain, forefoot complaints, ankle complaints, tendon inflammations, excessive callus formation or corns, ingrown toenails.",
        "item2": "Foot deformities such as flat feet, hollow feet, collapsed (fore)feet, hammer or claw toes.",
        "item3": "Pain in the lower legs, knees, hips or back caused by problems with the feet or an abnormal foot position.",
        "item4": "Tired or painful feet and/or legs after standing or walking for a long time.",
        "item5": "Tendon inflammations and strains.",
        "item6": "Complaints as a result of diabetes, rheumatism or other conditions that affect the feet.",
        "item7": "Pain or discomfort during walking or sports.",
    },
}


def section_veel_voorkomende_klachten(language: str) -> rx.Component:
    """
    Create the common complaints section.

    Lists frequently encountered complaints in podiatry practice including
    foot pain, heel pain, forefoot complaints, ankle issues, tendon
    inflammations, calluses, ingrown toenails, foot deformities, and
    related pain in legs, knees, hips, or back caused by foot problems.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")

    Returns
    -------
    rx.Component
        A section component with an image-text layout displaying common
        complaints that can be treated with podiatry.
    """
    image_column = column(
        rx.image(
            src="/images/page_information/anatomie-voet-hielpijn_voorvoet_podotherapie_enschede.jpg",
            width="100%",
            max_width="450px",
            height="auto",
            border_radius=Layout.image_border_radius,
            box_shadow=Layout.image_box_shadow,
            loading="lazy",
        ),
        size=Layout.image_column_size,
        display="flex",
        justify_content="center",
        align_items="center",
        margin_bottom=Spacing.image_margin_bottom,
        order=["1", "1", "1", "2"],
    )

    text_column = column(
        section_title(get_translation(TRANSLATIONS, "title", language), margin_bottom=Spacing.text_margin_bottom),
        regular_text(
            get_translation(TRANSLATIONS, "intro", language),
            text_align="left",
            margin_bottom="1.5rem",
            color=Colors.text["content"],
        ),
        rx.vstack(
            icon_list_item("fa-solid fa-circle", get_translation(TRANSLATIONS, "item1", language)),
            icon_list_item("fa-solid fa-circle", get_translation(TRANSLATIONS, "item2", language)),
            icon_list_item("fa-solid fa-circle", get_translation(TRANSLATIONS, "item3", language)),
            icon_list_item("fa-solid fa-circle", get_translation(TRANSLATIONS, "item4", language)),
            icon_list_item("fa-solid fa-circle", get_translation(TRANSLATIONS, "item5", language)),
            icon_list_item("fa-solid fa-circle", get_translation(TRANSLATIONS, "item6", language)),
            icon_list_item("fa-solid fa-circle", get_translation(TRANSLATIONS, "item7", language)),
            gap="0.5rem",
            align="start",
            width="100%",
            padding_left="1.5rem",
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
