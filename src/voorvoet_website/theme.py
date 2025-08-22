import reflex as rx

colors = {
    "voorvoet": {
        "50":  "#ecfdf5",
        "100": "#d1fae5",
        "300": "#6ee7b7",
        "500": "#10b981",
        "700": "#047857",
    }
}

theme = rx.theme(
    appearance="light",
    colors=colors,
    has_background=True,
)
