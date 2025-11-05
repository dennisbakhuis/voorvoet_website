"""Configuration-driven information cards section."""
import reflex as rx
from typing import List

from ..theme import Spacing
from .responsive_grid import responsive_grid
from .information_card import information_card


class CardConfig:
    """
    Configuration class for information card data.

    Attributes
    ----------
    title : str
        Card title text.
    description : str
        Card description text.
    icon : str
        FontAwesome icon class name.
    bg_color : str
        Background color for the card. Default is "white".
    show_box : bool
        Whether to show card box border and shadow. Default is False.
    button_text : str
        Text for the call-to-action button. Default is "Lees meer".
    button_link : str
        URL for the call-to-action button. Default is "#".
    """
    def __init__(
        self,
        title: str,
        description: str,
        icon: str,
        bg_color: str = "white",
        show_box: bool = False,
        button_text: str = "Lees meer",
        button_link: str = "#"
    ):
        self.title = title
        self.description = description
        self.icon = icon
        self.bg_color = bg_color
        self.show_box = show_box
        self.button_text = button_text
        self.button_link = button_link


def information_cards_grid(
    cards: List[CardConfig],
    columns: List[int] = [1, 2, 3],
    spacing: str | None = None,
    justify_items: str = "center",
    **grid_props
) -> rx.Component:
    """
    Create a responsive grid of information cards from configuration.

    Creates a grid layout that automatically adjusts the number of columns
    based on screen size. Each card is generated from a CardConfig object
    with consistent styling and spacing.

    Parameters
    ----------
    cards : list[CardConfig]
        List of CardConfig objects defining card content and styling.
    columns : list[int], optional
        Responsive column configuration for different breakpoints.
        Default is [1, 2, 3] (1 column mobile, 2 tablet, 3 desktop).
    spacing : str | None, optional
        Grid gap spacing between cards. If None, uses Spacing.grid_gap
        from theme. Default is None.
    justify_items : str, optional
        Grid item justification alignment. Default is "center".
    **grid_props : dict
        Additional style properties to apply to the responsive_grid.
        These will override the default styles.

    Returns
    -------
    rx.Component
        A responsive grid component containing information cards.
    """
    
    if spacing is None:
        spacing = Spacing.grid_gap
    
    card_components = []
    for card in cards:
        card_components.append(
            information_card(
                title=card.title,
                description=card.description,
                icon=card.icon,
                bg_color=card.bg_color,
                show_box=card.show_box,
                button_text=card.button_text,
                button_link=card.button_link
            )
        )
    
    return responsive_grid(
        *card_components,
        columns=columns,
        spacing=spacing,
        justify_items=justify_items,
        **grid_props
    )
