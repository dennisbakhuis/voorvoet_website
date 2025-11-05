# Main state file of the Reflex web app
import reflex as rx


class WebsiteState(rx.State):
    nav_open: bool = False

    modal_open: bool = False
    modal_title: str = ""
    modal_desc: str = ""
    modal_input: str = ""

    current_page_path: str = "/"

    # Toast notification state
    toast_visible: bool = False
    toast_message: str = ""
    toast_type: str = "success"  # "success" or "error"
    
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
        
    def nav_to_reimbursements(self):
        self.current_page_path = "/reimbursements/"
        return rx.redirect("/reimbursements/")
        
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

    def show_toast(self, message: str, toast_type: str = "success"):
        """Show a toast notification

        Args:
            message: The message to display
            toast_type: Either "success" or "error"
        """
        self.toast_message = message
        self.toast_type = toast_type
        self.toast_visible = True

    def hide_toast(self):
        """Hide the toast notification"""
        self.toast_visible = False
