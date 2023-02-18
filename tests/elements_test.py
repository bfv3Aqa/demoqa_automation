import random
import time

import allure

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage


@allure.suite("Elements")
class TestElements:
    @allure.feature("TextBox")
    class TestTextBox:
        @allure.title("Check TextBox")
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr, = text_box_page.check_filled_form()
            assert full_name == output_name, "the name does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_cur_addr, "the current address does not match"
            assert permanent_address == output_per_addr, "the permanent address does not match"

    @allure.feature("CheckBox")
    class TestCheckBox:
        @allure.title("Check CheckBox")
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkboxes = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkboxes == output_result, 'checkboxes have not been selected'

    @allure.feature("Radio Button")
    class TestRadioButton:
        @allure.title("Check Radio Button")
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', 'Yes have not been selected'
            assert output_impressive == 'Impressive', 'Impressive have not been selected'
            assert output_no == 'No', 'No have not been selected'
            time.sleep(5)

    @allure.feature("WebTables")
    class TestWebTables:
        @allure.title("Check add person in WebTable")
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            time.sleep(5)
            print(new_person)
            print(table_result)
            assert new_person in table_result

        @allure.title("Check search person in WebTable")
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, "the person was not found in the table"

        @allure.title("Check update person info in WebTable")
        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            last_name = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(last_name)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, "the person card has not been changed"

        @allure.title("Check delete person from WebTable")
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == 'No rows found'

        @allure.title("Check change row count in WebTable")
        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50,
                             100], "The number of rows in the table has not been changed or has changed incorrectly"

    @allure.feature("Buttons")
    class TestButtonsPage:
        @allure.title("Check clicks on the different buttons")
        def test_different_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            assert double == 'You have done a double click', 'The double click button was not pressed'
            assert right == 'You have done a right click', 'The right click button was not pressed'
            assert click == 'You have done a dynamic click', 'The dynamic click button was not pressed'

    @allure.feature("Links")
    class TestLinksPage:
        @allure.title("Check the link is correct")
        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, "The link is broken or url is incorrect"

        @allure.title("Check the link is broken")
        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400, "The link works or the status code not 400"

    @allure.feature("UploadAndDownload")
    class TestUploadAndDownload:
        @allure.title("Check uploading the file")
        def test_upload_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            result, file_name = upload_download_page.upload_file()
            assert result == file_name, 'the file has not been uploaded'

        @allure.title("Check downloading the file")
        def test_download_file(self, driver):
            upload_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            check = upload_download_page.download_file()
            assert check is True, 'the file has not been downloaded'

    @allure.feature("DynamicProperties")
    class TestDynamicPropertiesPage:
        @allure.title("Check the dynamic properties change")
        def test_dynamic_properties(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_after, color_before = dynamic_properties_page.check_changed_of_color()
            assert color_after != color_before, 'colors have not been changed'

        @allure.title("Check apper the button on page")
        def test_apper_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appear_of_button()
            assert appear is True, 'button did not appear after five seconds'

        @allure.title("Check enable the button after 5 sec")
        def test_check_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_enable_button()
            assert enable is True, 'button did not enable after five seconds'
