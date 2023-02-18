import random

from locators.interactions_locators import SortablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
	locators = SortablePageLocators()

	def get_sortable_items(self, element):
		item_list = self.elements_are_visible(element)
		return [item.text for item in item_list]

	def change_list_order(self, tab_name):
		tabs = {'list':
			        {'title': self.locators.TAB_LIST,
			         'content': self.locators.LIST_ITEM},
		        'grid':
			        {'title': self.locators.TAB_GRID,
			         'content': self.locators.GRID_ITEM}
		        }

		self.element_is_visible(tabs[tab_name]['title']).click()
		order_before = self.get_sortable_items(tabs[tab_name]['content'])
		item_list = random.sample(self.elements_are_visible(tabs[tab_name]['content']), k=2)
		item_what = item_list[0]
		item_where = item_list[1]
		self.action_drag_and_drop_by_element(item_what, item_where)
		order_after = self.get_sortable_items(tabs[tab_name]['content'])
		return order_before, order_after
