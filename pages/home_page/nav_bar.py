from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class NavBar(BasePage):
    def __init__(self, context):
        super().__init__(context)

        self.BUTTON__SING_IN = By.CSS_SELECTOR, "a.login"

        self.LABEL__USER_NAME = By.CSS_SELECTOR, "a.account span"

    @property
    def button__sign_in(self):
        return self.locate_element(10, self.BUTTON__SING_IN, error_msg="Button 'sing in' not found")

    @property
    def label__user_name(self):
        return self.locate_element(10, self.LABEL__USER_NAME, error_msg="Label 'user name' not found")
