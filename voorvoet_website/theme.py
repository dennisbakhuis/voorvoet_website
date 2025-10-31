# Theme settings for this project
class Colors:
    primary = {
        "50":  "#ffffff",  # Brand white
        "100": "#d1fae5",  # Brand lighter green
        "300": "#05a8a2",  # Brand light green
        "500": "#05847c",  # Brand medium green
        "700": "#005152",  # Brand dark green
    }

    backgrounds = {
        "white": "#ffffff",        # First (odd) sections are white background
        "green_light": "#dcedec",  # Alternating (even) sections are ligh green
    }

    text = {
        "heading": "#111827",        # Pure black for main headings
        "subheading": "#1f2937",     # Slightly less black for subheadings (gray-800)
        "content": "#131f1e",        # Content with a tiny blend of primary.300 teal
        "white": "#ffffff",          # White text for buttons
        "muted": "#666666",          # Muted/gray text for labels
        "placeholder": "#888888",    # Lighter text for placeholders
        "secondary": "#4a4a4a",      # Secondary text for body content
        "link": "#3b82f6",           # Blue color for links
    }

    borders = {
        "light": "#f3f4f6",          # Light borders for cards
    }

class FontSizes:
    section_title = ["24px", "28px", "32px", "36px"]
    section_sub_title = ["20px", "24px", "28px", "30px"]
    regular = "18px"
    button = "24px"
    nav_link = "24px"
    card_title = "20px"
    body_accent = "20px"
    small = ["16px", "18px", "22px", "24px"]  # icon_list_item text used in CTA


class Spacing:
    # Container and section spacing
    container_padding = ["1rem", "1.5rem", "2rem"]
    section_vertical = "5rem"

    # Common responsive spacing patterns
    responsive_2rem = ["0", "0", "0", "2rem"]
    responsive_2rem_left = ["0", "0", "0", "2rem"]
    responsive_2rem_right = ["0", "0", "0", "2rem"]

    # Grid and layout spacing
    grid_gap = "2rem"
    section_gap = "2rem"
    card_spacing = "3rem"

    # Component spacing
    image_margin_bottom = "2rem"
    text_margin_bottom = "1rem"
    button_margin_top = "1.5rem"


class Layout:
    # Image sizing
    image_max_width = "333px"
    image_border_radius = "4px"
    image_box_shadow = "0 4px 12px rgba(0, 0, 0, 0.15)"

    # Column sizing patterns
    image_column_size = ["100%", "100%", "100%", "40%", "40%"]
    text_column_size = ["100%", "100%", "100%", "60%", "60%"]

    # Responsive display patterns
    mobile_only = ["block", "block", "none", "none", "none"]
    desktop_only = ["none", "none", "flex", "flex", "flex"]
    responsive_flex = ["block", "block", "block", "flex"]

    # Container constraints
    max_width = "1200px"
    card_max_width = "350px"
    card_min_width = "280px"


# Utility functions for common responsive patterns
def responsive_padding(direction: str = "right") -> list[str]:
    """Generate responsive padding for left or right direction"""
    if direction == "right":
        return ["0", "0", "0", "2rem"]
    elif direction == "left":
        return ["0", "0", "0", "2rem"]
    else:
        return ["0", "0", "0", "0"]


def responsive_padding_both(left: bool = False, right: bool = False) -> dict:
    """Generate responsive padding for both directions"""
    result = {}
    if left:
        result["padding_left"] = responsive_padding("left")
    if right:
        result["padding_right"] = responsive_padding("right")
    return result
