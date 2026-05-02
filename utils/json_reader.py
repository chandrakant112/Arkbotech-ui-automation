import json
import os
from utils.logger import get_logger

logger = get_logger(__name__)


def read_json(file_path: str) -> dict:
    abs_path = os.path.join(os.path.dirname(__file__), "..", file_path)
    abs_path = os.path.normpath(abs_path)
    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"JSON file not found: {abs_path}")
    with open(abs_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    logger.info(f"Loaded JSON: {abs_path}")
    return data