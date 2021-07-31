import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from tests.test_base import BaseTest
from utilities.readProperties import ReadConfig


class Test_Login(BaseTest):

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    @pytest.mark.testrail(13)
    @pytest.mark.dependency(name="login")
    def test_login(self):
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.do_login(self.username, self.password)
        act_title = self.driver.title
        assert act_title == "Dashboard / nopCommerce administration"

    @pytest.mark.testrail(14)
    @pytest.mark.dependency(depends=["login"])
    def test_logout(self):
        self.hp = HomePage(self.driver)
        self.hp.do_logout()

        act_title = self.driver.title
        assert act_title == "Your store. Login"
