"""Order form section for ordering extra insoles."""

import reflex as rx
from ...components import (
    container,
    section,
    form_label,
    form_input,
    form_textarea,
    form_button,
    form_radio,
    form_select,
)
from ...theme import Colors, Spacing
from ...utils.get_translation import get_translation
from ...states.order_insoles_state import OrderInsolesState


TRANSLATIONS = {
    "nl": {
        "first_name": "Voornaam",
        "first_name_placeholder": "Voornaam",
        "last_name": "Achternaam",
        "last_name_placeholder": "Achternaam",
        "email_label": "Email",
        "email_tooltip": "Vul een geldig e-mailadres in",
        "email_placeholder": "voorbeeld@email.nl",
        "birth_date_label": "Geboortedatum",
        "birth_date_placeholder": "dd-mm-jjjj",
        "insole_type_label": "Soort zolen",
        "insole_type_daily": "Dagelijkse zolen",
        "insole_type_sport": "Sportzolen",
        "insole_type_work": "Zolen voor werkschoenen",
        "quantity_label": "Aantal gewenst",
        "quantity_placeholder": "1",
        "comments_label": "Opmerkingen",
        "comments_placeholder": "Eventuele opmerkingen...",
        "submit_button": "Bestel zolen",
    },
    "de": {
        "first_name": "Vorname",
        "first_name_placeholder": "Vorname",
        "last_name": "Nachname",
        "last_name_placeholder": "Nachname",
        "email_label": "Email",
        "email_tooltip": "Geben Sie eine gültige E-Mail-Adresse ein",
        "email_placeholder": "beispiel@email.de",
        "birth_date_label": "Geburtsdatum",
        "birth_date_placeholder": "tt-mm-jjjj",
        "insole_type_label": "Art der Einlagen",
        "insole_type_daily": "Tägliche Einlagen",
        "insole_type_sport": "Sporteinlagen",
        "insole_type_work": "Einlagen für Arbeitsschuhe",
        "quantity_label": "Gewünschte Anzahl",
        "quantity_placeholder": "1",
        "comments_label": "Anmerkungen",
        "comments_placeholder": "Eventuelle Anmerkungen...",
        "submit_button": "Einlagen bestellen",
    },
    "en": {
        "first_name": "First Name",
        "first_name_placeholder": "First Name",
        "last_name": "Last Name",
        "last_name_placeholder": "Last Name",
        "email_label": "Email",
        "email_tooltip": "Enter a valid email address",
        "email_placeholder": "example@email.com",
        "birth_date_label": "Birth Date",
        "birth_date_placeholder": "dd-mm-yyyy",
        "insole_type_label": "Type of insoles",
        "insole_type_daily": "Daily insoles",
        "insole_type_sport": "Sport insoles",
        "insole_type_work": "Work shoe insoles",
        "quantity_label": "Quantity desired",
        "quantity_placeholder": "1",
        "comments_label": "Comments",
        "comments_placeholder": "Any comments...",
        "submit_button": "Order insoles",
    },
}


