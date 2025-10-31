# Section "What is podiatry" on the information page
import reflex as rx
from ...components import container, section, image_text_section, section_sub_title, regular_text, centered_image
from ...theme import Colors


def section_risicovoet() -> rx.Component:
    paragraphs_1 = [
        "Met een risicovoet wordt bedoeld dat er een aantal factoren aanwezig zijn die de kans op het ontstaan van wonden vergroten, en daarbij ook alle mogelijke complicaties zoals een slechte genezing of zelfs amputatie. De risicofactoren voor het ontstaan van deze problemen zijn o.a. gevoelsstoornissen (neuropathie), verminderde doorbloeding (angiopathie), verminderde beweeglijkheid en/of een afwijkende voetstand. Dit kan leiden tot overmatige druk en wrijving waardoor er eelt, likdoorns, blaren of wonden kunnen ontstaan.",
        "Bij een verminderd gevoel in de voeten wordt dit minder snel of helemaal niet opgemerkt. Bij een slechte doorbloeding zal de wond ook slecht of niet genezen. Een combinatie van deze factoren kan leiden tot grote problemen en in het uiterste geval een amputatie. Dat willen we natuurlijk allemaal het liefst voorkomen.",
        "Er zijn veel verschillende oorzaken voor het ontstaan van neuropathie. Dat kan bijvoorbeeld een neurologische aandoening zijn, of als gevolg van o.a. diabetes of reuma. Ook kan het een bijwerking zijn van chemotherapie. Dit zijn slechts enkele voorbeelden.",
    ]

    paragraphs_2 = [
        "Als uw hoofdbehandelaar of praktijkondersteuner u heeft doorgestuurd naar VoorVoet Podotherapie Enschede i.v.m. een risicovoet, dan zal de podotherapeut uw voeten onderzoeken op deze risicofactoren. De risicofactoren worden in kaart gebracht en bij een verhoogd risico zal er een persoonlijk behandelplan worden opgesteld. Dit is per persoon verschillend en kan bestaan uit voetzorg adviezen, schoenadvies, het aanmeten van drukverdelende zolen, het vervaardigen van een orthese of een combinatie van bovenstaande.",
        "Er zal voor de voetbehandelingen nauw worden samengewerkt met de medisch pedicure die medisch noodzakelijke voetzorg zal uitvoeren. Ook werken we waar nodig samen met de praktijkondersteuner, huisarts of specialist om uw voeten in een zo goed mogelijke conditie te houden.",
        "Vanaf een bepaalde risicoclassificatie kunt in aanmerking komen voor een vergoeding vanuit de basisverzekering. Hiervoor heeft u een verwijzing nodig van uw hoofdbehandelaar.",
    ]
    
    return section(
        container(
            image_text_section(
                image_src="/images/page_information/voetklachten_hielpijn_sport_voorvoet_podotherapie_enschede.jpg",
                title="Wat is een risicovoet?",
                paragraphs=paragraphs_1,
                image_position="right",
                image_max_width="450px",
                padding_bottom="1rem",
            ),
            regular_text(
                paragraphs_2,
                color=Colors.text["content"],
            ),

            rx.center(
                centered_image(
                    src="/images/page_information/nagelbeugel_nagelproblemen_voorvoet_podotherapie_enschede.jpg",
                    alt="Kim Bakhuis legt podotherapie uit",
                    width="70%",
                    max_width="840px",
                ),
                width="100%",
            ),
            section_sub_title("Welke risicoclassificaties zijn er?"),
            regular_text(
                "Als uw hoofdbehandelaar of praktijkondersteuner u heeft doorgestuurd naar VoorVoet Podotherapie Enschede i.v.m. een risicovoet, dan zal de podotherapeut uw voeten onderzoeken op deze risicofactoren. De risicofactoren worden in kaart gebracht en bij een verhoogd risico zal er een persoonlijk behandelplan worden opgesteld. Dit is per persoon verschillend en kan bestaan uit voetzorg adviezen, schoenadvies, het aanmeten van drukverdelende zolen, het vervaardigen van een orthese of een combinatie van bovenstaande.",
                color=Colors.text["content"],
            ),
        ),
        id="de-risicovoet"
    )