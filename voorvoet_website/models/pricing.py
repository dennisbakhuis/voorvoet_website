"""Pricing data models for VoorVoet website."""

from typing import TypedDict
from decimal import Decimal


class PricingItem(TypedDict):
    """
    Single pricing entry with treatment name and price.

    Attributes
    ----------
    treatment : str
        Dutch treatment name from CSV, e.g., "Podotherapeutische zolen extra paar"
    price_raw : str
        Raw price string from CSV with symbol, e.g., "€ 130.00"
    price_decimal : Decimal
        Decimal value for precise calculations, e.g., Decimal("130.00")
    price_formatted : str
        Dutch locale formatted price for display, e.g., "€ 130,00"
    """

    treatment: str
    price_raw: str
    price_decimal: Decimal
    price_formatted: str


class PricingData(TypedDict):
    """
    Container for all pricing data with lookup capabilities.

    Attributes
    ----------
    items : list[PricingItem]
        Complete list of all pricing items in order from CSV
    by_treatment : dict[str, PricingItem]
        Dictionary for O(1) lookup of pricing by treatment name
    """

    items: list[PricingItem]
    by_treatment: dict[str, PricingItem]
