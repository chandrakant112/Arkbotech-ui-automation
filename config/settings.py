import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "dev")

    # Base URL
    BASE_URL: str = os.getenv("BASE_URL", "https://gtrixdev.serversync.work")

    # Test Credentials
    TEST_USERNAME: str = os.getenv("TEST_USERNAME", "")
    TEST_PASSWORD: str = os.getenv("TEST_PASSWORD", "")

    # Browser Settings
    BROWSER: str = os.getenv("BROWSER", "chromium")
    HEADLESS: bool = os.getenv("HEADLESS", "true").lower() == "true"
    SLOW_MO: int = int(os.getenv("SLOW_MO", "0"))

    # Timeouts
    DEFAULT_TIMEOUT: int = int(os.getenv("DEFAULT_TIMEOUT", "30000"))


settings = Settings()