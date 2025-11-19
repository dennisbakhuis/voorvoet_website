"""Risk level card component for displaying zorgprofiel information."""
import reflex as rx
from ..theme import Colors, FontSizes


def risk_level_card(
    level: int,
    risk_label: str,
    title: str,
    description: str,
) -> rx.Component:
    """
    Create a risk level card with colored visual indicator and description.

    Creates a responsive card displaying a risk level with a colored square
    containing the level number and risk label, alongside title and description
    text. The layout stacks vertically on mobile and horizontally on desktop.

    Parameters
    ----------
    level : int
        The zorgprofiel (care profile) number from 0 to 4.
        Determines the color gradient: 0=green, 1=yellow, 2=orange, 3=red, 4=dark red.
    risk_label : str
        The risk level label text (e.g., "Geen risico", "Laag risico").
        Displayed below the level number in the colored square.
    title : str
        The title text for the card (e.g., "Zorgprofiel 0").
    description : str
        The full description text explaining this risk level.

    Returns
    -------
    rx.Component
        A Reflex box component containing the risk level card layout.

    Notes
    -----
    The colored square uses SVG with linear gradient backgrounds.
    Color scheme: 0=green, 1=yellow, 2=orange, 3=red, 4=dark red.
    """
    RISK_COLORS = {
        0: {"start": "#4ade80", "end": "#22c55e"},
        1: {"start": "#fbbf24", "end": "#f59e0b"},
        2: {"start": "#fb923c", "end": "#f97316"},
        3: {"start": "#f87171", "end": "#ef4444"},
        4: {"start": "#dc2626", "end": "#b91c1c"},
    }

    colors = RISK_COLORS.get(level, RISK_COLORS[0])
    gradient_id = f"grad{level}"

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
        rx.box(
            rx.box(
                rx.html(svg_content),
                width="11.25rem",
                height="11.25rem",
                flex_shrink="0",
            ),
            display="flex",
            justify_content=["center", "center", "flex-start", "flex-start"],
            width=["100%", "100%", "11.25rem", "11.25rem"],
            margin_bottom=["1rem", "1rem", "0", "0"],
        ),
        rx.box(
            rx.text(
                title,
                font_size=FontSizes.regular,
                font_weight="700",
                color=Colors.text["heading"],
                margin_bottom="0.5rem",
                text_align=["center", "center", "left", "left"],
            ),
            rx.text(
                description,
                font_size=FontSizes.regular,
                line_height="1.6",
                color=Colors.text["content"],
                text_align=["center", "center", "left", "left"],
            ),
            flex="1",
            display="flex",
            flex_direction="column",
            justify_content="center",
            padding_left=["0", "0", "0", "1rem"],
            padding_right=["0", "0", "0", "1rem"],
            width=["100%", "100%", "auto", "auto"],
        ),
        display="flex",
        flex_direction=["column", "column", "row", "row"],
        align_items="center",
        gap=["0", "0", "1.5rem", "1.5rem"],
        margin_bottom="2rem",
        width="100%",
        padding_left=["0", "0", "1rem", "2rem"],
        padding_right=["0", "0", "1rem", "2rem"],
    )
