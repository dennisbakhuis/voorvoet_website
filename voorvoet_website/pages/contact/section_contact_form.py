"""Contact form section with form fields for user inquiries."""

import reflex as rx

from ...components import (
    container,
    section,
    form_label,
    form_input,
    form_textarea,
    form_button,
    form_radio,
)
from ...theme import Colors, Spacing
from ...states import ContactState
from ...utils import get_translation
from ...config import config


TRANSLATIONS = {
    "nl": {
        "first_name": "Voornaam",
        "first_name_placeholder": "Voornaam",
        "last_name": "Achternaam",
        "last_name_placeholder": "Achternaam",
        "request_type": "Voorkeur voor contact",
        "call_back": "Bel mij terug",
        "email_question": "Contact per email",
        "phone_label": "Telefoonnummer",
        "phone_placeholder": "0612345678",
        "email_label": "E-mailadres",
        "email_placeholder": "voorbeeld@email.nl",
        "description_label": "Beschrijving van je vraag",
        "description_placeholder": "Jouw beschrijving...",
        "submit_button": "Verstuur verzoek",
    },
    "de": {
        "first_name": "Vorname",
        "first_name_placeholder": "Vorname",
        "last_name": "Nachname",
        "last_name_placeholder": "Nachname",
        "request_type": "Kontaktpräferenz",
        "call_back": "Rufen Sie mich zurück",
        "email_question": "Kontakt per E-Mail",
        "phone_label": "Telefonnummer",
        "phone_placeholder": "0612345678",
        "email_label": "E-Mail-Adresse",
        "email_placeholder": "beispiel@email.de",
        "description_label": "Beschreibung Ihrer Frage",
        "description_placeholder": "Ihre Beschreibung...",
        "submit_button": "Anfrage senden",
    },
    "en": {
        "first_name": "First Name",
        "first_name_placeholder": "First Name",
        "last_name": "Last Name",
        "last_name_placeholder": "Last Name",
        "request_type": "Contact Preference",
        "call_back": "Call me back",
        "email_question": "Contact via email",
        "phone_label": "Phone Number",
        "phone_placeholder": "0612345678",
        "email_label": "Email Address",
        "email_placeholder": "example@email.com",
        "description_label": "Description of your question",
        "description_placeholder": "Your description...",
        "submit_button": "Submit Request",
    },
}


def section_contact_form(language: str) -> rx.Component:
    """
    Create the contact form section with form fields.

    The form collects user information including name, contact preference
    (phone or email), and inquiry description. Uses HTML5 validation for
    instant client-side feedback without server round-trips during typing.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")

    Returns
    -------
    rx.Component
        A section component containing the contact form with HTML5 validation
        and submit button with loading states.
    """
    form_styles = {
        ".rt-TooltipContent, .rt-TooltipContent *, [role='tooltip'], [role='tooltip'] *": {
            "font-size": "16px !important",
        },
    }

    turnstile_scripts = []
    if config.turnstile_enabled:
        turnstile_scripts = [
            rx.script(
                f"""
                // Define callbacks first
                window.turnstileToken = null;

                function onTurnstileSuccess(token) {{
                    console.log('Turnstile verification successful');
                    window.turnstileToken = token;
                    const hiddenInput = document.getElementById('turnstile-token');
                    if (hiddenInput) {{
                        hiddenInput.value = token;
                    }}
                }}

                function onTurnstileError(error) {{
                    console.error('Turnstile verification failed:', error);
                    window.turnstileToken = null;
                    const hiddenInput = document.getElementById('turnstile-token');
                    if (hiddenInput) {{
                        hiddenInput.value = '';
                    }}
                }}

                // Load and render Turnstile
                (function() {{
                    if (!window.turnstileLoaded) {{
                        var script = document.createElement('script');
                        script.src = 'https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit&onload=onTurnstileLoad&_=' + Date.now();
                        script.async = true;
                        document.head.appendChild(script);
                        window.turnstileLoaded = true;
                    }}
                }})();

                // Callback when Turnstile API loads
                window.onTurnstileLoad = function() {{
                    console.log('Turnstile API loaded');
                    const container = document.getElementById('turnstile-widget-container');
                    if (container && window.turnstile) {{
                        window.turnstile.render('#turnstile-widget-container', {{
                            sitekey: '{config.turnstile_site_key}',
                            theme: 'light',
                            callback: onTurnstileSuccess,
                            'error-callback': onTurnstileError
                        }});
                        console.log('Turnstile widget rendered');
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
                get_translation(TRANSLATIONS, "request_type", language),
                required=True,
            ),
            form_radio(
                items=[
                    get_translation(TRANSLATIONS, "call_back", language),
                    get_translation(TRANSLATIONS, "email_question", language),
                ],
                value=ContactState.request_type,
                on_change=ContactState.set_request_type,
            ),
            rx.el.input(
                type="hidden",
                name="request_type",
                value=ContactState.request_type,
            ),
            margin_bottom="1.5rem",
        ),
        rx.box(
            form_label(
                get_translation(TRANSLATIONS, "phone_label", language),
                required=True,
            ),
            form_input(
                name="phone",
                placeholder=get_translation(
                    TRANSLATIONS, "phone_placeholder", language
                ),
                input_type="tel",
                input_mode="numeric",
                required=True,
                pattern=r"^[0-9+\-\s]+$",
            ),
            margin_bottom="1.5rem",
        ),
        rx.box(
            form_label(
                get_translation(TRANSLATIONS, "email_label", language),
                required=True,
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
                get_translation(TRANSLATIONS, "description_label", language),
                required=True,
            ),
            form_textarea(
                name="description",
                placeholder=get_translation(
                    TRANSLATIONS, "description_placeholder", language
                ),
                required=True,
            ),
            margin_bottom="1.5rem",
        ),
    ]

    if config.turnstile_enabled:
        form_fields.append(
            rx.box(
                rx.box(
                    rx.box(id="turnstile-widget-container"),
                    rx.el.input(
                        type="hidden",
                        id="turnstile-token",
                        name="turnstile_token",
                        value="",
                    ),
                    display="flex",
                    align_items="flex-end",
                ),
                rx.box(
                    form_button(
                        label=get_translation(TRANSLATIONS, "submit_button", language),
                        is_loading=ContactState.form_submitting,
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
                    is_loading=ContactState.form_submitting,
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
                id="contact-form",
                on_submit=ContactState.handle_form_submit,
                reset_on_submit=True,
                background=Colors.backgrounds["green_light"],
                padding=Spacing.form_padding,
                border_radius="8px",
                box_shadow="0 4px 12px rgba(0, 0, 0, 0.1)",
                style=form_styles,
            ),
        ),
        background_color=Colors.backgrounds["white"],
        padding_top="1rem",
    )
