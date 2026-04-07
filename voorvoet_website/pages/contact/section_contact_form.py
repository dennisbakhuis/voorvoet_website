"""Contact form section with form fields for user inquiries."""

import json

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
from ...theme import Colors, FontSizes, Spacing
from ...states import ContactState
from ...utils import get_translation
from ...config import config


PRACTICE_PHONE_DISPLAY = "+31 (0) 6 577 509 97"


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
        "phone_tooltip": "Beide contactgegevens zijn vereist voor het geval we de andere methode moeten gebruiken",
        "phone_placeholder": "0612345678",
        "email_label": "E-mailadres",
        "email_tooltip": "Beide contactgegevens zijn vereist voor het geval we de andere methode moeten gebruiken",
        "email_placeholder": "voorbeeld@email.nl",
        "description_label": "Beschrijving van je vraag",
        "description_placeholder": "Jouw beschrijving...",
        "turnstile_label": "Verificatie",
        "turnstile_blocked": (
            "De verificatie kon niet laden. Schakel je adblocker uit voor "
            f"deze pagina, of bel ons direct op {PRACTICE_PHONE_DISPLAY}."
        ),
        "hint_fields": "Vul alle verplichte velden in.",
        "hint_verification": "Voltooi de verificatie hierboven.",
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
        "phone_tooltip": "Beide Kontaktdaten sind erforderlich, falls wir die andere Methode verwenden müssen",
        "phone_placeholder": "0612345678",
        "email_label": "E-Mail-Adresse",
        "email_tooltip": "Beide Kontaktdaten sind erforderlich, falls wir die andere Methode verwenden müssen",
        "email_placeholder": "beispiel@email.de",
        "description_label": "Beschreibung Ihrer Frage",
        "description_placeholder": "Ihre Beschreibung...",
        "turnstile_label": "Verifizierung",
        "turnstile_blocked": (
            "Die Verifizierung konnte nicht geladen werden. Deaktivieren Sie "
            "Ihren Adblocker für diese Seite oder rufen Sie uns direkt an: "
            f"{PRACTICE_PHONE_DISPLAY}."
        ),
        "hint_fields": "Bitte füllen Sie alle Pflichtfelder aus.",
        "hint_verification": "Bitte schließen Sie die Verifizierung oben ab.",
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
        "phone_tooltip": "Both contact details are required in case we need to use the other method",
        "phone_placeholder": "0612345678",
        "email_label": "Email Address",
        "email_tooltip": "Both contact details are required in case we need to use the other method",
        "email_placeholder": "example@email.com",
        "description_label": "Description of your question",
        "description_placeholder": "Your description...",
        "turnstile_label": "Verification",
        "turnstile_blocked": (
            "Verification could not load. Please disable your ad-blocker for "
            f"this page, or call us directly at {PRACTICE_PHONE_DISPLAY}."
        ),
        "hint_fields": "Please fill in all required fields.",
        "hint_verification": "Please complete the verification above.",
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
        blocked_message_json = json.dumps(
            get_translation(TRANSLATIONS, "turnstile_blocked", language)
        )
        turnstile_scripts = [
            rx.script(
                f"""
                // Define callbacks first
                window.turnstileToken = null;

                function showTurnstileFallback() {{
                    const container = document.getElementById('turnstile-widget-container');
                    if (container && !container.dataset.fallbackShown) {{
                        container.dataset.fallbackShown = 'true';
                        container.innerHTML = '';
                        var msg = document.createElement('div');
                        msg.textContent = {blocked_message_json};
                        msg.style.border = '2px solid red';
                        msg.style.background = '#fff5f5';
                        msg.style.color = '#a00';
                        msg.style.padding = '0.75rem';
                        msg.style.borderRadius = '4px';
                        msg.style.fontSize = '1rem';
                        msg.setAttribute('role', 'alert');
                        container.appendChild(msg);
                    }}
                    const hiddenInput = document.getElementById('turnstile-token');
                    if (hiddenInput) {{ hiddenInput.value = ''; }}
                    window.turnstileToken = null;
                    const form = document.getElementById('contact-form');
                    if (form) {{
                        form.dataset.turnstileBlocked = 'true';
                        form.dispatchEvent(new Event('change', {{ bubbles: true }}));
                    }}
                }}

                function onTurnstileSuccess(token) {{
                    window.turnstileToken = token;
                    const hiddenInput = document.getElementById('turnstile-token');
                    if (hiddenInput) {{
                        hiddenInput.value = token;
                        const form = document.getElementById('contact-form');
                        if (form) {{
                            delete form.dataset.turnstileBlocked;
                            form.dispatchEvent(new Event('change', {{ bubbles: true }}));
                        }}
                    }}
                }}

                function onTurnstileError(error) {{
                    console.error('Turnstile verification failed:', error);
                    showTurnstileFallback();
                }}

                // Load and render Turnstile
                (function() {{
                    if (!window.turnstileLoaded) {{
                        var script = document.createElement('script');
                        script.src = 'https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit&onload=onTurnstileLoad&_=' + Date.now();
                        script.async = true;
                        script.onerror = function() {{
                            console.error('Turnstile script failed to load');
                            showTurnstileFallback();
                        }};
                        document.head.appendChild(script);
                        window.turnstileLoaded = true;

                        // Fallback timeout: if Turnstile hasn't initialized in 8s, show message
                        setTimeout(function() {{
                            if (!window.turnstile) {{
                                showTurnstileFallback();
                            }}
                        }}, 8000);
                    }}
                }})();

                // Callback when Turnstile API loads
                window.onTurnstileLoad = function() {{
                    const container = document.getElementById('turnstile-widget-container');
                    if (container && window.turnstile && !container.dataset.fallbackShown) {{
                        window.turnstile.render('#turnstile-widget-container', {{
                            sitekey: '{config.turnstile_site_key}',
                            theme: 'light',
                            callback: onTurnstileSuccess,
                            'error-callback': onTurnstileError
                        }});

                        const form = document.getElementById('contact-form');
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
            rx.box(
                form_label(
                    get_translation(TRANSLATIONS, "phone_label", language),
                    required=True,
                    tooltip_text=get_translation(
                        TRANSLATIONS, "phone_tooltip", language
                    ),
                ),
                form_input(
                    name="phone",
                    placeholder=get_translation(
                        TRANSLATIONS, "phone_placeholder", language
                    ),
                    input_type="tel",
                    input_mode="tel",
                    required=True,
                    pattern=r"^[0-9+\-\s().\/]{8,}$",
                ),
                flex="1",
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
                    name="email",
                    placeholder=get_translation(
                        TRANSLATIONS, "email_placeholder", language
                    ),
                    input_type="email",
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
                direction=["column", "column", "row", "row"],
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

    hint_span = rx.el.span(
        id="contact-form-hint",
        custom_attrs={
            "data-msg-fields": get_translation(TRANSLATIONS, "hint_fields", language),
            "data-msg-verification": get_translation(
                TRANSLATIONS, "hint_verification", language
            ),
            "aria-live": "polite",
        },
        color=Colors.text["muted"],
        font_size=FontSizes.small,
        display="block",
        min_height="1.5rem",
        margin_top="0.5rem",
    )

    if config.turnstile_enabled:
        form_fields.append(
            rx.box(
                rx.box(
                    form_label(
                        get_translation(TRANSLATIONS, "turnstile_label", language),
                        required=False,
                    ),
                    rx.box(id="turnstile-widget-container"),
                    rx.el.input(
                        type="hidden",
                        id="turnstile-token",
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
                        is_loading=ContactState.form_submitting,
                        button_type="submit",
                    ),
                    hint_span,
                    display="flex",
                    flex_direction="column",
                    align_items=["center", "center", "flex-end", "flex-end"],
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
                hint_span,
                display="flex",
                flex_direction="column",
                align_items=["center", "center", "flex-end", "flex-end"],
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
