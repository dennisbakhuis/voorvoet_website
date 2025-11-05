"""Form label component with optional required indicator and tooltip."""
import reflex as rx
from ..theme import Colors, FontSizes


def form_label(
    text: str,
    required: bool = False,
    tooltip_text: str | None = None,
) -> rx.Component:
    """
    Create a form label with optional required indicator and info tooltip.

    Parameters
    ----------
    text : str
        The label text to display.
    required : bool, optional
        Whether to show a red asterisk indicating a required field.
        Default is False.
    tooltip_text : str | None, optional
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
    label_content = [
        rx.text(
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
    ]

    if tooltip_text:
        label_content.append(
            rx.tooltip(
                rx.html('<i class="fa fa-info-circle" style="color: #3b82f6;"/>'),
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
        )

    return rx.box(
        *label_content,
        display="flex",
        align_items="center",
        gap="0.5rem",
        margin_bottom="0.5rem",
    )
