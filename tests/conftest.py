# -*- coding: utf-8 -*-
import pytest

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import ChromeType
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = None

def pytest_addoption(parser):
    """ Add custom parameters to cmd line"""
    parser.addoption("--browser", action="store", default="chrome",
                     help="Type in browser name e.g. chrome:  ")


@pytest.fixture(scope="class")
def init_driver(request):
    browser = request.config.getoption("--browser")
    global driver
    if driver is None:
        if browser == "chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browser == "chromium":
            driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        elif browser == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser == "edge":
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        else:
            driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(3)
        driver.maximize_window()
        request.cls.driver = driver
        yield driver
        driver.close()
        driver.quit()
        driver = None