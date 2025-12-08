"""Order insoles form state management."""

import reflex as rx
import re
import asyncio
from datetime import datetime
from typing import TYPE_CHECKING, AsyncGenerator

from ..services import send_order_insoles_email
from .website_state import WebsiteState

if TYPE_CHECKING:
    pass


class OrderInsolesState(rx.State):
    """
    State manager for order insoles form functionality.

    Manages all form fields for ordering extra pairs of insoles.

    Attributes
    ----------
    first_name : str
        Patient's first name
    last_name : str
        Patient's last name
    email : str
        Patient's email address
    birth_date : str
        Patient's birth date
    insole_type : str
        Type of insoles (daily, sport, or work shoes)
    quantity : str
        Number of pairs desired
    comments : str
        Additional comments or notes
    """

    first_name: str = ""
    last_name: str = ""
    email: str = ""
    email_blurred: bool = False
    birth_date: str = ""
    birth_date_blurred: bool = False
    insole_type: str = "Dagelijkse zolen"
    quantity: str = "1"
    comments: str = ""
    form_submitting: bool = False

    @rx.event.EventCallback
    def set_first_name(self, value: str) -> None:
        """
        Update first name field.

        Parameters
        ----------
        value : str
            The new first name value.
        """
        self.first_name = value

    @rx.event.EventCallback
    def set_last_name(self, value: str) -> None:
        """
        Update last name field.

        Parameters
        ----------
        value : str
            The new last name value.
        """
        self.last_name = value

    @rx.event.EventCallback
    def set_email(self, value: str) -> None:
        """
        Update email field.

        Parameters
        ----------
        value : str
            The new email value.
        """
        self.email = value

    @rx.event.EventCallback
    def on_email_blur(self) -> None:
        """Mark email field as blurred to enable error display."""
        self.email_blurred = True

    @rx.event.EventCallback
    def set_birth_date(self, value: str) -> None:
        """
        Update birth date field.

        Parameters
        ----------
        value : str
            The new birth date value.
        """
        self.birth_date = value

    @rx.event.EventCallback
    def on_birth_date_blur(self) -> None:
        """Mark birth date field as blurred to enable error display."""
        self.birth_date_blurred = True

    @rx.event.EventCallback
    def set_insole_type(self, value: str) -> None:
        """
        Update insole type field.

        Parameters
        ----------
        value : str
            The new insole type value.
        """
        self.insole_type = value

    @rx.event.EventCallback
    def set_quantity(self, value: str) -> None:
        """
        Update quantity field.

        Parameters
        ----------
        value : str
            The new quantity value.
        """
        self.quantity = value

    @rx.event.EventCallback
    def set_comments(self, value: str) -> None:
        """
        Update comments field.

        Parameters
        ----------
        value : str
            The new comments value.
        """
        self.comments = value

    def _is_valid_email(self, email_str: str) -> bool:
        """
        Validate email format.

        Parameters
        ----------
        email_str : str
            The email string to validate

        Returns
        -------
        bool
            True if the email is valid, False otherwise
        """
        email = email_str.strip()
        if not email:
            return False
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(email_pattern, email))

    def _is_valid_birth_date(self, date_str: str) -> bool:
        """
        Validate birth date format and age constraints.

        Parameters
        ----------
        date_str : str
            The birth date string to validate in dd-mm-yyyy format.

        Returns
        -------
        bool
            True if the birth date is valid (dd-mm-yyyy format, valid calendar
            date, and age between 4-120 years), False otherwise.
        """
        if not date_str.strip():
            return False

        date_pattern = r"^(\d{1,2})[-/](\d{1,2})[-/](\d{4})$"
        match = re.match(date_pattern, date_str)
        if not match:
            return False

        try:
            day, month, year = match.groups()
            day = int(day)
            month = int(month)
            year = int(year)

            birth_date = datetime(year, month, day)

            today = datetime.now()
            age_years = (today - birth_date).days / 365.25

            if age_years < 4 or age_years > 120:
                return False

            if birth_date > today:
                return False

            return True

        except (ValueError, TypeError):
            return False

    @rx.var
    def should_show_email_error(self) -> bool:
        """
        Determine if email validation error should be displayed.

        Returns
        -------
        bool
            True if the user has interacted with the email field and it
            contains invalid data, False otherwise
        """
        return self.email_blurred and not self._is_valid_email(self.email)

    @rx.var
    def should_show_birth_date_error(self) -> bool:
        """
        Determine if birth date validation error should be displayed.

        Returns
        -------
        bool
            True if the user has interacted with the birth date field and it
            contains invalid data, False otherwise
        """
        return self.birth_date_blurred and not self._is_valid_birth_date(
            self.birth_date
        )

    @rx.var
    def can_submit_form(self) -> bool:
        """
        Check if the order form can be submitted.

        Returns
        -------
        bool
            True if all required fields are valid (first name, last name,
            valid email, birth date with age 4-120 years, insole type, and
            positive quantity), False otherwise.
        """
        if not self.first_name.strip():
            return False
        if not self.last_name.strip():
            return False
        if not self.insole_type.strip():
            return False

        if not self._is_valid_birth_date(self.birth_date):
            return False

        if not self._is_valid_email(self.email):
            return False

        if not self.quantity.strip():
            return False
        try:
            qty = int(self.quantity)
            if qty <= 0:
                return False
        except ValueError:
            return False

        return True

    @rx.event.EventCallback
    async def submit_order(self) -> AsyncGenerator[None, None]:
        """
        Submit the order form and send email notification.

        Yields
        ------
        State updates for UI reactivity during async operations.
        """
        if self.can_submit_form and not self.form_submitting:
            self.form_submitting = True
            yield

            email_sent = send_order_insoles_email(self)

            self.form_submitting = False

            website_state = await self.get_state(WebsiteState)

            if email_sent:
                self.first_name = ""
                self.last_name = ""
                self.email = ""
                self.email_blurred = False
                self.birth_date = ""
                self.birth_date_blurred = False
                self.insole_type = "Dagelijkse zolen"
                self.quantity = "1"
                self.comments = ""

                website_state.show_toast(
                    "Bedankt voor je bestelling! We nemen zo snel mogelijk contact met je op.",
                    "success",
                )
                yield

                await asyncio.sleep(5)
                website_state.hide_toast()
            else:
                website_state.show_toast(
                    "Het verzenden is mislukt. Probeer het later opnieuw of neem telefonisch contact op.",
                    "error",
                )
                yield

                await asyncio.sleep(5)
                website_state.hide_toast()
