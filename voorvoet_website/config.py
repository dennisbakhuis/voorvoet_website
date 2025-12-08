"""Configuration management for the VoorVoet website application.

This module defines the application configuration using Pydantic settings,
loading values from environment variables and .env file. Configuration includes
Cloudflare Turnstile settings, SMTP email settings, external links, and blog
display preferences.
"""

from typing import Optional
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """Application configuration loaded from environment variables.

    This class uses Pydantic settings to manage application configuration,
    automatically loading values from environment variables and a .env file.
    All field names are case-insensitive when loading from environment.

    Attributes
    ----------
    turnstile_site_key : str
        Site key for client-side Turnstile widget rendering.
        Get from: https://dash.cloudflare.com/
    turnstile_secret_key : Optional[str]
        Secret key for server-side token verification.
        Required for production use.
    turnstile_enabled : bool
        Enable/disable Turnstile verification.
        Set to False for local development.
    smtp_host : str
        SMTP server hostname for sending emails.
    smtp_port : int
        SMTP server port number (587 for STARTTLS).
    smtp_username : Optional[str]
        Username for SMTP authentication.
        Typically your email address.
    smtp_password : Optional[str]
        Password for SMTP authentication.
        Use app-specific password for Proton Mail.
    smtp_from_email : Optional[str]
        Email address to use in the 'From' field.
    smtp_to_email : Optional[str]
        Email address where contact form submissions are sent.
    link_plan_portal : Optional[str]
        URL to the external planning portal.
    blog_show_author : bool
        Show author name on blog posts.
    blog_show_publication_date : bool
        Show publication date on blog posts.
    blog_show_reading_time : bool
        Show estimated reading time on blog posts.
    """

    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).parent.parent / ".env"),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    turnstile_site_key: Optional[str] = Field(
        default=None,
        description="Site key for client-side Turnstile widget rendering. Get from: https://dash.cloudflare.com/",
    )
    turnstile_secret_key: Optional[str] = Field(
        default=None,
        description="Secret key for server-side token verification. Keep secret!",
    )
    turnstile_enabled: bool = Field(
        default=True,
        description="Enable/disable Turnstile verification. Useful for local development.",
    )

    smtp_host: str = Field(
        default="smtp.protonmail.ch",
        description="SMTP server hostname for sending emails",
    )
    smtp_port: int = Field(
        default=587,
        description="SMTP server port number (587 for STARTTLS)",
    )
    smtp_username: Optional[str] = Field(
        default=None,
        description="Username for SMTP authentication (typically your email address)",
    )
    smtp_password: Optional[str] = Field(
        default=None,
        description="Password for SMTP authentication (use app-specific password for Proton Mail)",
    )
    smtp_from_email: Optional[str] = Field(
        default=None,
        description="Email address to use in the 'From' field",
    )
    smtp_to_email: Optional[str] = Field(
        default=None,
        description="Email address where contact form submissions should be sent",
    )

    link_plan_portal: Optional[str] = Field(
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
    blog_show_reading_time: bool = Field(
        default=False,
        description="Show estimated reading time on blog posts",
    )

    site_url: str = Field(
        default="https://voorvoet.nl",
        description="Base URL of the website for Open Graph and canonical URLs",
    )


config = Config()
