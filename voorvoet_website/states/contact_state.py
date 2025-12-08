"""Contact form state management for form validation and submission.

This module contains the ContactState class which manages the state for the
contact form including field values, validation state, and form submission
with email notifications and toast feedback.
"""

import reflex as rx
import asyncio
from typing import TYPE_CHECKING, AsyncGenerator

from ..models import ContactForm
from ..services import send_contact_form_email

if TYPE_CHECKING:
    pass


class ContactState(rx.State):
    """
    State manager for contact form functionality.

    Manages all aspects of the contact form including field values, validation
    states, error display logic, and form submission. Implements real-time
    validation with blur-triggered error display to provide a good user
    experience. On submission, sends email notifications and displays toast
    feedback messages.

    The form uses a ContactForm model object to maintain immutable state and
    ensure consistent validation logic.

    Attributes
    ----------
    contact_form : ContactForm
        The contact form model containing all field values and validation state
    form_submitting : bool
        Loading state flag indicating whether the form is currently being
        submitted, used to prevent duplicate submissions and show loading UI
    """

    contact_form: ContactForm = ContactForm()
    form_submitting: bool = False

    @rx.var
    def contact_first_name(self) -> str:
        """
        Get the first name field value.

        Returns
        -------
        str
            The current first name value
        """
        return self.contact_form.first_name

    @rx.var
    def contact_last_name(self) -> str:
        """
        Get the last name field value.

        Returns
        -------
        str
            The current last name value
        """
        return self.contact_form.last_name

    @rx.var
    def contact_phone_value(self) -> str:
        """
        Get the phone number field value.

        Returns
        -------
        str
            The current phone number value for display in the input field
        """
        return self.contact_form.phone.value

    @rx.var
    def contact_email(self) -> str:
        """
        Get the email field value.

        Returns
        -------
        str
            The current email address value
        """
        return self.contact_form.email.value

    @rx.var
    def contact_description(self) -> str:
        """
        Get the description field value.

        Returns
        -------
        str
            The current message/description text
        """
        return self.contact_form.description

    @rx.var
    def contact_request_type(self) -> str:
        """
        Get the request type field value.

        Returns
        -------
        str
            The currently selected request type
        """
        return self.contact_form.request_type

    @rx.var
    def is_phone_valid(self) -> bool:
        """
        Check if the phone number is valid.

        Returns
        -------
        bool
            True if the phone number passes validation, False otherwise
        """
        return self.contact_form.phone.is_valid()

    @rx.var
    def should_show_phone_error(self) -> bool:
        """
        Determine if phone validation error should be displayed.

        Returns
        -------
        bool
            True if the user has interacted with the phone field and it
            contains invalid data, False otherwise
        """
        return self.contact_form.phone.should_show_error()

    @rx.var
    def is_email_valid(self) -> bool:
        """
        Check if the email address is valid.

        Returns
        -------
        bool
            True if the email passes validation, False otherwise
        """
        return self.contact_form.email.is_valid()

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
        return self.contact_form.email.should_show_error()

    @rx.var
    def can_submit_form(self) -> bool:
        """
        Check if the contact form can be submitted.

        Returns
        -------
        bool
            True if all form fields are valid and the form can be submitted,
            False otherwise
        """
        return self.contact_form.is_valid()

    @rx.event
    def set_contact_first_name(self, value: str) -> None:
        """
        Update the first name field.

        Parameters
        ----------
        value : str
            The new first name value
        """
        self.contact_form = self.contact_form.set_first_name(value)

    @rx.event
    def set_contact_last_name(self, value: str) -> None:
        """
        Update the last name field.

        Parameters
        ----------
        value : str
            The new last name value
        """
        self.contact_form = self.contact_form.set_last_name(value)

    @rx.event
    def set_contact_request_type(self, value: str) -> None:
        """
        Update the request type field.

        Parameters
        ----------
        value : str
            The new request type value
        """
        self.contact_form = self.contact_form.set_request_type(value)

    @rx.event
    def set_contact_phone_number(self, value: str) -> None:
        """
        Update the phone number field.

        Parameters
        ----------
        value : str
            The new phone number value
        """
        self.contact_form = self.contact_form.set_phone(value)

    @rx.event
    def on_phone_blur(self) -> None:
        """
        Handle phone input field losing focus.

        Marks the phone field as blurred to enable validation error display.
        This allows errors to show only after the user has interacted with
        the field, providing a better user experience than showing errors
        immediately on page load.
        """
        new_phone = self.contact_form.phone.mark_blurred()
        self.contact_form = ContactForm(
            first_name=self.contact_form.first_name,
            last_name=self.contact_form.last_name,
            request_type=self.contact_form.request_type,
            phone=new_phone,
            email=self.contact_form.email,
            description=self.contact_form.description,
        )

    @rx.event
    def on_email_blur(self) -> None:
        """
        Handle email input field losing focus.

        Marks the email field as blurred to enable validation error display.
        This allows errors to show only after the user has interacted with
        the field, providing a better user experience than showing errors
        immediately on page load.
        """
        new_email = self.contact_form.email.mark_blurred()
        self.contact_form = ContactForm(
            first_name=self.contact_form.first_name,
            last_name=self.contact_form.last_name,
            request_type=self.contact_form.request_type,
            phone=self.contact_form.phone,
            email=new_email,
            description=self.contact_form.description,
        )

    @rx.event
    def set_contact_email(self, value: str) -> None:
        """
        Update the email field.

        Parameters
        ----------
        value : str
            The new email address value
        """
        self.contact_form = self.contact_form.set_email(value)

    @rx.event
    def set_contact_description(self, value: str) -> None:
        """
        Update the description/message field.

        Parameters
        ----------
        value : str
            The new description text
        """
        self.contact_form = self.contact_form.set_description(value)

    @rx.event
    def set_turnstile_token(self, token: str) -> None:
        """
        Update the Cloudflare Turnstile verification token.

        Parameters
        ----------
        token : str
            The Turnstile token received from the CAPTCHA widget
        """
        self.contact_form = self.contact_form.set_turnstile_token(token)

    @rx.event
    async def submit_contact_form(self) -> AsyncGenerator[None, None]:
        """
        Submit the contact form and send email notification.

        Validates the form, sets loading state, sends the email, resets the
        form on success, and displays appropriate toast notifications. The
        form submission is prevented if already in progress or if validation
        fails.

        The toast notification automatically hides after 5 seconds.

        Yields
        ------
        State updates for UI reactivity during async operations
        """
        if self.contact_form.is_valid() and not self.form_submitting:
            self.form_submitting = True
            yield

            email_sent = send_contact_form_email(self.contact_form)

            self.form_submitting = False

            from .website_state import WebsiteState

            website_state = await self.get_state(WebsiteState)

            if email_sent:
                self.contact_form = self.contact_form.reset()

                website_state.show_toast(  # type: ignore[operator]
                    "Bedankt voor je bericht! We nemen zo snel mogelijk contact met je op.",
                    "success",
                )
                yield

                await asyncio.sleep(5)
                website_state.hide_toast()  # type: ignore[operator]
            else:
                website_state.show_toast(  # type: ignore[operator]
                    "Het verzenden is mislukt. Probeer het later opnieuw of neem telefonisch contact op.",
                    "error",
                )
                yield

                await asyncio.sleep(5)
                website_state.hide_toast()  # type: ignore[operator]
