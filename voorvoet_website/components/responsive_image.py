"""Responsive image component with AVIF, WebP, and fallback format support."""

import reflex as rx


def responsive_image(
    src_fallback: str | list[str] | None = None,
    alt: str | None = None,
    src_avif: str = "",
    src_webp: str = "",
    width: str | None = None,
    height: str | None = None,
    class_name: str | None = None,
    loading: str = "lazy",
    src: str | list[str] | None = None,  # Legacy parameter for backward compatibility
    **props,
) -> rx.Component:
    """
    Create a responsive image with modern format support.

    Parameters
    ----------
    src_fallback : str | list[str], optional
        Fallback image path (JPG or PNG) or list of paths (for backward compatibility)
    alt : str
        Alt text for accessibility
    src_avif : str, optional
        AVIF format image path (empty string if not available)
    src_webp : str, optional
        WebP format image path (empty string if not available)
    width : str, optional
        CSS width value
    height : str, optional
        CSS height value
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

    if width:
        img_props["width"] = width
    if height:
        img_props["height"] = height
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
