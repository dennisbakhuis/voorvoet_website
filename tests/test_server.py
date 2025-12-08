"""Basic server tests to verify the Reflex app starts correctly."""

import requests
from reflex.testing import AppHarness


def test_server_is_running(reflex_app: AppHarness) -> None:
    """
    Test that the Reflex server starts and is accessible.

    Parameters
    ----------
    reflex_app : AppHarness
        Running Reflex app harness.
    """
    assert reflex_app.frontend_url is not None
    assert reflex_app.backend is not None
    assert reflex_app.backend.started


def test_frontend_responds(server_url: str) -> None:
    """
    Test that the frontend server responds to HTTP requests.

    Parameters
    ----------
    server_url : str
        Base URL of the frontend server.
    """
    response = requests.get(server_url, timeout=10)
    assert response.status_code == 200
