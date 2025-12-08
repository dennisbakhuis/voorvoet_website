"""Main application entry point for the VoorVoet Reflex web application."""

import reflex as rx
from typing import Any, Callable

from .pages import (
    page_home,
    page_blog,
    page_blog_post,
    page_informatie,
    page_vergoedingen,
    page_contact,
    page_zolen_bestellen,
)
from .utils import get_translation
from .translations import (
    PAGE_TITLES,
    PAGE_IMAGES,
    ROUTE_MAPPINGS,
    get_page_meta_tags,
    get_blog_post_meta_tags,
)
from .services.blog_service import load_all_blog_posts_dict
from .config import config


app = rx.App(
    stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/lato-font/3.0.0/css/lato-font.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
        "/styles.css",
    ],
    style={
        "font-family": "Lato, ui-sans-serif, system-ui, sans-serif",
    },
)

PAGE_COMPONENTS = {
    "home": page_home,
    "information": page_informatie,
    "reimbursements": page_vergoedingen,
    "contact": page_contact,
    "order_insoles": page_zolen_bestellen,
}

main_pages = []
for lang in ["nl", "en", "de"]:
    for page_key, route in ROUTE_MAPPINGS[lang].items():
        if page_key in PAGE_COMPONENTS:
            main_pages.append((lang, page_key, route, PAGE_COMPONENTS[page_key]))

default_redirects = [
    ("nl", "home", "/", page_home),
    ("nl", "information", "/informatie", page_informatie),
    ("nl", "reimbursements", "/vergoedingen", page_vergoedingen),
    ("nl", "contact", "/contact", page_contact),
    ("nl", "order_insoles", "/zolen-bestellen", page_zolen_bestellen),
]
main_pages.extend(default_redirects)

for language, page_key, page_route, page in main_pages:
    page_image = PAGE_IMAGES.get(page_key)
    full_image_url = f"{config.site_url}{page_image}" if page_image else None

    priority = 1.0 if page_key == "home" else 0.6
    changefreq = "weekly" if page_key == "home" else "monthly"

    page_config: dict[str, Any] = {
        "component": lambda page_func=page, lang=language: page_func(language=lang),
        "route": page_route,
        "title": get_translation(PAGE_TITLES, page_key, language),
        "meta": get_page_meta_tags(
            page_key, language, page_route, image_url=full_image_url
        ),
        "context": {
            "sitemap": {
                "changefreq": changefreq,
                "priority": priority,
            }
        },
    }

    if full_image_url:
        page_config["image"] = full_image_url

    app.add_page(**page_config)

blog_posts = load_all_blog_posts_dict()

for language in ["nl", "en", "de"]:
    posts_for_lang = blog_posts.get(language, [])

    def make_blog_page(lang: str, posts_list: list[Any]) -> Callable[[], rx.Component]:
        def _page() -> rx.Component:
            return page_blog(language=lang, posts=posts_list)

        return _page

    blog_image = PAGE_IMAGES.get("blog")
    full_blog_image_url = f"{config.site_url}{blog_image}" if blog_image else None
    blog_route = ROUTE_MAPPINGS[language]["blog"]

    blog_config: dict[str, Any] = {
        "component": make_blog_page(language, posts_for_lang),
        "route": blog_route,
        "title": get_translation(PAGE_TITLES, "blog", language),
        "meta": get_page_meta_tags(
            "blog", language, blog_route, image_url=full_blog_image_url
        ),
        "context": {
            "sitemap": {
                "changefreq": "weekly",
                "priority": 0.8,
            }
        },
    }

    if full_blog_image_url:
        blog_config["image"] = full_blog_image_url

    app.add_page(**blog_config)

app.add_page(
    component=lambda: page_blog(language="nl", posts=blog_posts.get("nl", [])),
    route="/blog/",
    title=get_translation(PAGE_TITLES, "blog", "nl"),
    meta=get_page_meta_tags("blog", "nl", "/blog/", image_url=full_blog_image_url),
    context={
        "sitemap": {
            "changefreq": "weekly",
            "priority": 0.8,
        }
    },
)

for language, posts in blog_posts.items():
    for post in posts:
        slug = post["slug"]
        title = post["title"]

        blog_base = ROUTE_MAPPINGS[language]["blog"]
        route = f"{blog_base}{slug}/"

        def make_blog_post_page(
            lang: str, post_data: dict[str, Any]
        ) -> Callable[[], rx.Component]:
            def _page() -> rx.Component:
                return page_blog_post(language=lang, post=post_data)

            return _page

        post_image = (
            f"{config.site_url}{post['thumbnail_url']}"
            if post.get("thumbnail_url")
            else None
        )

        post_config: dict[str, Any] = {
            "component": make_blog_post_page(language, post),
            "route": route,
            "title": title,
            "meta": get_blog_post_meta_tags(
                post_title=post["title"],
                post_summary=post["summary"],
                language=language,
                route=route,
                story_number=post["story_number"],
                all_blog_posts=blog_posts,
                image_url=post_image,
            ),
            "context": {
                "sitemap": {
                    "changefreq": "monthly",
                    "priority": 0.7,
                }
            },
        }

        if post_image:
            post_config["image"] = post_image

        app.add_page(**post_config)
