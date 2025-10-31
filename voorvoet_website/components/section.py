import reflex as rx
from typing import Optional, Literal
from ..theme import Colors, Spacing

SVG_DIVIDERS = {
    "gentle_1": {
        "top": {"viewBox": "0 0 1200 120", "path": "M0,0V15C400,15,600,135,1200,85V0Z"},
        "bottom": {"viewBox": "0 0 1200 120", "path": "M0,0V15C400,15,600,135,1200,85V0Z"}
    },
    "gentle_2": {
        "top": {"viewBox": "0 0 1200 120", "path": "M0,0V85C400,135,600,15,1200,15V0Z"},
        "bottom": {"viewBox": "0 0 1200 120", "path": "M0,0V85C400,135,600,15,1200,15V0Z"}
    },
    "gentle_3": {
        "top": {"viewBox": "0 0 1200 120", "path": "M0,0V75C400,45,600,105,1200,15V0Z"},
        "bottom": {"viewBox": "0 0 1200 120", "path": "M0,0V75C400,45,600,105,1200,15V0Z"}
    },
    "gentle_4": {
        "top": {"viewBox": "0 0 1200 120", "path": "M0,0V45C400,75,600,15,1200,105V0Z"},
        "bottom": {"viewBox": "0 0 1200 120", "path": "M0,0V45C400,75,600,15,1200,105V0Z"}
    }
}

def _create_divider(divider_data: dict, divider_color: str, position: str) -> rx.Component:
    return rx.box(
        rx.html(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{divider_data["viewBox"]}" preserveAspectRatio="none"><path d="{divider_data["path"]}" class="shape-fill"></path></svg>'),
        position="absolute",
        **{position: "-1px", "left": "0", "width": "100%", "overflow": "hidden", "line_height": "0"},  # type: ignore
        **({"transform": "rotate(180deg)"} if position == "bottom" else {}),
        **{
            "& svg": {"position": "relative", "display": "block", "width": "calc(100% + 3px)", "height": "75px"},
            "& .shape-fill": {"fill": divider_color}
        }
    )

def section(
    *children,
    background_color: str = Colors.backgrounds["white"],
    divider_color: str = Colors.backgrounds["green_light"],
    clip_top: Optional[Literal["wave", "curve", "gentle_1", "gentle_2", "gentle_3", "gentle_4"]] = None,
    clip_bottom: Optional[Literal["wave", "curve", "gentle_1", "gentle_2", "gentle_3", "gentle_4"]] = None,
    **styles
) -> rx.Component:
    CLIP_PADDING_COMPENSATION = "3rem"
    
    # Calculate default padding, but allow override from styles
    default_padding_top = f"calc({Spacing.section_vertical} + {CLIP_PADDING_COMPENSATION})" if clip_top else Spacing.section_vertical
    default_padding_bottom = f"calc({Spacing.section_vertical} + {CLIP_PADDING_COMPENSATION})" if clip_bottom else Spacing.section_vertical
    
    # Use provided padding if specified, otherwise use calculated defaults
    padding_top = styles.pop("padding_top", default_padding_top)
    padding_bottom = styles.pop("padding_bottom", default_padding_bottom)
    
    defaults = {"width": "100%", "padding_top": padding_top, "padding_bottom": padding_bottom, "bg": background_color, "position": "relative"}
    defaults.update(styles)
    
    dividers = []
    if clip_top and clip_top in SVG_DIVIDERS:
        dividers.append(_create_divider(SVG_DIVIDERS[clip_top]["top"], divider_color, "top"))
    
    if clip_bottom and clip_bottom in SVG_DIVIDERS:
        data_key = "top" if clip_top == clip_bottom else "bottom"
        dividers.append(_create_divider(SVG_DIVIDERS[clip_bottom][data_key], divider_color, "bottom"))
    
    return rx.box(*children, *dividers, **defaults)  # type: ignore
