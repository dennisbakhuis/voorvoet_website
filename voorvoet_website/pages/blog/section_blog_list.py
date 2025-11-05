# Blog list section - displays grid of blog posts
import reflex as rx
from ...state import BlogState
from ...theme import Colors, FontSizes
from ...components import container
from .components import blog_card


def section_blog_list() -> rx.Component:
    """
    Display a grid of blog post cards

    Returns:
        Reflex component with blog post grid
    """
    return rx.section(
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
                # Empty state if no posts
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
