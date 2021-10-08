import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from tests.test_base import BaseTest
from config.config import baseURL, useremail, password


class Test_Login(BaseTest):

    @pytest.mark.dependency(name="login")
    def test_login(self):
        self.driver.get(baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.do_login(useremail, password)
        act_title = self.driver.title
        assert act_title == "Dashboard / nopCommerce administration"

    @pytest.mark.dependency(depends=["login"])
    def test_logout(self):
        self.hp = HomePage(self.driver)
        self.hp.do_logout()

        act_title = self.driver.title
        assert act_title == "Your store."
