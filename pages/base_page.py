from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
	def __init__(self, driver, url):
		self.driver = driver
		self.url = url

	def open(self):
		self.driver.get(self.url)

	def element_is_visible(self, locator, timeout=5):
		return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

	def elements_are_visible(self, locator, timeout=5):
		return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

	def element_is_present(self, locator, timeout=5):
		return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

	def elements_are_present(self, locator, timeout=5):
		return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

	def element_is_not_visible(self, locator, timeout=5):
		return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

	def element_is_clickable(self, locator, timeout=5):
		return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

	def go_to_element(self, element):
		self.driver.execute_script("arguments[0].scrollIntoView();", element)

	def action_double_click(self, element):
		action = ActionChains(self.driver)
		action.double_click(element)
		action.perform()

	def action_right_click(self, element):
		action = ActionChains(self.driver)
		action.context_click(element)
		action.perform()

	def switch_to(self, page_type):
		if page_type == 'window':
			self.driver.switch_to.window(self.driver.window_handles[1])
		elif page_type == 'alert_text':
			alert_window = self.driver.switch_to.alert
			return alert_window.text
		elif page_type == 'alert_button':
			alert_window = self.driver.switch_to.alert
			return alert_window

	def action_drag_and_drop_by_offset(self, element, x_coords, y_coords):
		action = ActionChains(self.driver)
		action.drag_and_drop_by_offset(element, x_coords, y_coords)
		action.perform()

	def action_drag_and_drop_by_element(self, what, where):
		action = ActionChains(self.driver)
		action.drag_and_drop(what, where)
		action.perform()

	def action_move_to_element(self, element):
		action = ActionChains(self.driver)
		action.move_to_element(element)
		action.perform()

	def remove_footer(self):
		self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
		self.driver.execute_script("document.getElementById('close-fixedban').remove();")


