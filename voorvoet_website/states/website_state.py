"""Main website state management for global UI components and navigation.

This module contains the WebsiteState class which manages the core application
state including navigation, modal dialogs, and toast notifications.
"""
import reflex as rx


class WebsiteState(rx.State):
    """
    Global state manager for the website application.

    Manages the state for global UI components including the navigation menu,
    modal dialogs, toast notifications, and page routing. This is the base
    state class that other state classes can inherit from or reference.

    Attributes
    ----------
    nav_open : bool
        Whether the mobile navigation menu is currently open
    modal_open : bool
        Whether the modal dialog is currently visible
    modal_title : str
        Title text displayed in the modal dialog
    modal_desc : str
        Description text displayed in the modal dialog
    modal_input : str
        User input value from the modal dialog
    current_page_path : str
        Current page path for navigation tracking
    toast_visible : bool
        Whether the toast notification is currently visible
    toast_message : str
        Message text displayed in the toast notification
    toast_type : str
        Type of toast notification, either "success" or "error"
    """

    nav_open: bool = False

    modal_open: bool = False
    modal_title: str = ""
    modal_desc: str = ""
    modal_input: str = ""

    current_page_path: str = "/"

    toast_visible: bool = False
    toast_message: str = ""
    toast_type: str = "success"

    def set_page_path(self, path: str):
        """
        Update the current page path.

        Parameters
        ----------
        path : str
            The new page path to set
        """
        self.current_page_path = path

    def nav_to_home(self):
        """
        Navigate to the home page.

        Returns
        -------
        rx.event
            Redirect event to the home page
        """
        self.current_page_path = "/"
        return rx.redirect("/")

    def nav_to_blog(self):
        """
        Navigate to the blog page.

        Returns
        -------
        rx.event
            Redirect event to the blog page
        """
        self.current_page_path = "/blog/"
        return rx.redirect("/blog/")

    def nav_to_informatie(self):
        """
        Navigate to the information page.

        Returns
        -------
        rx.event
            Redirect event to the information page
        """
        self.current_page_path = "/informatie/"
        return rx.redirect("/informatie/")

    def nav_to_reimbursements(self):
        """
        Navigate to the reimbursements page.

        Returns
        -------
        rx.event
            Redirect event to the reimbursements page
        """
        self.current_page_path = "/reimbursements/"
        return rx.redirect("/reimbursements/")

    def nav_to_contact(self):
        """
        Navigate to the contact page.

        Returns
        -------
        rx.event
            Redirect event to the contact page
        """
        self.current_page_path = "/contact/"
        return rx.redirect("/contact/")

    def toggle_nav(self):
        """Toggle the mobile navigation menu open/closed state."""
        self.nav_open = not self.nav_open

    def open_modal(self, title: str, desc: str):
        """
        Open the modal dialog with specified content.

        Parameters
        ----------
        title : str
            Title to display in the modal header
        desc : str
            Description text to display in the modal body
        """
        self.modal_title = title
        self.modal_desc = desc
        self.modal_open = True

    def close_modal(self):
        """Close the modal dialog and clear its input value."""
        self.modal_open = False
        self.modal_input = ""

    def set_modal_input(self, value: str):
        """
        Update the modal input field value.

        Parameters
        ----------
        value : str
            The new input value
        """
        self.modal_input = value

    def on_modal_change(self, is_open: bool):
        """
        Handle modal open/close state changes.

        Called when the modal's visibility changes, typically from user
        interaction with the modal's close button or overlay.

        Parameters
        ----------
        is_open : bool
            Whether the modal should be open
        """
        if not is_open:
            self.close_modal()
        else:
            self.modal_open = True

    def show_toast(self, message: str, toast_type: str = "success"):
        """
        Display a toast notification.

        Toast notifications appear temporarily to provide feedback to users
        about actions or events. They automatically hide after a timeout.

        Parameters
        ----------
        message : str
            The message text to display in the toast
        toast_type : str, optional
            Type of notification, either "success" or "error" (default: "success")
        """
        self.toast_message = message
        self.toast_type = toast_type
        self.toast_visible = True

    def hide_toast(self):
        """Hide the currently visible toast notification."""
        self.toast_visible = False
