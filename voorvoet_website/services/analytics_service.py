"""Server-side Umami analytics tracking service."""

import logging
from typing import Any

import httpx

from ..config import config


logger = logging.getLogger(__name__)

USER_AGENT = "VoorVoet-Website/1.0"


def _get_umami_base_url() -> str | None:
    """Derive Umami API base URL from the script URL."""
    if not config.umami_script_url:
        return None
    url = config.umami_script_url.rstrip("/")
    if url.endswith("/script.js"):
        return url[: -len("/script.js")]
    return url.rsplit("/", 1)[0] if "/" in url else url


def _get_hostname() -> str:
    """Extract hostname from site_url config."""
    return config.site_url.replace("https://", "").replace("http://", "").rstrip("/")


async def track_event(
    url: str,
    event_name: str | None = None,
    language: str | None = None,
    custom_data: dict[str, Any] | None = None,
) -> bool:
    """
    Send a tracking event to Umami.

    Parameters
    ----------
    url : str
        Page URL path (e.g., "/nl/contact")
    event_name : str | None
        Custom event name. If None, records a page view.
    language : str | None
        Language code (e.g., "nl")
    custom_data : dict | None
        Additional event data

    Returns
    -------
    bool
        True if event was sent successfully
    """
    base_url = _get_umami_base_url()
    if not base_url or not config.umami_website_id:
        return False

    payload: dict[str, Any] = {
        "website": config.umami_website_id,
        "url": url,
        "hostname": _get_hostname(),
    }

    if event_name:
        payload["name"] = event_name
    if language:
        payload["language"] = language
    if custom_data:
        payload["data"] = custom_data

    body = {
        "type": "event",
        "payload": payload,
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{base_url}/api/send",
                json=body,
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": USER_AGENT,
                },
                timeout=5.0,
            )

            if response.status_code not in (200, 201, 204):
                logger.warning(
                    "Umami tracking returned status %s", response.status_code
                )
                return False

            return True

    except httpx.TimeoutException:
        logger.warning("Umami tracking request timed out")
        return False
    except httpx.RequestError as e:
        logger.warning("Umami tracking request error: %s", e)
        return False
    except Exception as e:
        logger.exception("Unexpected error during Umami tracking: %s", e)
        return False
