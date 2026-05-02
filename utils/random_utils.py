import random
import string
import uuid


def random_string(length: int = 8) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=length))


def random_email() -> str:
    return f"test_{random_string(6)}@arkbotech.com"


def random_uuid() -> str:
    return str(uuid.uuid4())