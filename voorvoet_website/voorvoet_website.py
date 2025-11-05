"""Main application entry point for the VoorVoet Reflex web application.

This module initializes the Reflex application and defines all routes for the
VoorVoet podiatry practice website. It configures global styles, external
stylesheets (Lato font and Font Awesome icons), and registers all page
components with their respective routes and state handlers.

Routes
------
/ : Home page
/blog/ : Blog listing page
/blog/[slug] : Individual blog post pages
/informatie/ : Information page
/reimbursements/ : Insurance reimbursements page
/contact/ : Contact form page

Notes
-----
The app uses Lato as the primary font family and includes Font Awesome icons
for UI elements. Custom styles are defined in /styles.css.
"""

import reflex as rx

from .pages import page_home, page_blog, page_blog_post, page_information, page_reimbursements, page_contact
from .states import BlogState, ContactState


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
