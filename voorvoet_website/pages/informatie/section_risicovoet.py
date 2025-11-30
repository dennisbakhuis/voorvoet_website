"""Section explaining risk foot classification and care."""

import reflex as rx
from ...components import (
    container,
    section,
    image_text_section,
    section_sub_title,
    regular_text,
    centered_image,
    risk_level_card,
)
from ...theme import Colors
from ...utils.get_translation import get_translation


TRANSLATIONS = {
    "nl": {
        "title": "Wat is een risicovoet?",
        "paragraph1_1": "Met een risicovoet wordt bedoeld dat er een aantal factoren aanwezig zijn die de kans op het ontstaan van wonden vergroten, en daarbij ook alle mogelijke complicaties zoals een slechte genezing of zelfs amputatie. De risicofactoren voor het ontstaan van deze problemen zijn o.a. gevoelsstoornissen (neuropathie), verminderde doorbloeding (angiopathie), verminderde beweeglijkheid en/of een afwijkende voetstand. Dit kan leiden tot overmatige druk en wrijving waardoor er eelt, likdoorns, blaren of wonden kunnen ontstaan.",
        "paragraph1_2": "Bij een verminderd gevoel in de voeten wordt dit minder snel of helemaal niet opgemerkt. Bij een slechte doorbloeding zal de wond ook slecht of niet genezen. Een combinatie van deze factoren kan leiden tot grote problemen en in het uiterste geval een amputatie. Dat willen we natuurlijk allemaal het liefst voorkomen.",
        "paragraph1_3": "Er zijn veel verschillende oorzaken voor het ontstaan van neuropathie. Dat kan bijvoorbeeld een neurologische aandoening zijn, of als gevolg van o.a. diabetes of reuma. Ook kan het een bijwerking zijn van chemotherapie. Dit zijn slechts enkele voorbeelden.",
        "paragraph2_1": "Als uw hoofdbehandelaar of praktijkondersteuner u heeft doorgestuurd naar VoorVoet Podotherapie Enschede i.v.m. een risicovoet, dan zal de podotherapeut uw voeten onderzoeken op deze risicofactoren. De risicofactoren worden in kaart gebracht en bij een verhoogd risico zal er een persoonlijk behandelplan worden opgesteld. Dit is per persoon verschillend en kan bestaan uit voetzorg adviezen, schoenadvies, het aanmeten van drukverdelende zolen, het vervaardigen van een orthese of een combinatie van bovenstaande.",
        "paragraph2_2": "Er zal voor de voetbehandelingen nauw worden samengewerkt met de medisch pedicure die medisch noodzakelijke voetzorg zal uitvoeren. Ook werken we waar nodig samen met de praktijkondersteuner, huisarts of specialist om uw voeten in een zo goed mogelijke conditie te houden.",
        "paragraph2_3": "Vanaf een bepaalde risicoclassificatie kunt in aanmerking komen voor een vergoeding vanuit de basisverzekering. Hiervoor heeft u een verwijzing nodig van uw hoofdbehandelaar.",
        "classifications_title": "Welke risicoclassificaties zijn er?",
        "classifications_intro": "De risicoclassificaties worden zorgprofielen genoemd. Afhankelijk van het zorgprofiel worden de behandelingen wel of niet vergoedt vanuit de basisverzekering.",
        "level0_risk": "Geen risico",
        "level0_title": "Geen verhoogd risico",
        "level0_desc": "Er is geen sprake van neuropathie of een verminderde doorbloeding - er is geen verhoogd risico – er is geen vergoeding vanuit de basisverzekering mogelijk. Uw voeten zijn –wat dat betreft- in een goede conditie!",
        "level1_risk": "Laag risico",
        "level1_title": "Zorgprofiel 1",
        "level1_desc": "Er is alleen sprake van neuropathie of een verminderde doorbloeding, maar er is geen sprake van drukplekken – er is vergoeding voor een jaarlijks voetonderzoek bij de podotherapeut, maar geen vergoeding voor behandelingen vanuit de basisverzekering.",
        "level2_risk": "Gemiddeld risico",
        "level2_title": "Zorgprofiel 2",
        "level2_desc": "Er is sprake van neuropathie en verminderde doorbloeding maar er is geen sprake van drukplekken – er is een vergoeding voor behandelingen vanuit de basisverzekering.",
        "level3_risk": "Hoog risico",
        "level3_title": "Zorgprofiel 3",
        "level3_desc": "Er is sprake van neuropathie en/of verminderde doorbloeding en er zijn drukplekken aanwezig – er is een vergoeding voor behandelingen vanuit de basisverzekering.",
        "level4_risk": "Zeer hoog risico",
        "level4_title": "Zorgprofiel 4",
        "level4_desc": "Er is sprake van een wond in verleden, een amputatie of nierfunctie- vervangende therapie – er is een vergoeding voor behandelingen vanuit de basisverzekering.",
        "reimbursement_title": "Vergoeding hulpmiddelen",
        "reimbursement_text": "Heeft u podotherapeutische hulpmiddelen* nodig om te zorgen dat de voetstand-, de voetfunctie of de drukverdeling onder uw voeten beter wordt? Deze worden niet vanuit de basisverzekering gedekt. Mogelijk krijgt u wel een vergoeding vanuit uw aanvullende verzekering. Kijk voor mogelijke vergoedingen van podotherapeutische hulpmiddelen in de ",
        "reimbursement_link": "polis van uw aanvullende verzekering",
        "reimbursement_footnote": "(*) Podotherapeutische zolen, ortheses of nagelbeugels zijn podotherapeutische hulpmiddelen gebruikt door VoorVoet Podotherapie Enschede.",
    },
    "de": {
        "title": "Was ist ein Risikofuß?",
        "paragraph1_1": "Mit einem Risikofuß ist gemeint, dass eine Reihe von Faktoren vorhanden sind, die das Risiko für die Entstehung von Wunden erhöhen, und damit auch alle möglichen Komplikationen wie schlechte Heilung oder sogar Amputation. Die Risikofaktoren für die Entstehung dieser Probleme sind u.a. Gefühlsstörungen (Neuropathie), verminderte Durchblutung (Angiopathie), eingeschränkte Beweglichkeit und/oder eine abnormale Fußstellung. Dies kann zu übermäßigem Druck und Reibung führen, wodurch Hornhaut, Hühneraugen, Blasen oder Wunden entstehen können.",
        "paragraph1_2": "Bei vermindertem Gefühl in den Füßen wird dies weniger schnell oder gar nicht bemerkt. Bei schlechter Durchblutung wird die Wunde auch schlecht oder nicht heilen. Eine Kombination dieser Faktoren kann zu großen Problemen und im Extremfall zu einer Amputation führen. Das möchten wir natürlich alle am liebsten vermeiden.",
        "paragraph1_3": "Es gibt viele verschiedene Ursachen für die Entstehung von Neuropathie. Das kann zum Beispiel eine neurologische Erkrankung sein oder als Folge von u.a. Diabetes oder Rheuma. Es kann auch eine Nebenwirkung von Chemotherapie sein. Dies sind nur einige Beispiele.",
        "paragraph2_1": "Wenn Ihr Hauptbehandler oder Praxisunterstützer Sie wegen eines Risikofußes an VoorVoet Podotherapie Enschede überwiesen hat, wird der Podotherapeut Ihre Füße auf diese Risikofaktoren untersuchen. Die Risikofaktoren werden erfasst und bei erhöhtem Risiko wird ein persönlicher Behandlungsplan erstellt. Dies ist von Person zu Person unterschiedlich und kann aus Fußpflegeberatung, Schuhberatung, dem Anpassen von druckverteilenden Einlagen, der Anfertigung einer Orthese oder einer Kombination der oben genannten bestehen.",
        "paragraph2_2": "Für die Fußbehandlungen wird eng mit dem medizinischen Fußpfleger zusammengearbeitet, der medizinisch notwendige Fußpflege durchführt. Auch arbeiten wir bei Bedarf mit dem Praxisunterstützer, Hausarzt oder Spezialisten zusammen, um Ihre Füße in einem möglichst guten Zustand zu halten.",
        "paragraph2_3": "Ab einer bestimmten Risikoeinstufung können Sie für eine Erstattung aus der Grundversicherung in Frage kommen. Dafür benötigen Sie eine Überweisung von Ihrem Hauptbehandler.",
        "classifications_title": "Welche Risikoeinstufungen gibt es?",
        "classifications_intro": "Die Risikoeinstufungen werden Pflegeprofile genannt. Abhängig vom Pflegeprofil werden die Behandlungen aus der Grundversicherung erstattet oder nicht.",
        "level0_risk": "Kein Risiko",
        "level0_title": "Kein erhöhtes Risiko",
        "level0_desc": "Es liegt keine Neuropathie oder verminderte Durchblutung vor - es besteht kein erhöhtes Risiko - eine Erstattung aus der Grundversicherung ist nicht möglich. Ihre Füße sind - was das betrifft - in gutem Zustand!",
        "level1_risk": "Geringes Risiko",
        "level1_title": "Pflegeprofil 1",
        "level1_desc": "Es liegt nur Neuropathie oder verminderte Durchblutung vor, aber es gibt keine Druckstellen - es gibt Erstattung für eine jährliche Fußuntersuchung beim Podotherapeuten, aber keine Erstattung für Behandlungen aus der Grundversicherung.",
        "level2_risk": "Mittleres Risiko",
        "level2_title": "Pflegeprofil 2",
        "level2_desc": "Es liegt Neuropathie und verminderte Durchblutung vor, aber es gibt keine Druckstellen - es gibt eine Erstattung für Behandlungen aus der Grundversicherung.",
        "level3_risk": "Hohes Risiko",
        "level3_title": "Pflegeprofil 3",
        "level3_desc": "Es liegt Neuropathie und/oder verminderte Durchblutung vor und es sind Druckstellen vorhanden - es gibt eine Erstattung für Behandlungen aus der Grundversicherung.",
        "level4_risk": "Sehr hohes Risiko",
        "level4_title": "Pflegeprofil 4",
        "level4_desc": "Es liegt eine Wunde in der Vergangenheit, eine Amputation oder nierenersatztherapie vor - es gibt eine Erstattung für Behandlungen aus der Grundversicherung.",
        "reimbursement_title": "Erstattung Hilfsmittel",
        "reimbursement_text": "Benötigen Sie podotherapeutische Hilfsmittel*, um sicherzustellen, dass die Fußstellung, die Fußfunktion oder die Druckverteilung unter Ihren Füßen besser wird? Diese werden nicht von der Grundversicherung gedeckt. Möglicherweise erhalten Sie eine Erstattung aus Ihrer Zusatzversicherung. Schauen Sie für mögliche Erstattungen von podotherapeutischen Hilfsmitteln in die ",
        "reimbursement_link": "Police Ihrer Zusatzversicherung",
        "reimbursement_footnote": "(*) Podotherapeutische Einlagen, Orthesen oder Nagelspangen sind podotherapeutische Hilfsmittel, die von VoorVoet Podotherapie Enschede verwendet werden.",
    },
    "en": {
        "title": "What is a risk foot?",
        "paragraph1_1": "A risk foot means that there are a number of factors present that increase the risk of developing wounds, and also all possible complications such as poor healing or even amputation. The risk factors for the development of these problems include sensory disturbances (neuropathy), reduced blood flow (angiopathy), reduced mobility and/or an abnormal foot position. This can lead to excessive pressure and friction, which can cause calluses, corns, blisters or wounds.",
        "paragraph1_2": "With reduced feeling in the feet, this is noticed less quickly or not at all. With poor blood flow, the wound will also heal poorly or not at all. A combination of these factors can lead to major problems and in extreme cases amputation. We naturally want to prevent that as much as possible.",
        "paragraph1_3": "There are many different causes for the development of neuropathy. This can be, for example, a neurological condition, or as a result of diabetes or rheumatism. It can also be a side effect of chemotherapy. These are just a few examples.",
        "paragraph2_1": "If your primary care provider or practice assistant has referred you to VoorVoet Podotherapie Enschede due to a risk foot, the podotherapist will examine your feet for these risk factors. The risk factors will be mapped and if there is an increased risk, a personal treatment plan will be drawn up. This differs per person and can consist of foot care advice, shoe advice, fitting pressure-distributing insoles, manufacturing an orthosis or a combination of the above.",
        "paragraph2_2": "For foot treatments, close cooperation will be made with the medical pedicurist who will perform medically necessary foot care. We also work together with the practice assistant, general practitioner or specialist where necessary to keep your feet in the best possible condition.",
        "paragraph2_3": "From a certain risk classification you may be eligible for reimbursement from basic insurance. You need a referral from your primary care provider for this.",
        "classifications_title": "What risk classifications are there?",
        "classifications_intro": "The risk classifications are called care profiles. Depending on the care profile, treatments are or are not reimbursed from basic insurance.",
        "level0_risk": "No risk",
        "level0_title": "No increased risk",
        "level0_desc": "There is no neuropathy or reduced blood flow - there is no increased risk - no reimbursement from basic insurance is possible. Your feet are - in that respect - in good condition!",
        "level1_risk": "Low risk",
        "level1_title": "Care profile 1",
        "level1_desc": "There is only neuropathy or reduced blood flow, but there are no pressure points - there is reimbursement for an annual foot examination at the podotherapist, but no reimbursement for treatments from basic insurance.",
        "level2_risk": "Medium risk",
        "level2_title": "Care profile 2",
        "level2_desc": "There is neuropathy and reduced blood flow but there are no pressure points - there is reimbursement for treatments from basic insurance.",
        "level3_risk": "High risk",
        "level3_title": "Care profile 3",
        "level3_desc": "There is neuropathy and/or reduced blood flow and pressure points are present - there is reimbursement for treatments from basic insurance.",
        "level4_risk": "Very high risk",
        "level4_title": "Care profile 4",
        "level4_desc": "There is a wound in the past, an amputation or kidney function replacement therapy - there is reimbursement for treatments from basic insurance.",
        "reimbursement_title": "Reimbursement aids",
        "reimbursement_text": "Do you need podotherapeutic aids* to ensure that the foot position, foot function or pressure distribution under your feet improves? These are not covered by basic insurance. You may receive reimbursement from your supplementary insurance. Look for possible reimbursements of podotherapeutic aids in the ",
        "reimbursement_link": "policy of your supplementary insurance",
        "reimbursement_footnote": "(*) Podotherapeutic insoles, orthoses or nail braces are podotherapeutic aids used by VoorVoet Podotherapie Enschede.",
    },
}


