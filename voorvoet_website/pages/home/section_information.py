"""Information cards section displaying practice services and details."""
import reflex as rx

from ...components import container, section, information_cards_grid, CardConfig
from ...theme import Colors
from ...utils.translations import get_translation


TRANSLATIONS = {
    "nl": {
        "card1_title": "Wat doet een podotherapeut?",
        "card1_description": "Podotherapie (dus niet podologie, zie onze blog) behandelt diverse voet- en voetgerelateerde klachten die voortvloeien uit een afwijkende voetstand. Van nagelklachten tot lage rugpijn, en alles wat ertussenin zit.",
        "card1_button": "Wat doen we precies",
        "card2_title": "Veel voorkomende klachten",
        "card2_description": "Wil je weten voor welke voetklachten je het beste VoorVoet kan bezoeken?\n Op deze pagina vind je een kort overzicht voor welke klachten je bij ons aan het goede adres bent.",
        "card2_button": "Bekijk klachten",
        "card3_title": "Wat vergoedt mijn verzekering?",
        "card3_description": "We willen allemaal weten waar wij aan toe zijn. Daarom heeft VoorVoet een handig zoekbaar overzicht gemaakt om te zien op welke vergoeding je recht hebt.",
        "card3_button": "Check vergoeding",
        "card4_title": "Het behandeltraject",
        "card4_description": "Hoe ziet een bezoek bij VoorVoet er uit? Wat kan je verwachten en wat is handig om te weten. We leggen het graag aan je uit.",
        "card4_button": "Hoe gaat het in zijn werk",
        "card5_title": "Specifiek voor bedrijven",
        "card5_description": "Voor harde werkers die veel staan en lopen zijn voetklachten extra vervelend. Kijk hier voor meer informatie over wat we op het gebied van bedrijfspodotherapie kunnen betekenen.",
        "card5_button": "Voor bedrijven",
        "card6_title": "Voor wie?",
        "card6_description": "Iedereen met voet- of voetstand gerelateerde klachten is welkom. Van kinderen met doorgezakte voeten tot volwassenen en ouderen met pijnklachten of problemen met lopen.",
        "card6_button": "Therapie op maat",
    },
    "de": {
        "card1_title": "Was macht ein Podotherapeut?",
        "card1_description": "Podotherapie (also nicht Podologie, siehe unseren Blog) behandelt verschiedene Fuß- und fußbezogene Beschwerden, die aus einer abweichenden Fußstellung resultieren. Von Nagelbeschwerden bis zu Kreuzschmerzen und allem dazwischen.",
        "card1_button": "Was wir genau machen",
        "card2_title": "Häufige Beschwerden",
        "card2_description": "Möchten Sie wissen, bei welchen Fußbeschwerden Sie am besten VoorVoet besuchen können?\n Auf dieser Seite finden Sie eine kurze Übersicht, bei welchen Beschwerden Sie bei uns richtig sind.",
        "card2_button": "Beschwerden ansehen",
        "card3_title": "Was erstattet meine Versicherung?",
        "card3_description": "Wir alle möchten wissen, woran wir sind. Deshalb hat VoorVoet eine praktische durchsuchbare Übersicht erstellt, um zu sehen, auf welche Erstattung Sie Anspruch haben.",
        "card3_button": "Erstattung prüfen",
        "card4_title": "Der Behandlungsverlauf",
        "card4_description": "Wie sieht ein Besuch bei VoorVoet aus? Was können Sie erwarten und was ist wichtig zu wissen. Wir erklären es Ihnen gerne.",
        "card4_button": "Wie funktioniert es",
        "card5_title": "Speziell für Unternehmen",
        "card5_description": "Für hart arbeitende Menschen, die viel stehen und gehen, sind Fußbeschwerden besonders lästig. Schauen Sie hier für weitere Informationen darüber, was wir im Bereich der Betriebspodotherapie leisten können.",
        "card5_button": "Für Unternehmen",
        "card6_title": "Für wen?",
        "card6_description": "Jeder mit Fuß- oder fußstellungsbedingten Beschwerden ist willkommen. Von Kindern mit Plattfüßen bis zu Erwachsenen und Senioren mit Schmerzen oder Gehproblemen.",
        "card6_button": "Maßgeschneiderte Therapie",
    },
    "en": {
        "card1_title": "What does a podotherapist do?",
        "card1_description": "Podotherapy (not podiatry, see our blog) treats various foot and foot-related complaints resulting from abnormal foot position. From nail complaints to lower back pain, and everything in between.",
        "card1_button": "What we do exactly",
        "card2_title": "Common complaints",
        "card2_description": "Want to know which foot complaints are best addressed at VoorVoet?\n On this page you'll find a brief overview of which complaints we can help you with.",
        "card2_button": "View complaints",
        "card3_title": "What does my insurance cover?",
        "card3_description": "We all want to know where we stand. That's why VoorVoet has created a handy searchable overview to see what reimbursement you're entitled to.",
        "card3_button": "Check coverage",
        "card4_title": "The treatment process",
        "card4_description": "What does a visit to VoorVoet look like? What can you expect and what is important to know. We'd be happy to explain.",
        "card4_button": "How it works",
        "card5_title": "Specifically for businesses",
        "card5_description": "For hard workers who stand and walk a lot, foot complaints are especially annoying. Look here for more information about what we can do in the field of occupational podotherapy.",
        "card5_button": "For businesses",
        "card6_title": "For whom?",
        "card6_description": "Everyone with foot or foot position-related complaints is welcome. From children with flat feet to adults and elderly with pain or walking problems.",
        "card6_button": "Tailored therapy",
    },
}


