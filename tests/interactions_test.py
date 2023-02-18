import allure

from pages.interaction_page import SortablePage


@allure.suite("Interactions")
class TestInteractions:
	@allure.feature("Sortable")
	class TestSortablePage:
		@allure.title("Check sorting in list and grid on page")
		def test_sortable(self, driver):
			sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
			sortable_page.open()
			list_before, list_after = sortable_page.change_list_order(tab_name='list')
			grib_before, grid_after = sortable_page.change_list_order(tab_name='grid')
			assert list_before != list_after, 'The order of the list has not been changed'
			assert grib_before != grid_after, 'The order of the grid has not been changed'
