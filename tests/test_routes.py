"""Tests for routes within the project."""

import pytest
import requests

from voorvoet_website.translations import ROUTE_MAPPINGS


def test_home_page_accessible(server_url: str):
    """
    Test that the Dutch home page is accessible.

    Parameters
    ----------
    server_url : str
        Base URL of the frontend server.
    """
    response = requests.get(f"{server_url}/nl", timeout=10)
    assert response.status_code == 200


def test_multiple_language_routes(server_url: str):
    """
    Test that all language variants of the home page are accessible.

    Parameters
    ----------
    server_url : str
        Base URL of the frontend server.
    """
    languages = ["nl", "en", "de"]
    for lang in languages:
        home_route = ROUTE_MAPPINGS[lang]["home"]
        response = requests.get(f"{server_url}{home_route}", timeout=10)
        assert response.status_code == 200, f"Language {lang} home page failed"


@pytest.mark.slow
def test_all_main_routes_accessible(server_url: str):
    """
    Test that all main routes are accessible across all languages.

    This test dynamically uses the ROUTE_MAPPINGS from translations.py
    to ensure tests stay in sync with application routes.

    Parameters
    ----------
    server_url : str
        Base URL of the frontend server.
    """
    for lang in ROUTE_MAPPINGS:
        for page_key, route in ROUTE_MAPPINGS[lang].items():
            response = requests.get(f"{server_url}{route}", timeout=10)
            assert (
                response.status_code == 200
            ), f"Route {route} ({lang}/{page_key}) failed"
