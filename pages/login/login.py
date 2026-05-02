import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from locators.login.loginlocator import LoginLocators
from utils.logger import get_logger

logger = get_logger(__name__)


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        locators = LoginLocators(page)
        self.email_input = locators.email_input
        self.password_input = locators.password_input
        self.sign_in_button = locators.sign_in_button
        self.forgot_password_button = locators.forgot_password_button
        self.password_toggle = locators.password_toggle
        self.magic_link_button = locators.magic_link_button
        self.error_message = locators.error_message
        self.back_to_login = locators.back_to_login

    def go_to_login(self):
        self.navigate("login")

    def login(self, email: str, password: str):
        self.go_to_login()
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.sign_in_button.click()

    def click_forgot_password(self):
        self.forgot_password_button.click()

    def click_magic_link(self):
        self.magic_link_button.click()

    def toggle_password_visibility(self):
        self.password_toggle.click()

    def assert_login_successful(self):
        expect(self.page).to_have_url(re.compile("self/dashboard"))

    def assert_error_message_visible(self):
        expect(self.error_message).to_be_visible()

    def assert_sign_in_button_disabled(self):
        expect(self.sign_in_button).to_be_disabled()

    def assert_forgot_password_page(self):
        expect(self.page).to_have_url(re.compile("password/reset"))

    def assert_magic_link_page(self):
        expect(self.page).to_have_url(re.compile("magic-link"))

    def assert_password_is_hidden(self):
        expect(self.password_input).to_have_attribute("type", "password")

    def assert_password_is_visible(self):
        expect(self.password_input).to_have_attribute("type", "text")

    def assert_no_server_error(self):
        expect(self.page).not_to_have_url(re.compile("error|500|internal"))