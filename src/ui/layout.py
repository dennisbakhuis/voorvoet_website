# Main layout module for the Reflex web app
import reflex as rx
from .primitives import container, nav_link

def navbar():
    return rx.box(
        rx.hstack(
            rx.link(
                rx.hstack(
                    rx.box(class_name="logo-circle"),
                    rx.text("VoorVoet", class_name="logo-text"),
                    align="center",
                ),
                href="/",
                class_name="logo",
            ),
            rx.spacer(),
            rx.hstack(
                nav_link("/", "Home"),
                nav_link("/vergoedingen", "Vergoedingen"),
                nav_link("/locatie", "Locatie"),
                nav_link("/contact", "Contact"),
                spacing="4",
                align="center",
            ),
            class_name="navbar-inner",
        ),
        class_name="navbar",
    )

def footer():
    return rx.box(
        container(
            rx.vstack(
                rx.hstack(
                    rx.text("VoorVoet – Praktijk voor podotherapie", class_name="footer-brand"),
                    rx.spacer(),
                    rx.hstack(
                        rx.link("E-mail", href="mailto:info@voorvoet.nl", class_name="footer-link"),
                        rx.link("Bel", href="tel:+31657750997", class_name="footer-link"),
                        spacing="4",
                    ),
                    align="center",
                ),
                rx.text("Beethovenlaan 10, 7522 HJ Enschede", class_name="footer-muted"),
                rx.text("© VoorVoet", class_name="footer-muted"),
                spacing="2",
            ),
        ),
        class_name="footer",
    )
