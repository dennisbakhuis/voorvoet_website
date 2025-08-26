# Hero section for the home page
import reflex as rx
from ...theme import PRIMARY, DARK
from ...components import button, container


def hero_section() -> rx.Component:
    return rx.box(
        rx.image(
            src="/images/podotherapeut_enschede_voeten_in_bed_podotherapie_helpt.jpeg",
            object_fit="cover",
            position="absolute",
            inset="0",
            width="100%",
            height="100%",
            filter="brightness(1.05) saturate(1.06)",
        ),
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
            rx.box(
                rx.vstack(
                    rx.text(
                        "Voetklachten?",
                        color=PRIMARY,
                        font_weight="900",
                        text_align="center",
                        line_height="1.05",
                        font_size=["3rem", "4rem", "5rem", "6rem"],
                    ),
                    rx.text(
                        "Loop er niet mee door!",
                        color=DARK,
                        text_align="center",
                        opacity="0.95",
                        font_weight="600",
                        line_height="1.15",
                        font_size=["2rem", "2.25rem", "2.7rem", "3rem"],
                    ),
                    spacing="2",
                    align="center",
                ),
                display="flex",
                align_items="center",
                justify_content="center",
                height="100%",
            ),
            grid_row="1",
            width="100%",
            z_index=1, 
        ),

        container(
            rx.box(
                rx.vstack(
                    rx.text("Direct digitaal een afspraak maken!", color=DARK, class_name="text-slate-900 font-semibold"),
                    rx.vstack(
                        rx.hstack(rx.html(f"<i class='fa fa-check-square-o text-[{PRIMARY}] text-lg'/>"), rx.text("Geen verwijzing nodig!", class_name="text-slate-800")),
                        rx.hstack(rx.html(f"<i class='fa fa-check-square-o text-[{PRIMARY}] text-lg'/>"), rx.text("Snel geholpen door een professional.", class_name="text-slate-800")),
                        rx.hstack(rx.html(f"<i class='fa fa-check-square-o text-[{PRIMARY}] text-lg'/>"), rx.text("Snelste weg naar de specialist!", class_name="text-slate-800")),
                        spacing="2",
                        align="start",
                    ),
                    button("Maak een afspraak", href="#afspraak", variant="primary"),
                    spacing="4",
                    align="start",
                ),
                width=["100%", "22rem", "26rem", "30rem", "34rem"],
                max_width="38rem",
                bg="rgba(209, 250, 229, 0.95)",
                border_radius="0.75rem",
                padding=["1rem", "1.25rem", "1.5rem", "1.75rem", "2rem"],
                box_shadow="0 6px 18px rgba(0,0,0,.12)",
                backdrop_filter="saturate(1.05) blur(1px)",
                margin_left="auto",
                margin_right=["0", "1rem", "0"],
            ),
            grid_row="2",
            width="100%",
            padding_x=["1rem", "0"],
            padding_bottom=["1rem", "1.25rem", "1.5rem", "1.75rem", "2rem"],
        ),

        # GRID + sizing
        position="relative",
        display="grid",
        grid_template_rows="1fr auto",
        width="100%",
        height=["70dvh", "78dvh", "86dvh", "92dvh"],
        max_height=["640px", "720px", "840px", "920px"],
        min_height="520px",
        max_width="100vw",
        overflow="hidden",
    )
