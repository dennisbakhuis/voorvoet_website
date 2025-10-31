# Main state file of the Reflex web app
import reflex as rx
import asyncio
from ..models import ContactForm
from ..services import send_contact_form_email
from ..config import config


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

    # Contact form state
    contact_form: ContactForm = ContactForm()
    form_submitting: bool = False  # Loading state for form submission

    @rx.var
    def contact_first_name(self) -> str:
        """Get the first name value"""
        return self.contact_form.first_name

    @rx.var
    def contact_last_name(self) -> str:
        """Get the last name value"""
        return self.contact_form.last_name

    @rx.var
    def contact_phone_value(self) -> str:
        """Get the phone number value for the input field"""
        return self.contact_form.phone.value

    @rx.var
    def contact_email(self) -> str:
        """Get the email value"""
        return self.contact_form.email

    @rx.var
    def contact_description(self) -> str:
        """Get the description value"""
        return self.contact_form.description

    @rx.var
    def contact_request_type(self) -> str:
        """Get the request type"""
        return self.contact_form.request_type

    @rx.var
    def is_phone_valid(self) -> bool:
        """Check if phone number is valid"""
        return self.contact_form.phone.is_valid()

    @rx.var
    def should_show_phone_error(self) -> bool:
        """Show error if user has touched the field and it's not valid"""
        return self.contact_form.phone.should_show_error()

    @rx.var
    def can_submit_form(self) -> bool:
        """Check if the contact form can be submitted"""
        return self.contact_form.is_valid()
    
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

    @rx.event
    def set_contact_first_name(self, value: str):
        """Update first name"""
        self.contact_form = self.contact_form.set_first_name(value)

    @rx.event
    def set_contact_last_name(self, value: str):
        """Update last name"""
        self.contact_form = self.contact_form.set_last_name(value)

    @rx.event
    def set_contact_request_type(self, value: str):
        """Update request type"""
        self.contact_form = self.contact_form.set_request_type(value)

    @rx.event
    def set_contact_phone_number(self, value: str):
        """Update the phone number"""
        self.contact_form = self.contact_form.set_phone(value)

    @rx.event
    def on_phone_blur(self):
        """Handle phone input losing focus"""
        # Mark the phone field as blurred to enable validation error display
        # Don't increment version here to avoid focus loss
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
    def set_contact_email(self, value: str):
        """Update email"""
        self.contact_form = self.contact_form.set_email(value)

    @rx.event
    def set_contact_description(self, value: str):
        """Update description"""
        self.contact_form = self.contact_form.set_description(value)

    @rx.event
    def set_turnstile_token(self, token: str):
        """Update Turnstile token"""
        self.contact_form = self.contact_form.set_turnstile_token(token)

    @rx.event
    async def submit_contact_form(self):
        """Submit the contact form"""
        if self.contact_form.is_valid() and not self.form_submitting:
            # Set loading state immediately and update UI
            self.form_submitting = True
            yield

            # Send email notification
            email_sent = send_contact_form_email(self.contact_form)

            # Reset loading state
            self.form_submitting = False

            if email_sent:
                # Reset form first to clear all fields
                self.contact_form = self.contact_form.reset()

                # Show success toast
                self.show_toast(
                    "Bedankt voor je bericht! We nemen zo snel mogelijk contact met je op.",
                    "success"
                )
                yield

                # Auto-hide toast after 5 seconds
                await asyncio.sleep(5)
                self.hide_toast()
            else:
                # Show error toast
                self.show_toast(
                    "Het verzenden is mislukt. Probeer het later opnieuw of neem telefonisch contact op.",
                    "error"
                )
                yield

                # Auto-hide toast after 5 seconds
                await asyncio.sleep(5)
                self.hide_toast()
