from selenium.webdriver.common.by import By
from pages.basePage import BasePage


class HomePage(BasePage):
    login_successfully_label = (By.ID, "lblLoggedinSuccessfully")

    def __init__(self, driver):
        super().__init__(driver)



