"""Translation strings for multi-language support."""

from voorvoet_website.config import config


PAGE_TITLES = {
    "nl": {
        "home": "VoorVoet - Praktijk voor Podotherapie",
        "blog": "VoorVoet - Blog",
        "information": "VoorVoet - Informatie",
        "reimbursements": "VoorVoet - Vergoedingen",
        "contact": "VoorVoet - Contact",
        "order_insoles": "VoorVoet - Steunzolen Bestellen"
    },
    "de": {
        "home": "VoorVoet - Praxis für Podologie",
        "blog": "VoorVoet - Blog",
        "information": "VoorVoet - Informationen",
        "reimbursements": "VoorVoet - Erstattungen",
        "contact": "VoorVoet - Kontakt",
        "order_insoles": "VoorVoet - Einlagen Bestellen"
    },
    "en": {
        "home": "VoorVoet - Podiatry Practice",
        "blog": "VoorVoet - Blog",
        "information": "VoorVoet - Information",
        "reimbursements": "VoorVoet - Reimbursements",
        "contact": "VoorVoet - Contact",
        "order_insoles": "VoorVoet - Order Insoles"
    }
}

PAGE_DESCRIPTIONS = {
    "nl": {
        "home": "VoorVoet is uw podotherapeut in Enschede. Professionele behandeling van voetklachten, steunzolen op maat en podotherapie. Maak een afspraak voor persoonlijke zorg.",
        "blog": "Lees onze blog over podotherapie, voetklachten, steunzolen en tips voor gezonde voeten. Expert advies van VoorVoet podotherapeut in Enschede.",
        "information": "Informatie over podotherapie, behandelmethoden en veelvoorkomende voetklachten. Ontdek hoe VoorVoet u kan helpen met professionele podotherapie in Enschede.",
        "reimbursements": "Informatie over vergoedingen voor podotherapie en steunzolen. Bekijk de tarieven en zorgverzekering vergoedingen voor podotherapie bij VoorVoet Enschede.",
        "contact": "Neem contact op met VoorVoet podotherapie in Enschede. Maak een afspraak of stel uw vraag. Wij helpen u graag met uw voetklachten.",
        "order_insoles": "Bestel steunzolen op maat bij VoorVoet podotherapie Enschede. Professionele podotherapeutische zolen voor optimale ondersteuning en comfort."
    },
    "de": {
        "home": "VoorVoet ist Ihr Podologe in Enschede. Professionelle Behandlung von Fußbeschwerden, maßgefertigte Einlagen und Podologie. Vereinbaren Sie einen Termin.",
        "blog": "Lesen Sie unseren Blog über Podologie, Fußbeschwerden, Einlagen und Tipps für gesunde Füße. Expertenrat von VoorVoet Podologe in Enschede.",
        "information": "Informationen über Podologie, Behandlungsmethoden und häufige Fußbeschwerden. Erfahren Sie, wie VoorVoet Ihnen mit professioneller Podologie in Enschede helfen kann.",
        "reimbursements": "Informationen über Erstattungen für Podologie und Einlagen. Sehen Sie die Tarife und Krankenkassenerstattungen für Podologie bei VoorVoet Enschede.",
        "contact": "Kontaktieren Sie VoorVoet Podologie in Enschede. Vereinbaren Sie einen Termin oder stellen Sie Ihre Frage. Wir helfen Ihnen gerne bei Ihren Fußbeschwerden.",
        "order_insoles": "Bestellen Sie maßgefertigte Einlagen bei VoorVoet Podologie Enschede. Professionelle podologische Einlagen für optimale Unterstützung und Komfort."
    },
    "en": {
        "home": "VoorVoet is your podiatrist in Enschede. Professional treatment of foot complaints, custom insoles and podiatry. Make an appointment for personalized care.",
        "blog": "Read our blog about podiatry, foot complaints, insoles and tips for healthy feet. Expert advice from VoorVoet podiatrist in Enschede.",
        "information": "Information about podiatry, treatment methods and common foot complaints. Discover how VoorVoet can help you with professional podiatry in Enschede.",
        "reimbursements": "Information about reimbursements for podiatry and insoles. View rates and health insurance reimbursements for podiatry at VoorVoet Enschede.",
        "contact": "Contact VoorVoet podiatry in Enschede. Make an appointment or ask your question. We are happy to help you with your foot complaints.",
        "order_insoles": "Order custom insoles at VoorVoet podiatry Enschede. Professional podiatric insoles for optimal support and comfort."
    }
}


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


BREADCRUMB_NAMES = {
    "nl": {
        "home": "Home",
        "blog": "Blog",
        "information": "Informatie",
        "reimbursements": "Vergoedingen",
        "contact": "Contact",
        "order_insoles": "Steunzolen Bestellen"
    },
    "de": {
        "home": "Startseite",
        "blog": "Blog",
        "information": "Informationen",
        "reimbursements": "Erstattungen",
        "contact": "Kontakt",
        "order_insoles": "Einlagen Bestellen"
    },
    "en": {
        "home": "Home",
        "blog": "Blog",
        "information": "Information",
        "reimbursements": "Reimbursements",
        "contact": "Contact",
        "order_insoles": "Order Insoles"
    }
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
    title = PAGE_TITLES.get(language, {}).get(page_key, "VoorVoet")
    description = PAGE_DESCRIPTIONS.get(language, {}).get(page_key, "")
    image_path = PAGE_IMAGES.get(page_key, PAGE_IMAGES["home"])
    image_url = f"{config.site_url}{image_path}"
    page_url = f"{config.site_url}{route}"
    locale = LOCALE_MAP.get(language, "nl_NL")

    meta_tags = [
        {"name": "description", "content": description},

        {"property": "og:title", "content": title},
        {"property": "og:description", "content": description},
        {"property": "og:image", "content": image_url},
        {"property": "og:url", "content": page_url},
        {"property": "og:type", "content": page_type},
        {"property": "og:locale", "content": locale},
        {"property": "og:site_name", "content": "VoorVoet"},

        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:title", "content": title},
        {"name": "twitter:description", "content": description},
        {"name": "twitter:image", "content": image_url},

        {"name": "canonical", "content": page_url},
    ]

    return meta_tags
