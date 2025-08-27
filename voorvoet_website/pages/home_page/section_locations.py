import reflex as rx

from ...components import section, container, column, section_title, section_sub_title, regular_text, button
from ...theme import Colors


def location_map_section(
    title: str, 
    address: str, 
    description: str, 
    map_embed: str, 
    route_link: str,
    reverse_order: bool = False
) -> rx.Component:
    """Create a location section with map and info"""
    
    map_column = column(
        rx.box(
            rx.html(map_embed),
            width="100%",
            height="400px",
            border_radius="12px",
            overflow="hidden",
            box_shadow="0 4px 12px rgba(0, 0, 0, 0.1)",
            position="relative"
        ),
        padding_right=["0", "0", "0", "2rem"] if not reverse_order else ["0", "0", "0", "0"],
        padding_left=["0", "0", "0", "0"] if not reverse_order else ["0", "0", "0", "2rem"],
        display="flex",
        flex_direction="column",
        justify_content="center",
        align_items="center",
        margin_bottom="2rem"
    )
    
    info_column = column(
        section_title(title, margin_bottom="0.5rem", text_align=["center", "center", "left", "left", "left"]),
        regular_text(address, font_weight="700", color=Colors.text["subheading"], margin_bottom="1rem", text_align=["center", "center", "left", "left", "left"]),
        regular_text(description, text_align=["center", "center", "left", "left", "left"], margin_bottom="1.5rem"),
        rx.box(
            button(
                "Plan je route",
                href=route_link,
            ),
            display="flex",
            justify_content="center",
            width="100%"
        ),
        padding_left=["0", "0", "0", "2rem"] if not reverse_order else ["0", "0", "0", "0"],
        padding_right=["0", "0", "0", "0"] if not reverse_order else ["0", "0", "0", "2rem"],
        display="flex",
        flex_direction="column",
        justify_content="center"
    )
    
    # For smallest 2 breakpoints: always map first, then text
    mobile_columns = [map_column, info_column]  # Always map first when stacked
    # For largest 3 breakpoints: alternating sides (map+text, text+map)
    desktop_columns = [info_column, map_column] if reverse_order else [map_column, info_column]
    
    return rx.box(
        # Mobile/small: stacked layout (always map first)
        rx.box(
            *mobile_columns,
            display=["block", "block", "none", "none", "none"],
            gap="2rem",
            align_items="center",
        ),
        # Medium/large/xl screens: flex layout (alternating sides)
        rx.box(
            *desktop_columns,
            display=["none", "none", "flex", "flex", "flex"],
            gap="2rem",
            align_items="center",
        ),
        margin_top="3rem",
    )


def section_locations() -> rx.Component:
    return section(
        container(
            rx.vstack(
                section_title(
                    "Waar zitten wij", 
                    text_align=["center", "center", "left", "left", "left"],
                    margin_bottom="2rem",
                    width="100%"
                ),
                regular_text(
                    "VoorVoet heeft twee praktijklocaties in Enschede. Beide locaties zijn uitgerust met moderne faciliteiten en bieden een professionele omgeving voor uw behandeling.",
                    text_align=["center", "center", "left", "left", "left"],
                    width="100%"
                ),
                
                # Location 1: Eeftinksweg (map left, info right)
                location_map_section(
                    title="Locatie Eeftinksweg",
                    address="Eeftinksweg 13, 7541 WE Enschede",
                    description="Onze hoofdlocatie aan de Eeftinksweg biedt alle podotherapeutische behandelingen in een moderne en toegankelijke omgeving. Deze locatie is geopend op maandag en donderdag van 8:00 tot 17:00 uur. De praktijk is goed bereikbaar met de auto en heeft voldoende parkeermogelijkheden.",
                    map_embed='<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2443.8!2d6.8944!3d52.2215!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47b813bb8f8b8b8b%3A0x123456!2sEeftinksweg+13%2C+7541+WE+Enschede!5e0!3m2!1sen!2snl!4v1234567890" style="border:0;width:100%;height:400px;display:block;" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>',
                    route_link="https://www.google.com/maps/dir//Eeftinksweg+13,+7541+WE+Enschede",
                    reverse_order=False
                ),
                
                # Location 2: Beethovenlaan (map right, info left)  
                location_map_section(
                    title="Locatie Beethovenlaan",
                    address="Beethovenlaan 10, 7522 HJ Enschede",
                    description="Onze tweede locatie aan de Beethovenlaan biedt dezelfde hoogwaardige podotherapeutische zorg in een comfortabele setting. Deze locatie is geopend op dinsdag (8:30-19:30), woensdag (8:30-17:00) en vrijdag (8:00-13:00). Ook hier is voldoende parkeergelegenheid beschikbaar.",
                    map_embed='<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2443.5!2d6.8756!3d52.2289!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47b813bb8f8b8b8b%3A0x654321!2sBeethovenlaan+10%2C+7522+HJ+Enschede!5e0!3m2!1sen!2snl!4v1234567890" style="border:0;width:100%;height:400px;display:block;" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>',
                    route_link="https://www.google.com/maps/dir//Beethovenlaan+10,+7522+HJ+Enschede",
                    reverse_order=True
                ),
                
                spacing="0",
                align="start",
                width="100%"
            )
        ),
        id="locations"
    )
