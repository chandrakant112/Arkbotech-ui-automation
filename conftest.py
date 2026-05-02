import pytest
from playwright.sync_api import sync_playwright
from config.settings import settings
from config.browser_config import (
    get_browser_launch_options,
    get_context_options,
    get_browser_type
)


@pytest.fixture(scope="session")
def browser_instance():
    with sync_playwright() as playwright:
        browser_type = getattr(playwright, get_browser_type())
        browser = browser_type.launch(**get_browser_launch_options())
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context(browser_instance):
    ctx = browser_instance.new_context(**get_context_options())
    ctx.set_default_timeout(settings.DEFAULT_TIMEOUT)
    yield ctx
    ctx.clear_cookies()
    ctx.close()


@pytest.fixture(scope="function")
def page(context, request):
    page = context.new_page()
    yield page
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        page.screenshot(
            path=f"reports/screenshots/{request.node.name}.png"
        )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)