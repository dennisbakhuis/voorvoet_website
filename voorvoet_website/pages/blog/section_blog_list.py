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
            # Section title
            rx.heading(
                "Laatste artikelen",
                size="9",
                color=Colors.text['heading'],
                margin_bottom="3rem",
                text_align="center",
            ),

            # Blog posts grid
            rx.cond(
                BlogState.has_posts,
                rx.grid(
                    rx.foreach(
                        BlogState.sorted_posts,
                        blog_card,
                    ),
                    columns="3",  # 3 columns
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
                    padding="4rem",
                    align_items="center",
                ),
            ),
        ),
        padding_y="4rem",
        background=Colors.backgrounds['white'],
    )
