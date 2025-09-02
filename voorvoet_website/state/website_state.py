# Main state file of the Reflex web app
import reflex as rx


class WebsiteState(rx.State):
    nav_open: bool = False

    modal_open: bool = False
    modal_title: str = ""
    modal_desc: str = ""
    modal_input: str = ""
    
    current_page_path: str = "/"
    
    def set_page_path(self, path: str):
        self.current_page_path = path
    
    def nav_to_home(self):
        self.current_page_path = "/"
        return rx.redirect("/")
        
    def nav_to_blog(self):
        self.current_page_path = "/blog/"
        return rx.redirect("/blog/")
        
    def nav_to_informatie(self):
        self.current_page_path = "/informatie/"
        return rx.redirect("/informatie/")
        
    def nav_to_vergoeding(self):
        self.current_page_path = "/vergoeding/"
        return rx.redirect("/vergoeding/")
        
    def nav_to_contact(self):
        self.current_page_path = "/contact/"
        return rx.redirect("/contact/")


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
