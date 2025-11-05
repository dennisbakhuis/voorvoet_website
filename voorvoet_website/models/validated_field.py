"""Base class for validated form fields."""
from pydantic import BaseModel, ConfigDict
from abc import ABC, abstractmethod


class ValidatedField(BaseModel, ABC):
    """
    Abstract base class for form fields with validation and interaction tracking.

    This class provides common functionality for form fields that need to track
    user interaction state (touched/blurred) and display validation errors
    appropriately. Subclasses must implement the validation logic.

    Uses Pydantic BaseModel for serialization and type safety.
    Follows an immutable pattern where all mutations return new instances.

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
        frozen=False,                  # Allow mutation for Reflex state compatibility
        validate_assignment=True,      # Validate on assignment for type safety
        extra='forbid',                # Allow extra fields to be ignored
    )

    value: str = ""
    touched: bool = False
    blurred: bool = False

    @abstractmethod
    def is_valid(self) -> bool:
        """
        Check if the field value is valid.

        Returns
        -------
        bool
            True if the field value passes validation, False otherwise.
        """
        pass

    @abstractmethod
    def _clean_value(self, new_value: str) -> str:
        """
        Clean and format the input value.

        This method should implement any input filtering, formatting,
        or normalization logic specific to the field type.

        Parameters
        ----------
        new_value : str
            The raw input value to clean.

        Returns
        -------
        str
            The cleaned and formatted value.
        """
        pass

    def should_show_error(self) -> bool:
        """
        Determine if validation error should be displayed.

        Errors are only shown after the field has been blurred and
        contains an invalid value. Empty fields don't show errors.

        Returns
        -------
        bool
            True if error should be displayed, False otherwise.
        """
        if not self.value:
            return False
        return self.blurred and not self.is_valid()

    def reset(self) -> "ValidatedField":
        """
        Reset the field to its initial state.

        Returns
        -------
        ValidatedField
            A new instance with empty value and reset state flags.
        """
        return type(self)(value="", touched=False, blurred=False)

    def __str__(self) -> str:
        """
        Get string representation of the field value.

        Returns
        -------
        str
            The current field value.
        """
        return self.value
