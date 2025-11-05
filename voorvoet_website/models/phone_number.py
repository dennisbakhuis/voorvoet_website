"""Phone number validation model."""
from pydantic import field_validator
from .validated_field import ValidatedField


class PhoneNumber(ValidatedField):
    """
    Dutch phone number validator with interaction tracking.

    This class handles phone number validation for Dutch phone numbers
    (10 digits) and tracks user interaction state for proper error display.

    Uses Pydantic BaseModel for serialization and type safety.
    Follows an immutable pattern where all mutations return new instances.

    Attributes
    ----------
    value : str
        The phone number value (numeric only, max 10 digits).
    touched : bool
        Whether the user has interacted with the field.
    blurred : bool
        Whether the field has lost focus at least once.
    """

    @field_validator('value')
    @classmethod
    def validate_value(cls, v: str) -> str:
        """Validate that value is a string (allows any string for flexibility)."""
        return str(v)

    def set_value(self, new_value: str) -> "PhoneNumber":
        """
        Set the phone number value and mark as touched if non-empty.

        Parameters
        ----------
        new_value : str
            The raw input value (will be cleaned to numeric only).

        Returns
        -------
        PhoneNumber
            A new PhoneNumber instance with updated value and state.
        """
        clean_value = self._clean_value(new_value)
        touched = True if clean_value else self.touched

        return PhoneNumber(value=clean_value, touched=touched, blurred=self.blurred)

    def mark_blurred(self) -> "PhoneNumber":
        """
        Mark the field as blurred (lost focus).

        Returns
        -------
        PhoneNumber
            A new PhoneNumber instance with blurred flag set to True.
        """
        return PhoneNumber(value=self.value, touched=self.touched, blurred=True)

    def is_valid(self) -> bool:
        """
        Check if phone number is valid.

        A valid Dutch phone number has exactly 10 digits.

        Returns
        -------
        bool
            True if the phone number has exactly 10 digits, False otherwise.
        """
        return len(self.value) == 10 and self.value.isdigit()

    def _clean_value(self, new_value: str) -> str:
        """
        Clean and format the phone number input.

        Extracts only numeric characters and limits to 10 digits.

        Parameters
        ----------
        new_value : str
            The raw input value.

        Returns
        -------
        str
            Cleaned value containing only digits, max 10 characters.
        """
        numeric_value = ''.join(char for char in new_value if char.isdigit())
        return numeric_value[:10]
