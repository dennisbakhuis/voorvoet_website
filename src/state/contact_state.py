# State object for contact form handling
import reflex as rx

class ContactState(rx.State):
    name: str = ""
    email: str = ""
    phone: str = ""
    message: str = ""
    sent: bool = False

    def send(self):
        self.sent = True
        self.name = ""
        self.email = ""
        self.phone = ""
        self.message = ""
        return rx.toast.success("Bericht verzonden — we nemen snel contact op!")