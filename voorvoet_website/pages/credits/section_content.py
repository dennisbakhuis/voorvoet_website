"""Content section for the credits page."""

import reflex as rx

from ...components import container, section, header, regular_text, image_text_section
from ...data.credits import PYTHON_PACKAGES, IMAGES
from ...theme import Colors, Spacing, ImageDimensions, FontSizes
from ...utils import get_translation


TRANSLATIONS = {
    "nl": {
        "page_title": "Credits",
        "page_intro": "Websites bouwen is teamwork, ook al zit je alleen achter je laptop. Hier een bedankje aan alle tools, afbeeldingen en mensen die deze website mogelijk hebben gemaakt.",
        "images_title": "Afbeeldingen",
        "images_intro": "Deze website gebruikt afbeeldingen van de volgende bronnen:",
        "packages_title": "Gebouwd met",
        "packages_intro": "Deze website draait op de volgende technologieën en open-source packages:",
        "about_title": "De Bouwer",
        "about_intro": "Dennis Bakhuis - Data Scientist",
        "about_text_p1": "Dennis is een data scientist met een Ph.D. van de Universiteit Twente. Zijn achtergrond zit 'm in fluid dynamics, deep learning en natural language processing - kortom, hij vindt het leuk om met data te spelen en er inzichten uit te halen.",
        "about_text_p2": "Buiten zijn werk bij TenneT als data scientist, is Dennis het liefst buiten te vinden. Meerdaagse trekkings met tent, grotten verkennen (speleologie), en duiken in zowel open water als grotten staan regelmatig op het programma. Die liefde voor avontuur en technische uitdagingen zie je ook terug in hoe hij data science en webontwikkeling aanpakt.",
        "about_text_p3": "Nieuwsgierig naar zijn werk? Check zijn LinkedIn voor de professionele kant, of zijn GitHub voor code en projecten.",
        "connect": "Verbinden:",
        "github": "GitHub",
        "linkedin": "LinkedIn",
        "category_shared": "Gedeelde Assets",
        "category_page_home": "Homepage Afbeeldingen",
        "category_page_contact": "Contact Pagina",
        "category_page_credits": "Credits Pagina",
        "category_page_not_found": "404 Pagina",
        "category_page_order_insoles": "Zolen Bestellen Pagina",
        "category_page_reimbursements": "Vergoedingen Pagina",
        "category_page_information": "Informatie Pagina",
        "category_blog": "Blog Afbeeldingen",
        "image_col": "Afbeelding",
        "name_col": "Naam",
        "category_col": "Categorie",
        "attribution_col": "Toeschrijving",
        "cat_shared": "Gedeeld",
        "cat_home": "Home",
        "cat_contact": "Contact",
        "cat_credits": "Credits",
        "cat_404": "404",
        "cat_insoles": "Zolen",
        "cat_reimbursements": "Vergoedingen",
        "cat_info": "Info",
        "cat_blog": "Blog",
    },
    "de": {
        "page_title": "Credits",
        "page_intro": "Websites bauen ist Teamarbeit, auch wenn man alleine am Laptop sitzt. Hier ein Dankeschön an alle Tools, Bilder und Menschen, die diese Website möglich gemacht haben.",
        "images_title": "Bilder",
        "images_intro": "Diese Website verwendet Bilder aus den folgenden Quellen:",
        "packages_title": "Gebaut mit",
        "packages_intro": "Diese Website läuft auf den folgenden Technologien und Open-Source-Paketen:",
        "about_title": "Der Entwickler",
        "about_intro": "Dennis Bakhuis - Data Scientist",
        "about_text_p1": "Dennis ist ein Data Scientist mit einem Ph.D. von der Universität Twente. Sein Hintergrund liegt in Strömungsdynamik, Deep Learning und Natural Language Processing - kurz gesagt, er liebt es, mit Daten zu spielen und Erkenntnisse daraus zu gewinnen.",
        "about_text_p2": "Außerhalb seiner Arbeit als Data Scientist bei TenneT ist Dennis am liebsten draußen unterwegs. Mehrtägige Trekkingtouren mit Zelt, Höhlen erkunden (Speläologie) und Tauchen in offenen Gewässern und Höhlen stehen regelmäßig auf dem Programm. Diese Liebe zu Abenteuer und technischen Herausforderungen spiegelt sich auch in seinem Ansatz zu Data Science und Webentwicklung wider.",
        "about_text_p3": "Neugierig auf seine Arbeit? Schau dir sein LinkedIn für die professionelle Seite an, oder sein GitHub für Code und Projekte.",
        "connect": "Verbinden:",
        "github": "GitHub",
        "linkedin": "LinkedIn",
        "category_shared": "Gemeinsame Assets",
        "category_page_home": "Startseite Bilder",
        "category_page_contact": "Kontakt Seite",
        "category_page_credits": "Credits Seite",
        "category_page_not_found": "404 Seite",
        "category_page_order_insoles": "Einlagen Bestellen Seite",
        "category_page_reimbursements": "Erstattungen Seite",
        "category_page_information": "Informationen Seite",
        "category_blog": "Blog Bilder",
        "image_col": "Bild",
        "name_col": "Name",
        "category_col": "Kategorie",
        "attribution_col": "Zuordnung",
        "cat_shared": "Gemeinsam",
        "cat_home": "Startseite",
        "cat_contact": "Kontakt",
        "cat_credits": "Credits",
        "cat_404": "404",
        "cat_insoles": "Einlagen",
        "cat_reimbursements": "Erstattungen",
        "cat_info": "Info",
        "cat_blog": "Blog",
    },
    "en": {
        "page_title": "Credits",
        "page_intro": "Building websites is a team effort, even when you're sitting alone at your laptop. Here's a shout-out to all the tools, images, and people that made this website possible.",
        "images_title": "Images",
        "images_intro": "This website uses images from the following sources:",
        "packages_title": "Built With",
        "packages_intro": "This website runs on the following technologies and open-source packages:",
        "about_title": "The Builder",
        "about_intro": "Dennis Bakhuis - Data Scientist",
        "about_text_p1": "Dennis is a data scientist with a Ph.D. from the University of Twente. His background is in fluid dynamics, deep learning, and natural language processing - in short, he loves playing with data and extracting insights from it.",
        "about_text_p2": "Outside his work as a data scientist at TenneT, you'll most likely find Dennis outdoors. Multi-day treks with a tent, exploring caves (speleology), and diving in both open water and caves are regular activities. That love for adventure and technical challenges shows in how he approaches data science and web development too.",
        "about_text_p3": "Curious about his work? Check out his LinkedIn for the professional side, or his GitHub for code and projects.",
        "connect": "Connect:",
        "github": "GitHub",
        "linkedin": "LinkedIn",
        "category_shared": "Shared Assets",
        "category_page_home": "Homepage Images",
        "category_page_contact": "Contact Page",
        "category_page_credits": "Credits Page",
        "category_page_not_found": "404 Page",
        "category_page_order_insoles": "Order Insoles Page",
        "category_page_reimbursements": "Reimbursements Page",
        "category_page_information": "Information Page",
        "category_blog": "Blog Images",
        "image_col": "Image",
        "name_col": "Name",
        "category_col": "Category",
        "attribution_col": "Attribution",
        "cat_shared": "Shared",
        "cat_home": "Home",
        "cat_contact": "Contact",
        "cat_credits": "Credits",
        "cat_404": "404",
        "cat_insoles": "Insoles",
        "cat_reimbursements": "Reimbursements",
        "cat_info": "Info",
        "cat_blog": "Blog",
    },
}


