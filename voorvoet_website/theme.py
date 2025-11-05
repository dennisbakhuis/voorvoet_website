"""Theme settings and design system for the VoorVoet website.

This module defines the complete design system including colors, typography,
spacing, and layout constants. All visual styling should reference these
constants to maintain consistency across the application.

The theme uses a teal/green color palette aligned with the VoorVoet brand,
with responsive font sizes and spacing patterns for mobile-first design.
"""


class Colors:
    """Color palette for the VoorVoet brand and UI elements.

    Defines primary brand colors, background colors, text colors, border
    colors, and semantic colors used throughout the application. All colors
    are specified as hex values for consistency.

    Attributes
    ----------
    primary : dict
        Primary brand color shades from white (50) to dark green (700).
        Used for brand elements, buttons, and accents.
    backgrounds : dict
        Background colors for sections and containers.
        Alternates between white and light green for visual rhythm.
    text : dict
        Text colors for various content types including headings,
        body text, links, and muted text.
    borders : dict
        Border colors for cards and UI elements.
    semantic : dict
        Semantic colors for success, error, warning, and info states.
    """

    primary = {
        "50": "#ffffff",
        "100": "#d1fae5",
        "300": "#05a8a2",
        "500": "#05847c",
        "700": "#005152",
    }

    backgrounds = {
        "white": "#ffffff",
        "green_light": "#dcedec",
    }

    text = {
        "heading": "#111827",
        "subheading": "#1f2937",
        "content": "#131f1e",
        "white": "#ffffff",
        "muted": "#666666",
        "placeholder": "#888888",
        "secondary": "#4a4a4a",
        "link": "#3b82f6",
    }

    borders = {
        "light": "#f3f4f6",
    }

    semantic = {
        "error": "#ef4444",
        "success": "#05847c",
    }

class FontSizes:
    """Typography scale for responsive text sizing.

    All font sizes use rem units for accessibility. Base font size is 16px
    (browser default), so 1rem = 16px. Responsive sizes use arrays with
    values for different breakpoints: [mobile, tablet, desktop, large].

    Attributes
    ----------
    section_title : list[str]
        Main section heading sizes (24px to 36px responsive).
    section_sub_title : list[str]
        Section subheading sizes (20px to 30px responsive).
    regular : str
        Standard body text size (18px).
    button : str
        Button text size (24px).
    nav_link : str
        Navigation link text size (24px).
    card_title : str
        Card heading size (20px).
    body_accent : str
        Accented body text size (20px).
    small : list[str]
        Small text sizes for icons and CTAs (16px to 24px responsive).
    blog_heading_h1 : list[str]
        Blog post h1 heading sizes (responsive).
    blog_heading_h2 : list[str]
        Blog post h2 heading sizes (responsive).
    blog_heading_h3 : list[str]
        Blog post h3 heading sizes (responsive).
    blog_heading_h4 : list[str]
        Blog post h4 heading sizes (responsive, unused).
    blog_heading_h5 : list[str]
        Blog post h5 heading sizes (responsive, unused).
    blog_heading_h6 : list[str]
        Blog post h6 heading sizes (responsive, unused).
    """

    section_title = ["1.5rem", "1.75rem", "2rem", "2.25rem"]
    section_sub_title = ["1.25rem", "1.5rem", "1.75rem", "1.875rem"]
    regular = "1.125rem"
    button = "1.5rem"
    nav_link = "1.5rem"
    card_title = "1.25rem"
    body_accent = "1.25rem"
    small = ["1rem", "1.125rem", "1.375rem", "1.5rem"]

    blog_heading_h1 = ["1.375rem", "1.5rem", "1.75rem", "1.875rem"]
    blog_heading_h2 = ["1.25rem", "1.375rem", "1.5rem", "1.625rem"]
    blog_heading_h3 = ["1.25rem", "1.375rem", "1.5rem", "1.625rem"]
    blog_heading_h4 = ["1.25rem", "1.375rem", "1.5rem", "1.625rem"]
    blog_heading_h5 = ["1.25rem", "1.375rem", "1.5rem", "1.625rem"]
    blog_heading_h6 = ["1.25rem", "1.375rem", "1.5rem", "1.625rem"]


