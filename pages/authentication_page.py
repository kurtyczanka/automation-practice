from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AuthenticationPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

        self.AUTHENTICATION__PAGE = By.ID, "authentication"

        self.INPUT__CREATE_EMAIL = By.ID, "email_create"

        self.INPUT__REGISTERED_EMAIL = By.ID, "email"

        self.INPUT__REGISTERED_PASSWORD = By.ID, "passwd"

        self.BUTTON__SIGN_IN = By.CSS_SELECTOR, "button#SubmitLogin"

    @property
    def authentication__page(self):
        return self.locate_element(10, self.AUTHENTICATION__PAGE, error_msg="Authentication page not found")

    @property
    def input__create_email(self):
        return self.locate_element(10, self.INPUT__CREATE_EMAIL, error_msg="Input create email not found")

    @property
    def input__registered_email(self):
        return self.locate_element(10, self.INPUT__REGISTERED_EMAIL, error_msg="Input registered email not found")

    @property
    def input__registered_password(self):
        return self.locate_element(10, self.INPUT__REGISTERED_PASSWORD, error_msg="Input registered password not found")

    @property
    def button__sign_in(self):
        return self.locate_element(10, self.BUTTON__SIGN_IN, error_msg="Button sign in not found")

    def is_loaded(self):
        assert self.authentication__page
        assert self.input__create_email
        assert self.input__registered_email
        assert self.input__registered_password

    def login(self, email, password):
        self.send_text(self.input__registered_email, email)
        self.send_text(self.input__registered_password, password)
        self.scroll_and_click_element(self.button__sign_in)
