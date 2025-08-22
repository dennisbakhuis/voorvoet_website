import reflex as rx

from .hero_section import hero_section
from ..shared_components import footer, header, modal

from ...components import button, container, responsive_grid, section
from ...theme import LIGHT, PRIMARY


# -----------------------------
# ABOUT
# -----------------------------
def about(image_url: str, title: str, headline: str, body: str) -> rx.Component:
    return section(
        container(
            responsive_grid(
                rx.box(rx.image(src=image_url, width="100%", height="100%", object_fit="cover", border_radius="12px")),
                rx.vstack(
                    rx.text(title, color=PRIMARY, font_size=["20px", "24px"], font_weight="600"),
                    rx.heading(headline, size="8"),
                    rx.text(body, text_align=["justify", "justify"], max_width="540px"),
                    button("View on map", href="#map", variant="primary"),
                    spacing="3",
                ),
                columns=[1, 1, 2],
                spacing="8",
                align_items="center",
            )
        ),
        id="about",
    )


# -----------------------------
# MENU GRID
# -----------------------------
def menu_card(label: str, image_url: str, height="240px") -> rx.Component:
    return rx.box(
        rx.image(src=image_url, width="100%", height=height, object_fit="cover", transition="transform .25s ease", _hover={"transform": "scale(1.03)"}),
        rx.box(
            rx.text(label, font_size="20px", font_weight="700"),
            position="absolute",
            bottom="12px",
            left="12px",
            bg="rgba(0,0,0,.55)",
            color=LIGHT,
            px="12px",
            py="8px",
            border_radius="9999px",
        ),
        position="relative",
        overflow="hidden",
        border_radius="12px",
        cursor="pointer",
    )


def menu_grid() -> rx.Component:
    return section(
        container(
            rx.vstack(
                rx.text("Discover Authentic English Flavours", italic=True),
                rx.heading("Explore our menu", size="8", color=PRIMARY),
                responsive_grid(
                    rx.vstack(
                        responsive_grid(
                            menu_card("Coffee", "/assets/images/homepage/coffee.jpg", height="450px"),
                            menu_card("Lunch", "/assets/images/homepage/lunch.jpg", height="450px"),
                            columns=[1, 1, 2],
                            spacing="5",
                        ),
                        menu_card("Dinner", "/assets/images/homepage/dinner.jpg", height="240px"),
                        spacing="5",
                    ),
                    rx.vstack(
                        menu_card("Breakfast", "/assets/images/homepage/breakfast.jpg", height="210px"),
                        menu_card("Drinks", "/assets/images/homepage/wine.jpeg", height="210px"),
                        menu_card("Desserts", "/assets/images/homepage/dessert.jpg", height="210px"),
                        spacing="5",
                        width="100%",
                    ),
                    columns=[1, 1, 2],
                    spacing="5",
                ),
                spacing="6",
                align="center",
            )
        ),
        id="menus",
    )


# -----------------------------
# MAP + AWARD
# -----------------------------
def map_embed() -> rx.Component:
    return section(
        container(
            rx.vstack(
                rx.heading("On the map", size="7", color=PRIMARY),
                rx.box(
                    rx.html(
                        '<iframe src="https://www.google.com/maps/embed?" style="border:0;width:100%;height:350px" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>'
                    ),
                    width="100%",
                    max_width="800px",
                ),
                spacing="4",
                align="center",
            ),
            id="map",
        )
    )


def award() -> rx.Component:
    return section(
        container(
            rx.vstack(
                rx.heading("Award", size="7", color=PRIMARY),
                rx.image(src="/assets/images/homepage/tripadvisor-travellers choice.png", width=["150px", "250px"], height=["150px", "250px"]),
                spacing="4",
                align="center",
            )
        )
    )


# -----------------------------
# PAGE
# -----------------------------
def home_page() -> rx.Component:
    return rx.fragment(
        header(),
        hero_section(),
        about("/assets/images/homepage/coffee.jpg", "Bistro Restaurant", "Welcomes you", "Discover the charm of Bistro, an authentic English restaurant offering a taste of Ireland in every bite. Indulge in traditional cuisine complemented by warm hospitality and a cozy ambiance."),
        menu_grid(),
        map_embed(),
        award(),
        footer(),
        modal(),
    )
