"""Blog list section displaying grid of blog post cards."""
import reflex as rx
from ...states import BlogState
from ...theme import Colors, FontSizes
from ...components import container, blog_card, section
from ...utils.get_translations import get_translation


TRANSLATIONS = {
    "nl": {
        "no_posts": "Nog geen blogposts beschikbaar.",
    },
    "de": {
        "no_posts": "Noch keine Blogbeiträge verfügbar.",
    },
    "en": {
        "no_posts": "No blog posts available yet.",
    },
}


def section_blog_list(language: str) -> rx.Component:
    """
    Display a grid of blog post cards.

    Creates a responsive layout that shows all blog posts in a vertical stack.
    Each blog post card alternates its layout (flipped) for visual variety.
    Displays an empty state message when no posts are available.

    Parameters
    ----------
    language : str
        Current language code ("nl", "de", or "en")

    Returns
    -------
    rx.Component
        A section component containing either a vstack of blog cards or
        an empty state message when no posts exist.
    """
    return section(
        container(
            rx.cond(
                BlogState.has_posts,
                rx.vstack(
                    rx.foreach(
                        BlogState.sorted_posts,
                        lambda post, index: blog_card(post, flip=index % 2 == 1),
                    ),
                    spacing="5",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        get_translation(TRANSLATIONS, "no_posts", language),
                        color=Colors.text['muted'],
                        font_size=FontSizes.regular,
                    ),
                    align_items="center",
                ),
            ),
        ),
        background=Colors.backgrounds['white'],
    )
