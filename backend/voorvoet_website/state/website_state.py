# Main state file of the Reflex web app
import reflex as rx


class WebsiteState(rx.State):
    nav_open: bool = False

    modal_open: bool = False
    modal_title: str = ""
    modal_desc: str = ""
    modal_input: str = ""

    def toggle_nav(self):
        self.nav_open = not self.nav_open

    def open_modal(self, title: str, desc: str):
        self.modal_title = title
        self.modal_desc = desc
        self.modal_open = True

    def close_modal(self):
        self.modal_open = False
        self.modal_input = ""

    def set_modal_input(self, value: str):
        self.modal_input = value

    def on_modal_change(self, is_open: bool):
        if not is_open:
            self.close_modal()
        else:
            self.modal_open = True
