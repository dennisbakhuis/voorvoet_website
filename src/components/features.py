# Features section for the Reflex web app
import reflex as rx
from ui.primitives import section

def features():
    items = [
        ("Moderne diagnostiek", "Geavanceerde methoden voor een passende behandeling."),
        ("Persoonlijke aanpak", "Ruimte voor je verhaal en doelen."),
        ("Snel geholpen", "Korte lijnen en duidelijke stappen."),
    ]
    return section(
        "Waarom VoorVoet",
        rx.grid(
            *[
                rx.box(
                    rx.text(title, class_name="card-title"),
                    rx.text(desc, class_name="card-text"),
                    class_name="card",
                )
                for title, desc in items
            ],
            columns=rx.breakpoints(initial="1", md="3"),
            gap="4",
        ),
    )