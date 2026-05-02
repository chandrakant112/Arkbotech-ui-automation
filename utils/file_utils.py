import os
import shutil
from utils.logger import get_logger

logger = get_logger(__name__)


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)
    logger.info(f"Directory ensured: {path}")


def clean_dir(path: str) -> None:
    if os.path.exists(path):
        shutil.rmtree(path)
        os.makedirs(path)
        logger.info(f"Directory cleaned: {path}")