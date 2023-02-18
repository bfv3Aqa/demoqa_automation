import time

import allure

from pages.form_page import FormPage


@allure.suite("Form")
class TestForm:
    @allure.feature("Form")
    class TestFormPage:
        @allure.title("Check filling all fields in form")
        def test_form(self, driver):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            p = form_page.fill_form_fields()
            time.sleep(1)
            result = form_page.form_result()
            assert [p.first_name + " " + p.last_name, p.email] == [result[0], result[1]], "the form has not been filled"
