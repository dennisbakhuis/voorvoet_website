import reflex as rx

from ...components import container, section, information_card, responsive_grid


def section_information() -> rx.Component:
    return section(
        container(
            responsive_grid(
                information_card(
                    "Wat doet een podotherapeut?",
                    "Podotherapie (dus niet podologie, zie onze blog) behandelt diverse voet- en voetgerelateerde klachten die voortvloeien uit een afwijkende voetstand. Van nagelklachten tot lage rugpijn, en alles wat ertussenin zit.",
                    "fa-user-md",
                    "white",
                    show_box=False,
                    button_text="Wat doen we precies",
                    button_link="/podotherapie"
                ),
                information_card(
                    "Veel voorkomende klachten",
                    "Wil je weten voor welke voetklachten je het beste VoorVoet kan bezoeken?\n Op deze pagina vind je een kort overzicht voor welke klachten je bij ons aan het goede adres bent.",
                    "fa-exclamation-triangle",
                    "white",
                    show_box=False,
                    button_text="Bekijk klachten",
                    button_link="/klachten"
                ),
                information_card(
                    "Wat vergoedt mijn verzekering?",
                    "We willen allemaal weten waar wij aan toe zijn. Daarom heeft VoorVoet een handig zoekbaar overzicht gemaakt om te zien op welke vergoeding je recht hebt.",
                    "fa-money",
                    "white",
                    show_box=False,
                    button_text="Check vergoeding",
                    button_link="/verzekering"
                ),
                information_card(
                    "Het behandeltraject",
                    "Hoe ziet een bezoek bij VoorVoet er uit? Wat kan je verwachten en wat is handig om te weten. We leggen het graag aan je uit.",
                    "fa-heart-o",
                    "white",
                    show_box=False,
                    button_text="Hoe gaat het in zijn werk",
                    button_link="/behandeling"
                ),
                information_card(
                    "Specifiek voor bedrijven",
                    "Voor harde werkers die veel staan en lopen zijn voetklachten extra vervelend. Kijk hier voor meer informatie over wat we op het gebied van bedrijfspodotherapie kunnen betekenen.",
                    "fa-building-o",
                    "white",
                    show_box=False,
                    button_text="Voor bedrijven",
                    button_link="/bedrijven"
                ),
                information_card(
                    "Voor wie?",
                    "Iedereen met voet- of voetstand gerelateerde klachten is welkom. Van kinderen met doorgezakte voeten tot volwassenen en ouderen met pijnklachten of problemen met lopen.",
                    "fa-child",
                    "white",
                    show_box=False,
                    button_text="Therapie op maat",
                    button_link="/doelgroep"
                ),
                columns=[1, 2, 3],
                spacing="2rem",
                justify_items="center",
            )
        ),
        id="services",
        alternate_bg=True
    )
