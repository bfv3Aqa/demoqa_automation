import time

import allure

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


@allure.suite("AlertsFrameWindows")
class TestAlertsFrameWindow:
    @allure.feature("BrowserWindow")
    class TestBrowserWindow:
        @allure.title("Check opening new tab")
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab_or_window('new_tab')
            assert text_result == 'This is a sample page', 'A new tab has not opened or an incorrect tab has opened'

        @allure.title("Check opening new window")
        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab_or_window('new_window')
            assert text_result == 'This is a sample page', 'A new window has not opened or an incorrect window has opened'

    @allure.feature("TestAlerts")
    class TestAlertsPage:
        @allure.title("Checks what the alert shows after button click")
        def test_see_alerts(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == 'You clicked a button'

        @allure.title("Checks what the alert appear 5 sec after button click")
        def test_alert_appear_5_sec(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds'

        @allure.title("Checks what text appear in label after clicking OK or Cancel in alert message")
        def test_alert_confirm_box(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text_result_ok = alert_page.check_confirm_alert(confirm_type='ok')
            text_result_cancel = alert_page.check_confirm_alert(confirm_type='cancel')
            assert text_result_ok == 'You selected Ok', "Alert did not show up"
            assert text_result_cancel == 'You selected Cancel', "Alert did not show up"

        @allure.title("Check what text appear in label after entering text in alert message")
        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()
            assert text in alert_text, "Alert did not show up"

    @allure.feature("Frame")
    class TestFramePage:
        @allure.title("Checks text, weight, height of frame on page")
        def test_frames(self, driver):
            frame_page = FramesPage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.check_frame(frame_num='frame1')
            result_frame2 = frame_page.check_frame(frame_num='frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], 'The frame does not exist'
            assert result_frame2 == ['This is a sample page', '100px', '100px'], 'The frame does not exist'

    @allure.feature("NestedFrames")
    class TestNestedFramesPage:
        @allure.title("Check where are child and parent frames on page")
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == 'Parent frame'
            assert child_text == 'Child Iframe'

    @allure.feature("ModalDialogs")
    class TestModalDialogsPage:
        @allure.title("Check header title of modal window after pressing 'Small Modal' button on page")
        def test_small_modal_dialog(self, driver):
            modal_dialog_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialog_page.open()
            title_small, body_small = modal_dialog_page.check_small_modal_dialog()
            assert title_small == 'Small Modal', 'The header is not "Small Modal"'
            assert body_small == 47

        @allure.title("Check header title of modal window after pressing 'Large Modal' button on page")
        def test_large_modal_dialog(self, driver):
            modal_dialog_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialog_page.open()
            title_large, body_large = modal_dialog_page.check_large_modal_dialog()
            assert title_large == 'Large Modal', 'The header is not "Large Modal"'
            assert body_large == 574
