# Phone number validation model
from dataclasses import dataclass


@dataclass
class PhoneNumber:
    """Dutch phone number validator

    This class handles phone number validation and tracks whether
    the user has interacted with the input field.

    Uses dataclass to be serializable for Reflex state management.
    """

    value: str = ""
    touched: bool = False
    blurred: bool = False  # Track if field has lost focus

    def set_value(self, new_value: str) -> "PhoneNumber":
        """Set the phone number value and mark as touched if non-empty

        Returns a new PhoneNumber instance (immutable pattern for Reflex state)
        """
        # Only allow numeric characters
        numeric_value = ''.join(char for char in new_value if char.isdigit())
        clean_value = numeric_value[:10]  # Limit to 10 digits

        # Mark as touched after first input
        touched = True if clean_value else self.touched

        return PhoneNumber(value=clean_value, touched=touched, blurred=self.blurred)

    def mark_blurred(self) -> "PhoneNumber":
        """Mark the field as blurred (lost focus)"""
        return PhoneNumber(value=self.value, touched=self.touched, blurred=True)

    def is_valid(self) -> bool:
        """Check if phone number is valid (exactly 10 digits)"""
        return len(self.value) == 10 and self.value.isdigit()

    def should_show_error(self) -> bool:
        """Show error only after field has been blurred and is invalid"""
        # Don't show error if field is empty
        if not self.value:
            return False
        # Only show error after blur and if invalid
        return self.blurred and not self.is_valid()

    def reset(self) -> "PhoneNumber":
        """Reset the phone number and touched state"""
        return PhoneNumber(value="", touched=False, blurred=False)

    def __str__(self) -> str:
        return self.value
