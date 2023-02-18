from datetime import datetime

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
	options = Options()
	options.add_argument("--no-sandbox")
	driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)
	driver.maximize_window()
	yield driver
	attach = driver.get_screenshot_as_png()
	allure.attach(attach, name=f"Screenshot {datetime.now()}", attachment_type=allure.attachment_type.PNG)
	driver.quit()