class Spacing:
    """Spacing constants for consistent layout and rhythm.

    Defines padding, margins, and gaps used throughout the application.
    Responsive spacing uses arrays for different breakpoints.

    Attributes
    ----------
    container_padding : list[str]
        Responsive padding for main containers.
    section_vertical : str
        Vertical spacing between major sections.
    responsive_2rem : list[str]
        Generic responsive spacing pattern (2rem on large screens).
    responsive_2rem_left : list[str]
        Responsive left spacing (2rem on large screens).
    responsive_2rem_right : list[str]
        Responsive right spacing (2rem on large screens).
    grid_gap : str
        Gap between grid items.
    section_gap : str
        Gap between section elements.
    card_spacing : str
        Spacing around cards.
    image_margin_bottom : str
        Bottom margin for images.
    text_margin_bottom : str
        Bottom margin for text blocks.
    button_margin_top : str
        Top margin for buttons.
    blog_heading_margin_top : str
        Top margin for blog headings.
    blog_heading_margin_bottom : str
        Bottom margin for blog headings.
    blog_content_margin_bottom : str
        Bottom margin for blog content blocks.
    blog_image_margin : str
        Margin around blog images.
    blog_button_margin : str
        Margin around blog buttons.
    blog_caption_margin_top : str
        Top margin for blog image captions.
    """

    container_padding = ["1rem", "1.5rem", "2rem"]
    section_vertical = "5rem"

    responsive_2rem = ["0", "0", "0", "2rem"]
    responsive_2rem_left = ["0", "0", "0", "2rem"]
    responsive_2rem_right = ["0", "0", "0", "2rem"]

    grid_gap = "2rem"
    section_gap = "2rem"
    card_spacing = "3rem"

    image_margin_bottom = "2rem"
    text_margin_bottom = "1rem"
    button_margin_top = "1.5rem"

    blog_heading_margin_top = "2rem"
    blog_heading_margin_bottom = "1rem"
    blog_content_margin_bottom = "1rem"
    blog_image_margin = "2rem auto"
    blog_button_margin = "2rem 0"
    blog_caption_margin_top = "0.5rem"


class Layout:
    """Layout constants for sizing, positioning, and responsive behavior.

    Defines constraints for images, containers, and responsive display patterns.
    Uses arrays for breakpoint-based responsive values.

    Attributes
    ----------
    image_max_width : str
        Maximum width for content images.
    image_border_radius : str
        Border radius for content images.
    image_box_shadow : str
        Box shadow for content images.
    image_column_size : list[str]
        Responsive column widths for image columns.
    text_column_size : list[str]
        Responsive column widths for text columns.
    mobile_only : list[str]
        Display values to show only on mobile.
    desktop_only : list[str]
        Display values to show only on desktop.
    responsive_flex : list[str]
        Responsive display pattern for flex containers.
    max_width : str
        Maximum width for main containers.
    card_max_width : str
        Maximum width for card components.
    card_min_width : str
        Minimum width for card components.
    blog_image_max_width : str
        Maximum width for blog post images.
    blog_image_border_radius : str
        Border radius for blog post images.
    blog_button_border_radius : str
        Border radius for blog buttons.
    blog_button_padding_x : str
        Horizontal padding for blog buttons.
    blog_button_padding_y : str
        Vertical padding for blog buttons.
    """

    image_max_width = "333px"
    image_border_radius = "4px"
    image_box_shadow = "0 4px 12px rgba(0, 0, 0, 0.15)"

    image_column_size = ["100%", "100%", "100%", "40%", "40%"]
    text_column_size = ["100%", "100%", "100%", "60%", "60%"]

    mobile_only = ["block", "block", "none", "none", "none"]
    desktop_only = ["none", "none", "flex", "flex", "flex"]
    responsive_flex = ["block", "block", "block", "flex"]

    max_width = "1200px"
    card_max_width = "350px"
    card_min_width = "280px"

    blog_image_max_width = "800px"
    blog_image_border_radius = "8px"
    blog_button_border_radius = "3px"
    blog_button_padding_x = "0.8em"
    blog_button_padding_y = "0.1em"
