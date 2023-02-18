import time
import random

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
	NestedFramesPageLocators, ModalDialogsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
	locators = BrowserWindowsPageLocators()

	def check_opened_new_tab_or_window(self, button_type):
		if button_type == 'new_tab':
			self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
			self.switch_to(page_type='window')
			text_title = self.element_is_present(self.locators.TITLE_NEW).text
			return text_title
		elif button_type == 'new_window':
			self.element_is_visible(self.locators.NEW_WINDOW_TAB).click()
			self.switch_to(page_type='window')
			text_title = self.element_is_present(self.locators.TITLE_NEW).text
			return text_title


class AlertsPage(BasePage):
	locators = AlertsPageLocators()

	def check_see_alert(self):
		self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
		alert_text = self.switch_to(page_type='alert_text')
		return alert_text

	def check_alert_appear_5_sec(self):
		self.element_is_visible(self.locators.APPEAR_ALERT_IN_5_SEC_BUTTON).click()
		time.sleep(5)
		alert_text = self.switch_to(page_type='alert_text')
		return alert_text

	def check_confirm_alert(self, confirm_type):
		self.element_is_visible(self.locators.CONFIRM_BOX_BUTTON).click()
		alert_window = self.switch_to(page_type='alert_button')
		if confirm_type == 'ok':
			alert_window.accept()
		elif confirm_type == 'cancel':
			alert_window.dismiss()
		text_result = self.element_is_present(self.locators.RESULT_CONFIRM_ALERT_LABEL).text
		return text_result

	def check_prompt_alert(self):
		text = f"autotest{random.randint(0, 999)}"
		self.element_is_visible(self.locators.PROMPT_BOX_BUTTON).click()
		alert_window = self.driver.switch_to.alert
		alert_window.send_keys(text)
		alert_window.accept()
		text_result = self.element_is_present(self.locators.PROMPT_RESULT).text
		return text, text_result


class FramesPage(BasePage):
	locators = FramesPageLocators()

	def check_frame(self, frame_num):
		if frame_num == 'frame1':
			frame = self.element_is_present(self.locators.FIRST_FRAME)
			width = frame.get_attribute('width')
			height = frame.get_attribute('height')
			self.driver.switch_to.frame(frame)
			text = self.element_is_present(self.locators.TITLE_FRAME).text
			self.driver.switch_to.default_content()
			return [text, width, height]
		if frame_num == 'frame2':
			frame = self.element_is_present(self.locators.SECOND_FRAME)
			width = frame.get_attribute('width')
			height = frame.get_attribute('height')
			self.driver.switch_to.frame(frame)
			text = self.element_is_present(self.locators.TITLE_FRAME).text
			return [text, width, height]


class NestedFramesPage(BasePage):
	locators = NestedFramesPageLocators()

	def check_nested_frame(self):
		parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
		self.driver.switch_to.frame(parent_frame)
		parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
		child_frame = self.element_is_present(self.locators.CHILD_FRAME)
		self.driver.switch_to.frame(child_frame)
		child_text = self.element_is_present(self.locators.CHILD_TEXT).text
		return parent_text, child_text


class ModalDialogsPage(BasePage):
	locators = ModalDialogsPageLocators()

	def check_small_modal_dialog(self):
		self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
		title_small = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
		text_body_small = self.element_is_visible(self.locators.BODY_SMALL_MODAL).text
		self.element_is_visible(self.locators.CLOSE_SMALL_MODAL_BUTTON).click()
		return title_small, len(text_body_small)

	def check_large_modal_dialog(self):
		self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
		large_modal_text = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
		text_body_small = self.element_is_visible(self.locators.BODY_LARGE_MODAL).text
		self.element_is_visible(self.locators.CLOSE_LARGE_MODAL_BUTTON).click()
		return large_modal_text, len(text_body_small)
