from datetime import datetime

import allure
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--executor", action="store", default="localhost")
    parser.addoption("--bro_version", action="store", default="")


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    bro_version = request.config.getoption("--bro_version")
    executor = request.config.getoption("--executor")

    capabilities = {
        "browserName": browser,
        "browserVersion": bro_version,
    }

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub", desired_capabilities=capabilities)

    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.now()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()
