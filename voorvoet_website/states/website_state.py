"""Main website state management for global UI components and navigation."""

import reflex as rx

from ..services import track_event
from ..config import config


class WebsiteState(rx.State):
    """Global state for navigation, toast notifications, and language switching."""

    nav_open: bool = False

    toast_visible: bool = False
    toast_message: str = ""
    toast_type: str = "success"

    current_language: str = "nl"
    language_selector_open: bool = False
    language_selector_mobile_open: bool = False

    def _get_language_from_path(self) -> str:
        """Extract language code from the current URL path."""
        path = self.router.page.path
        parts = path.strip("/").split("/")
        if parts and parts[0] in ("nl", "en", "de"):
            return parts[0]
        return "nl"

    @rx.event
    async def track_page_view(self) -> None:
        """Track a page view via server-side Umami."""
        path = self.router.page.path
        lang = self._get_language_from_path()
        self.current_language = lang
        await track_event(url=path, language=lang)

    @rx.event
    async def handle_appointment_click(self) -> None:
        """Track appointment CTA click and redirect to portal."""
        lang = self._get_language_from_path()
        await track_event(
            url=f"/{lang}/",
            event_name="appointment-click",
            language=lang,
        )
        return rx.redirect(config.link_plan_portal or "", is_external=True)  # type: ignore[return-value]

    @rx.event
    def toggle_nav(self) -> None:
        """Toggle the mobile navigation menu open/closed state."""
        self.nav_open = not self.nav_open
        if self.nav_open:
            self.language_selector_open = False
        else:
            self.language_selector_mobile_open = False

    @rx.event
    def show_toast(self, message: str, toast_type: str = "success") -> None:
        """Display a toast notification (type: 'success' or 'error')."""
        self.toast_message = message
        self.toast_type = toast_type
        self.toast_visible = True

    @rx.event
    def hide_toast(self) -> None:
        """Hide the toast notification."""
        self.toast_visible = False

    @rx.event
    def toggle_language_selector(self) -> None:
        """Toggle the language selector popup (header version)."""
        self.language_selector_open = not self.language_selector_open
        if self.language_selector_open:
            self.nav_open = False

    @rx.event
    def toggle_language_selector_mobile(self) -> None:
        """Toggle the language selector popup (mobile menu version)."""
        self.language_selector_mobile_open = not self.language_selector_mobile_open
