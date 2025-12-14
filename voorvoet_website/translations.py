"""Translation strings for multi-language support."""

import reflex as rx

from .config import config
from .models import BlogPostDict


PAGE_TITLES = {
    "nl": {
        "home": "VoorVoet - Praktijk voor Podotherapie",
        "blog": "VoorVoet - Blog",
        "information": "VoorVoet - Informatie",
        "reimbursements": "VoorVoet - Vergoedingen",
        "contact": "VoorVoet - Contact",
        "order_insoles": "VoorVoet - Steunzolen Bestellen",
        "credits": "VoorVoet - Credits",
        "not_found": "VoorVoet - Pagina niet gevonden",
    },
    "de": {
        "home": "VoorVoet - Praxis für Podologie",
        "blog": "VoorVoet - Blog",
        "information": "VoorVoet - Informationen",
        "reimbursements": "VoorVoet - Erstattungen",
        "contact": "VoorVoet - Kontakt",
        "order_insoles": "VoorVoet - Einlagen Bestellen",
        "credits": "VoorVoet - Credits",
    },
    "en": {
        "home": "VoorVoet - Podiatry Practice",
        "blog": "VoorVoet - Blog",
        "information": "VoorVoet - Information",
        "reimbursements": "VoorVoet - Reimbursements",
        "contact": "VoorVoet - Contact",
        "order_insoles": "VoorVoet - Order Insoles",
        "credits": "VoorVoet - Credits",
    },
}

PAGE_DESCRIPTIONS = {
    "nl": {
        "home": "VoorVoet is uw podotherapeut in Enschede. Professionele behandeling van voetklachten, steunzolen op maat en podotherapie. Maak een afspraak voor persoonlijke zorg.",
        "blog": "Lees onze blog over podotherapie, voetklachten, steunzolen en tips voor gezonde voeten. Expert advies van VoorVoet podotherapeut in Enschede.",
        "information": "Informatie over podotherapie, behandelmethoden en veelvoorkomende voetklachten. Ontdek hoe VoorVoet u kan helpen met professionele podotherapie in Enschede.",
        "reimbursements": "Informatie over vergoedingen voor podotherapie en steunzolen. Bekijk de tarieven en zorgverzekering vergoedingen voor podotherapie bij VoorVoet Enschede.",
        "contact": "Neem contact op met VoorVoet podotherapie in Enschede. Maak een afspraak of stel uw vraag. Wij helpen u graag met uw voetklachten.",
        "order_insoles": "Bestel steunzolen op maat bij VoorVoet podotherapie Enschede. Professionele podotherapeutische zolen voor optimale ondersteuning en comfort.",
        "credits": "Credits voor afbeeldingen, Python packages en informatie over de website ontwikkelaar van VoorVoet podotherapie Enschede.",
        "not_found": "De pagina die u zoekt bestaat niet. Ga terug naar de homepage van VoorVoet podotherapie Enschede.",
    },
    "de": {
        "home": "VoorVoet ist Ihr Podologe in Enschede. Professionelle Behandlung von Fußbeschwerden, maßgefertigte Einlagen und Podologie. Vereinbaren Sie einen Termin.",
        "blog": "Lesen Sie unseren Blog über Podologie, Fußbeschwerden, Einlagen und Tipps für gesunde Füße. Expertenrat von VoorVoet Podologe in Enschede.",
        "information": "Informationen über Podologie, Behandlungsmethoden und häufige Fußbeschwerden. Erfahren Sie, wie VoorVoet Ihnen mit professioneller Podologie in Enschede helfen kann.",
        "reimbursements": "Informationen über Erstattungen für Podologie und Einlagen. Sehen Sie die Tarife und Krankenkassenerstattungen für Podologie bei VoorVoet Enschede.",
        "contact": "Kontaktieren Sie VoorVoet Podologie in Enschede. Vereinbaren Sie einen Termin oder stellen Sie Ihre Frage. Wir helfen Ihnen gerne bei Ihren Fußbeschwerden.",
        "order_insoles": "Bestellen Sie maßgefertigte Einlagen bei VoorVoet Podologie Enschede. Professionelle podologische Einlagen für optimale Unterstützung und Komfort.",
        "credits": "Credits für Bilder, Python-Pakete und Informationen über den Website-Entwickler von VoorVoet Podologie Enschede.",
    },
    "en": {
        "home": "VoorVoet is your podiatrist in Enschede. Professional treatment of foot complaints, custom insoles and podiatry. Make an appointment for personalized care.",
        "blog": "Read our blog about podiatry, foot complaints, insoles and tips for healthy feet. Expert advice from VoorVoet podiatrist in Enschede.",
        "information": "Information about podiatry, treatment methods and common foot complaints. Discover how VoorVoet can help you with professional podiatry in Enschede.",
        "reimbursements": "Information about reimbursements for podiatry and insoles. View rates and health insurance reimbursements for podiatry at VoorVoet Enschede.",
        "contact": "Contact VoorVoet podiatry in Enschede. Make an appointment or ask your question. We are happy to help you with your foot complaints.",
        "order_insoles": "Order custom insoles at VoorVoet podiatry Enschede. Professional podiatric insoles for optimal support and comfort.",
        "credits": "Credits for images, Python packages and information about the website developer of VoorVoet podiatry Enschede.",
    },
}


