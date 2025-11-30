"""Email service for sending contact form and order notifications."""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import TYPE_CHECKING
import logging
from datetime import datetime

from ..config import config
from ..models.contact_form import ContactForm

if TYPE_CHECKING:
    from ..states.order_insoles_state import OrderInsolesState

logger = logging.getLogger(__name__)

DUTCH_DAYS = [
    "Maandag",
    "Dinsdag",
    "Woensdag",
    "Donderdag",
    "Vrijdag",
    "Zaterdag",
    "Zondag",
]

DUTCH_MONTHS = [
    "januari",
    "februari",
    "maart",
    "april",
    "mei",
    "juni",
    "juli",
    "augustus",
    "september",
    "oktober",
    "november",
    "december",
]


def format_dutch_datetime(dt: datetime) -> str:
    """
    Format datetime in Dutch human-readable format.

    Parameters
    ----------
    dt : datetime
        The datetime to format.

    Returns
    -------
    str
        Formatted datetime string in Dutch (e.g., "Maandag 5 april 2025 om 11:47").
    """
    day_name = DUTCH_DAYS[dt.weekday()]
    day = dt.day
    month_name = DUTCH_MONTHS[dt.month - 1]
    year = dt.year
    time = dt.strftime("%H:%M")

    return f"{day_name} {day} {month_name} {year} om {time}"


def send_contact_form_email(form: ContactForm) -> bool:
    """
    Send an email notification when a contact form is submitted.

    Parameters
    ----------
    form : ContactForm
        The ContactForm instance containing submission data.

    Returns
    -------
    bool
        True if email was sent successfully, False otherwise.
    """
    smtp_username = config.smtp_username
    smtp_password = config.smtp_password
    from_email = config.smtp_from_email
    to_email = config.smtp_to_email

    if not all([smtp_username, smtp_password, from_email, to_email]):
        logger.error("SMTP configuration incomplete. Check environment variables.")
        return False

    # Type narrowing: after the check above, we know these are not None
    assert smtp_username is not None
    assert smtp_password is not None
    assert from_email is not None
    assert to_email is not None

    smtp_host = config.smtp_host
    smtp_port = config.smtp_port

    try:
        timestamp = format_dutch_datetime(datetime.now())

        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"Nieuw contactformulier: {form.request_type}"
        msg["From"] = from_email
        msg["To"] = to_email

        contact_method = ""
        if form.request_type == "Bel mij terug":
            contact_method = f"Telefoonnummer: {form.phone.value}"
        else:
            contact_method = f"E-mail: {form.email.value}"

        text_body = f"""
Nieuw contactformulier inzending

Ontvangen: {timestamp}

Naam: {form.first_name} {form.last_name}
Verzoek type: {form.request_type}
{contact_method}

Bericht:
{form.description}
"""

        html_body = f"""
<html>
<head></head>
<body>
    <h2>Nieuw contactformulier inzending</h2>
    <p><em>Ontvangen: {timestamp}</em></p>
    <hr style="border: none; border-top: 1px solid #ddd; margin: 1rem 0;">
    <p><strong>Naam:</strong> {form.first_name} {form.last_name}</p>
    <p><strong>Verzoek type:</strong> {form.request_type}</p>
    <p><strong>{contact_method.split(':')[0]}:</strong> {contact_method.split(':')[1].strip()}</p>
    <h3>Bericht:</h3>
    <p>{form.description.replace(chr(10), '<br>')}</p>
</body>
</html>
"""

        part1 = MIMEText(text_body, "plain")
        part2 = MIMEText(html_body, "html")
        msg.attach(part1)
        msg.attach(part2)

        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)

        logger.info(f"Contact form email sent successfully to {to_email}")
        return True

    except smtplib.SMTPAuthenticationError as e:
        logger.error(f"SMTP authentication failed: {e}")
        return False
    except smtplib.SMTPException as e:
        logger.error(f"SMTP error occurred: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error sending email: {e}")
        return False


def send_order_insoles_email(order_state: "OrderInsolesState") -> bool:
    """
    Send an email notification when an order insoles form is submitted.

    Parameters
    ----------
    order_state : OrderInsolesState
        The OrderInsolesState instance containing order data.

    Returns
    -------
    bool
        True if email was sent successfully, False otherwise.
    """
    smtp_username = config.smtp_username
    smtp_password = config.smtp_password
    from_email = config.smtp_from_email
    to_email = config.smtp_to_email

    if not all([smtp_username, smtp_password, from_email, to_email]):
        logger.error("SMTP configuration incomplete. Check environment variables.")
        return False

    # Type narrowing: after the check above, we know these are not None
    assert smtp_username is not None
    assert smtp_password is not None
    assert from_email is not None
    assert to_email is not None

    smtp_host = config.smtp_host
    smtp_port = config.smtp_port

    try:
        timestamp = format_dutch_datetime(datetime.now())

        msg = MIMEMultipart("alternative")
        msg["Subject"] = (
            f"Nieuw bestelling extra paar zolen: {order_state.first_name} {order_state.last_name}"
        )
        msg["From"] = from_email
        msg["To"] = to_email

        text_body = f"""
Nieuwe zoolbestelling

Ontvangen: {timestamp}

Naam: {order_state.first_name} {order_state.last_name}
E-mail: {order_state.email}
Geboortedatum: {order_state.birth_date}
Soort zolen: {order_state.insole_type}
Aantal: {order_state.quantity}

Opmerkingen:
{order_state.comments if order_state.comments.strip() else "(geen opmerkingen)"}
"""

        html_body = f"""
<html>
<head></head>
<body>
    <h2>Nieuwe zoolbestelling</h2>
    <p><em>Ontvangen: {timestamp}</em></p>
    <hr style="border: none; border-top: 1px solid #ddd; margin: 1rem 0;">
    <p><strong>Naam:</strong> {order_state.first_name} {order_state.last_name}</p>
    <p><strong>E-mail:</strong> {order_state.email}</p>
    <p><strong>Geboortedatum:</strong> {order_state.birth_date}</p>
    <p><strong>Soort zolen:</strong> {order_state.insole_type}</p>
    <p><strong>Aantal:</strong> {order_state.quantity}</p>
    <h3>Opmerkingen:</h3>
    <p>{order_state.comments.replace(chr(10), '<br>') if order_state.comments.strip() else "<em>(geen opmerkingen)</em>"}</p>
</body>
</html>
"""

        part1 = MIMEText(text_body, "plain")
        part2 = MIMEText(html_body, "html")
        msg.attach(part1)
        msg.attach(part2)

        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)

        logger.info(f"Order insoles email sent successfully to {to_email}")
        return True

    except smtplib.SMTPAuthenticationError as e:
        logger.error(f"SMTP authentication failed: {e}")
        return False
    except smtplib.SMTPException as e:
        logger.error(f"SMTP error occurred: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error sending email: {e}")
        return False
