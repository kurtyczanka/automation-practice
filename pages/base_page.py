from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def locate_element(self,
                       timeout,
                       element,
                       error_msg="Element not found"):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(element), error_msg
        )

    @staticmethod
    def send_text(element, text):
        element.send_keys(text)

    def scroll_and_click_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
