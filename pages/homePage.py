from selenium.webdriver.common.by import By
from pages.basePage import BasePage


class HomePage(BasePage):
    link_logout = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        super().__init__(driver)

    def do_logout(self):
        self.do_click(10, self.link_logout)
