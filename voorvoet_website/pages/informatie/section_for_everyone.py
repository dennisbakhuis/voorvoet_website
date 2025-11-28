"""Section explaining podiatry services for different age groups."""
import reflex as rx
from ...components import container, section, section_title, section_sub_title, regular_text, centered_image, icon_list_item
from ...theme import Colors
from ...utils.get_translations import get_translation


TRANSLATIONS = {
    "nl": {
        "main_title": "Podotherapie is voor iedereen",
        "main_intro": "In iedere leeftijdscategorie kan je te maken krijgen met andere klachten. Dit kan te maken hebben met de ontwikkeling bij kinderen en het veranderen van je lijf als je ouder wordt. Dus iedereen kan terecht bij VoorVoet Podotherapie Enschede.",
        "children_title": "Podotherapie bij kinderen",
        "children_intro": "Podotherapie kan helpen bij het verbeteren van de beweeglijkheid en het functioneren van de voeten bij kinderen, wat bijdraagt aan hun algehele gezondheid en welzijn. Het is belangrijk om op tijd te beginnen met podotherapie als uw kind last heeft van voetproblemen, zodat eventuele aandoeningen kunnen worden behandeld en voorkomen dat ze verergeren.",
        "children_can_benefit": "Kinderen kunnen baat hebben bij podotherapie als ze:",
        "children_item1": "Problemen hebben met lopen, rennen of springen",
        "children_item2": "Pijn of ongemak in de voeten, benen, knieën of rug ervaren",
        "children_item3": "Zich snel moe voelen tijdens het spelen",
        "children_item4": "Afwijkingen van de benen of voeten hebben, zoals X-benen of O-benen",
        "children_item5": "Schoenen snel en overmatig afslijten",
        "athletes_title": "Podotherapie bij sporters en actievelingen",
        "athletes_intro": "VoorVoet Podotherapie Enschede kan voor sporters een oplossing bieden. Sporters kunnen last hebben van voetproblemen als gevolg van de vele uren die ze doorbrengen met wandelen, hardlopen, springen, rennen en andere fysieke activiteiten. Veel voorkomende voetklachten bij actieve mensen zijn onder andere:",
        "athletes_item1": "Overbelasting van de voeten, waardoor ontstekingen, drukproblemen, blaren of wonden ontstaan.",
        "athletes_item2": "Verstuikingen of verrekkingen van de voeten.",
        "athletes_item3": "Stressfracturen, veroorzaakt door het herhaaldelijk belasten van de voeten.",
        "athletes_item4": "Verminderde beweeglijkheid van de enkels en voeten, wat de prestaties kan beïnvloeden.",
        "athletes_conclusion": "Podotherapie kan sporters en actievelingen helpen bij het voorkomen en behandelen van voetproblemen, door het verbeteren van de beweeglijkheid, het waar nodig aanpassen van de schoenen en/of het geven van oefeningen. Podotherapeuten kunnen ook specifieke inlegzolen of andere hulpmiddelen adviseren en vervaardigen die de prestaties kunnen verbeteren en de kans op blessures kunnen verkleinen. Door de juiste zorg en adviezen kan de podotherapeut ervoor zorgen dat je fit en actief kan blijven.",
        "elderly_title": "Podotherapie bij ouderen",
        "elderly_intro": "Ook als oudere kan je terecht bij VoorVoet Podotherapie Enschede. Met het ouder worden kunnen er veranderingen optreden in de voeten, waaronder bijvoorbeeld:",
        "elderly_item1": "Dunner wordend weefsel, waardoor de voeten gevoeliger worden.",
        "elderly_item2": "Verlies van elastische veerkracht, waardoor de voeten moeilijker kunnen reageren op belasting",
        "elderly_item3": "Osteoporose, wat bijdraagt aan het risico op fracturen in de voeten",
        "elderly_item4": "Diabetes, reuma, artritis en andere (chronische) aandoeningen die invloed kunnen hebben op het functioneren van de voeten, en het verzorgen van de voeten bemoeilijkt. Dit vormt een extra risico voor het ontstaan van voetproblemen.",
        "elderly_conclusion": "Podotherapie kan helpen bij het optimaliseren van de druk en ondersteuning onder de voeten zodat er minder pijnklachten ontstaan. Hierdoor kan je comfortabeler en veiliger bewegen, wat de kans op vallen verkleint. Het is belangrijk om op tijd hulp te zoeken bij voetproblemen, zodat eventuele aandoeningen en pijnklachten op tijd worden behandeld en de kwaliteit van leven wordt verbeterd.",
    },
    "de": {
        "main_title": "Podotherapie ist für jeden",
        "main_intro": "In jeder Altersgruppe kann man mit anderen Beschwerden konfrontiert werden. Dies kann mit der Entwicklung bei Kindern und den Veränderungen des Körpers mit zunehmendem Alter zusammenhängen. Daher kann jeder zu VoorVoet Podotherapie Enschede kommen.",
        "children_title": "Podotherapie bei Kindern",
        "children_intro": "Podotherapie kann helfen, die Beweglichkeit und Funktion der Füße bei Kindern zu verbessern, was zu ihrer allgemeinen Gesundheit und ihrem Wohlbefinden beiträgt. Es ist wichtig, rechtzeitig mit der Podotherapie zu beginnen, wenn Ihr Kind Fußprobleme hat, damit eventuelle Beschwerden behandelt und verschlimmert werden können.",
        "children_can_benefit": "Kinder können von Podotherapie profitieren, wenn sie:",
        "children_item1": "Probleme beim Gehen, Laufen oder Springen haben",
        "children_item2": "Schmerzen oder Unbehagen in Füßen, Beinen, Knien oder Rücken verspüren",
        "children_item3": "Sich beim Spielen schnell müde fühlen",
        "children_item4": "Abweichungen der Beine oder Füße haben, wie X-Beine oder O-Beine",
        "children_item5": "Schuhe schnell und übermäßig abnutzen",
        "athletes_title": "Podotherapie bei Sportlern und Aktiven",
        "athletes_intro": "VoorVoet Podotherapie Enschede kann für Sportler eine Lösung bieten. Sportler können Fußprobleme haben, die durch die vielen Stunden entstehen, die sie mit Wandern, Laufen, Springen, Rennen und anderen körperlichen Aktivitäten verbringen. Häufige Fußbeschwerden bei aktiven Menschen sind unter anderem:",
        "athletes_item1": "Überlastung der Füße, die zu Entzündungen, Druckproblemen, Blasen oder Wunden führt.",
        "athletes_item2": "Verstauchungen oder Zerrungen der Füße.",
        "athletes_item3": "Stressfrakturen, verursacht durch wiederholte Belastung der Füße.",
        "athletes_item4": "Verminderte Beweglichkeit der Knöchel und Füße, was die Leistung beeinträchtigen kann.",
        "athletes_conclusion": "Podotherapie kann Sportlern und Aktiven helfen, Fußprobleme zu verhindern und zu behandeln, indem sie die Beweglichkeit verbessert, die Schuhe bei Bedarf anpasst und/oder Übungen gibt. Podotherapeuten können auch spezifische Einlagen oder andere Hilfsmittel empfehlen und anfertigen, die die Leistung verbessern und das Verletzungsrisiko verringern können. Durch die richtige Pflege und Beratung kann der Podotherapeut dafür sorgen, dass Sie fit und aktiv bleiben können.",
        "elderly_title": "Podotherapie bei Senioren",
        "elderly_intro": "Auch als ältere Person können Sie zu VoorVoet Podotherapie Enschede kommen. Mit zunehmendem Alter können Veränderungen an den Füßen auftreten, darunter zum Beispiel:",
        "elderly_item1": "Dünner werdendes Gewebe, wodurch die Füße empfindlicher werden.",
        "elderly_item2": "Verlust der elastischen Spannkraft, wodurch die Füße schwerer auf Belastung reagieren können",
        "elderly_item3": "Osteoporose, was das Risiko für Frakturen in den Füßen erhöht",
        "elderly_item4": "Diabetes, Rheuma, Arthritis und andere (chronische) Erkrankungen, die die Funktion der Füße beeinflussen und die Pflege der Füße erschweren können. Dies stellt ein zusätzliches Risiko für die Entstehung von Fußproblemen dar.",
        "elderly_conclusion": "Podotherapie kann helfen, den Druck und die Unterstützung unter den Füßen zu optimieren, sodass weniger Schmerzen entstehen. Dadurch können Sie sich komfortabler und sicherer bewegen, was das Sturzrisiko verringert. Es ist wichtig, rechtzeitig Hilfe bei Fußproblemen zu suchen, damit eventuelle Beschwerden und Schmerzen rechtzeitig behandelt werden und die Lebensqualität verbessert wird.",
    },
    "en": {
        "main_title": "Podotherapy is for everyone",
        "main_intro": "In every age category you can encounter different complaints. This can be related to development in children and changes in your body as you get older. So everyone can come to VoorVoet Podotherapie Enschede.",
        "children_title": "Podotherapy for children",
        "children_intro": "Podotherapy can help improve the mobility and functioning of children's feet, which contributes to their overall health and well-being. It is important to start podotherapy in time if your child has foot problems, so that any conditions can be treated and prevented from worsening.",
        "children_can_benefit": "Children can benefit from podotherapy if they:",
        "children_item1": "Have problems with walking, running or jumping",
        "children_item2": "Experience pain or discomfort in the feet, legs, knees or back",
        "children_item3": "Tire quickly during play",
        "children_item4": "Have abnormalities of the legs or feet, such as knock knees or bow legs",
        "children_item5": "Wear out shoes quickly and excessively",
        "athletes_title": "Podotherapy for athletes and active people",
        "athletes_intro": "VoorVoet Podotherapie Enschede can provide a solution for athletes. Athletes can suffer from foot problems as a result of the many hours they spend hiking, running, jumping, running and other physical activities. Common foot complaints among active people include:",
        "athletes_item1": "Overload of the feet, causing inflammations, pressure problems, blisters or wounds.",
        "athletes_item2": "Sprains or strains of the feet.",
        "athletes_item3": "Stress fractures, caused by repeatedly loading the feet.",
        "athletes_item4": "Reduced mobility of the ankles and feet, which can affect performance.",
        "athletes_conclusion": "Podotherapy can help athletes and active people prevent and treat foot problems by improving mobility, adjusting shoes where necessary and/or providing exercises. Podotherapists can also advise and manufacture specific insoles or other aids that can improve performance and reduce the risk of injuries. Through proper care and advice, the podotherapist can ensure that you can stay fit and active.",
        "elderly_title": "Podotherapy for the elderly",
        "elderly_intro": "As an elderly person, you can also come to VoorVoet Podotherapie Enschede. As you get older, changes can occur in the feet, including:",
        "elderly_item1": "Thinning tissue, making the feet more sensitive.",
        "elderly_item2": "Loss of elastic resilience, making it harder for the feet to respond to load",
        "elderly_item3": "Osteoporosis, which contributes to the risk of fractures in the feet",
        "elderly_item4": "Diabetes, rheumatism, arthritis and other (chronic) conditions that can affect the functioning of the feet and make foot care more difficult. This poses an additional risk for the development of foot problems.",
        "elderly_conclusion": "Podotherapy can help optimize the pressure and support under the feet so that fewer pain complaints occur. This allows you to move more comfortably and safely, which reduces the risk of falling. It is important to seek help for foot problems in time, so that any conditions and pain complaints are treated in time and quality of life is improved.",
    },
}


