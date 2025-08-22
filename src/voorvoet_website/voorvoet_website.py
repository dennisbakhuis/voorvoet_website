# Main application file for the Reflex web app
import reflex as rx

from pages.test import bistro_page
from .theme import theme

app = rx.App(
    stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
        "/styles.css",
    ],
    theme=theme,
    style={
        "font-family": 'Lato, ui-sans-serif, system-ui, sans-serif',
    },
    
)

# app.add_page(index, route="/", title="VoorVoet – Podotherapeut Enschede")
# app.add_page(vergoedingen, route="/vergoedingen", title="Vergoedingen – VoorVoet")
# app.add_page(locatie, route="/locatie", title="Locatie – VoorVoet")
# app.add_page(contact, route="/contact", title="Contact – VoorVoet")

app.add_page(
    component=bistro_page, 
    route="/", 
    title="VoorVoet - Praktijk voor Podotherapie",
)
