from datetime import datetime

import allure
import pytest
from selenium import webdriver

desiredCapabilities = {
    "browserName": "chrome"
}


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Remote(command_executor='http://192.168.1.55:4444/wd/hub',
                              desired_capabilities=desiredCapabilities)
    # driver.maximize_window()
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.now()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()
