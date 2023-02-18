import time

import allure
from selenium.common import TimeoutException

from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuPage


@allure.suite("Widgets")
class TestWidgets:
    @allure.feature("Accordian")
    class TestAccordianPage:
        @allure.title("Check length of text more than 0 and text contains fhrase")
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian(accordian_num='first')
            second_title, second_content = accordian_page.check_accordian(accordian_num='second')
            third_title, third_content = accordian_page.check_accordian(accordian_num='third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, 'Incorrect title pr missing text'
            assert second_title == 'Where does it come from?' and second_content > 0, 'Incorrect title pr missing text'
            assert third_title == 'Why do we use it?' and third_content > 0, 'Incorrect title pr missing text'

    @allure.feature("AutoComplete")
    class TestAutoCompletePage:
        @allure.title("Check filling in multiple autocomplete field")
        def test_fill_multiple_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            assert colors == colors_result, 'The added colors are missing from the input'

        @allure.title("Check removing one value from multiple autocomplete field")
        def test_remove_value_from_multi(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            count_value_before, count_value_after = autocomplete_page.remove_value_multi()
            assert count_value_before != count_value_after, 'The value was not deleted'

        @allure.title("Check removing all fields from multiple autocomplete field")
        def test_remove_all_values_multi(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            colors_after_remove = autocomplete_page.remove_all_values_multi()
            assert colors_after_remove == 0, 'All values were not deleted'

        @allure.title("Check filling of single value in autocomplete multiple field")
        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            assert color == color_result, 'The added colors are missing from the input'

    @allure.feature("DatePicker")
    class TestDatePickerPage:
        @allure.title("Check changing date in field")
        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after, 'The date has not been changed'

        @allure.title("Check changing date and time in field")
        def test_check_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            print(value_date_before)
            print(value_date_after)
            assert value_date_before != value_date_after, 'The date and time has not been changed'

    @allure.feature("Slider")
    class TestSliderPage:
        @allure.title("Check what sliders value changing")
        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            value_before, value_after = slider.change_slider_value()
            assert value_before != value_after, 'The slider value has not been changed'

    @allure.feature("ProgressBar")
    class TestProgressBarPage:
        @allure.title("Check what value in progress bar chaning")
        def test_progress_bar(self, driver):
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            value_before, value_after = progress_bar_page.change_progress_bar_value()
            assert value_before != value_after, 'The progress bar value has not been changed'

    @allure.feature("Tabs")
    class TestTabsPage:
        @allure.title("Check buttom name on page and length of content on tab more than 0")
        def test_tabs(self, driver):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            what_button, what_content = tabs_page.check_tabs(tab_name='What')
            origin_button, origin_content = tabs_page.check_tabs(tab_name='Origin')
            use_button, use_content = tabs_page.check_tabs(tab_name='Use')
            more_button = tabs_page.check_tabs(tab_name='More')
            assert what_button == 'What' and what_content != 0, 'The tab What was not pressed or the text is missing'
            assert origin_button == 'Origin' and origin_content != 0, 'The tab Origin was not pressed or the text is missing'
            assert use_button == 'Use' and use_content != 0, 'The tab Use was not pressed or the text is missing'
            assert more_button == 'The tab More was not pressed or the text is missing'

    @allure.feature("Tooltips")
    class TestToolTips:
        @allure.title("Check text in hover")
        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            time.sleep(1)
            button_text, field_text, contrary_text, section_text = tool_tips_page.check_tool_tips()
            assert button_text == 'You hovered over the Button', 'Hover missing or incorrect content'
            assert field_text == 'You hovered over the text field', 'Hover missing or incorrect content'
            assert contrary_text == 'You hovered over the Contrary', 'Hover missing or incorrect content'
            assert section_text == 'You hovered over the 1.10.32', 'Hover missing or incorrect content'

    @allure.feature("Menu")
    class TestMenuPage:
        @allure.title("Check what actual data on page equal to expected in list")
        def test_menu(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu#')
            menu_page.open()
            time.sleep(1)
            data_actual, data_expected = menu_page.check_menu()
            assert data_actual == data_expected