def section_order_form(language: str) -> rx.Component:
    """
    Create the order form section for ordering extra insoles.

    The form collects patient information including name, email, birth date,
    insole type, quantity, and any comments.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")

    Returns
    -------
    rx.Component
        A section component containing the order form with all input
        fields and submit button.
    """
    return section(
        container(
            rx.box(
                rx.box(
                    rx.box(
                        form_label(
                            get_translation(TRANSLATIONS, "first_name", language),
                            required=True,
                        ),
                        form_input(
                            placeholder=get_translation(
                                TRANSLATIONS, "first_name_placeholder", language
                            ),
                            value=OrderInsolesState.first_name,
                            on_change=OrderInsolesState.set_first_name,
                        ),
                        flex="1",
                    ),
                    rx.box(
                        form_label(
                            get_translation(TRANSLATIONS, "last_name", language),
                            required=True,
                        ),
                        form_input(
                            placeholder=get_translation(
                                TRANSLATIONS, "last_name_placeholder", language
                            ),
                            value=OrderInsolesState.last_name,
                            on_change=OrderInsolesState.set_last_name,
                        ),
                        flex="1",
                    ),
                    display="flex",
                    gap="1rem",
                    margin_bottom="1.5rem",
                    flex_direction=["column", "column", "row", "row"],
                ),
                rx.box(
                    form_label(
                        get_translation(TRANSLATIONS, "email_label", language),
                        required=True,
                        tooltip_text=get_translation(
                            TRANSLATIONS, "email_tooltip", language
                        ),
                    ),
                    form_input(
                        placeholder=get_translation(
                            TRANSLATIONS, "email_placeholder", language
                        ),
                        value=OrderInsolesState.email,
                        on_change=OrderInsolesState.set_email,
                        input_type="email",
                        on_blur=OrderInsolesState.on_email_blur,
                        show_error=OrderInsolesState.should_show_email_error,
                    ),
                    margin_bottom="1.5rem",
                ),
                rx.box(
                    form_label(
                        get_translation(TRANSLATIONS, "birth_date_label", language),
                        required=True,
                    ),
                    form_input(
                        placeholder=get_translation(
                            TRANSLATIONS, "birth_date_placeholder", language
                        ),
                        value=OrderInsolesState.birth_date,
                        on_change=OrderInsolesState.set_birth_date,
                        input_type="text",
                        on_blur=OrderInsolesState.on_birth_date_blur,
                        show_error=OrderInsolesState.should_show_birth_date_error,
                    ),
                    margin_bottom="1.5rem",
                    max_width="250px",
                ),
                rx.box(
                    form_label(
                        get_translation(TRANSLATIONS, "insole_type_label", language),
                        required=True,
                    ),
                    form_radio(
                        items=[
                            get_translation(
                                TRANSLATIONS, "insole_type_daily", language
                            ),
                            get_translation(
                                TRANSLATIONS, "insole_type_sport", language
                            ),
                            get_translation(TRANSLATIONS, "insole_type_work", language),
                        ],
                        value=OrderInsolesState.insole_type,
                        on_change=OrderInsolesState.set_insole_type,
                    ),
                    margin_bottom="1.5rem",
                ),
                rx.box(
                    form_label(
                        get_translation(TRANSLATIONS, "quantity_label", language),
                        required=True,
                    ),
                    form_select(
                        items=["1", "2", "3"],
                        value=OrderInsolesState.quantity,
                        on_change=OrderInsolesState.set_quantity,
                        placeholder=get_translation(
                            TRANSLATIONS, "quantity_placeholder", language
                        ),
                    ),
                    margin_bottom="1.5rem",
                    max_width="250px",
                ),
                rx.box(
                    form_label(
                        get_translation(TRANSLATIONS, "comments_label", language),
                        required=False,
                    ),
                    form_textarea(
                        placeholder=get_translation(
                            TRANSLATIONS, "comments_placeholder", language
                        ),
                        value=OrderInsolesState.comments,
                        on_change=OrderInsolesState.set_comments,
                    ),
                    margin_bottom="1.5rem",
                ),
                rx.box(
                    form_button(
                        label=get_translation(TRANSLATIONS, "submit_button", language),
                        on_click=OrderInsolesState.submit_order,
                        is_loading=OrderInsolesState.form_submitting,
                        is_disabled=~OrderInsolesState.can_submit_form,
                    ),
                    display="flex",
                    justify_content=["center", "center", "flex-end", "flex-end"],
                    width="100%",
                ),
                background=Colors.backgrounds["green_light"],
                padding=Spacing.form_padding,
                border_radius="8px",
                box_shadow="0 4px 12px rgba(0, 0, 0, 0.1)",
            ),
        ),
        background_color=Colors.backgrounds["white"],
        padding_top="1rem",
    )