PAGE_IMAGES = {
    "home": "/images/voorvoet-podotherapie-enschede.jpg",
    "blog": "/images/voorvoet-blog.jpg",
    "information": "/images/voorvoet-informatie.jpg",
    "reimbursements": "/images/voorvoet-vergoedingen.jpg",
    "contact": "/images/voorvoet-contact.jpg",
    "order_insoles": "/images/voorvoet-steunzolen.jpg",
    "credits": "/images/page_credits/credits_hero_banner.jpg",
    "not_found": "/images/voorvoet-podotherapie-enschede.jpg",
}


LOCALE_MAP = {"nl": "nl_NL", "de": "de_DE", "en": "en_US"}


BREADCRUMB_NAMES = {
    "nl": {
        "home": "Home",
        "blog": "Blog",
        "information": "Informatie",
        "reimbursements": "Vergoedingen",
        "contact": "Contact",
        "order_insoles": "Steunzolen Bestellen",
        "credits": "Credits",
    },
    "de": {
        "home": "Startseite",
        "blog": "Blog",
        "information": "Informationen",
        "reimbursements": "Erstattungen",
        "contact": "Kontakt",
        "order_insoles": "Einlagen Bestellen",
        "credits": "Credits",
    },
    "en": {
        "home": "Home",
        "blog": "Blog",
        "information": "Information",
        "reimbursements": "Reimbursements",
        "contact": "Contact",
        "order_insoles": "Order Insoles",
        "credits": "Credits",
    },
}


ROUTE_MAPPINGS = {
    "nl": {
        "home": "/nl",
        "information": "/nl/informatie",
        "reimbursements": "/nl/vergoedingen",
        "contact": "/nl/contact",
        "order_insoles": "/nl/zolen-bestellen",
        "credits": "/nl/credits",
        "blog": "/nl/blog",
    },
    "de": {
        "home": "/de",
        "information": "/de/informationen",
        "reimbursements": "/de/erstattungen",
        "contact": "/de/kontakt",
        "order_insoles": "/de/einlagen-bestellen",
        "credits": "/de/credits",
        "blog": "/de/blog",
    },
    "en": {
        "home": "/en",
        "information": "/en/information",
        "reimbursements": "/en/reimbursements",
        "contact": "/en/contact",
        "order_insoles": "/en/order-insoles",
        "credits": "/en/credits",
        "blog": "/en/blog",
    },
}

PAGE_ROUTES = {
    "home": {"nl": "/nl", "de": "/de", "en": "/en"},
    "blog": {"nl": "/nl/blog", "de": "/de/blog", "en": "/en/blog"},
    "information": {
        "nl": "/nl/informatie",
        "de": "/de/informationen",
        "en": "/en/information",
    },
    "reimbursements": {
        "nl": "/nl/vergoedingen",
        "de": "/de/erstattungen",
        "en": "/en/reimbursements",
    },
    "contact": {"nl": "/nl/contact", "de": "/de/kontakt", "en": "/en/contact"},
    "order_insoles": {
        "nl": "/nl/zolen-bestellen",
        "de": "/de/einlagen-bestellen",
        "en": "/en/order-insoles",
    },
    "credits": {"nl": "/nl/credits", "de": "/de/credits", "en": "/en/credits"},
}


def get_favicon_links() -> list[rx.Component]:
    return [
        rx.el.link(
            rel="icon",
            href="/favicon.ico",
            custom_attrs={"type": "image/x-icon"},
        ),
        rx.el.link(
            rel="icon",
            href="/favicon-96x96.png",
            custom_attrs={"type": "image/png", "sizes": "96x96"},
        ),
        rx.el.link(
            rel="icon",
            href="/favicon.svg",
            custom_attrs={"type": "image/svg+xml"},
        ),
        rx.el.link(
            rel="apple-touch-icon",
            href="/apple-touch-icon.png",
            custom_attrs={"sizes": "180x180"},
        ),
        rx.el.link(rel="manifest", href="/site.webmanifest"),
    ]


def get_hreflang_tags(page_key: str) -> list:
    """Generate hreflang link tags for multi-language pages.

    Creates alternate language links for SEO to help search engines understand
    which language versions of a page are available.

    Parameters
    ----------
    page_key : str
        The key identifying the page (e.g., "home", "blog", "contact")

    Returns
    -------
    list
        List of rx.el.link components with hreflang attributes

    Notes
    -----
    - Includes hreflang for all available language versions
    - Adds x-default pointing to Dutch (nl) as the default language
    - Required for multi-language SEO per Google guidelines
    """
    hreflang_tags: list[rx.Component] = []

    page_routes = PAGE_ROUTES.get(page_key, {})

    if not page_routes:
        return hreflang_tags

    for lang, route in page_routes.items():
        full_url = f"{config.site_url}{route}"
        hreflang_tags.append(
            rx.el.link(
                rel="alternate",
                href=full_url,
                custom_attrs={"hreflang": lang},
            )
        )

    if "nl" in page_routes:
        default_url = f"{config.site_url}{page_routes['nl']}"
        hreflang_tags.append(
            rx.el.link(
                rel="alternate",
                href=default_url,
                custom_attrs={"hreflang": "x-default"},
            )
        )

    return hreflang_tags


