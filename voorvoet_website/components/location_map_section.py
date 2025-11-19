"""Reusable location map section component."""
import reflex as rx
from typing import List, Dict, Any

from ..theme import Colors, FontSizes, Layout, Spacing
from .column import column
from .section_title import section_title
from .regular_text import regular_text
from .button import button


class LocationConfig:
    """
    Configuration class for location data.

    Attributes
    ----------
    title : str
        Location title text.
    address : str
        Physical address of the location.
    description : str
        Description text for the location.
    map_embed : str
        HTML embed code for the map (e.g., Google Maps iframe).
    route_link : str
        URL for route planning link.
    reverse_order : bool
        Whether to reverse the order of map and info columns on desktop.
        Default is False.
    """
    def __init__(
        self,
        title: str,
        address: str,
        description: str,
        map_embed: str,
        route_link: str,
        reverse_order: bool = False
    ):
        self.title = title
        self.address = address
        self.description = description
        self.map_embed = map_embed
        self.route_link = route_link
        self.reverse_order = reverse_order


def location_map_item(
    title: str,
    address: str,
    description: str,
    map_embed: str,
    route_link: str,
    reverse_order: bool = False
) -> rx.Component:
    """
    Create a single location section with embedded map and information.

    Creates a responsive two-column layout with an embedded map on one side
    and location information (title, address, description, button) on the
    other. The layout stacks on mobile and displays side-by-side on desktop.
    Column order can be reversed for alternating layouts.

    Parameters
    ----------
    title : str
        Location title text.
    address : str
        Physical address of the location.
    description : str
        Description text for the location.
    map_embed : str
        HTML embed code for the map (typically an iframe from Google Maps).
    route_link : str
        URL for route planning (e.g., Google Maps directions link).
    reverse_order : bool, optional
        Whether to reverse the order of map and info columns on desktop.
        Default is False (map on left, info on right).

    Returns
    -------
    rx.Component
        A Reflex box component containing the location map layout.

    Notes
    -----
    On mobile, the map always appears first (on top) regardless of
    reverse_order setting.
    """
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
        padding_right=["0", "0", "0", Spacing.responsive_2rem[3]] if not reverse_order else ["0", "0", "0", "0"],
        padding_left=["0", "0", "0", "0"] if not reverse_order else ["0", "0", "0", Spacing.responsive_2rem[3]],
        display="flex",
        flex_direction="column",
        justify_content="center",
        align_items="center",
        margin_bottom=Spacing.image_margin_bottom
    )

    info_column = column(
        section_title(
            title, 
            margin_bottom="0.5rem", 
            text_align=["center", "center", "left", "left"]
        ),
        regular_text(
            address, 
            font_weight="700", 
            color=Colors.text["subheading"], 
            margin_bottom="1rem", 
            text_align=["center", "center", "left", "left"]
        ),
        regular_text(
            description, 
            text_align=["center", "center", "left", "left"], 
            margin_bottom="1.5rem"
        ),
        rx.box(
            button("Plan je route", href=route_link),
            display="flex",
            justify_content="center",
            width="100%"
        ),
        padding_left=["0", "0", "0", Spacing.responsive_2rem[3]] if not reverse_order else ["0", "0", "0", "0"],
        padding_right=["0", "0", "0", "0"] if not reverse_order else ["0", "0", "0", Spacing.responsive_2rem[3]],
        display="flex",
        flex_direction="column",
        justify_content="center"
    )

    mobile_columns = [map_column, info_column]
    desktop_columns = [info_column, map_column] if reverse_order else [map_column, info_column]

    return rx.box(
        rx.box(
            *mobile_columns,
            display=Layout.mobile_only,
            gap=Spacing.grid_gap,
            align_items="center",
        ),
        rx.box(
            *desktop_columns,
            display=Layout.desktop_only,
            gap=Spacing.grid_gap,
            align_items="center",
        ),
        margin_top=Spacing.card_spacing,
    )


def location_section(
    title: str,
    description: str,
    locations: List[LocationConfig],
    **section_props
) -> rx.Component:
    """
    Create a complete location section with multiple locations.

    Creates a vertical stack containing a section title, description,
    and multiple location map items. Each location is generated from
    a LocationConfig object and can have alternating layouts.

    Parameters
    ----------
    title : str
        Section title text.
    description : str
        Section description text.
    locations : list[LocationConfig]
        List of LocationConfig objects defining location content and layout.
    **section_props : dict
        Additional style properties to apply to the section.
        These will override the default styles.

    Returns
    -------
    rx.Component
        A Reflex vstack component containing the complete location section.
    """
    location_items = []
    for location in locations:
        location_items.append(
            location_map_item(
                title=location.title,
                address=location.address,
                description=location.description,
                map_embed=location.map_embed,
                route_link=location.route_link,
                reverse_order=location.reverse_order
            )
        )
    
    return rx.vstack(
        section_title(
            title,
            text_align=["center", "center", "left", "left"],
            margin_bottom=Spacing.grid_gap,
            width="100%"
        ),
        regular_text(
            description,
            text_align=["center", "center", "left", "left"],
            width="100%"
        ),
        *location_items,
        spacing="0",
        align="start",
        width="100%"
    )