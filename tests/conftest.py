"""Pytest configuration and fixtures for the VoorVoet website tests."""

import os
from pathlib import Path
from typing import Generator

import pytest
from reflex.testing import AppHarness, AppHarnessProd


USE_PROD_MODE = os.environ.get("REFLEX_TEST_MODE", "dev") == "prod"


@pytest.fixture(scope="session")
def app_root() -> Path:
    """
    Get the root directory of the Reflex app.

    Returns
    -------
    Path
        Path to the project root directory.
    """
    return Path(__file__).parent.parent


@pytest.fixture(scope="session")
def reflex_app(app_root: Path) -> Generator[AppHarness, None, None]:
    """
    Start the Reflex server for the entire test session.

    This fixture starts the server once and keeps it running for all tests.
    Use this for better performance when you don't need isolation between tests.

    Parameters
    ----------
    app_root : Path
        Root directory of the Reflex app.

    Yields
    ------
    AppHarness
        Running Reflex app harness with frontend and backend servers.
    """
    if USE_PROD_MODE:
        harness = AppHarnessProd.create(root=app_root)
    else:
        harness = AppHarness.create(root=app_root)

    with harness:
        print(f"\n✓ Reflex server started at: {harness.frontend_url}")
        yield harness
    print("\n✓ Reflex server stopped")


@pytest.fixture(scope="session")
def server_url(reflex_app: AppHarness) -> str:
    """
    Get the base URL of the running Reflex server.

    Parameters
    ----------
    reflex_app : AppHarness
        Running Reflex app harness.

    Returns
    -------
    str
        Base URL of the frontend server (e.g., 'http://localhost:3000').
    """
    if reflex_app.frontend_url is None:
        raise RuntimeError("Frontend URL is not available")
    return reflex_app.frontend_url


@pytest.fixture(scope="function")
def isolated_reflex_app(app_root: Path) -> Generator[AppHarness, None, None]:
    """
    Start a fresh Reflex server for each test function.

    Use this fixture when you need test isolation and don't want tests
    to affect each other. Note: This is slower than using the session-scoped
    reflex_app fixture.

    Parameters
    ----------
    app_root : Path
        Root directory of the Reflex app.

    Yields
    ------
    AppHarness
        Running Reflex app harness with frontend and backend servers.
    """
    if USE_PROD_MODE:
        harness = AppHarnessProd.create(root=app_root)
    else:
        harness = AppHarness.create(root=app_root)

    with harness:
        yield harness
