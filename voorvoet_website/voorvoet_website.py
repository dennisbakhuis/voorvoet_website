"""Main application entry point for the VoorVoet Reflex web application.

This module initializes the Reflex application and defines all routes for the
VoorVoet podiatry practice website. It configures global styles, external
stylesheets (Lato font and Font Awesome icons), and registers all page
components with their respective routes and state handlers.

Routes
------
Language-prefixed routes (nl, de, en):
/[lang] : Home page (nl, de, en)
/[lang]/blog/ : Blog listing page
/[lang]/blog/[slug] : Individual blog post pages
/[lang]/informatie/ : Information page
/[lang]/vergoedingen/ : Insurance reimbursements page
/[lang]/contact/ : Contact form page
/[lang]/zolen-bestellen/ : Order insoles page

Root redirects (automatically redirect to /nl/...):
/ → /nl
/blog/ → /nl/blog/
/informatie/ → /nl/informatie/
/vergoedingen/ → /nl/vergoedingen/
/contact/ → /nl/contact/
/zolen-bestellen/ → /nl/zolen-bestellen/

Notes
-----
The app uses Lato as the primary font family and includes Font Awesome icons
for UI elements. Custom styles are defined in /styles.css.
All routes support language prefixes for multi-language support.
"""

import reflex as rx

from .pages import page_home, page_blog, page_blog_post, page_informatie, page_vergoedingen, page_contact, page_zolen_bestellen
from .states import BlogState, WebsiteState


def redirect_placeholder() -> rx.Component:
    """Placeholder component for redirect routes."""
    return rx.fragment()


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
    component=redirect_placeholder,
    route="/",
    on_load=lambda: rx.redirect("/nl"),
)

app.add_page(
    component=redirect_placeholder,
    route="/blog/",
    on_load=lambda: rx.redirect("/nl/blog/"),
)

app.add_page(
    component=redirect_placeholder,
    route="/informatie/",
    on_load=lambda: rx.redirect("/nl/informatie/"),
)

app.add_page(
    component=redirect_placeholder,
    route="/vergoedingen/",
    on_load=lambda: rx.redirect("/nl/vergoedingen/"),
)

app.add_page(
    component=redirect_placeholder,
    route="/contact/",
    on_load=lambda: rx.redirect("/nl/contact/"),
)

app.add_page(
    component=redirect_placeholder,
    route="/zolen-bestellen/",
    on_load=lambda: rx.redirect("/nl/zolen-bestellen/"),
)


app.add_page(
    component=page_home,
    route="/[lang]",
    title=WebsiteState.page_title,  # type: ignore
    on_load=WebsiteState.detect_language_from_route,  # type: ignore
)

app.add_page(
    component=page_blog,
    route="/[lang]/blog/",
    title=WebsiteState.page_title,  # type: ignore
    on_load=BlogState.load_posts,  # type: ignore
)

app.add_page(
    component=page_blog_post,
    route="/[lang]/blog/[slug]",
    title=WebsiteState.page_title,  # type: ignore
    on_load=BlogState.load_post_by_slug,  # type: ignore
)

app.add_page(
    component=page_informatie,
    route="/[lang]/informatie/",
    title=WebsiteState.page_title,  # type: ignore
    on_load=WebsiteState.detect_language_from_route,  # type: ignore
)

app.add_page(
    component=page_vergoedingen,
    route="/[lang]/vergoedingen/",
    title=WebsiteState.page_title,  # type: ignore
    on_load=WebsiteState.detect_language_from_route,  # type: ignore
)

app.add_page(
    component=page_contact,
    route="/[lang]/contact/",
    title=WebsiteState.page_title,  # type: ignore
    on_load=WebsiteState.detect_language_from_route,  # type: ignore
)

app.add_page(
    component=page_zolen_bestellen,
    route="/[lang]/zolen-bestellen/",
    title=WebsiteState.page_title,  # type: ignore
    on_load=WebsiteState.detect_language_from_route,  # type: ignore
)
