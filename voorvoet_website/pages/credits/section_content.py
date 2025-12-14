"""Content section for the credits page."""

import reflex as rx

from ...components import container, section, header, regular_text
from ...theme import Colors, Spacing
from ...utils.get_translation import get_translation


TRANSLATIONS = {
    "nl": {
        "page_title": "Credits",
        "images_title": "Afbeeldingen",
        "images_intro": "Deze website gebruikt afbeeldingen van de volgende bronnen:",
        "404_credit": "404 pagina achtergrond",
        "404_source": "Photo by Daniel Jensen on Unsplash",
        "hero_images": "Hero banner afbeeldingen",
        "hero_placeholder": "[Naam pagina] - [Bron]",
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
    },
    "de": {
        "page_title": "Credits",
        "images_title": "Bilder",
        "images_intro": "Diese Website verwendet Bilder aus den folgenden Quellen:",
        "404_credit": "404-Seite Hintergrund",
        "404_source": "Foto von Daniel Jensen auf Unsplash",
        "hero_images": "Hero-Banner-Bilder",
        "hero_placeholder": "[Seitenname] - [Quelle]",
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
    },
    "en": {
        "page_title": "Credits",
        "images_title": "Images",
        "images_intro": "This website uses images from the following sources:",
        "404_credit": "404 page background",
        "404_source": "Photo by Daniel Jensen on Unsplash",
        "hero_images": "Hero banner images",
        "hero_placeholder": "[Page name] - [Source]",
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
    },
}


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
                        regular_text(
                            get_translation(TRANSLATIONS, "404_credit", language),
                            color=Colors.text["muted"],
                            font_weight="600",
                            margin_bottom="0.25rem",
                        ),
                        rx.box(
                            rx.link(
                                "Daniel Jensen",
                                href="https://unsplash.com/@dallehj",
                                color=Colors.text["link"],
                                text_decoration="underline",
                                is_external=True,
                                margin_right="0.25rem",
                            ),
                            regular_text(
                                "on",
                                color=Colors.text["secondary"],
                                display="inline",
                                margin_x="0.25rem",
                            ),
                            rx.link(
                                "Unsplash",
                                href="https://unsplash.com/photos/persons-hand-over-brown-floral-field-during-daytime-UDleHDOhBZ8",
                                color=Colors.text["link"],
                                text_decoration="underline",
                                is_external=True,
                                margin_left="0.25rem",
                            ),
                        ),
                        margin_bottom="0.75rem",
                    ),
                    rx.hstack(
                        regular_text(
                            "Credits hero",
                            color=Colors.text["muted"],
                            font_weight="600",
                            width="200px",
                        ),
                        regular_text(
                            "[Bron invullen]",
                            color=Colors.text["secondary"],
                        ),
                        spacing="4",
                        align="start",
                        margin_bottom="0.75rem",
                    ),
                    rx.hstack(
                        regular_text(
                            "Home hero",
                            color=Colors.text["muted"],
                            font_weight="600",
                            width="200px",
                        ),
                        regular_text(
                            "[Bron invullen]",
                            color=Colors.text["secondary"],
                        ),
                        spacing="4",
                        align="start",
                        margin_bottom="0.75rem",
                    ),
                    rx.hstack(
                        regular_text(
                            "Vergoedingen hero",
                            color=Colors.text["muted"],
                            font_weight="600",
                            width="200px",
                        ),
                        regular_text(
                            "[Bron invullen]",
                            color=Colors.text["secondary"],
                        ),
                        spacing="4",
                        align="start",
                        margin_bottom="0.75rem",
                    ),
                    rx.hstack(
                        regular_text(
                            "Informatie hero",
                            color=Colors.text["muted"],
                            font_weight="600",
                            width="200px",
                        ),
                        regular_text(
                            "[Bron invullen]",
                            color=Colors.text["secondary"],
                        ),
                        spacing="4",
                        align="start",
                        margin_bottom="0.75rem",
                    ),
                    rx.hstack(
                        regular_text(
                            "Contact hero",
                            color=Colors.text["muted"],
                            font_weight="600",
                            width="200px",
                        ),
                        regular_text(
                            "[Bron invullen]",
                            color=Colors.text["secondary"],
                        ),
                        spacing="4",
                        align="start",
                        margin_bottom="0.75rem",
                    ),
                    rx.hstack(
                        regular_text(
                            "Blog hero",
                            color=Colors.text["muted"],
                            font_weight="600",
                            width="200px",
                        ),
                        regular_text(
                            "[Bron invullen]",
                            color=Colors.text["secondary"],
                        ),
                        spacing="4",
                        align="start",
                        margin_bottom="0.75rem",
                    ),
                    rx.hstack(
                        regular_text(
                            "Zolen bestellen hero",
                            color=Colors.text["muted"],
                            font_weight="600",
                            width="200px",
                        ),
                        regular_text(
                            "[Bron invullen]",
                            color=Colors.text["secondary"],
                        ),
                        spacing="4",
                        align="start",
                    ),
                    margin_bottom=Spacing.section_gap,
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
                    rx.hstack(
                        rx.link(
                            "Reflex",
                            href="https://reflex.dev",
                            color=Colors.text["link"],
                            text_decoration="underline",
                            font_weight="600",
                            width="200px",
                            is_external=True,
                        ),
                        regular_text(
                            get_translation(TRANSLATIONS, "reflex_desc", language),
                            color=Colors.text["secondary"],
                        ),
                        spacing="4",
                        align="start",
                        margin_bottom="0.75rem",
                    ),
                    rx.hstack(
                        rx.link(
                            "Mistletoe",
                            href="https://github.com/miyuchina/mistletoe",
                            color=Colors.text["link"],
                            text_decoration="underline",
                            font_weight="600",
                            width="200px",
                            is_external=True,
                        ),
                        regular_text(
                            get_translation(TRANSLATIONS, "mistletoe_desc", language),
                            color=Colors.text["secondary"],
                        ),
                        spacing="4",
                        align="start",
                        margin_bottom="0.75rem",
                    ),
                    rx.hstack(
                        rx.link(
                            "Pydantic Settings",
                            href="https://docs.pydantic.dev/latest/concepts/pydantic_settings/",
                            color=Colors.text["link"],
                            text_decoration="underline",
                            font_weight="600",
                            width="200px",
                            is_external=True,
                        ),
                        regular_text(
                            get_translation(
                                TRANSLATIONS, "pydantic_settings_desc", language
                            ),
                            color=Colors.text["secondary"],
                        ),
                        spacing="4",
                        align="start",
                        margin_bottom="0.75rem",
                    ),
                    rx.hstack(
                        rx.link(
                            "Python Frontmatter",
                            href="https://github.com/eyeseast/python-frontmatter",
                            color=Colors.text["link"],
                            text_decoration="underline",
                            font_weight="600",
                            width="200px",
                            is_external=True,
                        ),
                        regular_text(
                            get_translation(TRANSLATIONS, "frontmatter_desc", language),
                            color=Colors.text["secondary"],
                        ),
                        spacing="4",
                        align="start",
                    ),
                    margin_bottom=Spacing.section_gap,
                ),
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
            ),
        ),
        background_color=Colors.backgrounds["white"],
        padding_top="2rem",
        padding_bottom="2rem",
    )