def section_risicovoet(language: str) -> rx.Component:
    """
    Create the risk foot (risicovoet) information section.

    Explains what constitutes a risk foot (factors like neuropathy,
    reduced blood flow, limited mobility, foot deformities) and the
    associated complications. Details the five risk classifications
    (zorgprofielen 0-4) used to determine treatment coverage from
    basic health insurance. Describes the treatment approach including
    foot care advice, shoe recommendations, pressure-distributing insoles,
    and orthoses.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")

    Returns
    -------
    rx.Component
        A section component containing detailed information about risk
        foot classifications, risk factors, treatment approaches, and
        insurance coverage for each risk level (0-4).
    """
    paragraphs_1 = [
        get_translation(TRANSLATIONS, "paragraph1_1", language),
        get_translation(TRANSLATIONS, "paragraph1_2", language),
        get_translation(TRANSLATIONS, "paragraph1_3", language),
    ]

    paragraphs_2 = [
        get_translation(TRANSLATIONS, "paragraph2_1", language),
        get_translation(TRANSLATIONS, "paragraph2_2", language),
        get_translation(TRANSLATIONS, "paragraph2_3", language),
    ]

    return section(
        container(
            image_text_section(
                image_src="/images/page_information/voetklachten_hielpijn_sport_voorvoet_podotherapie_enschede.jpg",
                title=get_translation(TRANSLATIONS, "title", language),
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
                    width="100%",
                    max_width="840px",
                ),
                width="100%",
                margin_bottom="2rem",
            ),
            section_sub_title(
                get_translation(TRANSLATIONS, "classifications_title", language),
                margin_bottom="1rem",
            ),
            regular_text(
                get_translation(TRANSLATIONS, "classifications_intro", language),
                color=Colors.text["content"],
                margin_bottom="2rem",
            ),
            risk_level_card(
                level=0,
                risk_label=get_translation(TRANSLATIONS, "level0_risk", language),
                title=get_translation(TRANSLATIONS, "level0_title", language),
                description=get_translation(TRANSLATIONS, "level0_desc", language),
            ),
            risk_level_card(
                level=1,
                risk_label=get_translation(TRANSLATIONS, "level1_risk", language),
                title=get_translation(TRANSLATIONS, "level1_title", language),
                description=get_translation(TRANSLATIONS, "level1_desc", language),
            ),
            risk_level_card(
                level=2,
                risk_label=get_translation(TRANSLATIONS, "level2_risk", language),
                title=get_translation(TRANSLATIONS, "level2_title", language),
                description=get_translation(TRANSLATIONS, "level2_desc", language),
            ),
            risk_level_card(
                level=3,
                risk_label=get_translation(TRANSLATIONS, "level3_risk", language),
                title=get_translation(TRANSLATIONS, "level3_title", language),
                description=get_translation(TRANSLATIONS, "level3_desc", language),
            ),
            risk_level_card(
                level=4,
                risk_label=get_translation(TRANSLATIONS, "level4_risk", language),
                title=get_translation(TRANSLATIONS, "level4_title", language),
                description=get_translation(TRANSLATIONS, "level4_desc", language),
            ),
            rx.box(height="1rem"),
            section_sub_title(
                get_translation(TRANSLATIONS, "reimbursement_title", language),
                margin_bottom="1rem",
            ),
            rx.text(
                get_translation(TRANSLATIONS, "reimbursement_text", language),
                rx.link(
                    get_translation(TRANSLATIONS, "reimbursement_link", language),
                    href=f"/{language}/vergoedingen/",
                    color=Colors.text["link"],
                    text_decoration="underline",
                    _hover={"color": Colors.primary["700"]},
                ),
                ".",
                font_size="18px",
                line_height="1.6",
                color=Colors.text["content"],
                margin_bottom="1rem",
            ),
            regular_text(
                get_translation(TRANSLATIONS, "reimbursement_footnote", language),
                color=Colors.text["muted"],
                font_style="italic",
            ),
        ),
        id="de-risicovoet",
    )
