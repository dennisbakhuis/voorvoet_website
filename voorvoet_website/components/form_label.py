"""Form label component with optional required indicator and tooltip."""
import reflex as rx
from ..theme import Colors, FontSizes
from .fa_icon import fa_icon


def form_label(
    text: str,
    required: bool = False,
    tooltip_text: str | None = None,
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
    """
    label_elements = [
        rx.text(
            text,
            font_size=FontSizes.regular,
            color=Colors.text["heading"],
            font_weight="500",
            display="inline",
        )
    ]

    if required:
        label_elements.append(
            rx.text(
                " *",
                color="red",
                font_size=FontSizes.regular,
                display="inline",
            )
        )

    label_text = rx.flex(
        *label_elements,
        gap="0",
        align_items="center",
    )

    if tooltip_text:
        tooltip_icon = rx.tooltip(
            fa_icon("fa-info-circle", color=Colors.text["link"]),
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

        return rx.box(
            label_text,
            tooltip_icon,
            display="flex",
            align_items="center",
            gap="0.5rem",
            margin_bottom="0.5rem",
        )
    else:
        return rx.box(
            label_text,
            display="flex",
            align_items="center",
            gap="0.5rem",
            margin_bottom="0.5rem",
        )
