# Risk level card component for displaying zorgprofiel information
import reflex as rx
from ..theme import Colors, FontSizes


def risk_level_card(
    level: int,
    risk_label: str,
    title: str,
    description: str,
) -> rx.Component:
    """
    Creates a risk level card with colored visual indicator and text description.

    Args:
        level: The zorgprofiel number (0-4)
        risk_label: The risk level label (e.g., "Geen risico", "Laag risico")
        title: The title text (e.g., "Zorgprofiel 0")
        description: The full description text
    """

    # Define color gradients for each risk level
    RISK_COLORS = {
        0: {"start": "#4ade80", "end": "#22c55e"},  # Green
        1: {"start": "#fbbf24", "end": "#f59e0b"},  # Yellow
        2: {"start": "#fb923c", "end": "#f97316"},  # Orange
        3: {"start": "#f87171", "end": "#ef4444"},  # Red
        4: {"start": "#dc2626", "end": "#b91c1c"},  # Dark Red
    }

    colors = RISK_COLORS.get(level, RISK_COLORS[0])
    gradient_id = f"grad{level}"

    # Create SVG with gradient and text
    svg_content = f"""
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" width="100%" height="100%" style="display: block;">
      <defs>
        <linearGradient id="{gradient_id}" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" style="stop-color:{colors['start']};stop-opacity:1" />
          <stop offset="100%" style="stop-color:{colors['end']};stop-opacity:1" />
        </linearGradient>
      </defs>
      <rect x="0" y="0" width="200" height="200" fill="url(#{gradient_id})" rx="8" />
      <text x="100" y="110" font-family="Arial, sans-serif" font-size="60" font-weight="bold" fill="white" text-anchor="middle">{level}</text>
      <text x="100" y="140" font-family="Arial, sans-serif" font-size="18" fill="white" text-anchor="middle">{risk_label}</text>
    </svg>
    """

    return rx.box(
        # Colored square with number and risk label (centered on mobile, left on desktop)
        rx.box(
            rx.box(
                rx.html(svg_content),
                width=["180px", "180px", "180px", "180px", "180px"],
                height=["180px", "180px", "180px", "180px", "180px"],
                flex_shrink="0",
            ),
            display="flex",
            justify_content=["center", "center", "flex-start", "flex-start", "flex-start"],
            width=["100%", "100%", "180px", "180px", "180px"],
            margin_bottom=["1rem", "1rem", "0", "0", "0"],
        ),
        # Text content (centered on mobile, left-aligned on desktop)
        rx.box(
            rx.text(
                title,
                font_size=FontSizes.regular,
                font_weight="700",
                color=Colors.text["heading"],
                margin_bottom="0.5rem",
                text_align=["center", "center", "left", "left", "left"],
            ),
            rx.text(
                description,
                font_size=FontSizes.regular,
                line_height="1.6",
                color=Colors.text["content"],
                text_align=["center", "center", "left", "left", "left"],
            ),
            flex="1",
            display="flex",
            flex_direction="column",
            justify_content="center",
            padding_left=["0", "0", "0", "1rem", "1rem"],
            padding_right=["0", "0", "0", "1rem", "1rem"],
            width=["100%", "100%", "auto", "auto", "auto"],
        ),
        # Container styling
        display="flex",
        flex_direction=["column", "column", "row", "row", "row"],
        align_items=["center", "center", "center", "center", "center"],
        gap=["0", "0", "1.5rem", "1.5rem", "1.5rem"],
        margin_bottom="2rem",
        width="100%",
        padding_left=["0", "0", "1rem", "2rem", "3rem"],
        padding_right=["0", "0", "1rem", "2rem", "3rem"],
    )