def section_for_everyone(language: str) -> rx.Component:
    """
    Create the 'Podiatry is for everyone' section.

    Explains how podiatry can help people of all ages including children,
    athletes/active individuals, and elderly patients. Each subsection
    details specific complaints and how podiatry addresses them for that
    demographic group.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")

    Returns
    -------
    rx.Component
        A section component with green background containing subsections
        for children, athletes, and elderly patients with relevant
        information and visual examples.
    """
    return section(
        container(
            rx.vstack(
                section_title(get_translation(TRANSLATIONS, "main_title", language)),
                regular_text(
                    get_translation(TRANSLATIONS, "main_intro", language),
                    color=Colors.text["content"],
                ),

                section_sub_title(get_translation(TRANSLATIONS, "children_title", language)),
                regular_text(
                    get_translation(TRANSLATIONS, "children_intro", language),
                    color=Colors.text["content"],
                ),
                regular_text(get_translation(TRANSLATIONS, "children_can_benefit", language), color=Colors.text["content"]),
                rx.vstack(
                    icon_list_item("fa-solid fa-circle", get_translation(TRANSLATIONS, "children_item1", language)),
                    icon_list_item("fa-solid fa-circle", get_translation(TRANSLATIONS, "children_item2", language)),
                    icon_list_item("fa-solid fa-circle", get_translation(TRANSLATIONS, "children_item3", language)),
                    icon_list_item("fa-solid fa-circle", get_translation(TRANSLATIONS, "children_item4", language)),
                    icon_list_item("fa-solid fa-circle", get_translation(TRANSLATIONS, "children_item5", language)),
                    gap="0.5rem",
                    align="start",
                    width="100%",
                    padding_left="1.5rem",
                ),

                rx.center(
                    centered_image(
                        src="/images/page_information/podotherapeut_enschede_kim_bakhuis_legt_het_met_een_lach_uit-VoorVoet_podotherapie_enschede.jpg",
                        alt="Kim Bakhuis legt podotherapie uit",
                        width="100%",
                        max_width="840px",
                    ),
                    width="100%",
                ),

                section_sub_title(get_translation(TRANSLATIONS, "athletes_title", language)),
                regular_text(
                    get_translation(TRANSLATIONS, "athletes_intro", language),
                    color=Colors.text["content"],
                ),
                rx.vstack(
                    icon_list_item("fa-solid fa-circle", get_translation(TRANSLATIONS, "athletes_item1", language)),
                    icon_list_item("fa-solid fa-circle", get_translation(TRANSLATIONS, "athletes_item2", language)),
                    icon_list_item("fa-solid fa-circle", get_translation(TRANSLATIONS, "athletes_item3", language)),
                    icon_list_item("fa-solid fa-circle", get_translation(TRANSLATIONS, "athletes_item4", language)),
                    gap="0.5rem",
                    align="start",
                    width="100%",
                    padding_left="1.5rem",
                ),
                regular_text(
                    get_translation(TRANSLATIONS, "athletes_conclusion", language),
                    color=Colors.text["content"],
                ),

                section_sub_title(get_translation(TRANSLATIONS, "elderly_title", language)),
                regular_text(
                    get_translation(TRANSLATIONS, "elderly_intro", language),
                    color=Colors.text["content"],
                ),
                rx.vstack(
                    icon_list_item("fa-solid fa-circle", get_translation(TRANSLATIONS, "elderly_item1", language)),
                    icon_list_item("fa-solid fa-circle", get_translation(TRANSLATIONS, "elderly_item2", language)),
                    icon_list_item("fa-solid fa-circle", get_translation(TRANSLATIONS, "elderly_item3", language)),
                    icon_list_item("fa-solid fa-circle", get_translation(TRANSLATIONS, "elderly_item4", language)),
                    gap="0.5rem",
                    align="start",
                    width="100%",
                    padding_left="1.5rem",
                ),
                regular_text(
                    get_translation(TRANSLATIONS, "elderly_conclusion", language),
                    color=Colors.text["content"],
                ),

                gap="1.5rem",
                align="start",
                width="100%",
            ),
        ),
        background=Colors.backgrounds["green_light"],
        divider_color=Colors.backgrounds["white"],
        clip_top="gentle_4",
        clip_bottom="gentle_1",
        id="for-everyone",
    )
