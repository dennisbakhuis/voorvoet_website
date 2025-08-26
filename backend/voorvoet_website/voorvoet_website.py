# Main application file for the Reflex web app
import reflex as rx

from .pages.home_page import home_page
from .theme import theme

app = rx.App(
    stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/lato-font/3.0.0/css/lato-font.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
        "/styles.css",
    ],
    theme=theme,
    style={
        "font-family": 'Lato, ui-sans-serif, system-ui, sans-serif',
    },
    
)

app.add_page(
    component=home_page, 
    route="/", 
    title="VoorVoet - Praktijk voor Podotherapie",
)
