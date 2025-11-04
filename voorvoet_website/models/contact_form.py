# Contact form model
from dataclasses import dataclass, field
from .phone_number import PhoneNumber
from ..config import config


@dataclass
class ContactForm:
    """Contact form data model

    Groups all contact form fields and provides validation methods.
    Uses dataclass to be serializable for Reflex state management.
    """

    first_name: str = ""
    last_name: str = ""
    request_type: str = "Bel mij terug"
    phone: PhoneNumber = field(default_factory=PhoneNumber)
    email: str = ""
    description: str = ""
    turnstile_token: str = ""  # Cloudflare Turnstile verification token

    def set_first_name(self, value: str) -> "ContactForm":
        """Update first name"""
        return ContactForm(
            first_name=value,
            last_name=self.last_name,
            request_type=self.request_type,
            phone=self.phone,
            email=self.email,
            description=self.description,
            turnstile_token=self.turnstile_token,
        )

    def set_last_name(self, value: str) -> "ContactForm":
        """Update last name"""
        return ContactForm(
            first_name=self.first_name,
            last_name=value,
            request_type=self.request_type,
            phone=self.phone,
            email=self.email,
            description=self.description,
            turnstile_token=self.turnstile_token,
        )

    def set_request_type(self, value: str) -> "ContactForm":
        """Update request type"""
        return ContactForm(
            first_name=self.first_name,
            last_name=self.last_name,
            request_type=value,
            phone=self.phone,
            email=self.email,
            description=self.description,
            turnstile_token=self.turnstile_token,
        )

    def set_phone(self, value: str) -> "ContactForm":
        """Update phone number"""
        return ContactForm(
            first_name=self.first_name,
            last_name=self.last_name,
            request_type=self.request_type,
            phone=self.phone.set_value(value),
            email=self.email,
            description=self.description,
            turnstile_token=self.turnstile_token,
        )

    def set_email(self, value: str) -> "ContactForm":
        """Update email"""
        return ContactForm(
            first_name=self.first_name,
            last_name=self.last_name,
            request_type=self.request_type,
            phone=self.phone,
            email=value,
            description=self.description,
            turnstile_token=self.turnstile_token,
        )

    def set_description(self, value: str) -> "ContactForm":
        """Update description"""
        return ContactForm(
            first_name=self.first_name,
            last_name=self.last_name,
            request_type=self.request_type,
            phone=self.phone,
            email=self.email,
            description=value,
            turnstile_token=self.turnstile_token,
        )

    def set_turnstile_token(self, token: str) -> "ContactForm":
        """Update Turnstile verification token"""
        return ContactForm(
            first_name=self.first_name,
            last_name=self.last_name,
            request_type=self.request_type,
            phone=self.phone,
            email=self.email,
            description=self.description,
            turnstile_token=token,
        )

    def is_valid(self) -> bool:
        """Check if the entire form is valid and ready to submit"""
        # Check required fields based on request type
        if not self.first_name or not self.last_name:
            return False

        if not self.description:
            return False

        # Require Turnstile verification token only if enabled
        if config.turnstile_enabled and not self.turnstile_token:
            return False

        # Validate based on request type
        if self.request_type == "Bel mij terug":
            # Phone callback requires valid phone number
            if not self.phone.is_valid():
                return False
        else:
            # Email request requires valid email
            if not self.email or not self._is_email_valid():
                return False

        return True

    def _is_email_valid(self) -> bool:
        """Basic email validation"""
        if not self.email:
            return False
        # Simple email validation
        return "@" in self.email and "." in self.email.split("@")[-1]

    def reset(self) -> "ContactForm":
        """Reset the form to default values"""
        return ContactForm()
