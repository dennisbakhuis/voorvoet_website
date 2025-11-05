"""Section explaining what podiatry is and its scope."""
import reflex as rx
from ...components import container, section, image_text_section


def section_what_is_podiatry() -> rx.Component:
    """
    Create the 'What is podiatry?' explanatory section.

    Provides an overview of podiatry as a medical discipline, explaining
    what it treats (foot, knee, hip, and lower back complaints) and the
    various treatment options available (custom insoles, shoe advice,
    exercises, orthoses, nail braces, taping, etc.).

    Returns
    -------
    rx.Component
        A section component with an image-text layout explaining podiatry
        services and treatment approaches.
    """
    paragraphs = [
        "Podotherapie richt zicht op het onderzoeken en behandelen van klachten in de onderste extremiteit. Denk hierbij aan voetklachten, maar ook klachten in knieën, heupen of de lage rug. Ervaar je pijnklachten? De podotherapeut doet onderzoek de oorzaak van je pijnklachten en zoekt vervolgens naar de best passende oplossing. Dat kan een op maat gemaakte zool zijn, maar ook schoenadvies, oefeningen, een orthese, nagelbeugel of een tijdelijke behandeling zoals taping of het aanleggen van vilt. Kort gezegd, voor bijna alle klachten die voet- of voetstand gerelateerd zijn, kijkt de podotherapeut naar een passende oplossing."
    ]
    
    return section(
        container(
            image_text_section(
                image_src="/images/page_information/skelet_botjes_voet_voorvoet_praktijk_voor_podotherapie_enschede.jpg",
                title="Wat is podotherapie nou eigenlijk?",
                paragraphs=paragraphs,
                image_position="right",
                image_max_width="450px",
            )
        ),
        id="what-is-podiatry"
    )