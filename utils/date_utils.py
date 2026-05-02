from datetime import datetime, timedelta


def today() -> str:
    return datetime.today().strftime("%Y-%m-%d")


def future_date(days: int = 7) -> str:
    return (datetime.today() + timedelta(days=days)).strftime("%Y-%m-%d")


def past_date(days: int = 7) -> str:
    return (datetime.today() - timedelta(days=days)).strftime("%Y-%m-%d")