"""Translation strings for multi-language support.

This module contains all translatable strings used throughout the application,
organized by category. Each translation is a dictionary with language codes
(nl, de, en) as keys.
"""

from voorvoet_website.config import config

PAGE_TITLES = {
    "home": {
        "nl": "VoorVoet - Praktijk voor Podotherapie",
        "de": "VoorVoet - Praxis für Podologie",
        "en": "VoorVoet - Podiatry Practice"
    },
    "blog": {
        "nl": "VoorVoet - Blog",
        "de": "VoorVoet - Blog",
        "en": "VoorVoet - Blog"
    },
    "information": {
        "nl": "VoorVoet - Informatie",
        "de": "VoorVoet - Informationen",
        "en": "VoorVoet - Information"
    },
    "reimbursements": {
        "nl": "VoorVoet - Vergoedingen",
        "de": "VoorVoet - Erstattungen",
        "en": "VoorVoet - Reimbursements"
    },
    "contact": {
        "nl": "VoorVoet - Contact",
        "de": "VoorVoet - Kontakt",
        "en": "VoorVoet - Contact"
    },
    "order_insoles": {
        "nl": "VoorVoet - Steunzolen Bestellen",
        "de": "VoorVoet - Einlagen Bestellen",
        "en": "VoorVoet - Order Insoles"
    }
}

PAGE_DESCRIPTIONS = {
    "home": {
        "nl": "VoorVoet is uw podotherapeut in Enschede. Professionele behandeling van voetklachten, steunzolen op maat en podotherapie. Maak een afspraak voor persoonlijke zorg.",
        "de": "VoorVoet ist Ihr Podologe in Enschede. Professionelle Behandlung von Fußbeschwerden, maßgefertigte Einlagen und Podologie. Vereinbaren Sie einen Termin.",
        "en": "VoorVoet is your podiatrist in Enschede. Professional treatment of foot complaints, custom insoles and podiatry. Make an appointment for personalized care."
    },
    "blog": {
        "nl": "Lees onze blog over podotherapie, voetklachten, steunzolen en tips voor gezonde voeten. Expert advies van VoorVoet podotherapeut in Enschede.",
        "de": "Lesen Sie unseren Blog über Podologie, Fußbeschwerden, Einlagen und Tipps für gesunde Füße. Expertenrat von VoorVoet Podologe in Enschede.",
        "en": "Read our blog about podiatry, foot complaints, insoles and tips for healthy feet. Expert advice from VoorVoet podiatrist in Enschede."
    },
    "information": {
        "nl": "Informatie over podotherapie, behandelmethoden en veelvoorkomende voetklachten. Ontdek hoe VoorVoet u kan helpen met professionele podotherapie in Enschede.",
        "de": "Informationen über Podologie, Behandlungsmethoden und häufige Fußbeschwerden. Erfahren Sie, wie VoorVoet Ihnen mit professioneller Podologie in Enschede helfen kann.",
        "en": "Information about podiatry, treatment methods and common foot complaints. Discover how VoorVoet can help you with professional podiatry in Enschede."
    },
    "reimbursements": {
        "nl": "Informatie over vergoedingen voor podotherapie en steunzolen. Bekijk de tarieven en zorgverzekering vergoedingen voor podotherapie bij VoorVoet Enschede.",
        "de": "Informationen über Erstattungen für Podologie und Einlagen. Sehen Sie die Tarife und Krankenkassenerstattungen für Podologie bei VoorVoet Enschede.",
        "en": "Information about reimbursements for podiatry and insoles. View rates and health insurance reimbursements for podiatry at VoorVoet Enschede."
    },
    "contact": {
        "nl": "Neem contact op met VoorVoet podotherapie in Enschede. Maak een afspraak of stel uw vraag. Wij helpen u graag met uw voetklachten.",
        "de": "Kontaktieren Sie VoorVoet Podologie in Enschede. Vereinbaren Sie einen Termin oder stellen Sie Ihre Frage. Wir helfen Ihnen gerne bei Ihren Fußbeschwerden.",
        "en": "Contact VoorVoet podiatry in Enschede. Make an appointment or ask your question. We are happy to help you with your foot complaints."
    },
    "order_insoles": {
        "nl": "Bestel steunzolen op maat bij VoorVoet podotherapie Enschede. Professionele podotherapeutische zolen voor optimale ondersteuning en comfort.",
        "de": "Bestellen Sie maßgefertigte Einlagen bei VoorVoet Podologie Enschede. Professionelle podologische Einlagen für optimale Unterstützung und Komfort.",
        "en": "Order custom insoles at VoorVoet podiatry Enschede. Professional podiatric insoles for optimal support and comfort."
    }
}


