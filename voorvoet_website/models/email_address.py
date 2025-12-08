"""Email address validation model."""

from pydantic import field_validator
from .validated_field import ValidatedField


class EmailAddress(ValidatedField):
    """
    Email address validator with interaction tracking.

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
        """Set the email address value and mark as touched if non-empty."""
        clean_value = self._clean_value(new_value)
        touched = True if clean_value else self.touched

        return EmailAddress(value=clean_value, touched=touched, blurred=self.blurred)

    def mark_blurred(self) -> "EmailAddress":
        """Mark the field as blurred (lost focus)."""
        return EmailAddress(value=self.value, touched=self.touched, blurred=True)

    def is_valid(self) -> bool:
        """Check if email address is valid."""
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
        """Clean and format the email address input."""
        return new_value.strip().lower()
