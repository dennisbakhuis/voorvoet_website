"""Main website state management for global UI components and navigation.

This module contains the WebsiteState class which manages the core application
state including navigation, and toast notifications.
"""
import reflex as rx
from .page_title_translations import PAGE_TITLES


class WebsiteState(rx.State):
    """
    Global state manager for the website application.

    Manages the state for global UI components including the navigation menu,
    toast notifications, and language switching. This is the base
    state class that other state classes can inherit from or reference.

    Attributes
    ----------
    nav_open : bool
        Whether the mobile navigation menu is currently open
    toast_visible : bool
        Whether the toast notification is currently visible
    toast_message : str
        Message text displayed in the toast notification
    toast_type : str
        Type of toast notification, either "success" or "error"
    current_language : str
        Current website language code (nl, de, en)
    language_selector_open : bool
        Whether the language selector popup is currently open (header version)
    language_selector_mobile_open : bool
        Whether the language selector popup is currently open (mobile/hamburger menu version)
    """

    nav_open: bool = False

    toast_visible: bool = False
    toast_message: str = ""
    toast_type: str = "success"

    current_language: str = "nl"
    language_selector_open: bool = False
    language_selector_mobile_open: bool = False

    def toggle_nav(self):
        """Toggle the mobile navigation menu open/closed state."""
        self.nav_open = not self.nav_open
        if self.nav_open:
            self.language_selector_open = False
        else:
            self.language_selector_mobile_open = False

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

    def toggle_language_selector(self):
        """Toggle the language selector popup open/closed state (header version)."""
        self.language_selector_open = not self.language_selector_open
        if self.language_selector_open:
            self.nav_open = False

    def toggle_language_selector_mobile(self):
        """Toggle the language selector popup open/closed state (mobile/hamburger menu version)."""
        self.language_selector_mobile_open = not self.language_selector_mobile_open

    def detect_language_from_route(self):
        """
        Detect and set the current language based on the URL route parameter.

        This method should be called on page load to synchronize the
        language state with the current route's [lang] parameter.
        """
        current_path = self.router.url.path

        if current_path.startswith("/"):
            path_parts = current_path[1:].split("/")
            if path_parts and len(path_parts) > 0:
                lang = path_parts[0]
                if lang in ["nl", "de", "en"]:
                    self.current_language = lang
                    return

        self.current_language = "nl"

    def set_language(self, lang: str):
        """
        Set the website language and navigate to appropriate route.

        Parameters
        ----------
        lang : str
            Language code to switch to (nl, de, en)
        """
        self.current_language = lang
        self.language_selector_open = False
        self.language_selector_mobile_open = False

        current_path = self.router.url.path

        if current_path.startswith("/nl"):
            base_path = current_path[3:] or ""
        elif current_path.startswith("/de"):
            base_path = current_path[3:] or ""
        elif current_path.startswith("/en"):
            base_path = current_path[3:] or ""
        else:
            base_path = current_path

        target_path = f"/{lang}{base_path}"

        return rx.redirect(target_path)

    @rx.var
    def page_title(self) -> str:
        """Get the page title in the current language based on current route."""
        current_path = self.router.url.path

        if "/blog/" in current_path:
            page_key = "blog"
        elif "/informatie/" in current_path:
            page_key = "information"
        elif "/vergoedingen/" in current_path:
            page_key = "reimbursements"
        elif "/contact/" in current_path:
            page_key = "contact"
        elif "/zolen-bestellen/" in current_path:
            page_key = "order_insoles"
        else:
            page_key = "home"

        return PAGE_TITLES.get(page_key, {}).get(self.current_language, PAGE_TITLES.get(page_key, {}).get("nl", "VoorVoet"))
