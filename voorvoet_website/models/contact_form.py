"""Contact form model."""
from pydantic import BaseModel, Field, ConfigDict
from .phone_number import PhoneNumber
from .email_address import EmailAddress
from ..config import config


class ContactForm(BaseModel):
    """
    Contact form data model with validation.

    Groups all contact form fields and provides validation methods.
    Uses Pydantic BaseModel for serialization and type safety.
    Follows an immutable pattern where all mutations return new instances.

    Attributes
    ----------
    first_name : str
        User's first name.
    last_name : str
        User's last name.
    request_type : str
        Type of contact request ("Bel mij terug" or "Stuur mij een mail").
    phone : PhoneNumber
        Phone number field with validation (required for callback requests).
    email : EmailAddress
        Email address field with validation (required for email requests).
    description : str
        Message or description from the user.
    turnstile_token : str
        Cloudflare Turnstile verification token for bot protection.
    """

    model_config = ConfigDict(
        frozen=False,                  # Allow mutation for Reflex state compatibility
        validate_assignment=True,      # Validate on assignment for type safety
        arbitrary_types_allowed=True,  # Arbitrary types allowed for nested Pydantic models
    )

    first_name: str = ""
    last_name: str = ""
    request_type: str = "Bel mij terug"
    phone: PhoneNumber = Field(default_factory=PhoneNumber)
    email: EmailAddress = Field(default_factory=EmailAddress)
    description: str = ""
    turnstile_token: str = ""

    def set_first_name(self, value: str) -> "ContactForm":
        """
        Update first name.

        Parameters
        ----------
        value : str
            The new first name value.

        Returns
        -------
        ContactForm
            A new ContactForm instance with updated first name.
        """
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
        """
        Update last name.

        Parameters
        ----------
        value : str
            The new last name value.

        Returns
        -------
        ContactForm
            A new ContactForm instance with updated last name.
        """
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
        """
        Update request type.

        Parameters
        ----------
        value : str
            The new request type value.

        Returns
        -------
        ContactForm
            A new ContactForm instance with updated request type.
        """
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
        """
        Update phone number.

        Parameters
        ----------
        value : str
            The new phone number value.

        Returns
        -------
        ContactForm
            A new ContactForm instance with updated phone number.
        """
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
        """
        Update email.

        Parameters
        ----------
        value : str
            The new email value.

        Returns
        -------
        ContactForm
            A new ContactForm instance with updated email.
        """
        return ContactForm(
            first_name=self.first_name,
            last_name=self.last_name,
            request_type=self.request_type,
            phone=self.phone,
            email=self.email.set_value(value),
            description=self.description,
            turnstile_token=self.turnstile_token,
        )

    def set_description(self, value: str) -> "ContactForm":
        """
        Update description.

        Parameters
        ----------
        value : str
            The new description value.

        Returns
        -------
        ContactForm
            A new ContactForm instance with updated description.
        """
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
        """
        Update Turnstile verification token.

        Parameters
        ----------
        token : str
            The new Turnstile token value.

        Returns
        -------
        ContactForm
            A new ContactForm instance with updated token.
        """
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
        """
        Check if the entire form is valid and ready to submit.

        Returns
        -------
        bool
            True if all required fields are valid, False otherwise.
        """
        if not self.first_name or not self.last_name:
            return False

        if not self.description:
            return False

        if config.turnstile_enabled and not self.turnstile_token:
            return False

        if self.request_type == "Bel mij terug":
            if not self.phone.is_valid():
                return False
        else:
            if not self.email.is_valid():
                return False

        return True

    def reset(self) -> "ContactForm":
        """
        Reset the form to default values.

        Returns
        -------
        ContactForm
            A new ContactForm instance with all fields reset to defaults.
        """
        return ContactForm()
