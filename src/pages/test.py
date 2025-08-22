import reflex as rx

# -----------------------------
# THEME / TOKENS
# -----------------------------
PRIMARY = "#0f766e"  # teal-700
ACCENT = "#111827"   # gray-900
LIGHT = "#ffffff"
MUTED = "#efefef"
DARK    = "#111827"   # gray-900

# -----------------------------
# APP STATE
# -----------------------------
class BistroState(rx.State):
    nav_open: bool = False

    modal_open: bool = False
    modal_title: str = ""
    modal_desc: str = ""
    modal_input: str = ""

    def toggle_nav(self):
        self.nav_open = not self.nav_open

    def open_modal(self, title: str, desc: str):
        self.modal_title = title
        self.modal_desc = desc
        self.modal_open = True

    def close_modal(self):
        self.modal_open = False
        self.modal_input = ""

    def set_modal_input(self, value: str):
        self.modal_input = value

    def on_modal_change(self, is_open: bool):
        if not is_open:
            self.close_modal()
        else:
            self.modal_open = True


# -----------------------------
# PRIMITIVES
# -----------------------------
# PRIMITIVES
def container(*children, **styles) -> rx.Component:
    base = dict(
        width="100%",
        max_width="1200px",
        margin_x="auto",                     # was: mx="auto"
        padding_x=["5%", "5%", "10%"],       # was: px=[...]
    )
    base.update(styles)
    return rx.box(*children, **base)


def section(*children, bg=LIGHT, **styles) -> rx.Component:
    return rx.box(
        *children,
        width="100%",
        py=["48px", "64px"],
        bg=bg,
        **styles,
    )


def button(label: str, href: str | None = None, on_click=None, variant: str = "solid") -> rx.Component:
    base = dict(
        px="20px",
        py="12px",
        border_radius="9999px",
        font_weight="600",
        transition="all .2s ease",
        cursor="pointer",
        display="inline-flex",
        align_items="center",
        gap="8px",
        white_space="nowrap",
    )
    if variant == "solid":
        base.update(bg=LIGHT, color=ACCENT, _hover={"bg": PRIMARY, "color": LIGHT})
    elif variant == "primary":
        base.update(bg=PRIMARY, color=LIGHT, _hover={"opacity": 0.9})
    else:
        base.update(bg="transparent", border=f"1px solid {LIGHT}", color=LIGHT, _hover={"bg": LIGHT, "color": ACCENT})

    element = rx.link(rx.hstack(rx.text(label),), href=href) if href else rx.box(rx.text(label))
    return rx.box(element, on_click=on_click, **base)


def responsive_grid(*children, columns=[1, 1, 2], spacing="8", **styles) -> rx.Component:
    labels = ["initial", "sm", "md", "lg", "xl", "2xl"]
    bp = {labels[i]: str(c) for i, c in enumerate(columns) if i < len(labels)}
    cols = rx.breakpoints(**bp)
    props = dict(columns=cols, gap=spacing)
    props.update(styles)
    return rx.grid(*children, **props)

# -----------------------------
# HEADER
# -----------------------------
def header() -> rx.Component:
    nav_links = [
        ("About us", "#about"),
        ("Menus", "#menus"),
        ("Contact us", "#footer"),
        ("Order online", "#order"),
    ]

    def nav_items(color=DARK):
        return [
            rx.link(
                l,
                href=h,
                color=DARK,                      # default text = gray-900
                font_size="24px",
                font_weight="600",
                _hover={"color": PRIMARY},        # hover = teal-700
            )
            for l, h in nav_links
        ]


    bar = rx.hstack(
        container(
            rx.hstack(
                rx.image(
                    src="/images/podotherapeut_enschede_voorvoet_praktijk_voor_podotherapie_logo.svg",
                    width="300px",
                    height="90px",
                ),
                rx.hstack(
                    rx.hstack(*nav_items(), gap="20px", display=["none", "none", "flex"]),
                    rx.icon_button(
                        "menu",
                        aria_label="menu",
                        on_click=BistroState.toggle_nav,
                        display=["inline-flex", "inline-flex", "none"],
                        color=LIGHT,
                        bg="transparent",
                    ),
                    align="center",
                    justify="end",
                ),
                align="center",
                justify="between",
                width="100%",
            ),
            # IMPORTANT: use the correct keys the helper expects
            max_width="1200px",
            margin_x="auto",
            padding_x=["12px", "16px", "24px"],  # small, consistent side padding
        ),
        position="fixed",
        top="0",
        left="0",
        z_index="20",
        width="100%",
        # height="60px",
        style={"backdropFilter": "saturate(180%) blur(6px)"},
    )

    mobile_menu = rx.cond(
        BistroState.nav_open,
        rx.box(
            container(
                rx.vstack(
                    *[
                        rx.link(
                            l,
                            href=h,
                            width="100%",
                            text_align="right",
                            color=LIGHT,
                            py="8px",
                            on_click=BistroState.toggle_nav,
                        )
                        for l, h in nav_links
                    ],
                    gap="10px",
                ),
                max_width="1200px",
                margin_x="auto",
                padding_x=["12px", "16px", "24px"],  # match header padding
            ),
            position="fixed",
            top="60px",
            left="0",
            width="100%",
            bg=ACCENT,
            py="16px",
            z_index="19",
        ),
        rx.box(),
    )

    return rx.fragment(bar, mobile_menu)