def get_page_title(page_key: str, language: str = "nl") -> str:
    """
    Get the page title for a specific page and language.

    Parameters
    ----------
    page_key : str
        The key identifying the page (e.g., "home", "blog", "contact")
    language : str, optional
        The language code ("nl", "de", "en"), defaults to "nl"

    Returns
    -------
    str
        The page title in the requested language, or Dutch if language not found
    """
    return PAGE_TITLES.get(page_key, {}).get(language, PAGE_TITLES.get(page_key, {}).get("nl", "VoorVoet"))


def get_page_description(page_key: str, language: str = "nl") -> str:
    """
    Get the page meta description for a specific page and language.

    Parameters
    ----------
    page_key : str
        The key identifying the page (e.g., "home", "blog", "contact")
    language : str, optional
        The language code ("nl", "de", "en"), defaults to "nl"

    Returns
    -------
    str
        The page description in the requested language, or Dutch if language not found
    """
    return PAGE_DESCRIPTIONS.get(page_key, {}).get(language, PAGE_DESCRIPTIONS.get(page_key, {}).get("nl", ""))


PAGE_IMAGES = {
    "home": "/images/voorvoet-podotherapie-enschede.jpg",
    "blog": "/images/voorvoet-blog.jpg",
    "information": "/images/voorvoet-informatie.jpg",
    "reimbursements": "/images/voorvoet-vergoedingen.jpg",
    "contact": "/images/voorvoet-contact.jpg",
    "order_insoles": "/images/voorvoet-steunzolen.jpg"
}


LOCALE_MAP = {
    "nl": "nl_NL",
    "de": "de_DE",
    "en": "en_US"
}


def get_page_meta_tags(page_key: str, language: str, route: str, page_type: str = "website") -> list[dict]:
    """
    Generate complete meta tags for SEO including Open Graph and Twitter Cards.

    Parameters
    ----------
    page_key : str
        The key identifying the page (e.g., "home", "blog", "contact")
    language : str
        The language code ("nl", "de", "en")
    route : str
        The page route (e.g., "/nl", "/de/blog/")
    page_type : str, optional
        Open Graph type ("website" or "article"), defaults to "website"

    Returns
    -------
    list[dict]
        List of meta tag dictionaries for use with Reflex's app.add_page()
    """
    title = get_page_title(page_key, language)
    description = get_page_description(page_key, language)
    image_path = PAGE_IMAGES.get(page_key, PAGE_IMAGES["home"])
    image_url = f"{config.site_url}{image_path}"
    page_url = f"{config.site_url}{route}"
    locale = LOCALE_MAP.get(language, "nl_NL")

    meta_tags = [
        # Standard meta tags
        {"name": "description", "content": description},

        # Open Graph tags
        {"property": "og:title", "content": title},
        {"property": "og:description", "content": description},
        {"property": "og:image", "content": image_url},
        {"property": "og:url", "content": page_url},
        {"property": "og:type", "content": page_type},
        {"property": "og:locale", "content": locale},
        {"property": "og:site_name", "content": "VoorVoet"},

        # Twitter Card tags
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:title", "content": title},
        {"name": "twitter:description", "content": description},
        {"name": "twitter:image", "content": image_url},

        # Canonical URL (not the correct implementation)
        {"name": "canonical", "content": page_url},
    ]

    # Add alternate language versions (hreflang will be added in Phase 5)
    return meta_tags

