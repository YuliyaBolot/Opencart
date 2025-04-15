import pytest
import logging
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver import FirefoxOptions, ChromeOptions, EdgeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--remote", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.0.192")
    parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--maximize", action="store_true")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")
    remote = request.config.getoption("--remote")
    executor = request.config.getoption("--executor")
    vnc = (request.config.getoption("--vnc"))
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    maximize = request.config.getoption("--maximize")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    executor_url = f"http://{executor}:4444/wd/hub"

    options = ChromeOptions()

    if remote:
        caps = {
            "browserName": browser,
            "browserVersion": "127.0",
            "selenoid:options": {
                "enableVNC": vnc
            }
        }
        for k, v in caps.items():
            options.set_capability(k, v)

        driver = webdriver.Remote(command_executor=executor_url, options=options)
    else:
        if browser == "chrome":
            driver = webdriver.Chrome(service=ChromiumService(), options=ChromeOptions())
        elif browser == "firefox":
            driver = webdriver.Firefox(service=FirefoxService(), options=FirefoxOptions())
        elif browser == "edge":
            driver = webdriver.Edge(options=EdgeOptions())
        else:
            raise ValueError("Browser name must be either 'chrome', 'firefox' or 'edge'")

    driver.get(url)
    driver.url = url
    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    if maximize:
        driver.maximize_window()

    yield driver

    if request.node.status == "failed":
        allure.attach(
            name="failure_screenshot",
            body=driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG
        )

    driver.quit()
