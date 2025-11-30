"""Main website state management for global UI components and navigation."""

import reflex as rx


class WebsiteState(rx.State):
    """Global state for navigation, toast notifications, and language switching."""

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
        """Display a toast notification (type: 'success' or 'error')."""
        self.toast_message = message
        self.toast_type = toast_type
        self.toast_visible = True

    def hide_toast(self):
        """Hide the toast notification."""
        self.toast_visible = False

    def toggle_language_selector(self):
        """Toggle the language selector popup (header version)."""
        self.language_selector_open = not self.language_selector_open
        if self.language_selector_open:
            self.nav_open = False

    def toggle_language_selector_mobile(self):
        """Toggle the language selector popup (mobile menu version)."""
        self.language_selector_mobile_open = not self.language_selector_mobile_open