# -----------------------------
# HERO
# -----------------------------
def hero(image_url: str, title: str, subtitle: str | None = None) -> rx.Component:
    return rx.box(
        # Image
        rx.image(
            src=image_url,
            object_fit="cover",
            width="100%",
            height=["90dvh", "100vh"],
            filter="brightness(1.05) saturate(1.06)",
        ),
        # Green/white tint + soft vignette
        rx.box(
            position="absolute",
            inset="0",
            bg="linear-gradient(180deg, rgba(255,255,255,.55) 0%, rgba(16,185,129,.35) 100%)",
            mix_blend_mode="screen",
            pointer_events="none",
        ),
        rx.box(
            position="absolute",
            inset="0",
            bg="linear-gradient(180deg, rgba(0,0,0,.08) 0%, rgba(0,0,0,.22) 100%)",
            pointer_events="none",
        ),

        container(
            rx.vstack(
                rx.text(
                    title,
                    color=PRIMARY,
                    font_weight="900",
                    text_align="center",
                    line_height="1.05",
                    font_size=["3rem", "4rem", "5rem", "6rem"],  # sm → xl screens
                ),
                rx.text(
                    subtitle or "",
                    color=DARK,
                    text_align="center",
                    opacity="0.95",
                    font_weight="600",
                    line_height="1.15",
                    font_size=["2rem", "2.25rem", "2.7rem", "3rem"],
                ) if subtitle else None,
                spacing="3",
                align="center",
            ),
            position="absolute",
            top="38%",                         # a bit higher, like the original
            left="50%",
            transform="translate(-50%, -50%)",
            width="100%",
            min_height="600px",  # ensure enough height for text
        ),

        # CTA aligned to the bottom-right of the 1200px container (not the viewport)
        rx.box(
            container(
                rx.box(
                    rx.vstack(
                        rx.text("Direct digitaal een afspraak maken!", color=DARK, class_name="text-slate-900 font-semibold"),
                        rx.vstack(
                            rx.hstack(rx.html(f"<i class='fa fa-check-square-o text-[{PRIMARY}] text-lg'></i>"), rx.text("Geen verwijzing nodig!", class_name="text-slate-800")),
                            rx.hstack(rx.html(f"<i class='fa fa-check-square-o text-[{PRIMARY}] text-lg'></i>"), rx.text("Snel geholpen door een professional.", class_name="text-slate-800")),
                            rx.hstack(rx.html(f"<i class='fa fa-check-square-o text-[{PRIMARY}] text-lg'></i>"), rx.text("Snelste weg naar de specialist!", class_name="text-slate-800")),
                            spacing="2",
                            align="start",
                        ),
                        button("Maak een afspraak", href="#afspraak", variant="primary"),
                        spacing="4",
                        align="start",
                    ),
                    position="absolute",
                    right=["1rem", "2rem", "3rem", "3rem", "3rem"],   # from container edge
                    bottom=["1rem", "2rem", "2.5rem", "3rem", "3rem"],
                    width=["92%", "22rem", "26rem", "30rem", "34rem"],  # larger on big screens
                    max_width="38rem",
                    bg="rgba(209, 250, 229, 0.95)",   # light green tint
                    border_radius="0.75rem",
                    padding=["1rem", "1.25rem", "1.5rem", "1.75rem", "2rem"],
                    box_shadow="0 6px 18px rgba(0,0,0,.12)",
                    backdrop_filter="saturate(1.05) blur(1px)",
                ),
                position="relative",   # makes this the positioning context
                width="100%",
                height="100%",
            ),
            position="absolute",
            inset="0",                # overlay spans the hero
        ),

        position="relative",
        width="100%",
        max_width="100vw",
        overflow="hidden",
    )


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
# MODAL
# -----------------------------
def modal() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.box()),
        rx.dialog.content(
            rx.hstack(rx.spacer(), rx.icon_button("x", on_click=BistroState.close_modal), align="center"),
            rx.heading(BistroState.modal_title, size="6", text_align="center"),
            rx.text(BistroState.modal_desc, mt="8px"),
            rx.text_area(
                placeholder="write...",
                value=BistroState.modal_input,
                on_change=BistroState.set_modal_input,
                max_length=2000,
            ),
            rx.hstack(button("Open", href="#", variant="primary"), justify="center", mt="12px"),
            width=["90vw", "480px"],
            max_width="600px",
            bg=LIGHT,
            border_radius="12px",
        ),
        open=BistroState.modal_open,
        on_open_change=BistroState.on_modal_change,   # <-- no lambda
    )


# -----------------------------
# FOOTER
# -----------------------------
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


# -----------------------------
# PAGE
# -----------------------------
def bistro_page() -> rx.Component:
    return rx.fragment(
        header(),
        hero("/images/podotherapeut_enschede_voeten_in_bed_podotherapie_helpt.jpeg", "Voetklachten?", "Loop er niet mee door!"),
        about("/assets/images/homepage/coffee.jpg", "Bistro Restaurant", "Welcomes you", "Discover the charm of Bistro, an authentic English restaurant offering a taste of Ireland in every bite. Indulge in traditional cuisine complemented by warm hospitality and a cozy ambiance."),
        menu_grid(),
        map_embed(),
        award(),
        footer(),
        modal(),
    )
