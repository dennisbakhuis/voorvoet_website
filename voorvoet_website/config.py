from typing import Optional
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """Application configuration loaded from environment variables"""

    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).parent.parent / ".env"),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Cloudflare Turnstile settings
    turnstile_site_key: str = Field(
        default="YOUR_SITE_KEY_HERE",
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

    # SMTP settings
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

    # External links
    link_plan_portal: Optional[str] = Field(
        default=None,
        description="URL to the planning portal",
    )

    # Blog settings
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


# Singleton instance
config = Config()
