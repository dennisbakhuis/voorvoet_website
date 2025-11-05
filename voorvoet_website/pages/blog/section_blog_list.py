"""Blog list section displaying grid of blog post cards."""
import reflex as rx
from ...states import BlogState
from ...theme import Colors, FontSizes
from ...components import container, blog_card, section


def section_blog_list() -> rx.Component:
    """
    Display a grid of blog post cards.

    Creates a responsive layout that shows all blog posts in a vertical stack.
    Each blog post card alternates its layout (flipped) for visual variety.
    Displays an empty state message when no posts are available.

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
                        "Nog geen blogposts beschikbaar.",
                        color=Colors.text['muted'],
                        font_size=FontSizes.regular,
                    ),
                    align_items="center",
                ),
            ),
        ),
        background=Colors.backgrounds['white'],
    )
