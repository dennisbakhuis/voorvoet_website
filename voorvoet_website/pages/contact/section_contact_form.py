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
from ...states.contact_state import ContactState
from ...config import config
from ...utils.get_translation import get_translation


TRANSLATIONS = {
    "nl": {
        "first_name": "Voornaam",
        "first_name_placeholder": "Voornaam",
        "last_name": "Achternaam",
        "last_name_placeholder": "Achternaam",
        "request_type": "Soort verzoek",
        "call_back": "Bel mij terug",
        "email_question": "Vraag per email",
        "phone_label": "Telefoonnummer (mobiel of vast)",
        "phone_tooltip": "Het telefoonnummer moet precies 10 cijfers bevatten",
        "phone_placeholder": "0612345678",
        "email_label": "E-mailadres",
        "email_tooltip": "Vul een geldig e-mailadres in",
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
        "request_type": "Art der Anfrage",
        "call_back": "Rufen Sie mich zurück",
        "email_question": "Frage per E-Mail",
        "phone_label": "Telefonnummer (Mobil oder Festnetz)",
        "phone_tooltip": "Die Telefonnummer muss genau 10 Ziffern enthalten",
        "phone_placeholder": "0612345678",
        "email_label": "E-Mail-Adresse",
        "email_tooltip": "Geben Sie eine gültige E-Mail-Adresse ein",
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
        "request_type": "Type of Request",
        "call_back": "Call me back",
        "email_question": "Question via email",
        "phone_label": "Phone Number (mobile or landline)",
        "phone_tooltip": "The phone number must contain exactly 10 digits",
        "phone_placeholder": "0612345678",
        "email_label": "Email Address",
        "email_tooltip": "Enter a valid email address",
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
    (phone or email), and inquiry description. Features validation, error
    states, optional Cloudflare Turnstile captcha, and submission handling.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")

    Returns
    -------
    rx.Component
        A section component containing the contact form with all input
        fields, validation, and submit button with loading states.
    """
    form_styles = {
        ".rt-TooltipContent, .rt-TooltipContent *, [role='tooltip'], [role='tooltip'] *": {
            "font-size": "16px !important",
        },
    }

    return section(
        container(
            rx.box(
                rx.box(
                    rx.box(
                        form_label(get_translation(TRANSLATIONS, "first_name", language), required=True),
                        form_input(
                            placeholder=get_translation(TRANSLATIONS, "first_name_placeholder", language),
                            value=ContactState.contact_first_name,  # type: ignore
                            on_change=ContactState.set_contact_first_name,
                        ),
                        flex="1",
                    ),
                    rx.box(
                        form_label(get_translation(TRANSLATIONS, "last_name", language), required=True),
                        form_input(
                            placeholder=get_translation(TRANSLATIONS, "last_name_placeholder", language),
                            value=ContactState.contact_last_name,  # type: ignore
                            on_change=ContactState.set_contact_last_name,
                        ),
                        flex="1",
                    ),
                    display="flex",
                    gap="1rem",
                    margin_bottom="1.5rem",
                    flex_direction=["column", "column", "row", "row"],
                ),
                rx.box(
                    form_label(get_translation(TRANSLATIONS, "request_type", language), required=True),
                    form_radio(
                        items=[get_translation(TRANSLATIONS, "call_back", language), get_translation(TRANSLATIONS, "email_question", language)],
                        value=ContactState.contact_request_type,
                        on_change=ContactState.set_contact_request_type,
                    ),
                    margin_bottom="1.5rem",
                ),
                rx.cond(
                    ContactState.contact_request_type == get_translation(TRANSLATIONS, "call_back", language),
                    rx.box(
                        form_label(
                            get_translation(TRANSLATIONS, "phone_label", language),
                            required=True,
                            tooltip_text=get_translation(TRANSLATIONS, "phone_tooltip", language),
                        ),
                        form_input(
                            placeholder=get_translation(TRANSLATIONS, "phone_placeholder", language),
                            value=ContactState.contact_phone_value,
                            on_change=ContactState.set_contact_phone_number,
                            on_blur=ContactState.on_phone_blur,
                            input_type="tel",
                            input_mode="numeric",
                            max_length=10,
                            custom_attrs={"oninput": "this.value = this.value.replace(/[^0-9]/g, '').slice(0, 10);"},
                            show_error=ContactState.should_show_phone_error,
                        ),
                        margin_bottom="1.5rem",
                    ),
                    rx.box(
                        form_label(
                            get_translation(TRANSLATIONS, "email_label", language),
                            required=True,
                            tooltip_text=get_translation(TRANSLATIONS, "email_tooltip", language),
                        ),
                        form_input(
                            placeholder=get_translation(TRANSLATIONS, "email_placeholder", language),
                            value=ContactState.contact_email,  # type: ignore
                            on_change=ContactState.set_contact_email,
                            input_type="email",
                            on_blur=ContactState.on_email_blur,
                            show_error=ContactState.should_show_email_error,  # type: ignore
                        ),
                        margin_bottom="1.5rem",
                    ),
                ),
                rx.box(
                    form_label(get_translation(TRANSLATIONS, "description_label", language), required=True),
                    form_textarea(
                        placeholder=get_translation(TRANSLATIONS, "description_placeholder", language),
                        value=ContactState.contact_description,  # type: ignore
                        on_change=ContactState.set_contact_description,
                    ),
                    margin_bottom="1.5rem",
                ),
                # rx.cond(  # TODO: test turnstile
                #     config.turnstile_enabled,
                #     rx.box(
                #         rx.html(
                #             f"""
                #             <div class="cf-turnstile"
                #                  data-sitekey="{config.turnstile_site_key}"
                #                  data-theme="light"
                #                  data-callback="onTurnstileSuccess"
                #                  style="margin-bottom: 1.5rem;">
                #             </div>
                #             <script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>
                #             <script>
                #                 function onTurnstileSuccess(token) {{
                #                     console.log('Turnstile verification successful');
                #                 }}
                #             </script>
                #             """
                #         ),
                #     ),
                #     rx.fragment(),
                # ),
                rx.box(
                    form_button(
                        label=get_translation(TRANSLATIONS, "submit_button", language),
                        on_click=ContactState.submit_contact_form,
                        is_loading=ContactState.form_submitting,
                        is_disabled=~ContactState.can_submit_form,
                    ),
                    display="flex",
                    justify_content=["center", "center", "flex-end", "flex-end"],
                    width="100%",
                ),
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
