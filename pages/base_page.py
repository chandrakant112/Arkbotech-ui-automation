from playwright.sync_api import Page, expect
from config.settings import settings
from utils.logger import get_logger

logger = get_logger(__name__)


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = settings.BASE_URL
        self.timeout = settings.DEFAULT_TIMEOUT

    def navigate(self, path: str = "") -> None:
        url = f"{self.base_url}/{path}".rstrip("/")
        self.page.goto(url)
        logger.info(f"Navigated to: {url}")

    def get_title(self) -> str:
        return self.page.title()

    def wait_for_page_load(self) -> None:
        self.page.wait_for_load_state("networkidle")

    def take_screenshot(self, name: str) -> None:
        path = f"reports/screenshots/{name}.png"
        self.page.screenshot(path=path)
        logger.info(f"Screenshot saved: {path}")