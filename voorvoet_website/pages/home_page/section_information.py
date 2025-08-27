import reflex as rx

from ...components import container, section, information_cards_grid, CardConfig


def section_information() -> rx.Component:
    # Define card configurations
    cards = [
        CardConfig(
            title="Wat doet een podotherapeut?",
            description="Podotherapie (dus niet podologie, zie onze blog) behandelt diverse voet- en voetgerelateerde klachten die voortvloeien uit een afwijkende voetstand. Van nagelklachten tot lage rugpijn, en alles wat ertussenin zit.",
            icon="fa-user-md",
            bg_color="white",
            show_box=False,
            button_text="Wat doen we precies",
            button_link="/podotherapie"
        ),
        CardConfig(
            title="Veel voorkomende klachten",
            description="Wil je weten voor welke voetklachten je het beste VoorVoet kan bezoeken?\n Op deze pagina vind je een kort overzicht voor welke klachten je bij ons aan het goede adres bent.",
            icon="fa-exclamation-triangle",
            bg_color="white",
            show_box=False,
            button_text="Bekijk klachten",
            button_link="/klachten"
        ),
        CardConfig(
            title="Wat vergoedt mijn verzekering?",
            description="We willen allemaal weten waar wij aan toe zijn. Daarom heeft VoorVoet een handig zoekbaar overzicht gemaakt om te zien op welke vergoeding je recht hebt.",
            icon="fa-money",
            bg_color="white",
            show_box=False,
            button_text="Check vergoeding",
            button_link="/verzekering"
        ),
        CardConfig(
            title="Het behandeltraject",
            description="Hoe ziet een bezoek bij VoorVoet er uit? Wat kan je verwachten en wat is handig om te weten. We leggen het graag aan je uit.",
            icon="fa-heart-o",
            bg_color="white",
            show_box=False,
            button_text="Hoe gaat het in zijn werk",
            button_link="/behandeling"
        ),
        CardConfig(
            title="Specifiek voor bedrijven",
            description="Voor harde werkers die veel staan en lopen zijn voetklachten extra vervelend. Kijk hier voor meer informatie over wat we op het gebied van bedrijfspodotherapie kunnen betekenen.",
            icon="fa-building-o",
            bg_color="white",
            show_box=False,
            button_text="Voor bedrijven",
            button_link="/bedrijven"
        ),
        CardConfig(
            title="Voor wie?",
            description="Iedereen met voet- of voetstand gerelateerde klachten is welkom. Van kinderen met doorgezakte voeten tot volwassenen en ouderen met pijnklachten of problemen met lopen.",
            icon="fa-child",
            bg_color="white",
            show_box=False,
            button_text="Therapie op maat",
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
        alternate_bg=True
    )
