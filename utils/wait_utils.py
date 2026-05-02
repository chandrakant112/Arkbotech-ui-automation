from playwright.sync_api import Page
from utils.logger import get_logger

logger = get_logger(__name__)


def wait_for_url_contains(page: Page, text: str, timeout: int = 30000) -> None:
    page.wait_for_url(f"**{text}**", timeout=timeout)
    logger.info(f"URL contains: {text}")


def wait_for_network_idle(page: Page, timeout: int = 30000) -> None:
    page.wait_for_load_state("networkidle", timeout=timeout)
    logger.info("Network is idle")