def section_information() -> rx.Component:
    """
    Create the information section with service and practice detail cards.

    This section displays a grid of information cards covering:
    - What a podotherapist does
    - Common complaints treated
    - Insurance reimbursement information
    - Treatment process overview
    - Business-specific services
    - Target audience information

    Each card includes an icon, title, description, and link button.

    Returns
    -------
    rx.Component
        A section component with a responsive grid of information cards
        on a light green background with wave-style clip paths.
    """
    cards = [
        CardConfig(
            title=get_translation(TRANSLATIONS, "card1_title"),
            description=get_translation(TRANSLATIONS, "card1_description"),
            icon="fa-user-md",
            bg_color="white",
            show_box=False,
            button_text=get_translation(TRANSLATIONS, "card1_button"),
            button_link="/podotherapie"
        ),
        CardConfig(
            title=get_translation(TRANSLATIONS, "card2_title"),
            description=get_translation(TRANSLATIONS, "card2_description"),
            icon="fa-exclamation-triangle",
            bg_color="white",
            show_box=False,
            button_text=get_translation(TRANSLATIONS, "card2_button"),
            button_link="/klachten"
        ),
        CardConfig(
            title=get_translation(TRANSLATIONS, "card3_title"),
            description=get_translation(TRANSLATIONS, "card3_description"),
            icon="fa-money",
            bg_color="white",
            show_box=False,
            button_text=get_translation(TRANSLATIONS, "card3_button"),
            button_link="/verzekering"
        ),
        CardConfig(
            title=get_translation(TRANSLATIONS, "card4_title"),
            description=get_translation(TRANSLATIONS, "card4_description"),
            icon="fa-heart-o",
            bg_color="white",
            show_box=False,
            button_text=get_translation(TRANSLATIONS, "card4_button"),
            button_link="/behandeling"
        ),
        CardConfig(
            title=get_translation(TRANSLATIONS, "card5_title"),
            description=get_translation(TRANSLATIONS, "card5_description"),
            icon="fa-building-o",
            bg_color="white",
            show_box=False,
            button_text=get_translation(TRANSLATIONS, "card5_button"),
            button_link="/bedrijven"
        ),
        CardConfig(
            title=get_translation(TRANSLATIONS, "card6_title"),
            description=get_translation(TRANSLATIONS, "card6_description"),
            icon="fa-child",
            bg_color="white",
            show_box=False,
            button_text=get_translation(TRANSLATIONS, "card6_button"),
            button_link="/doelgroep"
        )
    ]

    return section(
        container(
            information_cards_grid(
                cards=cards,
                columns=[1, 2, 3],
                spacing="2rem"
            )
        ),
        id="services",
        background_color= Colors.backgrounds["green_light"],
        divider_color=Colors.backgrounds["white"],
        clip_top="gentle_4",
        clip_bottom="gentle_1"

    )
