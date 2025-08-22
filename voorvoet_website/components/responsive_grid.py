# Responsive Grid component
import reflex as rx


def responsive_grid(*children, columns=[1, 1, 2], spacing="8", **styles) -> rx.Component:
    labels = ["initial", "sm", "md", "lg", "xl", "2xl"]
    bp = {labels[i]: str(c) for i, c in enumerate(columns) if i < len(labels)}
    cols = rx.breakpoints(**bp)  # type: ignore
    props = dict(columns=cols, gap=spacing)
    props.update(styles)
    return rx.grid(*children, **props)  # type: ignore