def _create_credit_row(
    label: str,
    content: str | None = None,
    is_link: bool = False,
    href: str | None = None,
) -> rx.Component:
    content_component: rx.Component
    if is_link and href:
        content_component = rx.link(
            label,
            href=href,
            color=Colors.text["link"],
            text_decoration="underline",
            font_weight="600",
            width="200px",
            is_external=True,
        )
    else:
        content_component = regular_text(
            label,
            color=Colors.text["muted"],
            font_weight="600",
            width="200px",
        )

    if content:
        return rx.hstack(
            content_component,
            regular_text(content, color=Colors.text["secondary"]),
            spacing="4",
            align="start",
            margin_bottom="0.75rem",
        )
    return content_component


def _get_category_translation_key(category: str) -> str:
    category_map = {
        "shared": "cat_shared",
        "page_home": "cat_home",
        "page_contact": "cat_contact",
        "page_credits": "cat_credits",
        "page_not_found": "cat_404",
        "page_order_insoles": "cat_insoles",
        "page_reimbursements": "cat_reimbursements",
        "page_information": "cat_info",
        "blog": "cat_blog",
    }
    return category_map.get(category, "cat_shared")


def _create_image_table_row(
    image_path: str,
    name: str,
    category: str,
    author: str | None,
    author_url: str | None,
    source: str,
    source_url: str | None,
    is_header: bool = False,
) -> rx.Component:
    if is_header:
        return rx.hstack(
            rx.box(width="64px"),
            rx.box(
                regular_text(name, font_weight="700", color=Colors.text["heading"]),
                width="200px",
                flex_shrink="0",
            ),
            rx.box(
                regular_text(category, font_weight="700", color=Colors.text["heading"]),
                width="120px",
                flex_shrink="0",
            ),
            rx.box(
                regular_text(source, font_weight="700", color=Colors.text["heading"]),
                flex="1",
            ),
            spacing="3",
            padding="0.5rem",
            border_bottom=f"2px solid {Colors.text['muted']}",
        )

    if author is None:
        attribution = regular_text(source, color=Colors.text["secondary"])
    else:
        attribution = rx.box(
            rx.link(
                author,
                href=author_url,
                color=Colors.text["link"],
                text_decoration="underline",
                is_external=True,
            ),
            regular_text(" on ", color=Colors.text["secondary"], display="inline"),
            rx.link(
                source,
                href=source_url,
                color=Colors.text["link"],
                text_decoration="underline",
                is_external=True,
            ),
        )

    return rx.hstack(
        rx.box(
            rx.image(
                src=image_path,
                alt=name,
                height="48px",
                width="64px",
                object_fit="cover",
                border_radius="4px",
            ),
            width="64px",
            flex_shrink="0",
        ),
        rx.box(
            regular_text(name, color=Colors.text["content"]),
            width="200px",
            flex_shrink="0",
        ),
        rx.box(
            regular_text(category, color=Colors.text["secondary"]),
            width="120px",
            flex_shrink="0",
        ),
        rx.box(attribution, flex="1"),
        spacing="3",
        padding="0.5rem",
        border_bottom=f"1px solid {Colors.borders['light']}",
        align="center",
    )


