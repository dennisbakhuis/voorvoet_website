"""Cloudflare Turnstile verification service.

This module provides server-side verification of Turnstile tokens
against Cloudflare's API to validate bot protection challenges.
"""

import logging
import httpx
from typing import Dict, Any

from ..config import config


logger = logging.getLogger(__name__)

TURNSTILE_VERIFY_URL = "https://challenges.cloudflare.com/turnstile/v0/siteverify"


async def verify_turnstile_token(token: str, remote_ip: str | None = None) -> bool:
    """
    Verify a Turnstile token with Cloudflare's API.

    Parameters
    ----------
    token : str
        The Turnstile response token from the client
    remote_ip : str | None
        Optional IP address of the user for additional validation

    Returns
    -------
    bool
        True if verification succeeds, False otherwise
    """
    if not config.turnstile_enabled:
        return True

    if not token:
        return False

    if not config.turnstile_secret_key:
        logger.warning("Turnstile is enabled but secret key is not configured")
        return False

    payload = {
        "secret": config.turnstile_secret_key,
        "response": token,
    }

    if remote_ip:
        payload["remoteip"] = remote_ip

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                TURNSTILE_VERIFY_URL,
                data=payload,
                timeout=10.0,
            )

            if response.status_code != 200:
                logger.warning(
                    "Turnstile verification failed with status %s",
                    response.status_code,
                )
                return False

            result: Dict[str, Any] = response.json()

            success = result.get("success", False)

            if not success:
                error_codes = result.get("error-codes", [])
                logger.warning("Turnstile verification failed: %s", error_codes)

            return bool(success)

    except httpx.TimeoutException:
        logger.warning("Turnstile verification timed out")
        return False
    except httpx.RequestError as e:
        logger.warning("Turnstile verification request error: %s", e)
        return False
    except Exception as e:
        logger.exception("Unexpected error during Turnstile verification: %s", e)
        return False
