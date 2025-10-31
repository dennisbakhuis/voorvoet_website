# Contact form section for the contact page
import reflex as rx
from ...components import container, section, section_title, regular_text, button
from ...theme import Colors, FontSizes


def section_contact_form() -> rx.Component:
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
                        default_value="Bel mij terug",
                        direction="column",
                        spacing="2",
                        color=Colors.text["content"],
                        font_size=FontSizes.regular,
                    ),
                    margin_bottom="1.5rem",
                ),

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
                        ),
                        display="flex",
                        align_items="center",
                        gap="0.5rem",
                        margin_bottom="0.5rem",
                    ),
                    rx.input(
                        placeholder="0612345678",
                        width="100%",
                        padding="0.75rem 0.75rem",
                        height="auto",
                        min_height="50px",
                        border_radius="4px",
                        border=f"1px solid {Colors.borders['light']}",
                        font_size=FontSizes.regular,
                        background="white",
                        color=Colors.text["content"],
                        type="tel",
                        max_length=10,
                        pattern="[0-9]{10}",
                    ),
                    margin_bottom="1.5rem",
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

                # Cloudflare Turnstile captcha
                rx.box(
                    rx.text(
                        "Beveiliging tegen robots",
                        font_size=FontSizes.regular,
                        color=Colors.text["heading"],
                        font_weight="500",
                        margin_bottom="0.5rem",
                    ),
                    # Placeholder for Cloudflare Turnstile widget
                    rx.box(
                        rx.html(
                            """
                            <div class="cf-turnstile" data-sitekey="0x4AAAAAAAxxxxxxxxxx" data-theme="light"></div>
                            """
                        ),
                        margin_bottom="1.5rem",
                    ),
                ),

                # Submit button (right-aligned on desktop, full width on mobile)
                rx.box(
                    button(
                        label="Verstuur het verzoek",
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
            ),
        ),
        background_color=Colors.backgrounds["white"],
    )
