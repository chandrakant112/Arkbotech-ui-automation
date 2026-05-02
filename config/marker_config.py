# This file documents all custom pytest markers used in this framework.
# All markers are registered in pytest.ini to avoid warnings.

MARKERS = {
    "smoke": "Critical tests that must always pass",
    "regression": "Full regression suite",
    "functional": "Functional UI tests",
    "integration": "Integration tests combining UI and API",
    "security": "Security and authorization tests",
    "api": "API only tests",
    "database": "Database validation tests",
}