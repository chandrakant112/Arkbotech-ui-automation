import pytest
from playwright.sync_api import sync_playwright
from config.settings import settings
from config.browser_config import get_browser_launch_options, get_context_options, get_browser_type


@pytest.fixture(scope="session")
def browser_instance():
    with sync_playwright() as playwright:
        browser_type = getattr(playwright, get_browser_type())
        browser = browser_type.launch(**get_browser_launch_options())
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser_instance):
    context = browser_instance.new_context(**get_context_options())
    context.set_default_timeout(settings.DEFAULT_TIMEOUT)
    page = context.new_page()
    yield page
    context.close()