import re
import pytest
from playwright.sync_api import Page, expect
from pages.login.login import LoginPage
from utils.json_reader import read_json

data = read_json("test_data/login/login_data.json")
messages = read_json("test_data/login/login_messages.json")
invalid = data["invalid_combinations"]


# ── Valid Login ────────────────────────────────────────────────

@pytest.mark.smoke
@pytest.mark.functional
def test_valid_login(page: Page):
    login = LoginPage(page)
    login.login(
        data["valid_user"]["email"],
        data["valid_user"]["password"]
    )
    login.assert_login_successful()


# ── Invalid Combinations ───────────────────────────────────────

@pytest.mark.functional
def test_wrong_email_wrong_password(page: Page):
    login = LoginPage(page)
    login.login(
        invalid["wrong_email_wrong_password"]["email"],
        invalid["wrong_email_wrong_password"]["password"]
    )
    login.assert_error_message_visible()


@pytest.mark.functional
def test_wrong_email_correct_password(page: Page):
    login = LoginPage(page)
    login.login(
        invalid["wrong_email_correct_password"]["email"],
        invalid["wrong_email_correct_password"]["password"]
    )
    login.assert_error_message_visible()


@pytest.mark.functional
def test_correct_email_wrong_password(page: Page):
    login = LoginPage(page)
    login.login(
        invalid["correct_email_wrong_password"]["email"],
        invalid["correct_email_wrong_password"]["password"]
    )
    login.assert_error_message_visible()


# ── Empty Fields ───────────────────────────────────────────────

@pytest.mark.functional
def test_empty_email_empty_password(page: Page):
    login = LoginPage(page)
    login.go_to_login()
    login.assert_sign_in_button_disabled()


@pytest.mark.functional
def test_empty_email_correct_password(page: Page):
    login = LoginPage(page)
    login.go_to_login()
    login.password_input.fill(data["valid_user"]["password"])
    login.assert_sign_in_button_disabled()


@pytest.mark.functional
def test_correct_email_empty_password(page: Page):
    login = LoginPage(page)
    login.go_to_login()
    login.email_input.fill(data["valid_user"]["email"])
    login.assert_sign_in_button_disabled()


# ── Spaces ─────────────────────────────────────────────────────

@pytest.mark.functional
def test_spaces_only_email(page: Page):
    login = LoginPage(page)
    login.go_to_login()
    login.email_input.fill(invalid["spaces_only_email"]["email"])
    login.password_input.fill(invalid["spaces_only_email"]["password"])
    login.assert_sign_in_button_disabled()


@pytest.mark.functional
def test_spaces_only_password(page: Page):
    login = LoginPage(page)
    login.go_to_login()
    login.email_input.fill(data["valid_user"]["email"])
    login.password_input.fill(invalid["spaces_only_password"]["password"])
    login.assert_sign_in_button_disabled()


# ── Security ───────────────────────────────────────────────────

@pytest.mark.security
def test_sql_injection_email(page: Page):
    login = LoginPage(page)
    login.login(
        invalid["sql_injection_email"]["email"],
        invalid["sql_injection_email"]["password"]
    )
    login.assert_no_server_error()
    login.assert_error_message_visible()


@pytest.mark.security
def test_sql_injection_password(page: Page):
    login = LoginPage(page)
    login.login(
        invalid["sql_injection_password"]["email"],
        invalid["sql_injection_password"]["password"]
    )
    login.assert_error_message_visible()


# ── Special Characters ─────────────────────────────────────────

@pytest.mark.functional
def test_special_characters_email(page: Page):
    login = LoginPage(page)
    login.login(
        invalid["special_characters_email"]["email"],
        invalid["special_characters_email"]["password"]
    )
    login.assert_error_message_visible()


@pytest.mark.functional
def test_special_characters_password(page: Page):
    login = LoginPage(page)
    login.login(
        invalid["special_characters_password"]["email"],
        invalid["special_characters_password"]["password"]
    )
    login.assert_error_message_visible()


# ── Long Inputs ────────────────────────────────────────────────

@pytest.mark.functional
def test_very_long_email(page: Page):
    login = LoginPage(page)
    login.login(
        invalid["very_long_email"]["email"],
        invalid["very_long_email"]["password"]
    )
    login.assert_error_message_visible()


@pytest.mark.functional
def test_very_long_password(page: Page):
    login = LoginPage(page)
    login.login(
        invalid["very_long_password"]["email"],
        invalid["very_long_password"]["password"]
    )
    login.assert_error_message_visible()


# ── Case Sensitivity ───────────────────────────────────────────

case = data["case_insensitive"]

@pytest.mark.functional
def test_uppercase_email_is_case_insensitive(page: Page):
    login = LoginPage(page)
    login.login(
        case["uppercase_email"]["email"],
        case["uppercase_email"]["password"]
    )
    login.assert_login_successful()


@pytest.mark.functional
def test_email_with_spaces(page: Page):
    login = LoginPage(page)
    login.login(
        invalid["email_with_spaces"]["email"],
        invalid["email_with_spaces"]["password"]
    )
    login.assert_error_message_visible()


# ── Numeric Inputs ─────────────────────────────────────────────

@pytest.mark.functional
def test_numeric_only_email(page: Page):
    login = LoginPage(page)
    login.login(
        invalid["numeric_only_email"]["email"],
        invalid["numeric_only_email"]["password"]
    )
    login.assert_error_message_visible()


@pytest.mark.functional
def test_numeric_only_password(page: Page):
    login = LoginPage(page)
    login.go_to_login()
    login.email_input.fill(invalid["numeric_only_password"]["email"])
    login.password_input.fill(invalid["numeric_only_password"]["password"])
    login.assert_sign_in_button_disabled()


# ── Password Toggle ────────────────────────────────────────────

@pytest.mark.functional
def test_password_hidden_by_default(page: Page):
    login = LoginPage(page)
    login.go_to_login()
    login.password_input.fill("testpassword")
    login.assert_password_is_hidden()


@pytest.mark.functional
def test_password_visible_after_toggle(page: Page):
    login = LoginPage(page)
    login.go_to_login()
    login.password_input.fill("testpassword")
    login.toggle_password_visibility()
    login.assert_password_is_visible()


@pytest.mark.functional
def test_password_hidden_after_double_toggle(page: Page):
    login = LoginPage(page)
    login.go_to_login()
    login.password_input.fill("testpassword")
    login.toggle_password_visibility()
    login.toggle_password_visibility()
    login.assert_password_is_hidden()


# ── Navigation ─────────────────────────────────────────────────

@pytest.mark.functional
def test_forgot_password_navigates(page: Page):
    login = LoginPage(page)
    login.go_to_login()
    login.click_forgot_password()
    login.assert_forgot_password_page()


@pytest.mark.functional
def test_magic_link_navigates(page: Page):
    login = LoginPage(page)
    login.go_to_login()
    login.click_magic_link()
    login.assert_magic_link_page()