"""Pricing data loading and access service."""

from pathlib import Path
from decimal import Decimal
import csv
from typing import Optional

from ..models.pricing import PricingItem, PricingData
from ..config import config


_pricing_cache: Optional[PricingData] = None


def _get_pricing_data_path() -> Path:
    """Get path to pricing CSV file."""
    current_file = Path(__file__)
    project_root = current_file.parent.parent.parent
    return (
        project_root
        / "voorvoet_website"
        / "data"
        / "reimbursements"
        / config.pricing_data_file
    )


def _parse_price(price_str: str) -> Decimal:
    """
    Parse price string to Decimal.

    Parameters
    ----------
    price_str : str
        Price string with Euro symbol, e.g., "€ 130.00"

    Returns
    -------
    Decimal
        Parsed decimal value, e.g., Decimal("130.00")
    """
    clean_price = price_str.replace("€", "").replace(" ", "").strip()
    return Decimal(clean_price)


def _format_price(price_decimal: Decimal) -> str:
    """
    Format Decimal to Dutch locale price string.

    Parameters
    ----------
    price_decimal : Decimal
        Decimal price value, e.g., Decimal("130.00")

    Returns
    -------
    str
        Dutch formatted price string, e.g., "€ 130,00"
    """
    price_str = f"{price_decimal:.2f}".replace(".", ",")
    return f"€ {price_str}"


def load_pricing_data(force_reload: bool = False) -> PricingData:
    """
    Load all pricing data from CSV with caching.

    Reads the pricing CSV file, parses all entries, and builds both
    a list of all items and a dictionary for fast lookup by treatment name.
    Results are cached for subsequent calls unless force_reload is True.

    Parameters
    ----------
    force_reload : bool
        If True, reload data even if cached (default: False)

    Returns
    -------
    PricingData
        Dictionary containing:
        - items: list of all pricing items
        - by_treatment: dict for O(1) lookup by treatment name
    """
    global _pricing_cache

    if _pricing_cache is not None and not force_reload:
        return _pricing_cache

    csv_path = _get_pricing_data_path()
    items: list[PricingItem] = []
    by_treatment: dict[str, PricingItem] = {}

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            treatment = row["Behandeling"].strip()
            price_raw = row["Prijs"].strip()

            if not treatment or not price_raw:
                continue

            price_decimal = _parse_price(price_raw)
            price_formatted = _format_price(price_decimal)

            item: PricingItem = {
                "treatment": treatment,
                "price_raw": price_raw,
                "price_decimal": price_decimal,
                "price_formatted": price_formatted,
            }

            items.append(item)
            by_treatment[treatment] = item

    _pricing_cache = {
        "items": items,
        "by_treatment": by_treatment,
    }

    return _pricing_cache


def get_price(pricing_data: PricingData, treatment: str) -> Optional[PricingItem]:
    """
    Get pricing item by treatment name.

    Parameters
    ----------
    pricing_data : PricingData
        The loaded pricing data
    treatment : str
        Exact treatment name from CSV (case-sensitive)

    Returns
    -------
    PricingItem | None
        Pricing item if found, None otherwise
    """
    return pricing_data["by_treatment"].get(treatment)


def get_price_formatted(
    pricing_data: PricingData, treatment: str, fallback: str = "€ 0,00"
) -> str:
    """
    Get formatted price string for a treatment.

    Parameters
    ----------
    pricing_data : PricingData
        The loaded pricing data
    treatment : str
        Exact treatment name from CSV
    fallback : str
        Fallback price if not found (default: "€ 0,00")

    Returns
    -------
    str
        Formatted price string, e.g., "€ 130,00"
    """
    item = get_price(pricing_data, treatment)
    if item is None:
        print(f"Warning: Treatment not found in pricing data: '{treatment}'")
        return fallback
    return item["price_formatted"]
