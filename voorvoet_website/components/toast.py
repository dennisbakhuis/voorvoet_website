# Toast notification component
import reflex as rx
from ..theme import Colors, FontSizes
from ..state import WebsiteState


def toast() -> rx.Component:
    """Toast notification component that slides in from the top

    Shows success or error messages based on the state.
    Displays at the top center of the screen and auto-dismisses.
    """
    return rx.box(
        rx.box(
            # Icon
            rx.box(
                rx.cond(
                    WebsiteState.toast_type == "success",
                    rx.html("✓"),
                    rx.html("✕"),
                ),
                display="flex",
                align_items="center",
                justify_content="center",
                font_size="1.5rem",
                font_weight="700",
                color="white",
                width="2rem",
                height="2rem",
                flex_shrink="0",
            ),
            # Message
            rx.box(
                rx.text(
                    WebsiteState.toast_message,
                    font_size=FontSizes.regular,
                    font_weight="500",
                    color="white",
                    line_height="1.5",
                ),
                flex="1",
            ),
            display="flex",
            align_items="center",
            gap="1rem",
            padding="1rem 1.5rem",
            background=rx.cond(
                WebsiteState.toast_type == "success",
                Colors.primary["500"],  # Brand medium green
                "#ef4444",  # Red for errors
            ),
            border_radius="8px",
            box_shadow="0 10px 25px rgba(0, 0, 0, 0.15)",
            min_width="320px",
            max_width="500px",
            animation=f"slideDown 0.3s ease-out",
        ),
        position="fixed",
        top="2rem",
        left="50%",
        transform="translateX(-50%)",
        z_index="9999",
        display=rx.cond(WebsiteState.toast_visible, "block", "none"),
        # Custom CSS for animation
        style={
            "@keyframes slideDown": {
                "from": {
                    "opacity": "0",
                    "transform": "translateX(-50%) translateY(-20px)",
                },
                "to": {
                    "opacity": "1",
                    "transform": "translateX(-50%) translateY(0)",
                },
            },
        },
    )
