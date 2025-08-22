# Footer for the whole site
import reflex as rx

from ...components import container, responsive_grid
from ...theme import LIGHT, PRIMARY


def footer() -> rx.Component:
    def col_links(title, links):
        return rx.vstack(
            rx.heading(title, size="6"),
            rx.vstack(*[rx.link(text, href="#", color=LIGHT) for text in links], align_items="start", spacing="2"),
            spacing="3",
            width="250px",
        )

    return rx.box(
        rx.box(
            container(
                responsive_grid(
                    rx.vstack(
                        rx.image(src="/assets/bistro-white.png", width="200px"),
                        rx.text("2 Lord Edward St,\nTemple Bar,\nD02 P634,\nUS"),
                        rx.text("Follow us", font_weight="700", font_size="18px"),
                        rx.hstack(
                            rx.link(rx.icon(tag="linkedin"), href="#"),
                            rx.link(rx.icon(tag="twitter"), href="https://twitter.com/pauls_freeman"),
                            rx.link(rx.icon(tag="instagram"), href="https://twitter.com/pauls_freeman"),
                            gap="16px",
                        ),
                        spacing="4",
                    ),
                    col_links("Menu", ["Breakfast menu", "Lunch menu", "Dessert menu", "Drinks menu"]),
                    col_links("Resources", ["About us", "FAQ", "Contact Us", "Locations", "Privacy policy"]),
                    columns=[1, 2, 3],
                    spacing="8",
                )
            )
        ),
        bg=PRIMARY,
        color=LIGHT,
        py="48px",
        id="footer",
    )
