# Hero component for the Reflex web app
import reflex as rx

BRAND_GREEN = "#48A5A0"
MINT_BG = "#CFE5E8"

def hero():
    return rx.box(
        # full-bleed bg
        rx.image(
            src="/assets/image/podotherapeut_enschede_voeten_in_bed_podotherapie_helpt.jpeg",
            alt="Podotherapeut Enschede – VoorVoet",
            class_name="absolute inset-0 w-full h-full object-cover -z-10",
        ),
        rx.box(class_name="absolute inset-0 bg-gradient-to-b from-black/40 via-black/25 to-black/10 -z-10"),

        # centered text (only this part is constrained)
        rx.box(
            rx.vstack(
                rx.heading("Voetklachten?", class_name="text-center font-extrabold leading-tight text-[clamp(2.5rem,6vw,5rem)]", style={"color": BRAND_GREEN}),
                rx.text("Loop er niet te lang mee door!", class_name="text-center text-slate-900 font-semibold text-[clamp(1.125rem,2.5vw,1.875rem)] mt-2"),
                spacing="3",
                class_name="py-24 md:py-40",
            ),
            class_name="container-center relative z-10",
        ),

        # CTA card
        rx.box(
            rx.vstack(
                rx.text("Direct digitaal een afspraak maken!", class_name="text-slate-900 font-semibold"),
                rx.vstack(
                    rx.hstack(rx.html(f"<i class='fa fa-check-square-o text-[{BRAND_GREEN}] text-lg'></i>"), rx.text("Geen verwijzing nodig!", class_name="text-slate-800")),
                    rx.hstack(rx.html(f"<i class='fa fa-check-square-o text-[{BRAND_GREEN}] text-lg'></i>"), rx.text("Snel geholpen door een professional.", class_name="text-slate-800")),
                    rx.hstack(rx.html(f"<i class='fa fa-check-square-o text-[{BRAND_GREEN}] text-lg'></i>"), rx.text("Snelste weg naar de specialist!", class_name="text-slate-800")),
                    class_name="space-y-2 mt-2",
                ),
                rx.link("Maak een afspraak", href="/contact",
                        class_name="w-full mt-4 inline-flex items-center justify-center rounded-lg px-5 py-3 text-white font-semibold shadow-md",
                        style={"backgroundColor": BRAND_GREEN}),
                spacing="2",
            ),
            class_name="absolute right-4 md:right-12 -bottom-10 w-[90%] md:w-[420px] rounded-xl shadow-xl p-5 border border-black/5 z-20",
            style={"backgroundColor": MINT_BG},
        ),

        class_name="relative min-h-[60vh] -mt-20 w-full",  # full width hero
    )