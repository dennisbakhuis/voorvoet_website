"""Responsive image component with AVIF, WebP, and fallback format support."""

import reflex as rx
from typing import Any
from ..theme import Layout


def responsive_image(
    src_fallback: str = "",
    alt: str | None = None,
    src_avif: str = "",
    src_webp: str = "",
    dimensions: dict[str, str] | None = None,
    img_width: str | None = None,
    img_height: str | None = None,
    width: str | None = None,
    height: str | None = None,
    max_width: str | None = None,
    border_radius: str | None = None,
    box_shadow: str | None = None,
    margin_y: str | None = None,
    class_name: str | None = None,
    loading: str = "lazy",
    **props: Any,
) -> rx.Component:
    """
    Create a responsive image with modern format support and styling.

    Parameters
    ----------
    src_fallback : str
        Fallback image path (JPG or PNG) or list of paths (for backward compatibility)
    alt : str
        Alt text for accessibility
    src_avif : str, optional
        AVIF format image path (empty string if not available)
    src_webp : str, optional
        WebP format image path (empty string if not available)
    dimensions : dict[str, str], optional
        Image dimensions dict with 'width' and 'height' keys (e.g., ImageDimensions.hero_banner)
        Sets HTML attributes for aspect ratio to prevent CLS
    img_width : str, optional
        HTML width attribute (alternative to dimensions dict)
    img_height : str, optional
        HTML height attribute (alternative to dimensions dict)
    width : str, optional
        CSS width value
    height : str, optional
        CSS height value
    max_width : str, optional
        Maximum width of the image
    border_radius : str, optional
        Border radius for the image (defaults to theme value)
    box_shadow : str, optional
        Box shadow for the image (defaults to theme value)
    margin_y : str, optional
        Vertical margin for the image
    class_name : str, optional
        CSS class name
    loading : str, default "lazy"
        Loading strategy: "lazy" or "eager"
    src : str | list[str], optional
        Legacy parameter for backward compatibility
    **props
        Additional props passed to img element

    Returns
    -------
    rx.Component
        Picture element with AVIF, WebP sources and fallback img
    """
    img_props = {"alt": alt or "", "loading": loading, **props}

    if dimensions:
        if "width" in dimensions and dimensions["width"]:
            img_props["custom_attrs"] = img_props.get("custom_attrs", {})
            img_props["custom_attrs"]["width"] = dimensions["width"]
        if "height" in dimensions and dimensions["height"]:
            img_props["custom_attrs"] = img_props.get("custom_attrs", {})
            img_props["custom_attrs"]["height"] = dimensions["height"]
    elif img_width or img_height:
        img_props["custom_attrs"] = img_props.get("custom_attrs", {})
        if img_width:
            img_props["custom_attrs"]["width"] = img_width
        if img_height:
            img_props["custom_attrs"]["height"] = img_height

    if width:
        img_props["width"] = width
    if height:
        img_props["height"] = height
    if max_width:
        img_props["max_width"] = max_width
    if border_radius is not None:
        img_props["border_radius"] = border_radius
    elif "border_radius" not in props:
        img_props["border_radius"] = Layout.image_border_radius
    if box_shadow is not None:
        img_props["box_shadow"] = box_shadow
    elif "box_shadow" not in props:
        img_props["box_shadow"] = Layout.image_box_shadow
    if margin_y:
        img_props["margin_y"] = margin_y
    if class_name:
        img_props["class_name"] = class_name

    return rx.el.picture(
        rx.cond(
            src_avif != "",
            rx.el.source(type="image/avif", custom_attrs={"srcset": src_avif}),
        ),
        rx.cond(
            src_webp != "",
            rx.el.source(type="image/webp", custom_attrs={"srcset": src_webp}),
        ),
        rx.image(src=src_fallback, **img_props),
    )
