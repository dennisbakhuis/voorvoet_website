# Email service for sending contact form notifications
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional
import logging
from datetime import datetime

from ..config import config
from ..models.contact_form import ContactForm

# Configure logging
logger = logging.getLogger(__name__)

# Dutch day and month names
DUTCH_DAYS = [
    "Maandag", "Dinsdag", "Woensdag", "Donderdag",
    "Vrijdag", "Zaterdag", "Zondag"
]

DUTCH_MONTHS = [
    "januari", "februari", "maart", "april", "mei", "juni",
    "juli", "augustus", "september", "oktober", "november", "december"
]


def format_dutch_datetime(dt: datetime) -> str:
    """Format datetime in Dutch human-readable format

    Example: Maandag 5 april 2025 om 11:47

    Args:
        dt: The datetime to format

    Returns:
        str: Formatted datetime string in Dutch
    """
    day_name = DUTCH_DAYS[dt.weekday()]
    day = dt.day
    month_name = DUTCH_MONTHS[dt.month - 1]
    year = dt.year
    time = dt.strftime("%H:%M")

    return f"{day_name} {day} {month_name} {year} om {time}"


def send_contact_form_email(form: ContactForm) -> bool:
    """Send an email notification when a contact form is submitted

    Args:
        form: The ContactForm instance containing submission data

    Returns:
        bool: True if email was sent successfully, False otherwise
    """
    # Get SMTP configuration
    smtp_host = config.smtp_host
    smtp_port = config.smtp_port
    smtp_username = config.smtp_username
    smtp_password = config.smtp_password
    from_email = config.smtp_from_email
    to_email = config.smtp_to_email

    # Validate configuration
    if not all([smtp_username, smtp_password, from_email, to_email]):
        logger.error("SMTP configuration incomplete. Check environment variables.")
        return False

    try:
        # Get current timestamp in Dutch format
        timestamp = format_dutch_datetime(datetime.now())

        # Create email message
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"Nieuw contactformulier: {form.request_type}"
        msg["From"] = from_email
        msg["To"] = to_email

        # Create email body
        contact_method = ""
        if form.request_type == "Bel mij terug":
            contact_method = f"Telefoonnummer: {form.phone.value}"
        else:
            contact_method = f"E-mail: {form.email.value}"

        # Plain text version
        text_body = f"""
Nieuw contactformulier inzending

Ontvangen: {timestamp}

Naam: {form.first_name} {form.last_name}
Verzoek type: {form.request_type}
{contact_method}

Bericht:
{form.description}
"""

        # HTML version
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

        # Attach parts
        part1 = MIMEText(text_body, "plain")
        part2 = MIMEText(html_body, "html")
        msg.attach(part1)
        msg.attach(part2)

        # Send email
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()  # Enable TLS encryption
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
