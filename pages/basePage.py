from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, time, by_locator):
        element = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(by_locator))
        element.click()

    def do_send_keys(self, time, by_locator, text):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)

    def do_send_file(self, time, by_locator, file):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(by_locator))
        element.send_keys(file)

    def is_invisible(self, time, by_locator):
        element = WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(by_locator))
        return bool(element)