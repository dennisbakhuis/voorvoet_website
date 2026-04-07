"""Contact form state management for form submission.

This module contains the ContactState class which manages the state for the
contact form submission with email notifications and toast feedback.
Form validation is handled client-side via HTML5 validation.
"""

import logging
import reflex as rx
import asyncio
from typing import AsyncGenerator

from reflex.event import EventSpec

from ..models import ContactForm, PhoneNumber, EmailAddress
from ..services import send_contact_form_email, track_event, verify_turnstile_token
from ..config import config


logger = logging.getLogger(__name__)


TURNSTILE_RESET_SCRIPT = (
    "(function() {"
    "  var c = document.getElementById('turnstile-widget-container');"
    "  if (c && window.turnstile && c.dataset.widgetId != null) {"
    "    try { window.turnstile.reset(c); } catch (e) {}"
    "  }"
    "  var t = document.getElementById('turnstile-token');"
    "  if (t) { t.value = ''; }"
    "  var form = document.getElementById('contact-form');"
    "  if (form) { form.dispatchEvent(new Event('change', { bubbles: true })); }"
    "})();"
)


class ContactState(rx.State):
    """
    State manager for contact form functionality.

    Manages form submission with email notifications and toast feedback.
    Form validation is handled client-side via HTML5 validation attributes.
    Only the request_type (radio button) uses server state since it's a
    single-click selection with acceptable latency.

    Attributes
    ----------
    request_type : str
        The selected contact preference (phone callback or email)
    form_submitting : bool
        Loading state flag for preventing duplicate submissions
    """

    request_type: str = "Bel mij terug"
    form_submitting: bool = False

    @rx.event
    def set_request_type(self, value: str) -> None:
        """Update the request type (preferred contact method)."""
        self.request_type = value

    @rx.event
    async def handle_form_submit(
        self, form_data: dict
    ) -> AsyncGenerator[EventSpec | None, None]:
        """
        Handle form submission with all field data at once.

        Parameters
        ----------
        form_data : dict
            Dictionary containing all form field values from FormData
        """
        if self.form_submitting:
            return

        self.form_submitting = True
        yield None

        first_name = (form_data.get("first_name") or "").strip()
        last_name = (form_data.get("last_name") or "").strip()
        phone = (form_data.get("phone") or "").strip()
        email = (form_data.get("email") or "").strip()
        description = (form_data.get("description") or "").strip()
        request_type = (form_data.get("request_type") or "").strip()
        turnstile_token = (form_data.get("turnstile_token") or "").strip()

        from .website_state import WebsiteState

        website_state = await self.get_state(WebsiteState)

        lang = website_state.current_language

        if config.turnstile_enabled:
            is_valid = await verify_turnstile_token(turnstile_token)
            if not is_valid:
                self.form_submitting = False
                reason = (
                    "turnstile_blocked" if not turnstile_token else "turnstile_invalid"
                )
                logger.warning(
                    "contact form rejected: %s (name=%s %s)",
                    reason,
                    first_name,
                    last_name,
                )
                await track_event(
                    url=f"/{lang}/contact",
                    event_name="contact-form-failed",
                    language=lang,
                    custom_data={"reason": reason},
                )
                website_state.show_toast(  # type: ignore[operator]
                    "Bot verificatie mislukt. Probeer de pagina te vernieuwen.",
                    "error",
                )
                yield rx.call_script(TURNSTILE_RESET_SCRIPT)
                yield None

                await asyncio.sleep(5)
                website_state.hide_toast()  # type: ignore[operator]
                return

        contact_form = ContactForm(
            first_name=first_name,
            last_name=last_name,
            request_type=request_type,
            phone=PhoneNumber(value=phone),
            email=EmailAddress(value=email),
            description=description,
        )

        email_sent = send_contact_form_email(contact_form)

        self.form_submitting = False

        if email_sent:
            await track_event(
                url=f"/{lang}/contact",
                event_name="contact-form-submitted",
                language=lang,
                custom_data={"request_type": request_type},
            )
            website_state.show_toast(  # type: ignore[operator]
                "Bedankt voor je bericht! We nemen zo snel mogelijk contact met je op.",
                "success",
            )
            yield rx.call_script(TURNSTILE_RESET_SCRIPT)
            yield None

            await asyncio.sleep(5)
            website_state.hide_toast()  # type: ignore[operator]
        else:
            logger.warning(
                "contact form email send failed (name=%s %s)",
                first_name,
                last_name,
            )
            await track_event(
                url=f"/{lang}/contact",
                event_name="contact-form-failed",
                language=lang,
                custom_data={"reason": "email_send_failed"},
            )
            website_state.show_toast(  # type: ignore[operator]
                "Het verzenden is mislukt. Probeer het later opnieuw of neem telefonisch contact op.",
                "error",
            )
            yield rx.call_script(TURNSTILE_RESET_SCRIPT)
            yield None

            await asyncio.sleep(5)
            website_state.hide_toast()  # type: ignore[operator]
