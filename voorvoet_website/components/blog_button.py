"""Blog button component for rendering call-to-action buttons as links."""
import reflex as rx
from ..theme import Colors, FontSizes, Spacing, Layout


def blog_button(label: str, url: str) -> rx.Component:
    """
    Create a styled call-to-action button for blog content.

    Renders a prominent button-styled link with hover effects, typically used
    for calls-to-action within blog posts like "Read More", "Contact Us",
    "Learn More", etc. The button uses the site's primary color scheme.

    Parameters
    ----------
    label : str
        The text to display on the button
    url : str
        The URL destination when the button is clicked (can be internal or external)

    Returns
    -------
    rx.Component
        A Reflex box component containing a styled link that looks like a button

    Notes
    -----
    - Uses primary color with hover effect to darker shade
    - Centered display with 2rem top and bottom margins
    - Bold font (weight 700) for emphasis
    - Drop shadow for depth, enhanced on hover
    - Smooth transition animation (0.2s) for hover effects
    - Inline-flex display for proper text centering
    - No text decoration (removes default link underline)
    - Hover effects:
        - Background color darkens to primary[500]
        - Shadow expands (0 4px 12px → 0 6px 16px)
        - Opacity increases on shadow

    Examples
    --------
    >>> blog_button("Read More", "/blog/full-article")
    >>> blog_button("Contact Us", "/contact")
    >>> blog_button("Learn More", "https://example.com/docs")
    """
    return rx.box(
        rx.link(
            rx.text(label),
            href=url,
            border_radius=Layout.blog_button_border_radius,
            font_weight="700",
            font_size=FontSizes.regular,
            padding_x=Layout.blog_button_padding_x,
            padding_y=Layout.blog_button_padding_y,
            transition="all 0.2s ease",
            cursor="pointer",
            display="inline-flex",
            align_items="center",
            justify_content="center",
            text_decoration="none",
            border="none",
            white_space="nowrap",
            bg=Colors.primary['300'],
            color=Colors.text['white'],
            box_shadow="0 4px 12px rgba(5, 168, 162, 0.3)",
            _hover={
                "bg": Colors.primary['500'],
                "box_shadow": "0 6px 16px rgba(5, 168, 162, 0.4)"
            },
        ),
        display="flex",
        justify_content="center",
        margin=Spacing.blog_button_margin,
    )
