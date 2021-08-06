# -*- coding: utf-8 -*-
import pytest
import time
import os

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import ChromeType
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.options import Options as FOptions

from tests.testrail_plugins import TestRailPlugin

driver = None

def pytest_addoption(parser):
    """ Add custom parameters to cmd line"""
    parser.addoption("--browser", action="store", default="chrome",
                     help="Type in browser name e.g. chrome:  ")
    parser.addoption('--ids', action='store', metavar='id1,id2,id3...',
                     help='only run tests with the specified IDs')
    parser.addoption('--publish', action='store_true', default=False,
                     help='If set, create a new test run and publish results')
    parser.addoption('--include_all', action='store_true', default=False,
                     help='Used with --publish. If set, the test run will\
                     contain all test cases.')
    parser.addoption('--tr_name', action='store', metavar='<run name>',
                     help='Used with --publish to configure run name.')
    parser.addoption('--tr_id', action='store', metavar='run_id',
                     help='If set, run tests in the test run and publish')
					 
def pytest_configure(config):
    """ Configure marker"""
    config.addinivalue_line('markers',
                            'testrail(id): mark test with the case id')
    if config.getoption('--publish') or config.getoption('--tr_id'):
        config.pluginmanager.register(
            TestRailPlugin(
                config.getoption('--tr_id'),
                config.getoption('--include_all'),
                config.getoption('--tr_name')))
				
def pytest_runtest_setup(item):
    """ This handle test case skipping when plugin is not available"""
    ids = item.config.getoption('--ids')
    if not ids:
        return
    ids = set([int(x) for x in ids.split(',')])
    idmarker = item.get_closest_marker('testrail')
    if idmarker is None:
        pytest.skip('skip')
    else:
        tid = idmarker.args[0]
        if tid not in ids:
            pytest.skip('skip')

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
            firefox_options = FOptions()
            firefox_options.add_argument("--headless")
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)
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