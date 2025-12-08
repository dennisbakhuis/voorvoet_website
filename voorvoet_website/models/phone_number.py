"""Phone number validation model."""

from pydantic import field_validator
from .validated_field import ValidatedField


class PhoneNumber(ValidatedField):
    """
    Dutch phone number validator with interaction tracking.

    Attributes
    ----------
    value : str
        The phone number value (numeric only, max 10 digits).
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

    def set_value(self, new_value: str) -> "PhoneNumber":
        """Set the phone number value and mark as touched if non-empty."""
        clean_value = self._clean_value(new_value)
        touched = True if clean_value else self.touched

        return PhoneNumber(value=clean_value, touched=touched, blurred=self.blurred)

    def mark_blurred(self) -> "PhoneNumber":
        """Mark the field as blurred (lost focus)."""
        return PhoneNumber(value=self.value, touched=self.touched, blurred=True)

    def is_valid(self) -> bool:
        """Check if phone number is valid."""
        return len(self.value) == 10 and self.value.isdigit()

    def _clean_value(self, new_value: str) -> str:
        """Clean and format the phone number input."""
        numeric_value = "".join(char for char in new_value if char.isdigit())
        return numeric_value[:10]
