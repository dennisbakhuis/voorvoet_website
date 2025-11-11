"""Order insoles form state management."""
import reflex as rx


class OrderInsolesState(rx.State):
    """
    State manager for order insoles form functionality.

    Manages all form fields for ordering extra pairs of insoles.

    Attributes
    ----------
    first_name : str
        Patient's first name
    last_name : str
        Patient's last name
    email : str
        Patient's email address
    birth_date : str
        Patient's birth date
    insole_type : str
        Type of insoles (daily, sport, or work shoes)
    quantity : str
        Number of pairs desired
    comments : str
        Additional comments or notes
    """

    first_name: str = ""
    last_name: str = ""
    email: str = ""
    birth_date: str = ""
    insole_type: str = ""
    quantity: str = ""
    comments: str = ""

    @rx.event
    def set_first_name(self, value: str):
        """Update first name field."""
        self.first_name = value

    @rx.event
    def set_last_name(self, value: str):
        """Update last name field."""
        self.last_name = value

    @rx.event
    def set_email(self, value: str):
        """Update email field."""
        self.email = value

    @rx.event
    def set_birth_date(self, value: str):
        """Update birth date field."""
        self.birth_date = value

    @rx.event
    def set_insole_type(self, value: str):
        """Update insole type field."""
        self.insole_type = value

    @rx.event
    def set_quantity(self, value: str):
        """Update quantity field."""
        self.quantity = value

    @rx.event
    def set_comments(self, value: str):
        """Update comments field."""
        self.comments = value

    @rx.event
    def submit_order(self):
        """
        Submit the order form.

        This is a placeholder for future implementation that would
        send the order to the backend or email system.
        """
        # TODO: Implement order submission logic
        pass
