"""Form label component with optional required indicator and tooltip."""
import reflex as rx
from ..theme import Colors, FontSizes


def form_label(
    text: str | rx.Var,
    required: bool = False,
    tooltip_text: str | rx.Var | None = None,
) -> rx.Component:
    """
    Create a form label with optional required indicator and info tooltip.

    Parameters
    ----------
    text : str | rx.Var
        The label text to display.
    required : bool, optional
        Whether to show a red asterisk indicating a required field.
        Default is False.
    tooltip_text : str | rx.Var | None, optional
        Optional tooltip text to show in an info icon next to the label.
        If None, no tooltip is displayed. Default is None.

    Returns
    -------
    rx.Component
        A box component containing the label text with optional asterisk
        and tooltip icon.

    Examples
    --------
    Simple required label:
        >>> form_label("Email", required=True)

    Label with tooltip:
        >>> form_label("Phone", required=True, tooltip_text="10 digits required")
    """
    label_text = rx.text(
        text + " ",
        rx.cond(
            required,
            rx.text("*", color="red", display="inline"),
            rx.fragment(),
        ),
        font_size=FontSizes.regular,
        color=Colors.text["heading"],
        font_weight="500",
        display="inline",
    )

    tooltip_icon = rx.tooltip(
        rx.html(f'<i class="fa fa-info-circle" style="color: {Colors.text["link"]};"/>'),
        content=tooltip_text,
        style={
            "backgroundColor": "white",
            "color": Colors.text["content"],
            "border": f"1px solid {Colors.primary['500']}",
            "padding": "0.5rem 0.75rem",
            "borderRadius": "4px",
            "boxShadow": "0 2px 8px rgba(0, 0, 0, 0.1)",
        },
    )

    # Check if tooltip_text is provided - handle both static and Var values
    if isinstance(tooltip_text, str) and tooltip_text:
        # Static string provided
        return rx.box(
            label_text,
            tooltip_icon,
            display="flex",
            align_items="center",
            gap="0.5rem",
            margin_bottom="0.5rem",
        )
    elif tooltip_text is not None and not isinstance(tooltip_text, str):
        # Var provided - always show tooltip (Reflex will handle reactivity)
        return rx.box(
            label_text,
            tooltip_icon,
            display="flex",
            align_items="center",
            gap="0.5rem",
            margin_bottom="0.5rem",
        )
    else:
        # No tooltip
        return rx.box(
            label_text,
            display="flex",
            align_items="center",
            gap="0.5rem",
            margin_bottom="0.5rem",
        )
