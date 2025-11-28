"""Introduction section with personal story from the practice owner."""
import reflex as rx
from ...components import container, section, image_text_section
from ...utils.get_translation import get_translation


TRANSLATIONS = {
    "nl": {
        "title": "Even voorstellen",
        "paragraph1": "Mijn naam is Kim Bakhuis, podotherapeut en eigenaar van VoorVoet. In 2004 studeerde ik af als fysiotherapeut en na 3 jaar kwam ik in aanraking met podotherapie. Dit vak sprak me zo aan dat ik besloot me te laten omscholen. Inmiddels heb ik ruim 16 jaar werkervaring opgedaan in dit mooie vak. De laatste jaren kriebelde het en heb ik besloten om in 2023 mijn eigen praktijk op te zetten.",
        "paragraph2": "Door mijn vooropleiding, verschillende scholingen en jarenlange ervaring heb ik een brede kijk op voet- en voetgerelateerde problemen. Het is belangrijk om me goed in te kunnen leven en mijn uiterste best te doen om je zo goed mogelijk te helpen met jouw hulpvraag. Dat kan in de vorm van advies, behandeling en waar nodig de vervaardiging van ortheses, nagelbeugels of steunzolen. Vanuit mijn praktische instelling werk ik graag samen met andere disciplines om het beste resultaat voor jou te boeken. Privé ben ik een erg actief persoon die houdt van wandelen, hardlopen en Crossfit. Daarnaast daag ik mijzelf graag uit door (grot)duiken en speleo tripjes.",
    },
    "de": {
        "title": "Kurz vorgestellt",
        "paragraph1": "Mein Name ist Kim Bakhuis, Podotherapeutin und Inhaberin von VoorVoet. 2004 habe ich mein Studium als Physiotherapeutin abgeschlossen und kam nach 3 Jahren mit Podotherapie in Kontakt. Dieses Fach sprach mich so an, dass ich beschloss, mich umschulen zu lassen. Mittlerweile habe ich mehr als 16 Jahre Berufserfahrung in diesem schönen Beruf gesammelt. In den letzten Jahren hat es mich gereizt und ich habe beschlossen, 2023 meine eigene Praxis zu eröffnen.",
        "paragraph2": "Durch meine Grundausbildung, verschiedene Schulungen und langjährige Erfahrung habe ich einen breiten Blick auf Fuß- und fußbezogene Probleme. Es ist wichtig, mich gut hineinversetzen zu können und mein Bestes zu tun, um Ihnen bei Ihrer Hilfsanfrage bestmöglich zu helfen. Das kann in Form von Beratung, Behandlung und gegebenenfalls der Anfertigung von Orthesen, Nagelspangen oder Einlagen sein. Mit meiner praktischen Einstellung arbeite ich gerne mit anderen Disziplinen zusammen, um das beste Ergebnis für Sie zu erzielen. Privat bin ich eine sehr aktive Person, die gerne wandert, läuft und Crossfit macht. Außerdem fordere ich mich gerne durch (Höhlen-)Tauchen und Speleo-Trips heraus.",
    },
    "en": {
        "title": "Let me introduce myself",
        "paragraph1": "My name is Kim Bakhuis, podotherapist and owner of VoorVoet. In 2004 I graduated as a physiotherapist and after 3 years I came into contact with podotherapy. This profession appealed to me so much that I decided to retrain. I now have more than 16 years of work experience in this beautiful profession. In recent years I felt the urge and decided to set up my own practice in 2023.",
        "paragraph2": "Through my prior education, various training courses and years of experience, I have a broad view of foot and foot-related problems. It is important to be able to empathize well and do my utmost to help you as best as possible with your request for help. This can be in the form of advice, treatment and, where necessary, the manufacture of orthoses, nail braces or insoles. From my practical attitude, I like to work together with other disciplines to achieve the best result for you. In my private life, I am a very active person who enjoys hiking, running and Crossfit. I also like to challenge myself through cave diving and speleology trips.",
    },
}


def section_introduction(language: str) -> rx.Component:
    """
    Create the introduction section with owner's personal story.

    This section features an image-text layout introducing Kim Bakhuis,
    the podotherapist and owner of VoorVoet. It describes her background,
    qualifications, approach to patient care, and personal interests.

    Parameters
    ----------
    language : str
        The language code for translations (e.g., 'nl', 'de', 'en').

    Returns
    -------
    rx.Component
        A section component with an image-text layout displaying the
        owner's photo on the left and biographical text on the right.
    """
    paragraphs = [
        get_translation(TRANSLATIONS, "paragraph1", language),
        get_translation(TRANSLATIONS, "paragraph2", language)
    ]

    return section(
        container(
            image_text_section(
                image_src="/images/page_home/podotherapeut_enschede_kim_bakhuis_loopt_op_strand_voorvoet_praktijk_voor_podotherapie.jpg",
                title=get_translation(TRANSLATIONS, "title", language),
                paragraphs=paragraphs,
                image_position="left"
            )
        ),
        id="introduction"
    )
