import os
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from generator.generator import generated_person, generated_file, generated_subject, generated_state
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
	locators = FormPageLocators()

	def fill_form_fields(self):
		person = next(generated_person())
		file_name, path = generated_file()
		self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.first_name)
		self.element_is_visible(self.locators.LAST_NAME).send_keys(person.last_name)
		self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
		self.element_is_visible(self.locators.GENDER).click()
		self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)
		self.element_is_visible(self.locators.SUBJECT).send_keys(generated_subject())
		self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
		self.element_is_visible(self.locators.HOBBIES).click()
		self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
		os.remove(path)
		self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
		self.element_is_visible(self.locators.SELECT_STATE).click()
		self.element_is_visible(self.locators.STATE_INPUT).send_keys(generated_state())
		self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
		self.element_is_visible(self.locators.SELECT_CITY).click()
		self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
		self.element_is_visible(self.locators.SUBMIT).click()
		return person

	def form_result(self):
		result_list = self.driver.find_elements(By.XPATH, self.locators.RESULT_TABLE)
		data = []
		for item in result_list:
			data.append(item.text)
		return data
