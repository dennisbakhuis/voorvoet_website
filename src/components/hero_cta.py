import reflex as rx

BRAND_GREEN = "#48A5A0"   # extracted from screenshot
MINT_BG      = "#CFE5E8"  # light mint from screenshot

def hero_cta():
    return rx.box(
        rx.vstack(
            rx.text("Direct digitaal een afspraak maken!", class_name="text-slate-900 font-semibold"),
            
            # checklist
            rx.vstack(
                rx.hstack(
                    rx.html(f"<i class='fa fa-check-square-o text-[{BRAND_GREEN}] text-lg'></i>"),
                    rx.text("Geen verwijzing nodig!", class_name="text-slate-800"),
                ),
                rx.hstack(
                    rx.html(f"<i class='fa fa-check-square-o text-[{BRAND_GREEN}] text-lg'></i>"),
                    rx.text("Snel geholpen door een professional.", class_name="text-slate-800"),
                ),
                rx.hstack(
                    rx.html(f"<i class='fa fa-check-square-o text-[{BRAND_GREEN}] text-lg'></i>"),
                    rx.text("Snelste weg naar de specialist!", class_name="text-slate-800"),
                ),
                class_name="space-y-2 mt-2",
            ),
            
            # button
            rx.link(
                "Maak een afspraak",
                href="/contact",
                class_name="w-full mt-4 inline-flex items-center justify-center rounded-lg px-5 py-3 text-white font-semibold shadow-md",
                style={"backgroundColor": BRAND_GREEN},
            ),
            spacing="2",
        ),
        class_name="absolute right-4 md:right-12 -bottom-10 w-[90%] md:w-[420px] rounded-xl shadow-xl p-5 border border-black/5 z-20",
        style={"backgroundColor": MINT_BG},
    )