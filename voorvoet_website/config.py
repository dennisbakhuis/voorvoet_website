# Application configuration
import os
from typing import Optional
from pathlib import Path

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    # Load .env from the project root
    env_path = Path(__file__).parent.parent / ".env"
    load_dotenv(dotenv_path=env_path)
except ImportError:
    # python-dotenv not installed, environment variables must be set manually
    pass


class Config:
    """Application configuration loaded from environment variables"""

    @staticmethod
    def get_turnstile_site_key() -> str:
        """Get Cloudflare Turnstile site key from environment

        Returns the site key for client-side Turnstile widget rendering.
        Get your key from: https://dash.cloudflare.com/
        """
        key = os.getenv("TURNSTILE_SITE_KEY", "")
        if not key:
            # Return a placeholder for development
            return "YOUR_SITE_KEY_HERE"
        return key

    @staticmethod
    def get_turnstile_secret_key() -> Optional[str]:
        """Get Cloudflare Turnstile secret key from environment

        Returns the secret key for server-side token verification.
        This should be kept secret and never exposed to the client.
        """
        return os.getenv("TURNSTILE_SECRET_KEY")

    @staticmethod
    def is_turnstile_enabled() -> bool:
        """Check if Turnstile verification is enabled

        Returns True if Turnstile should be used, False otherwise.
        Useful for disabling bot protection during local development.
        Defaults to True if not specified.
        """
        enabled = os.getenv("TURNSTILE_ENABLED", "true").lower()
        return enabled in ("true", "1", "yes")

    @staticmethod
    def get_smtp_host() -> str:
        """Get SMTP server host from environment

        Returns the SMTP server hostname for sending emails.
        Defaults to Proton Mail's SMTP server.
        """
        return os.getenv("SMTP_HOST", "smtp.protonmail.ch")

    @staticmethod
    def get_smtp_port() -> int:
        """Get SMTP server port from environment

        Returns the SMTP server port number.
        Defaults to 587 (STARTTLS).
        """
        return int(os.getenv("SMTP_PORT", "587"))

    @staticmethod
    def get_smtp_username() -> Optional[str]:
        """Get SMTP username from environment

        Returns the username for SMTP authentication.
        Typically your Proton Mail email address.
        """
        return os.getenv("SMTP_USERNAME")

    @staticmethod
    def get_smtp_password() -> Optional[str]:
        """Get SMTP password from environment

        Returns the password for SMTP authentication.
        For Proton Mail, use an app-specific password.
        This should be kept secret and never exposed to the client.
        """
        return os.getenv("SMTP_PASSWORD")

    @staticmethod
    def get_smtp_from_email() -> Optional[str]:
        """Get SMTP 'from' email address from environment

        Returns the email address to use in the 'From' field.
        Should match your SMTP account email.
        """
        return os.getenv("SMTP_FROM_EMAIL")

    @staticmethod
    def get_smtp_to_email() -> Optional[str]:
        """Get notification recipient email from environment

        Returns the email address where contact form submissions
        should be sent.
        """
        return os.getenv("SMTP_TO_EMAIL")


# Singleton instance
config = Config()
