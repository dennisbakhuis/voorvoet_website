"""Introductory text section for the reimbursements page."""
import reflex as rx

from ...theme import Colors
from ...components import section, container, section_title, regular_text


def section_starter() -> rx.Component:
    """
    Create the introductory section for the reimbursements page.

    Displays a welcoming title and introductory text explaining that
    podiatry is often covered by health insurance and directing visitors
    to the comprehensive information below about reimbursements, costs,
    and what to expect during treatment.

    Returns
    -------
    rx.Component
        A section component with white background containing the title
        and introductory text about insurance coverage and costs.
    """
    return section(
        container(
            section_title(
                "Vergoedingen en Kosten",
            ),
            regular_text(
                "Podotherapie wordt vaak vergoed door uw zorgverzekering. Hier vindt u "
                "alle informatie over vergoedingen, kosten en wat u kunt verwachten "
                "bij uw behandeling bij VoorVoet.",
                color=Colors.text["content"],
                max_width="800px",
            ),
        ),
        background=Colors.backgrounds["white"],
        padding_y="3rem",
    )
