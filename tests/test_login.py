import pytest
from pages.basePage import BasePage
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from tests.test_base import BaseTest
from config.config import baseURL, useremail, password


class Test_Login(BaseTest):

    @pytest.mark.dependency(name="login")
    def test_login_email_not_exist(self):
        self.driver.get(baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.do_login("", password)
        self.bp = BasePage(self.driver)

        is_err_visible = self.bp.is_invisible(10, self.lp.password_error_label)
        assert is_err_visible

    @pytest.mark.dependency(depends=["login"])
    def test_logout(self):
        self.driver.get(baseURL)
        self.lp.do_login(useremail, password)
        self.hp = HomePage(self.driver)

        is_success_mgs_visible = self.bp.is_invisible(10, self.hp.login_successfully_label)
        assert is_success_mgs_visible
