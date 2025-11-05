"""Locations section displaying practice addresses and maps."""
import reflex as rx

from ...components import section, container, location_section, LocationConfig


def section_locations() -> rx.Component:
    """
    Create the locations section with practice address details.

    This section displays information about both VoorVoet practice locations
    in Enschede (Eeftinksweg and Beethovenlaan), including addresses,
    descriptions, opening hours, embedded Google Maps, and route links.

    Returns
    -------
    rx.Component
        A section component containing location cards with maps and details
        for both practice locations arranged in an alternating layout.
    """
    locations = [
        LocationConfig(
            title="Locatie Eeftinksweg",
            address="Eeftinksweg 13, 7541 WE Enschede",
            description="Onze hoofdlocatie aan de Eeftinksweg biedt alle podotherapeutische behandelingen in een moderne en toegankelijke omgeving. Deze locatie is geopend op maandag en donderdag van 8:00 tot 17:00 uur. De praktijk is goed bereikbaar met de auto en heeft voldoende parkeermogelijkheden.",
            map_embed='<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2443.8!2d6.8944!3d52.2215!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47b813bb8f8b8b8b%3A0x123456!2sEeftinksweg+13%2C+7541+WE+Enschede!5e0!3m2!1sen!2snl!4v1234567890" style="border:0;width:100%;height:400px;display:block;" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>',
            route_link="https://www.google.com/maps/dir//Eeftinksweg+13,+7541+WE+Enschede",
            reverse_order=False
        ),
        LocationConfig(
            title="Locatie Beethovenlaan",
            address="Beethovenlaan 10, 7522 HJ Enschede",
            description="Onze tweede locatie aan de Beethovenlaan biedt dezelfde hoogwaardige podotherapeutische zorg in een comfortabele setting. Deze locatie is geopend op dinsdag (8:30-19:30), woensdag (8:30-17:00) en vrijdag (8:00-13:00). Ook hier is voldoende parkeergelegenheid beschikbaar.",
            map_embed='<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2443.5!2d6.8756!3d52.2289!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47b813bb8f8b8b8b%3A0x654321!2sBeethovenlaan+10%2C+7522+HJ+Enschede!5e0!3m2!1sen!2snl!4v1234567890" style="border:0;width:100%;height:400px;display:block;" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>',
            route_link="https://www.google.com/maps/dir//Beethovenlaan+10,+7522+HJ+Enschede",
            reverse_order=True
        )
    ]

    return section(
        container(
            location_section(
                title="Waar zitten wij",
                description="VoorVoet heeft twee praktijklocaties in Enschede. Beide locaties zijn uitgerust met moderne faciliteiten en bieden een professionele omgeving voor uw behandeling.",
                locations=locations
            )
        ),
        id="locations"
    )
