"""Content section for the credits page."""

import reflex as rx

from ...components import container, section, header, regular_text
from ...data.credits import PYTHON_PACKAGES, IMAGES
from ...theme import Colors, Spacing
from ...utils.get_translation import get_translation


TRANSLATIONS = {
    "nl": {
        "page_title": "Credits",
        "images_title": "Afbeeldingen",
        "images_intro": "Deze website gebruikt afbeeldingen van de volgende bronnen:",
        "packages_title": "Python Packages",
        "packages_intro": "Deze website is gebouwd met de volgende open-source packages:",
        "reflex_desc": "Full-stack web framework voor Python",
        "mistletoe_desc": "Fast, extensible Markdown parser",
        "pydantic_settings_desc": "Settings management using Pydantic",
        "frontmatter_desc": "Parse and manage posts with YAML frontmatter",
        "about_title": "Over de Website",
        "about_text": "Deze website is met veel zorg ontwikkeld door Dennis Bakhuis, een software engineer met een passie voor webontwikkeling en data science.",
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
        "logo_image": "VoorVoet Logo",
        "nvvp_badge": "NVVP Lidmaatschap Badge",
        "register_paramedici_badge": "Register Paramedici Certificering",
        "nvvp_quality_mark": "NVVP Kwaliteitskeurmerk",
        "home_hero_beach": "Hero: Kim Bakhuis op strand",
        "home_who_is_voorvoet": "Wie is VoorVoet: Kim Bakhuis portret",
        "home_outdoor_shoes": "Outdoor schoenen",
        "home_feet_in_bed": "Voeten in bed",
        "contact_hero": "Contact hero banner",
        "credits_hero": "Credits hero banner",
        "404_image": "404 pagina achtergrond",
        "order_insoles_hero": "Zolen bestellen hero",
        "reimbursements_hero": "Vergoedingen hero",
        "info_foot_anatomy": "Voet anatomie",
        "info_business_podotherapy": "Bedrijfs podotherapie",
        "info_nail_bracket": "Nagelbeugel behandeling",
        "info_practitioner": "Behandelaar met patiënt",
        "info_forest_walk": "Wandeling in het bos",
        "info_foot_skeleton": "Voet skelet",
        "info_sports": "Sport voetklachten",
        "info_walking": "Wandelen zonder pijn",
        "blog_default_thumbnail": "Blog standaard thumbnail",
        "blog_default_filler": "Blog standaard opvulling",
        "blog_sandals": "Sandalen afbeelding",
        "blog_001_thumbnail": "Blog post 001: Thumbnail",
        "blog_001_hero": "Blog post 001: Hero",
        "blog_002_thumbnail": "Blog post 002: Thumbnail",
        "blog_002_hero": "Blog post 002: Hero",
        "blog_003_thumbnail": "Blog post 003: Thumbnail",
        "blog_003_hero_1": "Blog post 003: Hero 1",
        "blog_003_hero_2": "Blog post 003: Hero 2",
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
        "images_title": "Bilder",
        "images_intro": "Diese Website verwendet Bilder aus den folgenden Quellen:",
        "packages_title": "Python-Pakete",
        "packages_intro": "Diese Website wurde mit den folgenden Open-Source-Paketen erstellt:",
        "reflex_desc": "Full-Stack-Webframework für Python",
        "mistletoe_desc": "Schneller, erweiterbarer Markdown-Parser",
        "pydantic_settings_desc": "Einstellungsverwaltung mit Pydantic",
        "frontmatter_desc": "Beiträge mit YAML-Frontmatter parsen und verwalten",
        "about_title": "Über die Website",
        "about_text": "Diese Website wurde mit viel Sorgfalt von Dennis Bakhuis entwickelt, einem Software-Ingenieur mit einer Leidenschaft für Webentwicklung und Data Science.",
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
        "logo_image": "VoorVoet Logo",
        "nvvp_badge": "NVVP Mitgliedschaftsabzeichen",
        "register_paramedici_badge": "Register Paramedici Zertifizierung",
        "nvvp_quality_mark": "NVVP Qualitätszeichen",
        "home_hero_beach": "Hero: Kim Bakhuis am Strand",
        "home_who_is_voorvoet": "Wer ist VoorVoet: Kim Bakhuis Porträt",
        "home_outdoor_shoes": "Outdoor-Schuhe",
        "home_feet_in_bed": "Füße im Bett",
        "contact_hero": "Kontakt Hero-Banner",
        "credits_hero": "Credits Hero-Banner",
        "404_image": "404-Seite Hintergrund",
        "order_insoles_hero": "Einlagen bestellen Hero",
        "reimbursements_hero": "Erstattungen Hero",
        "info_foot_anatomy": "Fuß Anatomie",
        "info_business_podotherapy": "Betriebliche Podotherapie",
        "info_nail_bracket": "Nagelspangen-Behandlung",
        "info_practitioner": "Behandler mit Patient",
        "info_forest_walk": "Waldspaziergang",
        "info_foot_skeleton": "Fuß Skelett",
        "info_sports": "Sport Fußbeschwerden",
        "info_walking": "Schmerzfrei gehen",
        "blog_default_thumbnail": "Blog Standard-Thumbnail",
        "blog_default_filler": "Blog Standard-Füller",
        "blog_sandals": "Sandalen Bild",
        "blog_001_thumbnail": "Blog-Post 001: Thumbnail",
        "blog_001_hero": "Blog-Post 001: Hero",
        "blog_002_thumbnail": "Blog-Post 002: Thumbnail",
        "blog_002_hero": "Blog-Post 002: Hero",
        "blog_003_thumbnail": "Blog-Post 003: Thumbnail",
        "blog_003_hero_1": "Blog-Post 003: Hero 1",
        "blog_003_hero_2": "Blog-Post 003: Hero 2",
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
        "images_title": "Images",
        "images_intro": "This website uses images from the following sources:",
        "packages_title": "Python Packages",
        "packages_intro": "This website was built using the following open-source packages:",
        "reflex_desc": "Full-stack web framework for Python",
        "mistletoe_desc": "Fast, extensible Markdown parser",
        "pydantic_settings_desc": "Settings management using Pydantic",
        "frontmatter_desc": "Parse and manage posts with YAML frontmatter",
        "about_title": "About the Website",
        "about_text": "This website was carefully developed by Dennis Bakhuis, a software engineer with a passion for web development and data science.",
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
        "logo_image": "VoorVoet Logo",
        "nvvp_badge": "NVVP Membership Badge",
        "register_paramedici_badge": "Register Paramedici Certification",
        "nvvp_quality_mark": "NVVP Quality Mark",
        "home_hero_beach": "Hero: Kim Bakhuis on beach",
        "home_who_is_voorvoet": "Who is VoorVoet: Kim Bakhuis portrait",
        "home_outdoor_shoes": "Outdoor shoes",
        "home_feet_in_bed": "Feet in bed",
        "contact_hero": "Contact hero banner",
        "credits_hero": "Credits hero banner",
        "404_image": "404 page background",
        "order_insoles_hero": "Order insoles hero",
        "reimbursements_hero": "Reimbursements hero",
        "info_foot_anatomy": "Foot anatomy",
        "info_business_podotherapy": "Business podotherapy",
        "info_nail_bracket": "Nail bracket treatment",
        "info_practitioner": "Practitioner with patient",
        "info_forest_walk": "Forest walk",
        "info_foot_skeleton": "Foot skeleton",
        "info_sports": "Sports foot complaints",
        "info_walking": "Walking without pain",
        "blog_default_thumbnail": "Blog default thumbnail",
        "blog_default_filler": "Blog default filler",
        "blog_sandals": "Sandals image",
        "blog_001_thumbnail": "Blog post 001: Thumbnail",
        "blog_001_hero": "Blog post 001: Hero",
        "blog_002_thumbnail": "Blog post 002: Thumbnail",
        "blog_002_hero": "Blog post 002: Hero",
        "blog_003_thumbnail": "Blog post 003: Thumbnail",
        "blog_003_hero_1": "Blog post 003: Hero 1",
        "blog_003_hero_2": "Blog post 003: Hero 2",
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
                margin_bottom=Spacing.section_gap,
            ),
            rx.box(
                header(
                    get_translation(TRANSLATIONS, "about_title", language),
                    level=2,
                    color=Colors.text["subheading"],
                    margin_bottom=Spacing.text_margin_bottom,
                ),
                regular_text(
                    get_translation(TRANSLATIONS, "about_text", language),
                    color=Colors.text["secondary"],
                    margin_bottom=Spacing.text_margin_bottom,
                ),
                rx.hstack(
                    regular_text(
                        get_translation(TRANSLATIONS, "connect", language),
                        color=Colors.text["muted"],
                        font_weight="600",
                    ),
                    rx.link(
                        get_translation(TRANSLATIONS, "linkedin", language),
                        href="https://linkedin.com/in/dennisbakhuis",
                        color=Colors.text["link"],
                        text_decoration="underline",
                        is_external=True,
                    ),
                    regular_text("|", color=Colors.text["muted"]),
                    rx.link(
                        get_translation(TRANSLATIONS, "github", language),
                        href="https://github.com/dennisbakhuis",
                        color=Colors.text["link"],
                        text_decoration="underline",
                        is_external=True,
                    ),
                    spacing="2",
                    align="center",
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
                            get_translation(TRANSLATIONS, pkg["desc_key"], language),
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
                                get_translation(
                                    TRANSLATIONS, img["desc_key"], language
                                ),
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