def get_blog_post_hreflang_tags(
    story_number: str, all_blog_posts: dict[str, list[BlogPostDict]]
) -> list:
    """Generate hreflang tags for blog posts based on story number."""
    hreflang_tags = []
    nl_slug = None

    for lang, posts in all_blog_posts.items():
        for post in posts:
            if post.get("story_number") == story_number:
                slug = post["slug"]
                full_url = f"{config.site_url}/{lang}/blog/{slug}"
                hreflang_tags.append(
                    rx.el.link(
                        rel="alternate",
                        href=full_url,
                        custom_attrs={"hreflang": lang},
                    )
                )
                if lang == "nl":
                    nl_slug = slug
                break

    if nl_slug:
        default_url = f"{config.site_url}/nl/blog/{nl_slug}"
        hreflang_tags.append(
            rx.el.link(
                rel="alternate",
                href=default_url,
                custom_attrs={"hreflang": "x-default"},
            )
        )

    return hreflang_tags


def get_page_meta_tags(
    page_key: str,
    language: str,
    route: str,
    page_type: str = "website",
    image_url: str | None = None,
) -> list:
    """
    Generate complete meta tags for SEO including Open Graph and Twitter Cards.

    Parameters
    ----------
    page_key : str
        The key identifying the page (e.g., "home", "blog", "contact")
    language : str
        The language code ("nl", "de", "en")
    route : str
        The page route (e.g., "/nl", "/de/blog")
    page_type : str, optional
        Open Graph type ("website" or "article"), defaults to "website"
    image_url : str, optional
        Full URL to the page image for Twitter Cards

    Returns
    -------
    list[dict]
        List of meta tag dictionaries for use with Reflex's app.add_page()
    """
    title = PAGE_TITLES.get(language, {}).get(page_key, "VoorVoet")
    description = PAGE_DESCRIPTIONS.get(language, {}).get(page_key, "")
    page_url = f"{config.site_url}{route}"
    locale = LOCALE_MAP.get(language, "nl_NL")

    meta_tags: list = [
        {"name": "description", "content": description},
        {"property": "og:title", "content": title},
        {"property": "og:description", "content": description},
        {"property": "og:url", "content": page_url},
        {"property": "og:type", "content": page_type},
        {"property": "og:locale", "content": locale},
        {"property": "og:site_name", "content": "VoorVoet"},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:title", "content": title},
        {"name": "twitter:description", "content": description},
    ]

    if image_url:
        meta_tags.append({"name": "twitter:image", "content": image_url})

    meta_tags.append({"name": "apple-mobile-web-app-title", "content": "VoorVoet"})

    meta_tags.append(
        rx.el.link(
            rel="canonical",
            href=page_url,
        )
    )

    hreflang_tags = get_hreflang_tags(page_key)
    meta_tags.extend(hreflang_tags)

    favicon_links = get_favicon_links()
    meta_tags.extend(favicon_links)

    return meta_tags


def get_blog_post_meta_tags(
    post_title: str,
    post_summary: str,
    language: str,
    route: str,
    story_number: str = "",
    all_blog_posts: dict[str, list[BlogPostDict]] = {},
    image_url: str | None = None,
) -> list:
    """Generate post-specific meta tags for individual blog posts."""
    full_title = f"{post_title} - VoorVoet Blog"

    page_url = f"{config.site_url}{route}"
    locale = LOCALE_MAP.get(language, "nl_NL")

    meta_tags: list = [
        {"name": "description", "content": post_summary},
        {"property": "og:title", "content": full_title},
        {"property": "og:description", "content": post_summary},
        {"property": "og:url", "content": page_url},
        {"property": "og:type", "content": "article"},
        {"property": "og:locale", "content": locale},
        {"property": "og:site_name", "content": "VoorVoet"},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:title", "content": full_title},
        {"name": "twitter:description", "content": post_summary},
    ]

    if image_url:
        meta_tags.append({"name": "twitter:image", "content": image_url})

    meta_tags.append({"name": "apple-mobile-web-app-title", "content": "VoorVoet"})

    meta_tags.append(
        rx.el.link(
            rel="canonical",
            href=page_url,
        )
    )

    if story_number:
        hreflang_tags = get_blog_post_hreflang_tags(story_number, all_blog_posts)
        meta_tags.extend(hreflang_tags)

    favicon_links = get_favicon_links()
    meta_tags.extend(favicon_links)

    return meta_tags
