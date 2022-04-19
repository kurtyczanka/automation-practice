from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AccountPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

        self.TEXT__WELCOME = By.CSS_SELECTOR, "p.info-account"

        self.LIST__ADDRESSES = By.CSS_SELECTOR, "div.addresses-lists"

        self.HEADER = By.CSS_SELECTOR, "h1.page-heading"

        self.FOOTER = By.CSS_SELECTOR, "ul.footer_links"

    @property
    def text__welcome(self):
        return self.locate_element(10, self.TEXT__WELCOME, error_msg="Welcome text is not displayed")

    @property
    def list__addresses(self):
        return self.locate_element(10, self.LIST__ADDRESSES, error_msg="List of addresses not found")

    @property
    def header(self):
        return self.locate_element(10, self.HEADER, error_msg="Header not found")

    @property
    def footer(self):
        return self.locate_element(10, self.FOOTER, error_msg="Footer not found")

    def is_loaded(self):
        assert self.text__welcome
        assert self.list__addresses
        assert self.header
        assert self.footer
