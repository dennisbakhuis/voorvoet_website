"""Section explaining what podiatry is and its scope."""
import reflex as rx
from ...components import container, section, image_text_section
from ...utils.translations import get_translation


TRANSLATIONS = {
    "nl": {
        "title": "Wat is podotherapie nou eigenlijk?",
        "paragraph1": "Podotherapie richt zicht op het onderzoeken en behandelen van klachten in de onderste extremiteit. Denk hierbij aan voetklachten, maar ook klachten in knieën, heupen of de lage rug. Ervaar je pijnklachten? De podotherapeut doet onderzoek de oorzaak van je pijnklachten en zoekt vervolgens naar de best passende oplossing. Dat kan een op maat gemaakte zool zijn, maar ook schoenadvies, oefeningen, een orthese, nagelbeugel of een tijdelijke behandeling zoals taping of het aanleggen van vilt. Kort gezegd, voor bijna alle klachten die voet- of voetstand gerelateerd zijn, kijkt de podotherapeut naar een passende oplossing.",
    },
    "de": {
        "title": "Was ist Podotherapie eigentlich?",
        "paragraph1": "Podotherapie konzentriert sich auf die Untersuchung und Behandlung von Beschwerden in den unteren Extremitäten. Denken Sie dabei an Fußbeschwerden, aber auch an Beschwerden in Knien, Hüften oder im unteren Rücken. Haben Sie Schmerzen? Der Podotherapeut untersucht die Ursache Ihrer Schmerzen und sucht dann nach der am besten geeigneten Lösung. Das kann eine maßgefertigte Einlage sein, aber auch Schuhberatung, Übungen, eine Orthese, eine Nagelspange oder eine temporäre Behandlung wie Taping oder das Anlegen von Filz. Kurz gesagt, für fast alle Beschwerden, die mit den Füßen oder der Fußstellung zusammenhängen, sucht der Podotherapeut nach einer passenden Lösung.",
    },
    "en": {
        "title": "What is podotherapy actually?",
        "paragraph1": "Podotherapy focuses on examining and treating complaints in the lower extremities. Think of foot complaints, but also complaints in knees, hips or the lower back. Do you experience pain? The podotherapist investigates the cause of your pain and then looks for the most suitable solution. This can be a custom-made insole, but also shoe advice, exercises, an orthosis, nail brace or a temporary treatment such as taping or applying felt. In short, for almost all complaints that are foot or foot position related, the podotherapist looks for a suitable solution.",
    },
}


def section_what_is_podiatry(language: str) -> rx.Component:
    """
    Create the 'What is podiatry?' explanatory section.

    Provides an overview of podiatry as a medical discipline, explaining
    what it treats (foot, knee, hip, and lower back complaints) and the
    various treatment options available (custom insoles, shoe advice,
    exercises, orthoses, nail braces, taping, etc.).

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")

    Returns
    -------
    rx.Component
        A section component with an image-text layout explaining podiatry
        services and treatment approaches.
    """
    paragraphs = [
        get_translation(TRANSLATIONS, "paragraph1", language)
    ]

    return section(
        container(
            image_text_section(
                image_src="/images/page_information/skelet_botjes_voet_voorvoet_praktijk_voor_podotherapie_enschede.jpg",
                title=get_translation(TRANSLATIONS, "title", language),
                paragraphs=paragraphs,
                image_position="right",
                image_max_width="450px",
            )
        ),
        id="what-is-podiatry"
    )