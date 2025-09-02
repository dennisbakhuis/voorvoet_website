# Main application file for the Reflex web app
import reflex as rx

from .pages import page_home, page_blog, page_information, page_vergoeding, page_contact


app = rx.App(
    stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/lato-font/3.0.0/css/lato-font.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
        "/styles.css",
    ],
    style={
        "font-family": 'Lato, ui-sans-serif, system-ui, sans-serif',
    },
    
)

app.add_page(
    component=page_home, 
    route="/", 
    title="VoorVoet - Praktijk voor Podotherapie",
)

app.add_page(
    component=page_blog, 
    route="/blog/", 
    title="VoorVoet - Blog - Praktijk voor Podotherapie",
)

app.add_page(
    component=page_information, 
    route="/informatie/", 
    title="VoorVoet - Informatie - Praktijk voor Podotherapie",
)

app.add_page(
    component=page_vergoeding, 
    route="/vergoeding/", 
    title="VoorVoet - Vergoedingen - Praktijk voor Podotherapie",
)

app.add_page(
    component=page_contact, 
    route="/contact/", 
    title="VoorVoet - Contact - Praktijk voor Podotherapie",
)
