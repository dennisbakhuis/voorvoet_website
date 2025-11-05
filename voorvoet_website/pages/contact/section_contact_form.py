"""Contact form section with form fields for user inquiries."""
import reflex as rx
from ...components import (
    container,
    section,
    section_title,
    regular_text,
    form_label,
    form_input,
    form_textarea,
    form_button,
)
from ...theme import Colors, FontSizes
from ...states.contact_state import ContactState
from ...config import config


def section_contact_form() -> rx.Component:
    """
    Create the contact form section with form fields.

    The form collects user information including name, contact preference
    (phone or email), and inquiry description. Features validation, error
    states, optional Cloudflare Turnstile captcha, and submission handling.

    Returns
    -------
    rx.Component
        A section component containing the contact form with all input
        fields, validation, and submit button with loading states.
    """
    form_styles = {
        "input::placeholder, textarea::placeholder": {
            "color": "#888888 !important",
            "opacity": "1 !important",
        },
        ".rt-TextAreaRoot .rt-TextAreaInput": {
            "font-size": "18px !important",
            "line-height": "1.6 !important",
        },
        ".rt-RadioGroupRoot .rt-Text": {
            "font-size": "18px !important",
        },
        ".rt-TooltipContent, .rt-TooltipContent *, [role='tooltip'], [role='tooltip'] *": {
            "font-size": "16px !important",
        },
    }

    return section(
        container(
            section_title("Contact"),
            regular_text(
                "Heb je een vraag stel hem dan via onderstaand formulier. Je kunt antwoord krijgen via email of een terugbelverzoek sturen.",
                color=Colors.text["content"],
                margin_bottom="2rem",
            ),
            rx.box(
                rx.box(
                    rx.box(
                        form_label("Voornaam", required=True),
                        form_input(
                            placeholder="Voornaam",
                            value=ContactState.contact_first_name,
                            on_change=ContactState.set_contact_first_name,
                        ),
                        flex="1",
                    ),
                    rx.box(
                        form_label("Achternaam", required=True),
                        form_input(
                            placeholder="Achternaam",
                            value=ContactState.contact_last_name,
                            on_change=ContactState.set_contact_last_name,
                        ),
                        flex="1",
                    ),
                    display="flex",
                    gap="1rem",
                    margin_bottom="1.5rem",
                    flex_direction=["column", "column", "row", "row", "row"],
                ),
                rx.box(
                    form_label("Soort verzoek", required=True),
                    rx.radio(
                        ["Bel mij terug", "Vraag per email"],
                        value=ContactState.contact_request_type,
                        on_change=ContactState.set_contact_request_type,
                        direction="column",
                        spacing="2",
                        color=Colors.text["content"],
                        font_size=FontSizes.regular,
                    ),
                    margin_bottom="1.5rem",
                ),
                rx.cond(
                    ContactState.contact_request_type == "Bel mij terug",
                    rx.box(
                        form_label(
                            "Telefoonnummer (mobiel of vast)",
                            required=True,
                            tooltip_text="Het telefoonnummer moet precies 10 cijfers bevatten",
                        ),
                        rx.el.input(
                            placeholder="0612345678",
                            value=ContactState.contact_phone_value,
                            on_change=ContactState.set_contact_phone_number,
                            on_blur=ContactState.on_phone_blur,
                            custom_attrs={"oninput": "this.value = this.value.replace(/[^0-9]/g, '').slice(0, 10);"},
                            width="100%",
                            padding="0.75rem 0.75rem",
                            height="auto",
                            min_height="50px",
                            border_radius="4px",
                            font_size=FontSizes.regular,
                            background="white",
                            color=Colors.text["content"],
                            type="tel",
                            input_mode="numeric",
                            max_length=10,
                            border=rx.cond(
                                ContactState.should_show_phone_error,
                                "3px solid red",
                                f"1px solid {Colors.borders['light']}",
                            ),
                        ),
                        margin_bottom="1.5rem",
                    ),
                    rx.box(
                        form_label(
                            "E-mailadres",
                            required=True,
                            tooltip_text="Vul een geldig e-mailadres in",
                        ),
                        form_input(
                            placeholder="voorbeeld@email.nl",
                            value=ContactState.contact_email,
                            on_change=ContactState.set_contact_email,
                            input_type="email",
                            on_blur=ContactState.on_email_blur,
                            show_error=ContactState.should_show_email_error,
                        ),
                        margin_bottom="1.5rem",
                    ),
                ),
                rx.box(
                    form_label("Beschrijving van je vraag", required=True),
                    form_textarea(
                        placeholder="Jouw beschrijving...",
                        value=ContactState.contact_description,
                        on_change=ContactState.set_contact_description,
                    ),
                    margin_bottom="1.5rem",
                ),
                rx.cond(
                    config.turnstile_enabled,
                    rx.box(
                        rx.html(
                            f"""
                            <div class="cf-turnstile"
                                 data-sitekey="{config.turnstile_site_key}"
                                 data-theme="light"
                                 data-callback="onTurnstileSuccess"
                                 style="margin-bottom: 1.5rem;">
                            </div>
                            <script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>
                            <script>
                                function onTurnstileSuccess(token) {{
                                    console.log('Turnstile verification successful');
                                }}
                            </script>
                            """
                        ),
                    ),
                    rx.fragment(),
                ),
                rx.box(
                    form_button(
                        label="Verstuur het verzoek",
                        on_click=ContactState.submit_contact_form,
                        is_loading=ContactState.form_submitting,
                        is_disabled=~ContactState.can_submit_form,
                    ),
                    display="flex",
                    justify_content=["center", "center", "flex-end", "flex-end", "flex-end"],
                    width="100%",
                ),
                background=Colors.backgrounds["green_light"],
                padding=["1.5rem", "1.5rem", "2rem", "2.5rem", "3rem"],
                border_radius="8px",
                box_shadow="0 4px 12px rgba(0, 0, 0, 0.1)",
                max_width="700px",
                style=form_styles,
            ),
        ),
        background_color=Colors.backgrounds["white"],
    )
