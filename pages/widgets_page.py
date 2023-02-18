import random
import time

from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
	SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsPageLocators, MenuPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
	locators = AccordianPageLocators()

	def check_accordian(self, accordian_num):
		accordian = {'first':
			             {'title': self.locators.SECTION_FIRST,
			              'content': self.locators.SECTION_CONTENT_FIRST},
		             'second':
			             {'title': self.locators.SECTION_SECOND,
			              'content': self.locators.SECTION_CONTENT_SECOND},
		             'third':
			             {'title': self.locators.SECTION_THIRD,
			              'content': self.locators.SECTION_CONTENT_THIRD},
		             }
		section_title = self.element_is_visible(accordian[accordian_num]['title'])
		try:
			section_content = self.element_is_visible(accordian[accordian_num]['content']).text
		except TimeoutException:
			section_title.click()
			section_content = self.element_is_visible(accordian[accordian_num]['content']).text
		return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):
	locators = AutoCompletePageLocators()

	def fill_input_multi(self):
		colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
		for color in colors:
			input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
			input_multi.send_keys(color)
			time.sleep(1)
			input_multi.send_keys(Keys.ENTER)
		return colors

	def remove_value_multi(self):
		count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
		remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
		for value in remove_button_list:
			value.click()
			break
		count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE))
		return count_value_before, count_value_after

	def remove_all_values_multi(self):
		remove_all_button = self.element_is_visible(self.locators.MULTI_REMOVE_ALL_VALUES)
		remove_all_button.click()
		try:
			values_after_remove = len(self.elements_are_present(self.locators.MULTI_VALUE))
		except TimeoutException:
			values_after_remove = 0
		return values_after_remove

	def check_color_in_multi(self):
		color_list = self.elements_are_present(self.locators.MULTI_VALUE)
		colors = []
		for color in color_list:
			colors.append(color.text)
		return colors

	def fill_input_single(self):
		color = random.sample(next(generated_color()).color_name, k=1)
		input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
		input_single.send_keys(color)
		time.sleep(1)
		input_single.send_keys(Keys.ENTER)
		return color[0]

	def check_color_in_single(self):
		color = self.element_is_visible(self.locators.SINGLE_VALUE)
		return color.text


class DatePickerPage(BasePage):
	locators = DatePickerPageLocators()

	def select_date(self):
		date = next(generated_date())
		input_date = self.element_is_visible(self.locators.DATE_INPUT)
		value_date_before = input_date.get_attribute('value')
		input_date.click()
		self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
		self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
		self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
		value_date_after = input_date.get_attribute('value')
		return value_date_before, value_date_after

	def set_date_by_text(self, element, value):
		select = Select(self.element_is_present(element))
		select.select_by_visible_text(value)

	def set_date_item_from_list(self, elements, value):
		item_list = self.elements_are_present(elements)
		for item in item_list:
			if item.text == value:
				item.click()
				break

	def select_date_and_time(self):
		date = next(generated_date())
		input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
		value_date_before = input_date.get_attribute('value')
		input_date.click()
		self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()
		self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
		self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()
		self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, '2020')
		self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
		self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)
		input_day_after = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
		value_date_after = input_date.get_attribute('value')
		return value_date_before, value_date_after


class SliderPage(BasePage):
	locators = SliderPageLocators()

	def change_slider_value(self):
		value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
		slider_input = self.element_is_visible(self.locators.SLIDER_INPUT)
		self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
		value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
		return value_before, value_after


class ProgressBarPage(BasePage):
	locators = ProgressBarPageLocators()

	def change_progress_bar_value(self):
		value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
		progress_bar_button = self.element_is_clickable(self.locators.PROGRESS_BAR_BUTTON)
		progress_bar_button.click()
		time.sleep(random.randint(2, 8))
		progress_bar_button.click()
		value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
		return value_before, value_after


class TabsPage(BasePage):
	locators = TabsPageLocators()

	def check_tabs(self, tab_name):
		tabs = {'What':
			        {'title': self.locators.WHAT_TAB,
			         'content': self.locators.WHAT_TAB_CONTENT},
		        'Origin':
			        {'title': self.locators.ORIGIN_TAB,
			         'content': self.locators.ORIGIN_TAB_CONTENT},
		        'Use':
			        {'title': self.locators.USE_TAB,
			         'content': self.locators.USE_TAB_CONTENT},
		        'More':
			        {'title': self.locators.MORE_TAB,
			         'content': self.locators.MORE_TAB_CONTENT},

		        }
		button = self.element_is_visible(tabs[tab_name]['title'])
		try:
			button.click()
		except ElementClickInterceptedException:
			message = f'The tab {tab_name} was not pressed or the text is missing'
			return message
		content = self.element_is_visible(tabs[tab_name]['content']).text
		return button.text, len(content)


class ToolTipsPage(BasePage):
	locators = ToolTipsPageLocators()

	def get_text_from_tool_tips(self, hover_element, wait_element):
		element = self.element_is_present(hover_element)
		self.action_move_to_element(element)
		self.element_is_visible(wait_element)
		time.sleep(1)
		tool_tip_text = self.element_is_visible(self.locators.TOOL_TIPS_INNERS)
		text = tool_tip_text.text
		return text

	def check_tool_tips(self):
		tool_tip_text_button = self.get_text_from_tool_tips(self.locators.BUTTON, self.locators.TOOL_TIP_BUTTON)
		tool_tip_text_field = self.get_text_from_tool_tips(self.locators.FIELD, self.locators.TOOL_TIP_FIELD)
		tool_tip_text_contrary = self.get_text_from_tool_tips(self.locators.CONTRARY,
		                                                      self.locators.TOOL_TIP_CONTRARY)
		tool_tip_text_section = self.get_text_from_tool_tips(self.locators.SECTION,
		                                                     self.locators.TOOL_TIP_SECTION)
		return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section


class MenuPage(BasePage):
	locators = MenuPageLocators()

	def check_menu(self):
		data_expected = ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1',
			                'Sub Sub Item 2', 'Main Item 3']
		menu_item_list = self.elements_are_present(self.locators.MENU_ITEM_LIST)
		data_actual = []
		for item in menu_item_list:
			self.action_move_to_element(item)
			data_actual.append(item.text)
		return data_actual, data_expected