# def get_breadcrumb_name(page_key: str, language: str = "nl") -> str:
#     """
#     Get the breadcrumb name for a specific page and language.

#     Parameters
#     ----------
#     page_key : str
#         The key identifying the page (e.g., "blog", "contact", "information")
#     language : str, optional
#         The language code ("nl", "de", "en"), defaults to "nl"

#     Returns
#     -------
#     str
#         The breadcrumb name in the requested language, or Dutch if language not found
#     """
#     return BREADCRUMB_NAMES.get(page_key, {}).get(language, BREADCRUMB_NAMES.get(page_key, {}).get("nl", ""))

# def get_page_meta_tags(page_key: str, language: str, route: str, page_type: str = "website") -> list[dict]:
#     """
#     Generate complete meta tags for SEO including Open Graph and Twitter Cards.

#     Parameters
#     ----------
#     page_key : str
#         The key identifying the page (e.g., "home", "blog", "contact")
#     language : str
#         The language code ("nl", "de", "en")
#     route : str
#         The page route (e.g., "/nl", "/de/blog/")
#     page_type : str, optional
#         Open Graph type ("website" or "article"), defaults to "website"

#     Returns
#     -------
#     list[dict]
#         List of meta tag dictionaries for use with Reflex's app.add_page()
#     """
#     title = get_page_title(page_key, language)
#     description = get_page_description(page_key, language)
#     image_path = PAGE_IMAGES.get(page_key, PAGE_IMAGES["home"])
#     image_url = f"{config.site_url}{image_path}"
#     page_url = f"{config.site_url}{route}"
#     locale = LOCALE_MAP.get(language, "nl_NL")

#     meta_tags = [
#         {"name": "description", "content": description},

#         {"property": "og:title", "content": title},
#         {"property": "og:description", "content": description},
#         {"property": "og:image", "content": image_url},
#         {"property": "og:url", "content": page_url},
#         {"property": "og:type", "content": page_type},
#         {"property": "og:locale", "content": locale},
#         {"property": "og:site_name", "content": "VoorVoet"},

#         {"name": "twitter:card", "content": "summary_large_image"},
#         {"name": "twitter:title", "content": title},
#         {"name": "twitter:description", "content": description},
#         {"name": "twitter:image", "content": image_url},

#         {"name": "canonical", "content": page_url},
#     ]

#     return meta_tags


# def get_blog_post_meta_tags(post_title: str, post_summary: str, post_thumbnail: str, language: str, route: str) -> list[dict]:
#     """
#     Generate post-specific meta tags for individual blog posts.

#     Parameters
#     ----------
#     post_title : str
#         The blog post title
#     post_summary : str
#         The blog post summary/excerpt
#     post_thumbnail : str
#         The blog post thumbnail URL path
#     language : str
#         The language code ("nl", "de", "en")
#     route : str
#         The blog post route (e.g., "/nl/blog/slug")

#     Returns
#     -------
#     list[dict]
#         List of meta tag dictionaries optimized for blog posts
#     """
#     full_title = f"{post_title} - VoorVoet Blog"

#     image_url = f"{config.site_url}{post_thumbnail}"
#     page_url = f"{config.site_url}{route}"
#     locale = LOCALE_MAP.get(language, "nl_NL")

#     meta_tags = [
#         {"name": "description", "content": post_summary},

#         {"property": "og:title", "content": full_title},
#         {"property": "og:description", "content": post_summary},
#         {"property": "og:image", "content": image_url},
#         {"property": "og:url", "content": page_url},
#         {"property": "og:type", "content": "article"},
#         {"property": "og:locale", "content": locale},
#         {"property": "og:site_name", "content": "VoorVoet"},

#         {"name": "twitter:card", "content": "summary_large_image"},
#         {"name": "twitter:title", "content": full_title},
#         {"name": "twitter:description", "content": post_summary},
#         {"name": "twitter:image", "content": image_url},

#         {"name": "canonical", "content": page_url},
#     ]

#     return meta_tags
