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
/[lang]/reimbursements/ : Insurance reimbursements page
/[lang]/contact/ : Contact form page
/[lang]/order-insoles/ : Order insoles page

Root redirects (automatically redirect to /nl/...):
/ → /nl
/blog/ → /nl/blog/
/informatie/ → /nl/informatie/
/reimbursements/ → /nl/reimbursements/
/contact/ → /nl/contact/
/order-insoles/ → /nl/order-insoles/

Notes
-----
The app uses Lato as the primary font family and includes Font Awesome icons
for UI elements. Custom styles are defined in /styles.css.
All routes support language prefixes for multi-language support.
"""

import reflex as rx

from .pages import page_home, page_blog, page_blog_post, page_information, page_reimbursements, page_contact, page_order_insoles
from .states import BlogState, WebsiteState


def redirect_to_nl_home() -> rx.Component:
    """Redirect root path to Dutch home page."""
    return rx.fragment()


def redirect_to_nl_blog() -> rx.Component:
    """Redirect root blog path to Dutch blog page."""
    return rx.fragment()


def redirect_to_nl_informatie() -> rx.Component:
    """Redirect root informatie path to Dutch informatie page."""
    return rx.fragment()


def redirect_to_nl_reimbursements() -> rx.Component:
    """Redirect root reimbursements path to Dutch reimbursements page."""
    return rx.fragment()


def redirect_to_nl_contact() -> rx.Component:
    """Redirect root contact path to Dutch contact page."""
    return rx.fragment()


def redirect_to_nl_order_insoles() -> rx.Component:
    """Redirect root order-insoles path to Dutch order insoles page."""
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

# Redirect root paths to /nl/...
app.add_page(
    component=redirect_to_nl_home,
    route="/",
    on_load=lambda: rx.redirect("/nl"),
)

app.add_page(
    component=redirect_to_nl_blog,
    route="/blog/",
    on_load=lambda: rx.redirect("/nl/blog/"),
)

app.add_page(
    component=redirect_to_nl_informatie,
    route="/informatie/",
    on_load=lambda: rx.redirect("/nl/informatie/"),
)

app.add_page(
    component=redirect_to_nl_reimbursements,
    route="/reimbursements/",
    on_load=lambda: rx.redirect("/nl/reimbursements/"),
)

app.add_page(
    component=redirect_to_nl_contact,
    route="/contact/",
    on_load=lambda: rx.redirect("/nl/contact/"),
)

app.add_page(
    component=redirect_to_nl_order_insoles,
    route="/order-insoles/",
    on_load=lambda: rx.redirect("/nl/order-insoles/"),
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
    component=page_information,
    route="/[lang]/informatie/",
    title=WebsiteState.page_title,  # type: ignore
    on_load=WebsiteState.detect_language_from_route,  # type: ignore
)

app.add_page(
    component=page_reimbursements,
    route="/[lang]/reimbursements/",
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
    component=page_order_insoles,
    route="/[lang]/order-insoles/",
    title=WebsiteState.page_title,  # type: ignore
    on_load=WebsiteState.detect_language_from_route,  # type: ignore
)
