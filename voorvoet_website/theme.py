import reflex as rx

COLORS = {
    "voorvoet": {
        "50":  "#ecfdf5",
        "100": "#d1fae5",
        "300": "#6ee7b7",
        "500": "#10b981",
        "700": "#047857",
    }
}

PRIMARY     = "#0f766e"
ACCENT      = "#111827"
LIGHT       = "#ffffff"
MUTED       = "#efefef"
DARK        = "#111827"


theme = rx.theme(
    appearance="light",
    colors=COLORS,
    has_background=True,
)
