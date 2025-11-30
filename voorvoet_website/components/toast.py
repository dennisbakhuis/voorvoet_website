"""Toast notification component."""

import reflex as rx
from ..theme import Colors, FontSizes
from ..states import WebsiteState


def toast() -> rx.Component:
    """
    Create a toast notification component that slides in from the top.

    Creates a fixed-position notification that appears at the top center
    of the screen. Shows success or error messages with appropriate colors
    and icons based on the WebsiteState. Automatically animates in and
    can be programmatically dismissed.

    Returns
    -------
    rx.Component
        A Reflex box component containing the toast notification.
    """
    return rx.box(
        rx.box(
            rx.box(
                rx.cond(
                    WebsiteState.toast_type == "success",
                    rx.text("✓"),
                    rx.text("✕"),
                ),
                display="flex",
                align_items="center",
                justify_content="center",
                font_size=FontSizes.button,
                font_weight="700",
                color="white",
                width="2rem",
                height="2rem",
                flex_shrink="0",
            ),
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
                Colors.semantic["success"],
                Colors.semantic["error"],
            ),
            border_radius="8px",
            box_shadow="0 10px 25px rgba(0, 0, 0, 0.15)",
            min_width="320px",
            max_width="500px",
            animation="slideDown 0.3s ease-out",
        ),
        position="fixed",
        top="2rem",
        left="50%",
        transform="translateX(-50%)",
        z_index="9999",
        display=rx.cond(WebsiteState.toast_visible, "block", "none"),
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
