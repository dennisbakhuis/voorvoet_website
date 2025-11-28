"""FontAwesome icon component for consistent icon rendering."""
import reflex as rx
from ..theme import Colors


def fa_icon(
    icon: str,
    color: str = Colors.text["content"],
    size: str = "1rem",
    **props
) -> rx.Component:
    """
    Create a FontAwesome icon element.

    Creates an SSR-safe FontAwesome icon using rx.el.i() instead of
    raw HTML to avoid minify errors during server-side rendering.

    Parameters
    ----------
    icon : str
        FontAwesome icon class name (e.g., "fa-check", "fa-star").
        The "fa" prefix will be added automatically.
    color : str, optional
        Icon color. Defaults to Colors.text["content"].
    size : str, optional
        Icon font size as CSS value (e.g., "1rem", "24px", "4.5rem").
        Defaults to "1rem".
    **props : dict
        Additional style properties to apply to the icon element.
        These will override the default styles.

    Returns
    -------
    rx.Component
        A Reflex i element component for FontAwesome icons.

    Examples
    --------
    >>> fa_icon("fa-check", color=Colors.primary, size="2rem")
    >>> fa_icon("fa-heart", size="24px", margin_top="10px")
    """
    return rx.el.i(
        class_name=f"fa {icon}",
        color=color,
        font_size=size,
        **props
    )
