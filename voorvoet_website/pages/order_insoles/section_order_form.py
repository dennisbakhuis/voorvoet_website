"""Order form section for ordering extra insoles.

Uses HTML5 validation and client-side JavaScript for zero-lag input experience.
Form data is collected via FormData on submit, not via per-keystroke on_change handlers.
"""

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
from ...utils import get_translation
from ...states import OrderInsolesState
from ...config import config


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
        "turnstile_label": "Automatische robot beveiliging",
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
        "turnstile_label": "Automatischer Roboterschutz",
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
        "turnstile_label": "Automatic robot protection",
        "submit_button": "Order insoles",
    },
}


def section_order_form(language: str) -> rx.Component:
    """
    Create the order form section for ordering extra insoles.

    The form collects patient information including name, email, birth date,
    insole type, quantity, and any comments. Uses HTML5 validation for
    instant client-side feedback without server round-trips during typing.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")

    Returns
    -------
    rx.Component
        A section component containing the order form with HTML5 validation
        and submit button with loading states.
    """
    turnstile_scripts = []
    if config.turnstile_enabled:
        turnstile_scripts = [
            rx.script(
                f"""
                // Define callbacks first
                window.turnstileTokenInsole = null;

                function onTurnstileSuccessInsole(token) {{
                    console.log('Turnstile verification successful (insole form)');
                    window.turnstileTokenInsole = token;
                    const hiddenInput = document.getElementById('turnstile-token-insole');
                    if (hiddenInput) {{
                        hiddenInput.value = token;
                        // Trigger validation update
                        const form = document.getElementById('insole-order-form');
                        if (form) {{
                            form.dispatchEvent(new Event('change', {{ bubbles: true }}));
                        }}
                    }}
                }}

                function onTurnstileErrorInsole(error) {{
                    console.error('Turnstile verification failed (insole form):', error);
                    window.turnstileTokenInsole = null;
                    const hiddenInput = document.getElementById('turnstile-token-insole');
                    if (hiddenInput) {{
                        hiddenInput.value = '';
                        // Trigger validation update
                        const form = document.getElementById('insole-order-form');
                        if (form) {{
                            form.dispatchEvent(new Event('change', {{ bubbles: true }}));
                        }}
                    }}
                }}

                // Load and render Turnstile
                (function() {{
                    if (!window.turnstileLoadedInsole) {{
                        var script = document.createElement('script');
                        script.src = 'https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit&onload=onTurnstileLoadInsole&_=' + Date.now();
                        script.async = true;
                        document.head.appendChild(script);
                        window.turnstileLoadedInsole = true;
                    }}
                }})();

                // Callback when Turnstile API loads
                window.onTurnstileLoadInsole = function() {{
                    console.log('Turnstile API loaded (insole form)');
                    const container = document.getElementById('turnstile-widget-container-insole');
                    if (container && window.turnstile) {{
                        window.turnstile.render('#turnstile-widget-container-insole', {{
                            sitekey: '{config.turnstile_site_key}',
                            theme: 'light',
                            callback: onTurnstileSuccessInsole,
                            'error-callback': onTurnstileErrorInsole
                        }});
                        console.log('Turnstile widget rendered (insole form)');

                        // Trigger validation to update button state
                        const form = document.getElementById('insole-order-form');
                        if (form) {{
                            form.dispatchEvent(new Event('change', {{ bubbles: true }}));
                        }}
                    }}
                }};
                """
            ),
        ]

    form_fields = [
        rx.box(
            rx.box(
                form_label(
                    get_translation(TRANSLATIONS, "first_name", language),
                    required=True,
                ),
                form_input(
                    name="first_name",
                    placeholder=get_translation(
                        TRANSLATIONS, "first_name_placeholder", language
                    ),
                    required=True,
                ),
                flex="1",
            ),
            rx.box(
                form_label(
                    get_translation(TRANSLATIONS, "last_name", language),
                    required=True,
                ),
                form_input(
                    name="last_name",
                    placeholder=get_translation(
                        TRANSLATIONS, "last_name_placeholder", language
                    ),
                    required=True,
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
                tooltip_text=get_translation(TRANSLATIONS, "email_tooltip", language),
            ),
            form_input(
                name="email",
                placeholder=get_translation(
                    TRANSLATIONS, "email_placeholder", language
                ),
                input_type="email",
                required=True,
                pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
            ),
            margin_bottom="1.5rem",
        ),
        rx.box(
            form_label(
                get_translation(TRANSLATIONS, "birth_date_label", language),
                required=True,
            ),
            form_input(
                name="birth_date",
                placeholder=get_translation(
                    TRANSLATIONS, "birth_date_placeholder", language
                ),
                input_type="text",
                required=True,
                pattern=r"^\d{1,2}[-/]\d{1,2}[-/]\d{4}$",
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
                    get_translation(TRANSLATIONS, "insole_type_daily", language),
                    get_translation(TRANSLATIONS, "insole_type_sport", language),
                    get_translation(TRANSLATIONS, "insole_type_work", language),
                ],
                value=OrderInsolesState.insole_type,
                on_change=OrderInsolesState.set_insole_type,
            ),
            rx.el.input(
                type="hidden",
                name="insole_type",
                value=OrderInsolesState.insole_type,
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
            rx.el.input(
                type="hidden",
                name="quantity",
                value=OrderInsolesState.quantity,
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
                name="comments",
                placeholder=get_translation(
                    TRANSLATIONS, "comments_placeholder", language
                ),
            ),
            margin_bottom="1.5rem",
        ),
    ]

    if config.turnstile_enabled:
        form_fields.append(
            rx.box(
                rx.box(
                    form_label(
                        get_translation(TRANSLATIONS, "turnstile_label", language),
                        required=False,
                    ),
                    rx.box(id="turnstile-widget-container-insole"),
                    rx.el.input(
                        type="hidden",
                        id="turnstile-token-insole",
                        name="turnstile_token",
                        value="",
                    ),
                    display="flex",
                    flex_direction="column",
                    gap="0.5rem",
                ),
                rx.box(
                    form_button(
                        label=get_translation(TRANSLATIONS, "submit_button", language),
                        is_loading=OrderInsolesState.form_submitting,
                        button_type="submit",
                    ),
                ),
                display="flex",
                justify_content="space-between",
                align_items="flex-end",
                gap="1rem",
                flex_direction=["column", "column", "row", "row"],
            )
        )
    else:
        form_fields.append(
            rx.box(
                form_button(
                    label=get_translation(TRANSLATIONS, "submit_button", language),
                    is_loading=OrderInsolesState.form_submitting,
                    button_type="submit",
                ),
                display="flex",
                justify_content=["center", "center", "flex-end", "flex-end"],
                width="100%",
            )
        )

    return section(
        rx.script(src="/form-validation.js"),
        *turnstile_scripts,
        container(
            rx.el.form(
                *form_fields,
                id="insole-order-form",
                on_submit=OrderInsolesState.handle_form_submit,
                reset_on_submit=True,
                background=Colors.backgrounds["green_light"],
                padding=Spacing.form_padding,
                border_radius="8px",
                box_shadow="0 4px 12px rgba(0, 0, 0, 0.1)",
            ),
        ),
        background_color=Colors.backgrounds["white"],
        padding_top="1rem",
    )
