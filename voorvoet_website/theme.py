"""Theme settings for this project."""
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
        "placeholder": "#888888",    # Lighter text for placeholders (not working, set through styles.css)
        "secondary": "#4a4a4a",      # Secondary text for body content
        "link": "#3b82f6",           # Blue color for links
    }

    borders = {
        "light": "#f3f4f6",          # Light borders for cards
    }

class FontSizes:
    # Base font size is 16px (browser default), so 1rem = 16px
    section_title = ["1.5rem", "1.75rem", "2rem", "2.25rem"]  # 24px, 28px, 32px, 36px
    section_sub_title = ["1.25rem", "1.5rem", "1.75rem", "1.875rem"]  # 20px, 24px, 28px, 30px
    regular = "1.125rem"  # 18px
    button = "1.5rem"  # 24px
    nav_link = "1.5rem"  # 24px
    card_title = "1.25rem"  # 20px
    body_accent = "1.25rem"  # 20px
    small = ["1rem", "1.125rem", "1.375rem", "1.5rem"]  # 16px, 18px, 22px, 24px - icon_list_item text used in CTA

    # Blog-specific font sizes (responsive, matching section_title pattern for h1)
    blog_heading_h1 = ["1.375rem", "1.5rem", "1.75rem", "1.875rem"]  # Same as section_title
    blog_heading_h2 = ["1.25rem", "1.375rem", "1.5rem", "1.625rem"]  # Slightly smaller than h1
    blog_heading_h3 = ["1.25rem", "1.375rem", "1.5rem", "1.625rem"]  # Slightly smaller than h2
    blog_heading_h4 = ["1.25rem", "1.375rem", "1.5rem", "1.625rem"]  # Dummy value as I do not use h4..h6
    blog_heading_h5 = ["1.25rem", "1.375rem", "1.5rem", "1.625rem"]  # Dummy value as I do not use h4..h6
    blog_heading_h6 = ["1.25rem", "1.375rem", "1.5rem", "1.625rem"]  # Dummy value as I do not use h4..h6


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

    # Blog-specific spacing
    blog_heading_margin_top = "2rem"
    blog_heading_margin_bottom = "1rem"
    blog_content_margin_bottom = "1rem"
    blog_image_margin = "2rem auto"
    blog_button_margin = "2rem 0"
    blog_caption_margin_top = "0.5rem"


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

    # Blog-specific layout
    blog_image_max_width = "800px"
    blog_image_border_radius = "8px"
    blog_button_border_radius = "3px"
    blog_button_padding_x = "0.8em"
    blog_button_padding_y = "0.1em"


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
