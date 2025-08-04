import pytest
import base64
import os 
import pytest_html
from datetime import datetime
from pathlib import Path
from pytest_metadata.plugin import metadata_key 
from playwright.sync_api import sync_playwright, expect

@pytest.fixture(scope="session")
def playwright_instance():
    """Initialize Playwright once for the entire test session."""
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance):
    """Launch the browser."""
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
    """Create a fresh page for each test."""
    page = browser.new_page(ignore_https_errors=True)
    yield page
    page.close()

def pytest_configure(config):
    config.option.htmlpath = "report.html"

# @pytest.fixture
# def expect():
#     return lambda expr: assert expr