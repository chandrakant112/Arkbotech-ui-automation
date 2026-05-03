
from playwright.sync_api import Page


class LoginLocators:
    def __init__(self, page: Page):
        self.email_input = page.get_by_role("textbox", name="Email Address")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.sign_in_button = page.get_by_role("button", name="Sign in")
        self.forgot_password_button = page.get_by_role("button", name="Forgot password?")
        self.password_toggle = page.locator(".tw-absolute.tw-right-4")
        self.magic_link_button = page.get_by_text("Sign in with Magic Link")
        self.error_message = page.get_by_text("Invalid user name or password")
        self.back_to_login = page.get_by_text("← Back to Login")