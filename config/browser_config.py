from config.settings import settings


def get_browser_launch_options() -> dict:
    return {
        "headless": settings.HEADLESS,
        "slow_mo": settings.SLOW_MO,
    }


def get_context_options() -> dict:
    return {
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": True,
    }

def get_browser_type() -> str:
    return settings.BROWSER.lower()