"""Responsive image component with AVIF, WebP, and fallback format support."""

import reflex as rx


def responsive_image(
    src: str | list[str],
    alt: str,
    width: str | None = None,
    height: str | None = None,
    class_name: str | None = None,
    loading: str = "lazy",
    **props,
) -> rx.Component:
    """
    Create a responsive image with modern format support.

    Parameters
    ----------
    src : str | list[str]
        Image or List of image paths. Can be:
        - Single element (SVG or any format): returns simple img
        - Multiple elements: builds picture with sources based on extensions
    alt : str
        Alt text for accessibility
    width : str, optional
        CSS width value
    height : str, optional
        CSS height value
    class_name : str, optional
        CSS class name
    loading : str, default "lazy"
        Loading strategy: "lazy" or "eager"
    **props
        Additional props passed to img element

    Returns
    -------
    rx.Component
        Simple img element for single source, picture element for multiple sources
    """
    img_props = {"alt": alt, "loading": loading, **props}

    if width:
        img_props["width"] = width
    if height:
        img_props["height"] = height
    if class_name:
        img_props["class_name"] = class_name

    if isinstance(src, str):
        src = [src]
    if len(src) <= 1:
        return rx.image(src=src[0] if src else "", **img_props)

    mime_types = {
        ".avif": "image/avif",
        ".webp": "image/webp",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
    }

    fallback_src = None
    sources = []

    for img_path in src:
        ext = img_path[img_path.rfind(".") :].lower()
        mime_type = mime_types.get(ext)

        if mime_type in ("image/jpeg", "image/png"):
            fallback_src = img_path
        elif mime_type:
            sources.append(
                rx.el.source(type=mime_type, custom_attrs={"srcset": img_path})
            )

    if not fallback_src:
        fallback_src = src[-1]

    return rx.el.picture(*sources, rx.image(src=fallback_src, **img_props))
