import pytest
from time import sleep
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver

from pages.account_page import AccountPage
from pages.authentication_page import AuthenticationPage
from pages.home_page.nav_bar import NavBar

scenarios('../features/login/login.feature')

DUCKDUCKGO_HOME = 'https://automationpractice.com/index.php'


@pytest.fixture
def browser():
    # For this example, we will use Firefox
    # You can change this fixture to use other browsers, too.
    # A better practice would be to get browser choice from a config file.
    b = webdriver.Chrome()
    b.maximize_window()
    b.implicitly_wait(10)
    yield b
    b.quit()


@given('the automation practice page is displayed', target_fixture='ddg_home')
def ddg_home(browser):
    browser.get(DUCKDUCKGO_HOME)


@when("I click on 'Sing in' button")
def step_impl(browser):
    page = NavBar(browser)
    page.button__sign_in.click()


@when(parsers.parse("I log in as '{user}'"))
def step_impl(browser, user):
    page = AuthenticationPage(browser)
    page.is_loaded()
    if user == 'User1':
        page.login(email='aaa121@aaa.pl', password='aaa111')
    else:
        raise Exception("User not found. Test refactoring is needed")


@then(parsers.parse("User name: '{user_name}' is displayed in navigation bar"))
def step_impl(browser, user_name):
    page = NavBar(browser)
    assert page.label__user_name.text == user_name, "User name in navigation bar is different than expected."


@then("My account page is displayed")
def step_impl(browser):
    page = AccountPage(browser)
    page.is_loaded()
