"""Section explaining company podiatry services."""

import reflex as rx
from ...components import (
    container,
    section,
    header,
    regular_text,
    icon_list_item,
    column,
    responsive_image,
)
from ...theme import Colors, Layout, Spacing
from ...utils import get_translation


TRANSLATIONS = {
    "nl": {
        "title": "Bedrijfspodotherapie via VoorVoet podotherapie Enschede",
        "intro": "Bedrijfspodotherapie is een specifieke vorm van podotherapie die gericht is op het verbeteren van de gezondheid en het welzijn van werknemers. Het richt zich op het voorkomen en behandelen van voetklachten die ontstaan zijn door de werkomgeving, zoals bijvoorbeeld door het dragen van niet goed passende werkschoenen, het lange staan op harde ondergronden en repetitieve werkzaamheden. Ook als je voor je werk veel moet staan en lopen kan dit natuurlijk klachten geven.",
        "includes_intro": "Bedrijfspodotherapie kan worden aangeboden als onderdeel van een bedrijfsgezondheidsprogramma en omvat onder meer:",
        "item1": "Beoordeling van de werkomgeving en het werkverrichtingsproces",
        "item2": "Advies over het dragen van geschikte schoenen en indien nodig het aanmeten van steunzolen welke geschikt zijn voor het werkschoeisel. Hiervoor geldt specifiek wet- en regelgeving.",
        "item3": "Behandeling van voetklachten",
        "item4": "Oefeningen voor de voeten en het verbeteren van de houding",
        "item5": "Preventie van voetproblemen door het verbeteren van de werkomgeving en werkverrichtingsproces.",
        "conclusion": "Bedrijfspodotherapie kan helpen bij het voorkomen en behandelen van voetklachten en verminderen van het ziekteverzuim en de kosten die daarmee gepaard gaan. Het kan ook bijdragen aan het verbeteren van de productiviteit en tevredenheid van de werknemers.",
        "contact": "Neem voor meer informatie vrijblijvend contact op.",
        "image_alt": "Werknemer met pijnlijke voeten en hielpijn - bedrijfspodotherapie VoorVoet Enschede",
    },
    "de": {
        "title": "Betriebspodotherapie über VoorVoet Podotherapie Enschede",
        "intro": "Betriebspodotherapie ist eine spezifische Form der Podotherapie, die darauf abzielt, die Gesundheit und das Wohlbefinden von Mitarbeitern zu verbessern. Sie konzentriert sich auf die Vorbeugung und Behandlung von Fußbeschwerden, die durch die Arbeitsumgebung entstehen, wie zum Beispiel durch das Tragen von nicht gut passenden Arbeitsschuhen, langes Stehen auf harten Oberflächen und repetitive Tätigkeiten. Auch wenn Sie für Ihre Arbeit viel stehen und gehen müssen, kann dies natürlich Beschwerden verursachen.",
        "includes_intro": "Betriebspodotherapie kann als Teil eines betrieblichen Gesundheitsprogramms angeboten werden und umfasst unter anderem:",
        "item1": "Beurteilung der Arbeitsumgebung und des Arbeitsprozesses",
        "item2": "Beratung über das Tragen geeigneter Schuhe und bei Bedarf das Anpassen von Einlagen, die für Arbeitsschuhe geeignet sind. Hierfür gelten spezifische Gesetze und Vorschriften.",
        "item3": "Behandlung von Fußbeschwerden",
        "item4": "Übungen für die Füße und Verbesserung der Haltung",
        "item5": "Prävention von Fußproblemen durch Verbesserung der Arbeitsumgebung und des Arbeitsprozesses.",
        "conclusion": "Betriebspodotherapie kann helfen, Fußbeschwerden vorzubeugen und zu behandeln sowie Krankheitsausfälle und damit verbundene Kosten zu reduzieren. Sie kann auch zur Verbesserung der Produktivität und Zufriedenheit der Mitarbeiter beitragen.",
        "contact": "Nehmen Sie für weitere Informationen unverbindlich Kontakt auf.",
        "image_alt": "Arbeitnehmer mit schmerzenden Füßen und Fersenschmerzen - Betriebspodotherapie VoorVoet Enschede",
    },
    "en": {
        "title": "Company podotherapy via VoorVoet podotherapie Enschede",
        "intro": "Company podotherapy is a specific form of podotherapy aimed at improving the health and well-being of employees. It focuses on preventing and treating foot complaints that arise from the work environment, such as wearing poorly fitting work shoes, prolonged standing on hard surfaces and repetitive tasks. If you have to stand and walk a lot for your work, this can naturally cause complaints.",
        "includes_intro": "Company podotherapy can be offered as part of a corporate health program and includes:",
        "item1": "Assessment of the work environment and work process",
        "item2": "Advice on wearing suitable shoes and, if necessary, fitting insoles that are suitable for work shoes. Specific laws and regulations apply to this.",
        "item3": "Treatment of foot complaints",
        "item4": "Exercises for the feet and improving posture",
        "item5": "Prevention of foot problems by improving the work environment and work process.",
        "conclusion": "Company podotherapy can help prevent and treat foot complaints and reduce absenteeism and associated costs. It can also contribute to improving employee productivity and satisfaction.",
        "contact": "Please contact us for more information without obligation.",
        "image_alt": "Employee with painful feet and heel pain - company podotherapy VoorVoet Enschede",
    },
}


