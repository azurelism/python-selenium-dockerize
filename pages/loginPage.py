from selenium.webdriver.common.by import By
from pages.basePage import BasePage


class LoginPage(BasePage):
    # Login Page
    textbox_username_id = (By.ID, "txtEmail ")
    textbox_password_id = (By.ID, "txtPassword ")
    button_login_id = (By.XPATH, "btnLogin")

    password_error_label = (By.ID, "lblPasswordErr")


    def __init__(self, driver):
        super().__init__(driver)

    def do_login(self, username, password):
        self.do_send_keys(20, self.textbox_username_id, username)
        self.do_send_keys(10, self.textbox_password_id, password)
        self.do_click(10, self.button_login_id)