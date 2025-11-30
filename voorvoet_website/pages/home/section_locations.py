"""Locations section displaying practice addresses and maps."""

import reflex as rx

from ...components import section, container, location_section, LocationConfig
from ...utils.get_translation import get_translation


TRANSLATIONS = {
    "nl": {
        "main_title": "Waar zitten wij",
        "main_description": "VoorVoet heeft twee praktijklocaties in Enschede. Beide locaties zijn uitgerust met moderne faciliteiten en bieden een professionele omgeving voor uw behandeling.",
        "location1_title": "Locatie Eeftinksweg",
        "location1_address": "Eeftinksweg 13, 7541 WE Enschede",
        "location1_description": "Onze hoofdlocatie aan de Eeftinksweg biedt alle podotherapeutische behandelingen in een moderne en toegankelijke omgeving. Deze locatie is geopend op maandag en donderdag van 8:00 tot 17:00 uur. De praktijk is goed bereikbaar met de auto en heeft voldoende parkeermogelijkheden.",
        "location2_title": "Locatie Beethovenlaan",
        "location2_address": "Beethovenlaan 10, 7522 HJ Enschede",
        "location2_description": "Onze tweede locatie aan de Beethovenlaan biedt dezelfde hoogwaardige podotherapeutische zorg in een comfortabele setting. Deze locatie is geopend op dinsdag (8:30-19:30), woensdag (8:30-17:00) en vrijdag (8:00-13:00). Ook hier is voldoende parkeergelegenheid beschikbaar.",
    },
    "de": {
        "main_title": "Wo wir sind",
        "main_description": "VoorVoet hat zwei Praxisstandorte in Enschede. Beide Standorte sind mit modernen Einrichtungen ausgestattet und bieten eine professionelle Umgebung für Ihre Behandlung.",
        "location1_title": "Standort Eeftinksweg",
        "location1_address": "Eeftinksweg 13, 7541 WE Enschede",
        "location1_description": "Unser Hauptstandort an der Eeftinksweg bietet alle podotherapeutischen Behandlungen in einer modernen und zugänglichen Umgebung. Dieser Standort ist montags und donnerstags von 8:00 bis 17:00 Uhr geöffnet. Die Praxis ist gut mit dem Auto erreichbar und verfügt über ausreichend Parkmöglichkeiten.",
        "location2_title": "Standort Beethovenlaan",
        "location2_address": "Beethovenlaan 10, 7522 HJ Enschede",
        "location2_description": "Unser zweiter Standort an der Beethovenlaan bietet die gleiche hochwertige podotherapeutische Versorgung in einer komfortablen Umgebung. Dieser Standort ist dienstags (8:30-19:30), mittwochs (8:30-17:00) und freitags (8:00-13:00) geöffnet. Auch hier stehen ausreichend Parkplätze zur Verfügung.",
    },
    "en": {
        "main_title": "Where we are located",
        "main_description": "VoorVoet has two practice locations in Enschede. Both locations are equipped with modern facilities and provide a professional environment for your treatment.",
        "location1_title": "Location Eeftinksweg",
        "location1_address": "Eeftinksweg 13, 7541 WE Enschede",
        "location1_description": "Our main location on Eeftinksweg offers all podotherapeutic treatments in a modern and accessible environment. This location is open on Mondays and Thursdays from 8:00 to 17:00. The practice is easily accessible by car and has ample parking facilities.",
        "location2_title": "Location Beethovenlaan",
        "location2_address": "Beethovenlaan 10, 7522 HJ Enschede",
        "location2_description": "Our second location on Beethovenlaan offers the same high-quality podotherapeutic care in a comfortable setting. This location is open on Tuesdays (8:30-19:30), Wednesdays (8:30-17:00) and Fridays (8:00-13:00). Ample parking is also available here.",
    },
}


def section_locations(language: str) -> rx.Component:
    """
    Create the locations section with practice address details.

    This section displays information about both VoorVoet practice locations
    in Enschede (Eeftinksweg and Beethovenlaan), including addresses,
    descriptions, opening hours, embedded Google Maps, and route links.

    Parameters
    ----------
    language : str
        The language code for translations (e.g., 'nl', 'de', 'en').

    Returns
    -------
    rx.Component
        A section component containing location cards with maps and details
        for both practice locations arranged in an alternating layout.
    """
    locations = [
        LocationConfig(
            title=get_translation(TRANSLATIONS, "location1_title", language),
            address=get_translation(TRANSLATIONS, "location1_address", language),
            description=get_translation(
                TRANSLATIONS, "location1_description", language
            ),
            map_embed='<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2443.8!2d6.8944!3d52.2215!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47b813bb8f8b8b8b%3A0x123456!2sEeftinksweg+13%2C+7541+WE+Enschede!5e0!3m2!1sen!2snl!4v1234567890" style="border:0;width:100%;height:400px;display:block;" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>',
            route_link="https://www.google.com/maps/dir//Eeftinksweg+13,+7541+WE+Enschede",
            reverse_order=False,
        ),
        LocationConfig(
            title=get_translation(TRANSLATIONS, "location2_title", language),
            address=get_translation(TRANSLATIONS, "location2_address", language),
            description=get_translation(
                TRANSLATIONS, "location2_description", language
            ),
            map_embed='<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2443.5!2d6.8756!3d52.2289!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47b813bb8f8b8b8b%3A0x654321!2sBeethovenlaan+10%2C+7522+HJ+Enschede!5e0!3m2!1sen!2snl!4v1234567890" style="border:0;width:100%;height:400px;display:block;" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>',
            route_link="https://www.google.com/maps/dir//Beethovenlaan+10,+7522+HJ+Enschede",
            reverse_order=True,
        ),
    ]

    return section(
        container(
            location_section(
                title=get_translation(TRANSLATIONS, "main_title", language),
                description=get_translation(TRANSLATIONS, "main_description", language),
                locations=locations,
            )
        ),
        id="locations",
    )
