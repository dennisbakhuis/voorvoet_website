# Configuration-driven information cards section
import reflex as rx
from typing import List

from ..theme import Spacing
from .responsive_grid import responsive_grid
from .information_card import information_card


class CardConfig:
    """Configuration class for information card data"""
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
    Create a responsive grid of information cards from configuration
    
    Args:
        cards: List of CardConfig objects
        columns: Responsive column configuration
        spacing: Grid spacing (defaults to theme spacing)
        justify_items: Grid item justification
        **grid_props: Additional props passed to responsive_grid
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
