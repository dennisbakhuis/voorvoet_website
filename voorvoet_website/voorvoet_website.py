"""Main application entry point for the VoorVoet Reflex web application.

Routes
------
Language-prefixed routes (nl, de, en):
/[lang] : Home page (nl, de, en)
/[lang]/blog/ : Blog listing page
/[lang]/blog/[slug] : Individual blog post pages
/[lang]/informatie : Information page
/[lang]/vergoedingen : Insurance reimbursements page
/[lang]/contact : Contact form page
/[lang]/zolen-bestellen : Order insoles page
"""
import reflex as rx

from .pages import page_home, page_blog, page_blog_post, page_informatie, page_vergoedingen, page_contact, page_zolen_bestellen
from .states import WebsiteState
from .utils import get_translation
from .translations import PAGE_TITLES, get_page_meta_tags
from .services.blog_service import load_all_blog_posts_dict


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

###############
## Redirects ##
###############
redirect_routes = [
    ("/", "/nl"),
    ("/blog/", "/nl/blog/"),
    ("/informatie", "/nl/informatie"),
    ("/vergoedingen", "/nl/vergoedingen"),
    ("/contact", "/nl/contact"),
    ("/zolen-bestellen", "/nl/zolen-bestellen"),
]

for route, redirect_to in redirect_routes:
    app.add_page(
        component=redirect_placeholder,
        route=route,
        on_load=lambda target=redirect_to: rx.redirect(target),
    )


################
## Main pages ##
################
main_pages = [
    ("nl", "home", "/nl", page_home),
    ("nl", "information", "/nl/informatie", page_informatie),
    ("nl", "reimbursements", "/nl/vergoedingen", page_vergoedingen),
    ("nl", "contact", "/nl/contact", page_contact),
    ("nl", "order_insoles", "/nl/zolen-bestellen", page_zolen_bestellen),

    ("en", "home", "/en", page_home),
    ("en", "information", "/en/information", page_informatie),
    ("en", "reimbursements", "/en/reimbursements", page_vergoedingen),
    ("en", "contact", "/en/contact", page_contact),
    ("en", "order_insoles", "/en/order-insoles", page_zolen_bestellen),

    ("de", "home", "/de", page_home),
    ("de", "information", "/de/informationen", page_informatie),
    ("de", "reimbursements", "/de/erstattungen", page_vergoedingen),
    ("de", "contact", "/de/kontakt", page_contact),
    ("de", "order_insoles", "/de/einlagen-bestellen", page_zolen_bestellen),
]

for (language, page_key, page_route, page) in main_pages:
    app.add_page(
        component=lambda page_func=page, lang=language: page_func(language=lang),
        route=page_route,
        title=get_translation(PAGE_TITLES, page_key, language),
        meta=get_page_meta_tags(page_key, language, page_route)
    )


#######################
## Blog / blog posts ##
#######################
blog_posts = load_all_blog_posts_dict()

for language in ['nl', 'en', 'de']:
    posts_for_lang = blog_posts.get(language, [])

    def make_blog_page(lang: str, posts_list: list):
        def _page():
            return page_blog(language=lang, posts=posts_list)
        return _page

    app.add_page(
        component=make_blog_page(language, posts_for_lang),
        route=f"/{language}/blog/",
        title=get_translation(PAGE_TITLES, "blog", language),
        meta=get_page_meta_tags("blog", language, f"/{language}/blog/")
    )

for language, posts in blog_posts.items():
    for post in posts:
        slug = post["slug"]
        title = post["title"]
        route = f"/{language}/blog/{slug}/"

        def make_blog_post_page(lang: str, post_data: dict):
            def _page():
                return page_blog_post(language=lang, post=post_data)
            return _page

        app.add_page(
            component=make_blog_post_page(language, post),
            route=route,
            title=title,
        )
