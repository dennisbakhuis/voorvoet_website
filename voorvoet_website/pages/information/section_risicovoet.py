# Section "What is podiatry" on the information page
import reflex as rx
from ...components import container, section, image_text_section, section_sub_title, regular_text, centered_image, risk_level_card
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
                margin_bottom="2rem",
            ),
            section_sub_title("Welke risicoclassificaties zijn er?", margin_bottom="1rem"),
            regular_text(
                "De risicoclassificaties worden zorgprofielen genoemd. Afhankelijk van het zorgprofiel worden de behandelingen wel of niet vergoedt vanuit de basisverzekering.",
                color=Colors.text["content"],
                margin_bottom="2rem",
            ),

            risk_level_card(
                level=0,
                risk_label="Geen risico",
                title="Geen verhoogd risico",
                description="Er is geen sprake van neuropathie of een verminderde doorbloeding - er is geen verhoogd risico – er is geen vergoeding vanuit de basisverzekering mogelijk. Uw voeten zijn –wat dat betreft- in een goede conditie!"
            ),
            risk_level_card(
                level=1,
                risk_label="Laag risico",
                title="Zorgprofiel 1",
                description="Er is alleen sprake van neuropathie of een verminderde doorbloeding, maar er is geen sprake van drukplekken – er is vergoeding voor een jaarlijks voetonderzoek bij de podotherapeut, maar geen vergoeding voor behandelingen vanuit de basisverzekering."
            ),
            risk_level_card(
                level=2,
                risk_label="Gemiddeld risico",
                title="Zorgprofiel 2",
                description="Er is sprake van neuropathie en verminderde doorbloeding maar er is geen sprake van drukplekken – er is een vergoeding voor behandelingen vanuit de basisverzekering."
            ),
            risk_level_card(
                level=3,
                risk_label="Hoog risico",
                title="Zorgprofiel 3",
                description="Er is sprake van neuropathie en/of verminderde doorbloeding en er zijn drukplekken aanwezig – er is een vergoeding voor behandelingen vanuit de basisverzekering."
            ),
            risk_level_card(
                level=4,
                risk_label="Zeer hoog risico",
                title="Zorgprofiel 4",
                description="Er is sprake van een wond in verleden, een amputatie of nierfunctie- vervangende therapie – er is een vergoeding voor behandelingen vanuit de basisverzekering."
            ),

            rx.box(height="1rem"),
            section_sub_title("Vergoeding hulpmiddelen", margin_bottom="1rem"),
            rx.text(
                "Heeft u podotherapeutische hulpmiddelen* nodig om te zorgen dat de voetstand-, de voetfunctie of de drukverdeling onder uw voeten beter wordt? Deze worden niet vanuit de basisverzekering gedekt. Mogelijk krijgt u wel een vergoeding vanuit uw aanvullende verzekering. Kijk voor mogelijke vergoedingen van podotherapeutische hulpmiddelen in de ",
                rx.link(
                    "polis van uw aanvullende verzekering",
                    href="/reimbursements/",
                    color=Colors.text["link"],
                    text_decoration="underline",
                    _hover={"color": Colors.primary["700"]}
                ),
                ".",
                font_size="18px",
                line_height="1.6",
                color=Colors.text["content"],
                margin_bottom="1rem",
            ),
            regular_text(
                "(*) Podotherapeutische zolen, ortheses of nagelbeugels zijn podotherapeutische hulpmiddelen gebruikt door VoorVoet Podotherapie Enschede.",
                color=Colors.text["muted"],
                font_style="italic",
            ),
        ),
        id="de-risicovoet"
    )
