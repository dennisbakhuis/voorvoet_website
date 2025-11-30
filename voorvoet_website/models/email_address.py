"""Email address validation model."""

from pydantic import field_validator
from .validated_field import ValidatedField


class EmailAddress(ValidatedField):
    """
    Email address validator with interaction tracking.

    This class handles email address validation and tracks user interaction
    state for proper error display. Validates basic email format requirements
    (contains @ and domain with extension).

    Uses Pydantic BaseModel for serialization and type safety.
    Follows an immutable pattern where all mutations return new instances.

    Attributes
    ----------
    value : str
        The email address value.
    touched : bool
        Whether the user has interacted with the field.
    blurred : bool
        Whether the field has lost focus at least once.
    """

    @field_validator("value")
    @classmethod
    def validate_value(cls, v: str) -> str:
        """Validate that value is a string (allows any string for flexibility)."""
        return str(v)

    def set_value(self, new_value: str) -> "EmailAddress":
        """
        Set the email address value and mark as touched if non-empty.

        Parameters
        ----------
        new_value : str
            The raw input value.

        Returns
        -------
        EmailAddress
            A new EmailAddress instance with updated value and state.
        """
        clean_value = self._clean_value(new_value)
        touched = True if clean_value else self.touched

        return EmailAddress(value=clean_value, touched=touched, blurred=self.blurred)

    def mark_blurred(self) -> "EmailAddress":
        """
        Mark the field as blurred (lost focus).

        Returns
        -------
        EmailAddress
            A new EmailAddress instance with blurred flag set to True.
        """
        return EmailAddress(value=self.value, touched=self.touched, blurred=True)

    def is_valid(self) -> bool:
        """
        Check if email address is valid.

        Performs basic email validation checking for:
        - Presence of @ symbol
        - Domain part contains at least one dot
        - Both local and domain parts are non-empty

        Returns
        -------
        bool
            True if the email meets basic validation requirements, False otherwise.
        """
        if not self.value:
            return False

        if "@" not in self.value:
            return False

        parts = self.value.split("@")
        if len(parts) != 2:
            return False

        local_part, domain = parts
        if not local_part or not domain:
            return False

        return "." in domain

    def _clean_value(self, new_value: str) -> str:
        """
        Clean and format the email address input.

        Currently performs minimal cleaning (strip whitespace and lowercase).
        Email addresses are case-insensitive according to RFC 5321.

        Parameters
        ----------
        new_value : str
            The raw input value.

        Returns
        -------
        str
            Cleaned email address (trimmed and lowercased).
        """
        return new_value.strip().lower()