def section_bedrijfspodotherapie(language: str) -> rx.Component:
    """
    Create the company podiatry section.

    Explains bedrijfspodotherapie (company/workplace podiatry) as a
    specialized form of podiatry focused on preventing and treating foot
    complaints arising from work environments. Details services including
    workplace assessments, footwear advice, custom work insoles, treatment,
    exercises, and preventive measures to reduce absenteeism and improve
    employee productivity.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")

    Returns
    -------
    rx.Component
        A section component with green background containing detailed
        information about company podiatry services and benefits.
    """
    image_column = column(
        responsive_image(
            src=[
                "/images/page_information/bedrijfs_podotherapie_pijnlijke_voeten_hielpijn_voorvoet_podotherapie_enschede.avif",
                "/images/page_information/bedrijfs_podotherapie_pijnlijke_voeten_hielpijn_voorvoet_podotherapie_enschede.webp",
                "/images/page_information/bedrijfs_podotherapie_pijnlijke_voeten_hielpijn_voorvoet_podotherapie_enschede.jpg",
            ],
            alt=get_translation(TRANSLATIONS, "image_alt", language),
            width="100%",
            max_width="450px",
            height="auto",
            border_radius=Layout.image_border_radius,
            box_shadow=Layout.image_box_shadow,
            loading="lazy",
        ),
        size=Layout.image_column_size,
        padding_right=Spacing.responsive_2rem_right,
        display="flex",
        justify_content="center",
        align_items="center",
        margin_bottom=Spacing.image_margin_bottom,
        order=["1", "1", "1", "1"],
    )

    text_column = column(
        header(
            get_translation(TRANSLATIONS, "title", language),
            level=2,
            margin_bottom=Spacing.text_margin_bottom,
        ),
        regular_text(
            get_translation(TRANSLATIONS, "intro", language),
            text_align="left",
            margin_bottom="1.5rem",
            color=Colors.text["content"],
        ),
        regular_text(
            get_translation(TRANSLATIONS, "includes_intro", language),
            text_align="left",
            margin_bottom="1rem",
            color=Colors.text["content"],
        ),
        rx.vstack(
            icon_list_item(
                "fa-solid fa-circle", get_translation(TRANSLATIONS, "item1", language)
            ),
            icon_list_item(
                "fa-solid fa-circle", get_translation(TRANSLATIONS, "item2", language)
            ),
            icon_list_item(
                "fa-solid fa-circle", get_translation(TRANSLATIONS, "item3", language)
            ),
            icon_list_item(
                "fa-solid fa-circle", get_translation(TRANSLATIONS, "item4", language)
            ),
            icon_list_item(
                "fa-solid fa-circle", get_translation(TRANSLATIONS, "item5", language)
            ),
            gap="0.5rem",
            align="start",
            width="100%",
            padding_left="1.5rem",
        ),
        regular_text(
            get_translation(TRANSLATIONS, "conclusion", language),
            text_align="left",
            margin_bottom="1rem",
            margin_top="1.5rem",
            color=Colors.text["content"],
        ),
        regular_text(
            get_translation(TRANSLATIONS, "contact", language),
            text_align="left",
            color=Colors.text["content"],
        ),
        size=Layout.text_column_size,
        padding_left=Spacing.responsive_2rem_left,
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
