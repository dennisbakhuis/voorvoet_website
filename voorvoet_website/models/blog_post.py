"""BlogPost data model definition using TypedDict."""

from typing import TypedDict, Any, Literal
from datetime import datetime


ContentType = Literal["heading", "paragraph", "markdown", "image", "button", "list"]
ContentDict = dict[str, Any]

FALLBACK_DATE = datetime(2023, 2, 1)

MONTHS_NL = {
    1: "januari",
    2: "februari",
    3: "maart",
    4: "april",
    5: "mei",
    6: "juni",
    7: "juli",
    8: "augustus",
    9: "september",
    10: "oktober",
    11: "november",
    12: "december",
}

MONTHS_DE = {
    1: "Januar",
    2: "Februar",
    3: "März",
    4: "April",
    5: "Mai",
    6: "Juni",
    7: "Juli",
    8: "August",
    9: "September",
    10: "Oktober",
    11: "November",
    12: "Dezember",
}

MONTHS_EN = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}


class BlogPostDict(TypedDict):
    """
    Blog post data structure with all pre-computed fields.

    All dynamic properties (formatted_date, url, datetime) are pre-computed
    during parsing, so this is a plain dictionary with no methods.
    """

    title: str
    slug: str
    summary: str
    author: str
    category: str
    language: str
    date: str
    formatted_date: str
    datetime_iso: str
    thumbnail_fallback: str
    thumbnail_avif: str
    thumbnail_webp: str
    thumbnail_alt: str
    content: str
    content_objects: list[dict[str, Any]]
    url: str
    filename: str
    story_number: str


def parse_datetime(date_str: str) -> datetime:
    """
    Parse date string to datetime (YYYY-MM-DD, DD-MM-YYYY, or ISO format).

    Parameters
    ----------
    date_str : str
        Date string in one of the supported formats

    Returns
    -------
    datetime
        Parsed datetime object, or FALLBACK_DATE if parsing fails
    """
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        try:
            return datetime.strptime(date_str, "%d-%m-%Y")
        except ValueError:
            try:
                return datetime.fromisoformat(date_str)
            except ValueError:
                print(f"Warning: Could not parse date '{date_str}'")
                return FALLBACK_DATE


def format_date(date_str: str, language: str) -> str:
    """
    Format date with language-specific month names.

    Parameters
    ----------
    date_str : str
        Date string to format
    language : str
        Language code ("nl", "de", or "en")

    Returns
    -------
    str
        Formatted date string with language-specific month names
    """
    date_obj = parse_datetime(date_str)

    if language == "de":
        month_name = MONTHS_DE[date_obj.month]
        return f"{date_obj.day}. {month_name} {date_obj.year}"
    elif language == "en":
        month_name = MONTHS_EN[date_obj.month]
        return f"{month_name} {date_obj.day}, {date_obj.year}"
    else:
        month_name = MONTHS_NL[date_obj.month]
        return f"{date_obj.day} {month_name} {date_obj.year}"
