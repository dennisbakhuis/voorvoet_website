"""Base class for validated form fields."""

from pydantic import BaseModel, ConfigDict
from abc import ABC, abstractmethod


class ValidatedField(BaseModel, ABC):
    """
    Abstract base class for form fields with validation and interaction tracking.

    Attributes
    ----------
    value : str
        The current value of the field.
    touched : bool
        Whether the user has interacted with the field.
    blurred : bool
        Whether the field has lost focus at least once.
    """

    model_config = ConfigDict(
        frozen=False,
        validate_assignment=True,
        extra="forbid",
    )

    value: str = ""
    touched: bool = False
    blurred: bool = False

    @abstractmethod
    def is_valid(self) -> bool:
        """Check if the field value is valid."""
        pass

    @abstractmethod
    def _clean_value(self, new_value: str) -> str:
        """Clean and format the input value."""
        pass

    def should_show_error(self) -> bool:
        """Determine if validation error should be displayed."""
        if not self.value:
            return False
        return self.blurred and not self.is_valid()

    def reset(self) -> "ValidatedField":
        """Reset the field to its initial state."""
        return type(self)(value="", touched=False, blurred=False)

    def __str__(self) -> str:
        """Get string representation of the field value."""
        return self.value
