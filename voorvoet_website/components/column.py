# Column component for flexible layout
import reflex as rx


def column(*children, size=None, **props) -> rx.Component:
    flex_props = {}
    if size:
        if isinstance(size, list):
            # Responsive sizing: convert each breakpoint size to flex values
            flex_values = []
            width_values = []
            for s in size:
                if s == "100%":
                    flex_values.append("1")
                    width_values.append("100%")
                else:
                    flex_values.append(f"0 0 {s}")
                    width_values.append(s)
            flex_props["flex"] = flex_values
            flex_props["width"] = width_values
        else:
            # Single size value
            flex_props["flex"] = f"0 0 {size}"
            flex_props["width"] = size
    else:
        flex_props["width"] = "100%"
        flex_props["flex"] = "1"
    
    return rx.box(
        *children,
        **flex_props,
        **props
    )