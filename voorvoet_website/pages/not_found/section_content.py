"""Content section for the 404 page."""

import reflex as rx

from ...theme import Colors, Spacing
from ...components import section, container, header, regular_text, button, jumbo_text


def section_content() -> rx.Component:
    """
    Create the 404 error page content section.

    Returns
    -------
    rx.Component
        A centered section with 404 error message and call-to-action.
    """
    return section(
        container(
            rx.box(
                jumbo_text(
                    "404",
                    text_align="center",
                    margin_bottom=Spacing.section_gap,
                ),
                header(
                    "Pagina niet gevonden",
                    level=1,
                    text_align="center",
                ),
                regular_text(
                    "Sorry, de pagina die u zoekt bestaat niet of is verplaatst. Controleer of de URL correct is of ga terug naar de homepage.",
                    color=Colors.text["content"],
                    text_align="center",
                    max_width="600px",
                    margin_x="auto",
                ),
                rx.box(
                    button(
                        "Ga naar homepage",
                        href="/nl",
                    ),
                    margin_top="2rem",
                ),
                display="flex",
                flex_direction="column",
                align_items="center",
                text_align="center",
            ),
        ),
        background=Colors.backgrounds["white"],
        padding_y="4rem",
    )
