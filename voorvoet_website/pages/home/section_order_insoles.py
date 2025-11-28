"""Order insoles section promoting extra insole purchases."""
import reflex as rx
from ...components import container, section, image_text_section, button
from ...theme import Colors
from ...utils.translations import get_translation


TRANSLATIONS = {
    "nl": {
        "title": "Extra paar podotherapeutische zolen",
        "paragraph1": "Een extra paar zolen kan handig zijn om bijvoorbeeld met een ander paar schoenen te gebruiken, bijvoorbeeld in uw sport- of wandelschoenen. Dit scheelt niet alleen gedoe met wisselen maar verlengt ook de levensduur van de zolen.",
        "paragraph2": "Een extra paar zolen kan alleen als u al eens eerder bij VoorVoet bent geweest en wij een digitale scan van de voet hebben. Als het langer dan een jaar geleden is dat u een scan van u voet heeft laten maken is het raadzaam om een controle in te plannen.",
        "button": "Bestel een extra paar",
    },
    "de": {
        "title": "Zusätzliches Paar podotherapeutische Einlagen",
        "paragraph1": "Ein zusätzliches Paar Einlagen kann praktisch sein, um sie beispielsweise mit einem anderen Paar Schuhen zu verwenden, etwa in Ihren Sport- oder Wanderschuhen. Dies erspart nicht nur den Aufwand des Wechselns, sondern verlängert auch die Lebensdauer der Einlagen.",
        "paragraph2": "Ein zusätzliches Paar Einlagen ist nur möglich, wenn Sie bereits bei VoorVoet waren und wir einen digitalen Scan Ihres Fußes haben. Wenn der Scan Ihres Fußes länger als ein Jahr zurückliegt, ist es ratsam, eine Kontrolle zu vereinbaren.",
        "button": "Bestellen Sie ein zusätzliches Paar",
    },
    "en": {
        "title": "Extra pair of podotherapeutic insoles",
        "paragraph1": "An extra pair of insoles can be handy to use with a different pair of shoes, for example in your sports or hiking shoes. This not only saves the hassle of switching but also extends the lifespan of the insoles.",
        "paragraph2": "An extra pair of insoles is only possible if you have been to VoorVoet before and we have a digital scan of your foot. If it has been longer than a year since you had a scan of your foot, it is advisable to schedule a check-up.",
        "button": "Order an extra pair",
    },
}


def section_order_insoles(language: str) -> rx.Component:
    """
    Create the section for ordering extra pairs of insoles.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")

    Returns
    -------
    rx.Component
        A section component with an image-text layout on a light green
        background, displaying shoe imagery on the right and promotional
        text on the left, with a call-to-action button.
    """
    paragraphs = [
        get_translation(TRANSLATIONS, "paragraph1", language),
        get_translation(TRANSLATIONS, "paragraph2", language)
    ]

    return section(
        container(
            image_text_section(
                image_src="/images/page_home/podoloog_enschede_outdoor_schoenen_voorvoet_praktijk_voor_podotherapie.jpg",
                title=get_translation(TRANSLATIONS, "title", language),
                paragraphs=paragraphs,
                image_position="right"
            ),
            rx.box(
                button(
                    label=get_translation(TRANSLATIONS, "button", language),
                    href="/order-insoles"
                ),
                display="flex",
                justify_content="center",
                margin_top="2rem"
            )
        ),
        id="order-insoles",
        background_color=Colors.backgrounds["green_light"],
        divider_color=Colors.backgrounds["white"],
        clip_top="gentle_2",
        clip_bottom="gentle_3"
    )
