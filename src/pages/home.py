# Home page for the Reflex web app
import reflex as rx
from ui.layout import navbar, footer
from components.hero import hero
from components.features import features

def index() -> rx.Component:
    return rx.fragment(navbar(), hero(), features(), footer())