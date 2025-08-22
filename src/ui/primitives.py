# Primitives for the Reflex UI components
import reflex as rx

def container(*children, **props):
    return rx.box(*children, class_name="container", **props)

def nav_link(href: str, label: str):
    return rx.link(label, href=href, class_name="nav-link")

def section(title: str, body):
    return rx.box(
        container(
            rx.vstack(
                rx.text(title, class_name="section-title"),
                body if isinstance(body, rx.Component) else rx.box(body),
                spacing="4",
            )
        ),
        class_name="section",
    )