def section_content(language: str) -> rx.Component:
    """
    Create the main content section for the credits page.

    Parameters
    ----------
    language : str
        The current language code (nl, de, or en).

    Returns
    -------
    rx.Component
        A section component containing all credits information.
    """
    return section(
        container(
            header(
                get_translation(TRANSLATIONS, "page_title", language),
                level=1,
                color=Colors.text["heading"],
                margin_bottom=Spacing.text_margin_bottom,
            ),
            regular_text(
                get_translation(TRANSLATIONS, "page_intro", language),
                color=Colors.text["secondary"],
                margin_bottom=Spacing.section_gap,
            ),
            rx.box(
                image_text_section(
                    image_fallback="/images/page_credits/dennis_bakhuis_data_scientist_voorvoet_website_developer.jpg",
                    image_avif="/images/page_credits/dennis_bakhuis_data_scientist_voorvoet_website_developer.avif",
                    image_webp="/images/page_credits/dennis_bakhuis_data_scientist_voorvoet_website_developer.webp",
                    image_alt=get_translation(
                        TRANSLATIONS, "credits_dennis_portrait", language
                    ),
                    dimensions=ImageDimensions.content_portrait,
                    image_position="left",
                    title=get_translation(TRANSLATIONS, "about_title", language),
                    paragraphs=[
                        get_translation(TRANSLATIONS, "about_text_p1", language),
                        get_translation(TRANSLATIONS, "about_text_p2", language),
                    ],
                ),
                rx.text(
                    get_translation(TRANSLATIONS, "about_text_p3", language).split(
                        "LinkedIn"
                    )[0],
                    rx.link(
                        "LinkedIn",
                        href="https://linkedin.com/in/dennisbakhuis",
                        color=Colors.text["link"],
                        text_decoration="underline",
                        is_external=True,
                    ),
                    get_translation(TRANSLATIONS, "about_text_p3", language)
                    .split("LinkedIn")[1]
                    .split("GitHub")[0],
                    rx.link(
                        "GitHub",
                        href="https://github.com/dennisbakhuis",
                        color=Colors.text["link"],
                        text_decoration="underline",
                        is_external=True,
                    ),
                    get_translation(TRANSLATIONS, "about_text_p3", language).split(
                        "GitHub"
                    )[1],
                    font_size=FontSizes.regular,
                    color=Colors.text["content"],
                    line_height="1.6",
                    text_align="left",
                ),
                margin_bottom=Spacing.section_gap,
            ),
            rx.box(
                header(
                    get_translation(TRANSLATIONS, "packages_title", language),
                    level=2,
                    color=Colors.text["subheading"],
                    margin_bottom=Spacing.text_margin_bottom,
                ),
                regular_text(
                    get_translation(TRANSLATIONS, "packages_intro", language),
                    color=Colors.text["secondary"],
                    margin_bottom=Spacing.text_margin_bottom,
                ),
                rx.box(
                    *[
                        _create_credit_row(
                            pkg["name"],
                            pkg["desc"][language],
                            is_link=True,
                            href=pkg["url"],
                        )
                        for pkg in PYTHON_PACKAGES
                    ],
                    margin_bottom=Spacing.section_gap,
                ),
                margin_bottom=Spacing.section_gap,
            ),
            rx.box(
                header(
                    get_translation(TRANSLATIONS, "images_title", language),
                    level=2,
                    color=Colors.text["subheading"],
                    margin_bottom=Spacing.text_margin_bottom,
                ),
                regular_text(
                    get_translation(TRANSLATIONS, "images_intro", language),
                    color=Colors.text["secondary"],
                    margin_bottom=Spacing.text_margin_bottom,
                ),
                rx.box(
                    rx.box(
                        _create_image_table_row(
                            "",
                            get_translation(TRANSLATIONS, "name_col", language),
                            get_translation(TRANSLATIONS, "category_col", language),
                            None,
                            None,
                            get_translation(TRANSLATIONS, "attribution_col", language),
                            None,
                            is_header=True,
                        ),
                        *[
                            _create_image_table_row(
                                img["image_path"],
                                img["desc"][language],
                                get_translation(
                                    TRANSLATIONS,
                                    _get_category_translation_key(img["category"]),
                                    language,
                                ),
                                img["author"],
                                img["author_url"],
                                img["source"],
                                img["source_url"],
                            )
                            for img in sorted(IMAGES, key=lambda x: x["category"])
                        ],
                    ),
                    overflow_x="auto",
                    margin_bottom=Spacing.section_gap,
                ),
            ),
        ),
        background_color=Colors.backgrounds["white"],
        padding_top="2rem",
        padding_bottom="2rem",
    )
