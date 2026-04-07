"""Order insoles form state management for form submission.

This module contains the OrderInsolesState class which manages the state for the
insole order form submission with email notifications and toast feedback.
Form validation is handled client-side via HTML5 validation and JavaScript.
"""

import logging
import reflex as rx
import asyncio
from typing import AsyncGenerator

from reflex.event import EventSpec

from ..services import send_order_insoles_email, track_event, verify_turnstile_token
from ..config import config


logger = logging.getLogger(__name__)


TURNSTILE_RESET_SCRIPT_INSOLE = (
    "(function() {"
    "  var c = document.getElementById('turnstile-widget-container-insole');"
    "  if (c && window.turnstile && c.dataset.widgetId != null) {"
    "    try { window.turnstile.reset(c); } catch (e) {}"
    "  }"
    "  var t = document.getElementById('turnstile-token-insole');"
    "  if (t) { t.value = ''; }"
    "  var form = document.getElementById('insole-order-form');"
    "  if (form) { form.dispatchEvent(new Event('change', { bubbles: true })); }"
    "})();"
)


class OrderInsolesState(rx.State):
    """
    State manager for order insoles form functionality.

    Manages form submission with email notifications and toast feedback.
    Form validation is handled client-side via HTML5 validation attributes
    and JavaScript. Only the insole_type (radio) and quantity (select) use
    server state since they are single-click selections with acceptable latency.

    Attributes
    ----------
    insole_type : str
        The selected insole type (daily, sport, or work shoes)
    quantity : str
        The selected quantity (1, 2, or 3)
    form_submitting : bool
        Loading state flag for preventing duplicate submissions
    """

    insole_type: str = "Dagelijkse zolen"
    quantity: str = "1"
    form_submitting: bool = False

    @rx.event
    def set_insole_type(self, value: str) -> None:
        """Update the insole type (radio selection)."""
        self.insole_type = value

    @rx.event
    def set_quantity(self, value: str) -> None:
        """Update the quantity (select value)."""
        self.quantity = value

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
        email = (form_data.get("email") or "").strip()
        birth_date = (form_data.get("birth_date") or "").strip()
        insole_type = (form_data.get("insole_type") or "").strip()
        quantity = (form_data.get("quantity") or "1").strip()
        comments = (form_data.get("comments") or "").strip()
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
                    "insole order rejected: %s (name=%s %s)",
                    reason,
                    first_name,
                    last_name,
                )
                await track_event(
                    url=f"/{lang}/zolen-bestellen",
                    event_name="insole-order-failed",
                    language=lang,
                    custom_data={"reason": reason},
                )
                website_state.show_toast(  # type: ignore[operator]
                    "Bot verificatie mislukt. Probeer de pagina te vernieuwen.",
                    "error",
                )
                yield rx.call_script(TURNSTILE_RESET_SCRIPT_INSOLE)
                yield None

                await asyncio.sleep(5)
                website_state.hide_toast()  # type: ignore[operator]
                return

        order_data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "birth_date": birth_date,
            "insole_type": insole_type,
            "quantity": quantity,
            "comments": comments,
        }

        email_sent = send_order_insoles_email(order_data)

        self.form_submitting = False

        if email_sent:
            await track_event(
                url=f"/{lang}/zolen-bestellen",
                event_name="insole-order-submitted",
                language=lang,
                custom_data={"insole_type": insole_type, "quantity": quantity},
            )
            website_state.show_toast(  # type: ignore[operator]
                "Bedankt voor je bestelling! We nemen zo snel mogelijk contact met je op.",
                "success",
            )
            yield rx.call_script(TURNSTILE_RESET_SCRIPT_INSOLE)
            yield None

            await asyncio.sleep(5)
            website_state.hide_toast()  # type: ignore[operator]
        else:
            logger.warning(
                "insole order email send failed (name=%s %s)",
                first_name,
                last_name,
            )
            await track_event(
                url=f"/{lang}/zolen-bestellen",
                event_name="insole-order-failed",
                language=lang,
                custom_data={"reason": "email_send_failed"},
            )
            website_state.show_toast(  # type: ignore[operator]
                "Het verzenden is mislukt. Probeer het later opnieuw of neem telefonisch contact op.",
                "error",
            )
            yield rx.call_script(TURNSTILE_RESET_SCRIPT_INSOLE)
            yield None

            await asyncio.sleep(5)
            website_state.hide_toast()  # type: ignore[operator]
