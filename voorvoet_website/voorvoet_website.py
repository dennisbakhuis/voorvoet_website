# Main application file for the Reflex web app
import reflex as rx

from .pages import page_home, page_blog, page_blog_post, page_information, page_reimbursements, page_contact
from .state import BlogState, ContactState


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
    on_load=BlogState.load_posts,
)

app.add_page(
    component=page_blog_post,
    route="/blog/[slug]",
    title="VoorVoet - Blog - Praktijk voor Podotherapie",
    on_load=BlogState.load_post_by_slug,
)

app.add_page(
    component=page_information, 
    route="/informatie/", 
    title="VoorVoet - Informatie - Praktijk voor Podotherapie",
)

app.add_page(
    component=page_reimbursements,
    route="/reimbursements/",
    title="VoorVoet - Reimbursements - Praktijk voor Podotherapie",
)

app.add_page(
    component=page_contact, 
    route="/contact/", 
    title="VoorVoet - Contact - Praktijk voor Podotherapie",
)
