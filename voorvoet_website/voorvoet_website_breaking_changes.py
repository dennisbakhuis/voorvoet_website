"""Main application entry point for the VoorVoet Reflex web application.

This module initializes the Reflex application and defines all routes for the
VoorVoet podiatry practice website. It configures global styles, external
stylesheets (Lato font and Font Awesome icons), and registers all page
components with their respective routes, SEO meta tags, and state handlers.

Routes
------
Dutch routes (/nl):
/nl : Home page
/nl/blog/ : Blog listing page
/nl/blog/[slug] : Individual blog post pages
/nl/informatie/ : Information page
/nl/vergoedingen/ : Insurance reimbursements page
/nl/contact/ : Contact form page
/nl/zolen-bestellen/ : Order insoles page

German routes (/de):
/de : Home page
/de/blog/ : Blog listing page
/de/blog/[slug] : Individual blog post pages
/de/informationen/ : Information page
/de/erstattungen/ : Insurance reimbursements page
/de/kontakt/ : Contact form page
/de/einlagen-bestellen/ : Order insoles page

English routes (/en):
/en : Home page
/en/blog/ : Blog listing page
/en/blog/[slug] : Individual blog post pages
/en/information/ : Information page
/en/reimbursements/ : Insurance reimbursements page
/en/contact/ : Contact form page
/en/order-insoles/ : Order insoles page

Redirects (non-prefixed URLs redirect to appropriate language version):
/ → /nl
/blog/ → /nl/blog/
/informatie/ → /nl/informatie/
/vergoedingen/ → /nl/vergoedingen/
/contact/ → /nl/contact/
/zolen-bestellen/ → /nl/zolen-bestellen/
/informationen/ → /de/informationen/
/erstattungen/ → /de/erstattungen/
/kontakt/ → /de/kontakt/
/einlagen-bestellen/ → /de/einlagen-bestellen/
/information/ → /en/information/
/reimbursements/ → /en/reimbursements/
/order-insoles/ → /en/order-insoles/

SEO Configuration
-----------------
Each language-specific route includes:
- Translated page titles from PAGE_TITLES dictionary
- SEO-optimized meta descriptions (150-160 chars)
- Open Graph tags (og:title, og:description, og:image, og:url, og:type, og:locale, og:site_name)
- Twitter Card tags (twitter:card, twitter:title, twitter:description, twitter:image)
- Canonical URLs for preventing duplicate content
- Language-appropriate content via state handlers

Notes
-----
The app uses Lato as the primary font family and includes Font Awesome icons
for UI elements. Custom styles are defined in /styles.css.
All routes support language prefixes for multi-language SEO optimization.
"""

import reflex as rx

from .pages import page_home, page_blog, page_blog_post, page_information, page_reimbursements, page_contact, page_order_insoles
from .states import BlogState, WebsiteState
from .states.page_title_translations import PAGE_TITLES, get_page_meta_tags


def redirect_page() -> rx.Component:
    """Placeholder component for redirect-only routes."""
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

for route, redirect_to in [
    ("/", "/nl"),
    ("/blog/", "/nl/blog/"),
    ("/informatie/", "/nl/informatie/"),
    ("/vergoedingen/", "/nl/vergoedingen/"),
    ("/contact/", "/nl/contact/"),
    ("/zolen-bestellen/", "/nl/zolen-bestellen/"),
    # German redirects
    ("/informationen/", "/de/informationen/"),
    ("/erstattungen/", "/de/erstattungen/"),
    ("/kontakt/", "/de/kontakt/"),
    ("/einlagen-bestellen/", "/de/einlagen-bestellen/"),
    # English redirects
    ("/information/", "/en/information/"),
    ("/reimbursements/", "/en/reimbursements/"),
    ("/order-insoles/", "/en/zolen-bestellen/"),
]:
    app.add_page(
        component=redirect_page,
        route=route,
        on_load=lambda target=redirect_to: rx.redirect(target),
    )

for route, page_key, component, state_load in [
    ("/nl", "home", page_home, WebsiteState.detect_language_from_route),
    ("/nl/blog/", "blog", page_blog, BlogState.load_posts),
    ("/nl/blog/[slug]", "blog", page_blog_post, BlogState.load_post_by_slug),
    ("/nl/informatie/", "information", page_information, WebsiteState.detect_language_from_route),
    ("/nl/vergoedingen/", "reimbursements", page_reimbursements, WebsiteState.detect_language_from_route),
    ("/nl/contact/", "contact", page_contact, WebsiteState.detect_language_from_route),
    ("/nl/zolen-bestellen/", "order_insoles", page_order_insoles, WebsiteState.detect_language_from_route),
]:
    app.add_page(
        component=component,
        route=route,
        title=PAGE_TITLES[page_key]["nl"],
        meta=get_page_meta_tags(page_key, "nl", route),
        on_load=state_load,  # type: ignore
    )

for route, page_key, component, state_load in [
    ("/de", "home", page_home, WebsiteState.detect_language_from_route),
    ("/de/blog/", "blog", page_blog, BlogState.load_posts),
    ("/de/blog/[slug]", "blog", page_blog_post, BlogState.load_post_by_slug),
    ("/de/informationen/", "information", page_information, WebsiteState.detect_language_from_route),
    ("/de/erstattungen/", "reimbursements", page_reimbursements, WebsiteState.detect_language_from_route),
    ("/de/kontakt/", "contact", page_contact, WebsiteState.detect_language_from_route),
    ("/de/einlagen-bestellen/", "order_insoles", page_order_insoles, WebsiteState.detect_language_from_route),
]:
    app.add_page(
        component=component,
        route=route,
        title=PAGE_TITLES[page_key]["de"],
        meta=get_page_meta_tags(page_key, "de", route),
        on_load=state_load,  # type: ignore
    )

for route, page_key, component, state_load in [
    ("/en", "home", page_home, WebsiteState.detect_language_from_route),
    ("/en/blog/", "blog", page_blog, BlogState.load_posts),
    ("/en/blog/[slug]", "blog", page_blog_post, BlogState.load_post_by_slug),
    ("/en/information/", "information", page_information, WebsiteState.detect_language_from_route),
    ("/en/reimbursements/", "reimbursements", page_reimbursements, WebsiteState.detect_language_from_route),
    ("/en/contact/", "contact", page_contact, WebsiteState.detect_language_from_route),
    ("/en/order-insoles/", "order_insoles", page_order_insoles, WebsiteState.detect_language_from_route),
]:
    app.add_page(
        component=component,
        route=route,
        title=PAGE_TITLES[page_key]["en"],
        meta=get_page_meta_tags(page_key, "en", route),
        on_load=state_load,  # type: ignore
    )
