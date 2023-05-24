from datetime import datetime

import allure
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--bversion", action="store", default="113.0")
    parser.addoption("--executor", action="store", default="localhost")


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    bversion = request.config.getoption("--bversion")

    capabilities = {
        "browserName": browser,
        "browserVersion": bversion,
        "selenoid:options": {
            "enableVideo": False
        }
    }

    driver = webdriver.Remote(
        command_executor=f"http://{executor}:4444/wd/hub", desired_capabilities=capabilities)

    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.now()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()
