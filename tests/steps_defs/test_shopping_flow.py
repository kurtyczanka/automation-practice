import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver

scenarios('../features/shopping flow/shopping flow.feature')

DUCKDUCKGO_HOME = 'https://duckduckgo.com/'


# @pytest.fixture
# def browser():
#     # For this example, we will use Firefox
#     # You can change this fixture to use other browsers, too.
#     # A better practice would be to get browser choice from a config file.
#     b = webdriver.Chrome()
#     b.implicitly_wait(10)
#     yield b
#     b.quit()
#
#
# @given('the DuckDuckGo home page is displayed', target_fixture='ddg_home')
# def ddg_home(browser):
#     browser.get(DUCKDUCKGO_HOME)