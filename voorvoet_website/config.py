"""Configuration management for the VoorVoet website application.

This module defines the application configuration using Pydantic settings,
loading values from environment variables and .env file. Configuration includes
Cloudflare Turnstile settings, SMTP email settings, external links, and blog
display preferences.
"""

from pathlib import Path
from typing import Literal
from pydantic import Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """Application configuration loaded from environment variables.

    This class uses Pydantic settings to manage application configuration,
    automatically loading values from environment variables and a .env file.
    All field names are case-insensitive when loading from environment.

    Attributes
    ----------
    turnstile_site_key : str | None
        Site key for client-side Turnstile widget rendering.
        Get from: https://dash.cloudflare.com/
        If not set, uses dummy key based on turnstile_dummy_mode.
    turnstile_secret_key : str | None
        Secret key for server-side token verification.
        If not set, uses dummy key based on turnstile_dummy_mode.
    turnstile_enabled : bool
        Enable/disable Turnstile verification.
        Set to False for local development.
    turnstile_dummy_mode : str
        Dummy mode for testing (always_pass, always_fail, always_pass_invisible,
        always_fail_invisible, interactive). Used when no real keys are set.
    smtp_host : str
        SMTP server hostname for sending emails.
    smtp_port : int
        SMTP server port number (587 for STARTTLS).
    smtp_username : str | None
        Username for SMTP authentication.
        Typically your email address.
    smtp_password : str | None
        Password for SMTP authentication.
        Use app-specific password for Proton Mail.
    smtp_from_email : str | None
        Email address to use in the 'From' field.
    smtp_to_email : str | None
        Email address where contact form submissions are sent.
    link_plan_portal : str | None
        URL to the external planning portal.
    blog_show_author : bool
        Show author name on blog posts.
    blog_show_publication_date : bool
        Show publication date on blog posts.
    """

    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).parent.parent / ".env"),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    turnstile_site_key: str | None = Field(
        default=None,
        description="Site key for client-side Turnstile widget rendering. Get from: https://dash.cloudflare.com/",
    )
    turnstile_secret_key: str | None = Field(
        default=None,
        description="Secret key for server-side token verification. Keep secret!",
    )
    turnstile_enabled: bool = Field(
        default=False,
        description="Enable/disable Turnstile verification. Useful for local development.",
    )
    turnstile_dummy_mode: Literal[
        "always_pass",
        "always_fail",
        "always_pass_invisible",
        "always_fail_invisible",
        "interactive",
    ] = Field(
        default="always_pass",
        description="Dummy mode for testing when no real keys are set",
    )

    @model_validator(mode="after")
    def set_dummy_keys(self) -> "Config":
        """Set dummy keys based on dummy_mode if no real keys are provided."""
        site_key_map = {
            "always_pass": "1x00000000000000000000AA",
            "always_fail": "2x00000000000000000000AB",
            "always_pass_invisible": "1x00000000000000000000BB",
            "always_fail_invisible": "2x00000000000000000000BB",
            "interactive": "3x00000000000000000000FF",
        }

        secret_key_map = {
            "always_pass": "1x0000000000000000000000000000000AA",
            "always_fail": "2x0000000000000000000000000000000AB",
            "always_pass_invisible": "1x0000000000000000000000000000000BB",
            "always_fail_invisible": "2x0000000000000000000000000000000BB",
            "interactive": "3x0000000000000000000000000000000FF",
        }

        if (
            not self.turnstile_site_key
            or self.turnstile_site_key == "your_site_key_here"
        ):
            self.turnstile_site_key = site_key_map.get(
                self.turnstile_dummy_mode, "1x00000000000000000000AA"
            )

        if (
            not self.turnstile_secret_key
            or self.turnstile_secret_key == "your_secret_key_here"
        ):
            self.turnstile_secret_key = secret_key_map.get(
                self.turnstile_dummy_mode, "1x0000000000000000000000000000000AA"
            )

        return self

    smtp_host: str = Field(
        default="smtp.protonmail.ch",
        description="SMTP server hostname for sending emails",
    )
    smtp_port: int = Field(
        default=587,
        description="SMTP server port number (587 for STARTTLS)",
    )
    smtp_username: str | None = Field(
        default=None,
        description="Username for SMTP authentication (typically your email address)",
    )
    smtp_password: str | None = Field(
        default=None,
        description="Password for SMTP authentication (use app-specific password for Proton Mail)",
    )
    smtp_from_email: str | None = Field(
        default=None,
        description="Email address to use in the 'From' field",
    )
    smtp_to_email: str | None = Field(
        default=None,
        description="Email address where contact form submissions should be sent",
    )

    link_plan_portal: str | None = Field(
        default=None,
        description="URL to the planning portal",
    )

    blog_show_author: bool = Field(
        default=False,
        description="Show author name on blog posts",
    )
    blog_show_publication_date: bool = Field(
        default=False,
        description="Show publication date on blog posts",
    )

    site_url: str = Field(
        default="https://voorvoet.nl",
        description="Base URL of the website for Open Graph and canonical URLs",
    )


config = Config()
