"""404 page composition."""

import reflex as rx

from .section_hero import section_hero
from .section_content import section_content
from ..shared_sections import footer, header


def page_not_found() -> rx.Component:
    """
    Create the complete 404 error page.

    Returns
    -------
    rx.Component
        A fragment containing the 404 page sections.
    """
    return rx.fragment(
        header("nl", page_key=None),
        rx.box(
            section_hero(),
            section_content(),
            id="main-content",
            role="main",
        ),
        footer("nl"),
    )
