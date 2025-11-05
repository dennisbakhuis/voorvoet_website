# Contact form section for the contact page
import reflex as rx
from ...components import container, section, section_title, regular_text, button
from ...theme import Colors, FontSizes
from ...state.contact_state import ContactState
from ...config import config


def section_contact_form() -> rx.Component:
    # Custom styles for form elements
    form_styles = {
        # Placeholder text styling for form inputs
        "input::placeholder, textarea::placeholder": {
            "color": "#888888 !important",
            "opacity": "1 !important",
        },
        # Textarea font size override
        ".rt-TextAreaRoot .rt-TextAreaInput": {
            "font-size": "18px !important",
            "line-height": "1.6 !important",
        },
        # Radio button text size override
        ".rt-RadioGroupRoot .rt-Text": {
            "font-size": "18px !important",
        },
        # Tooltip font size override
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

            # Form container with light background
            rx.box(
                # First name and last name row
                rx.box(
                    # First name field
                    rx.box(
                        rx.text(
                            "Voornaam ",
                            rx.text("*", color="red", display="inline"),
                            font_size=FontSizes.regular,
                            color=Colors.text["heading"],
                            font_weight="500",
                            margin_bottom="0.5rem",
                        ),
                        rx.input(
                            placeholder="Voornaam",
                            value=ContactState.contact_first_name,
                            on_change=ContactState.set_contact_first_name,  # type: ignore
                            width="100%",
                            padding="0.75rem 0.75rem",
                            height="auto",
                            min_height="50px",
                            border_radius="4px",
                            border=f"1px solid {Colors.borders['light']}",
                            font_size=FontSizes.regular,
                            background="white",
                            color=Colors.text["content"],
                        ),
                        flex="1",
                    ),
                    # Last name field
                    rx.box(
                        rx.text(
                            "Achternaam ",
                            rx.text("*", color="red", display="inline"),
                            font_size=FontSizes.regular,
                            color=Colors.text["heading"],
                            font_weight="500",
                            margin_bottom="0.5rem",
                        ),
                        rx.input(
                            placeholder="Achternaam",
                            value=ContactState.contact_last_name,
                            on_change=ContactState.set_contact_last_name,  # type: ignore
                            width="100%",
                            padding="0.75rem 0.75rem",
                            height="auto",
                            min_height="50px",
                            border_radius="4px",
                            border=f"1px solid {Colors.borders['light']}",
                            font_size=FontSizes.regular,
                            background="white",
                            color=Colors.text["content"],
                        ),
                        flex="1",
                    ),
                    display="flex",
                    gap="1rem",
                    margin_bottom="1.5rem",
                    flex_direction=["column", "column", "row", "row", "row"],
                ),

                # Request type radio buttons
                rx.box(
                    rx.text(
                        "Soort verzoek ",
                        rx.text("*", color="red", display="inline"),
                        font_size=FontSizes.regular,
                        color=Colors.text["heading"],
                        font_weight="500",
                        margin_bottom="0.5rem",
                    ),
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

                # Conditional phone number or email field
                rx.cond(
                    ContactState.contact_request_type == "Bel mij terug",
                    # Phone number field
                    rx.box(
                        rx.box(
                            rx.text(
                                "Telefoonnummer (mobiel of vast) ",
                                rx.text("*", color="red", display="inline"),
                                font_size=FontSizes.regular,
                                color=Colors.text["heading"],
                                font_weight="500",
                                display="inline",
                            ),
                            rx.tooltip(
                                rx.html('<i class="fa fa-info-circle" style="color: #3b82f6;"/>'),
                                content="Het telefoonnummer moet precies 10 cijfers bevatten",
                                style={
                                    "backgroundColor": "white",
                                    "color": Colors.text["content"],
                                    "border": f"1px solid {Colors.primary['500']}",
                                    "padding": "0.5rem 0.75rem",
                                    "borderRadius": "4px",
                                    "boxShadow": "0 2px 8px rgba(0, 0, 0, 0.1)",
                                },
                            ),
                            display="flex",
                            align_items="center",
                            gap="0.5rem",
                            margin_bottom="0.5rem",
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
                    # Email field
                    rx.box(
                        rx.box(
                            rx.text(
                                "E-mailadres ",
                                rx.text("*", color="red", display="inline"),
                                font_size=FontSizes.regular,
                                color=Colors.text["heading"],
                                font_weight="500",
                                display="inline",
                            ),
                            rx.tooltip(
                                rx.html('<i class="fa fa-info-circle" style="color: #3b82f6;"/>'),
                                content="Vul een geldig e-mailadres in",
                                style={
                                    "backgroundColor": "white",
                                    "color": Colors.text["content"],
                                    "border": f"1px solid {Colors.primary['500']}",
                                    "padding": "0.5rem 0.75rem",
                                    "borderRadius": "4px",
                                    "boxShadow": "0 2px 8px rgba(0, 0, 0, 0.1)",
                                },
                            ),
                            display="flex",
                            align_items="center",
                            gap="0.5rem",
                            margin_bottom="0.5rem",
                        ),
                        rx.input(
                            placeholder="voorbeeld@email.nl",
                            value=ContactState.contact_email,
                            on_change=ContactState.set_contact_email,  # type: ignore
                            on_blur=ContactState.on_email_blur,
                            width="100%",
                            padding="0.75rem 0.75rem",
                            height="auto",
                            min_height="50px",
                            border_radius="4px",
                            border=rx.cond(
                                ContactState.should_show_email_error,
                                "3px solid red",
                                f"1px solid {Colors.borders['light']}",
                            ),
                            font_size=FontSizes.regular,
                            background="white",
                            color=Colors.text["content"],
                            type="email",
                        ),
                        margin_bottom="1.5rem",
                    ),
                ),

                # Description textarea
                rx.box(
                    rx.text(
                        "Beschrijving van je vraag ",
                        rx.text("*", color="red", display="inline"),
                        font_size=FontSizes.regular,
                        color=Colors.text["heading"],
                        font_weight="500",
                        margin_bottom="0.5rem",
                    ),
                    rx.text_area(
                        placeholder="Jouw beschrijving...",
                        value=ContactState.contact_description,
                        on_change=ContactState.set_contact_description,  # type: ignore
                        width="100%",
                        min_height="120px",
                        padding="0.75rem",
                        border_radius="4px",
                        border=f"1px solid {Colors.borders['light']}",
                        resize="vertical",
                        background="white",
                        color=Colors.text["content"],
                        style={
                            "fontSize": FontSizes.regular,
                            "lineHeight": "1.6",
                        },
                    ),
                    margin_bottom="1.5rem",
                ),

                # Cloudflare Turnstile captcha (conditionally rendered)
                rx.cond(
                    config.turnstile_enabled,
                    rx.box(
                        # Cloudflare Turnstile widget
                        # Site key is loaded from TURNSTILE_SITE_KEY environment variable
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
                                    // Note: Token handling would need to be implemented via backend endpoint
                                    // For now, this is a placeholder for the callback
                                }}
                            </script>
                            """
                        ),
                    ),
                    rx.fragment(),  # Empty fragment when Turnstile is disabled
                ),

                # Submit button (right-aligned on desktop, full width on mobile)
                rx.box(
                    rx.cond(
                        ContactState.form_submitting,
                        # Loading state button
                        rx.box(
                            rx.html("⏳ "),
                            rx.text("Versturen...", display="inline"),
                            border_radius="3px",
                            font_weight="700",
                            font_size=FontSizes.button,
                            padding_x="0.8em",
                            padding_y="0.1em",
                            cursor="wait",
                            display="inline-flex",
                            align_items="center",
                            justify_content="center",
                            text_decoration="none",
                            border="none",
                            white_space="nowrap",
                            bg=Colors.borders["light"],
                            color=Colors.text["muted"],
                            opacity="0.7",
                        ),
                        rx.cond(
                            ContactState.can_submit_form,
                            # Active button
                            button(
                                label="Verstuur het verzoek",
                                on_click=ContactState.submit_contact_form,
                            ),
                            # Disabled button
                            rx.box(
                                rx.text("Verstuur het verzoek"),
                                border_radius="3px",
                                font_weight="700",
                                font_size=FontSizes.button,
                                padding_x="0.8em",
                                padding_y="0.1em",
                                cursor="not-allowed",
                                display="inline-flex",
                                align_items="center",
                                justify_content="center",
                                text_decoration="none",
                                border="none",
                                white_space="nowrap",
                                bg=Colors.borders["light"],
                                color=Colors.text["muted"],
                                opacity="0.6",
                            ),
                        ),
                    ),
                    display="flex",
                    justify_content=["center", "center", "flex-end", "flex-end", "flex-end"],
                    width="100%",
                ),

                # Form styling
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
