# Section "Podiatry is for everyone" on the information page
import reflex as rx
from ...components import container, section, section_title, section_sub_title, regular_text, centered_image, icon_list_item
from ...theme import Colors


def section_for_everyone() -> rx.Component:
    return section(
        container(
            rx.vstack(
                section_title("Podotherapie is voor iedereen"),
                regular_text(
                    "In iedere leeftijdscategorie kan je te maken krijgen met andere klachten. Dit kan te maken hebben met de ontwikkeling bij kinderen en het veranderen van je lijf als je ouder wordt. Dus iedereen kan terecht bij VoorVoet Podotherapie Enschede.",
                    color=Colors.text["content"],
                ),
                
                section_sub_title("Podotherapie bij kinderen"),
                regular_text(
                    "Podotherapie kan helpen bij het verbeteren van de beweeglijkheid en het functioneren van de voeten bij kinderen, wat bijdraagt aan hun algehele gezondheid en welzijn. Het is belangrijk om op tijd te beginnen met podotherapie als uw kind last heeft van voetproblemen, zodat eventuele aandoeningen kunnen worden behandeld en voorkomen dat ze verergeren.",
                    color=Colors.text["content"],
                ),
                regular_text("Kinderen kunnen baat hebben bij podotherapie als ze:", color=Colors.text["content"]),
                rx.vstack(
                    icon_list_item("fa-solid fa-circle", "Problemen hebben met lopen, rennen of springen"),
                    icon_list_item("fa-solid fa-circle", "Pijn of ongemak in de voeten, benen, knieën of rug ervaren"),
                    icon_list_item("fa-solid fa-circle", "Zich snel moe voelen tijdens het spelen"),
                    icon_list_item("fa-solid fa-circle", "Afwijkingen van de benen of voeten hebben, zoals X-benen of O-benen"),
                    icon_list_item("fa-solid fa-circle", "Schoenen snel en overmatig afslijten"),
                    gap="0.5rem",
                    align="start",
                    width="100%",
                    margin_left="1.5rem",
                ),
                
                rx.center(
                    centered_image(
                        src="/images/page_information/podotherapeut_enschede_kim_bakhuis_legt_het_met_een_lach_uit-VoorVoet_podotherapie_enschede.jpg",
                        alt="Kim Bakhuis legt podotherapie uit",
                        width="70%",
                        max_width="840px",
                    ),
                    width="100%",
                ),
                
                section_sub_title("Podotherapie bij sporters en actievelingen"),
                regular_text(
                    "VoorVoet Podotherapie Enschede kan voor sporters een oplossing bieden. Sporters kunnen last hebben van voetproblemen als gevolg van de vele uren die ze doorbrengen met wandelen, hardlopen, springen, rennen en andere fysieke activiteiten. Veel voorkomende voetklachten bij actieve mensen zijn onder andere:",
                    color=Colors.text["content"],
                ),
                rx.vstack(
                    icon_list_item("fa-solid fa-circle", "Overbelasting van de voeten, waardoor ontstekingen, drukproblemen, blaren of wonden ontstaan."),
                    icon_list_item("fa-solid fa-circle", "Verstuikingen of verrekkingen van de voeten."),
                    icon_list_item("fa-solid fa-circle", "Stressfracturen, veroorzaakt door het herhaaldelijk belasten van de voeten."),
                    icon_list_item("fa-solid fa-circle", "Verminderde beweeglijkheid van de enkels en voeten, wat de prestaties kan beïnvloeden."),
                    gap="0.5rem",
                    align="start",
                    width="100%",
                    margin_left="1.5rem",
                ),
                regular_text(
                    "Podotherapie kan sporters en actievelingen helpen bij het voorkomen en behandelen van voetproblemen, door het verbeteren van de beweeglijkheid, het waar nodig aanpassen van de schoenen en/of het geven van oefeningen. Podotherapeuten kunnen ook specifieke inlegzolen of andere hulpmiddelen adviseren en vervaardigen die de prestaties kunnen verbeteren en de kans op blessures kunnen verkleinen. Door de juiste zorg en adviezen kan de podotherapeut ervoor zorgen dat je fit en actief kan blijven.",
                    color=Colors.text["content"],
                ),
                
                section_sub_title("Podotherapie bij ouderen"),
                regular_text(
                    "Ook als oudere kan je terecht bij VoorVoet Podotherapie Enschede. Met het ouder worden kunnen er veranderingen optreden in de voeten, waaronder bijvoorbeeld:",
                    color=Colors.text["content"],
                ),
                rx.vstack(
                    icon_list_item("fa-solid fa-circle", "Dunner wordend weefsel, waardoor de voeten gevoeliger worden."),
                    icon_list_item("fa-solid fa-circle", "Verlies van elastische veerkracht, waardoor de voeten moeilijker kunnen reageren op belasting"),
                    icon_list_item("fa-solid fa-circle", "Osteoporose, wat bijdraagt aan het risico op fracturen in de voeten"),
                    icon_list_item("fa-solid fa-circle", "Diabetes, reuma, artritis en andere (chronische) aandoeningen die invloed kunnen hebben op het functioneren van de voeten, en het verzorgen van de voeten bemoeilijkt. Dit vormt een extra risico voor het ontstaan van voetproblemen."),
                    gap="0.5rem",
                    align="start",
                    width="100%",
                    margin_left="1.5rem",
                ),
                regular_text(
                    "Podotherapie kan helpen bij het optimaliseren van de druk en ondersteuning onder de voeten zodat er minder pijnklachten ontstaan. Hierdoor kan je comfortabeler en veiliger bewegen, wat de kans op vallen verkleint. Het is belangrijk om op tijd hulp te zoeken bij voetproblemen, zodat eventuele aandoeningen en pijnklachten op tijd worden behandeld en de kwaliteit van leven wordt verbeterd.",
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