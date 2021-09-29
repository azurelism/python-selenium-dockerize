# -*- coding: utf-8 -*-
import os
import time
import pytest
from selenium import webdriver

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
            caps = {'browserName': 'chrome'}
            driver = webdriver.Remote(
                command_executor='http://chrome:4444/wd/hub',
                desired_capabilities=caps)
        else:
            caps = {'browserName': 'chrome'}
            driver = webdriver.Remote(
                command_executor='http://chrome:4444/wd/hub',
                desired_capabilities=caps)
        driver.implicitly_wait(5)
        driver.maximize_window()
        request.cls.driver = driver
        yield driver
        driver.close()
        driver.quit()
        driver = None

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """Capture screenshot on test case failure pytest-HTML Report"""
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
            screenshot = "screenshots" + os.sep + timestamp + '.png'
            driver.get_screenshot_as_file(screenshot)
            if screenshot:
                html = '<div><img src="../%s" alt="screenshot" style="width:480px;height:222px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screenshot
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
