from conftest import driver
from pages.textbox_page import TextBoxPage
from data import UserData


class TestTextBoxPage:

    def test_fill_textbox_page_info(self, driver):
        textbox_page = TextBoxPage(driver)
        textbox_page.open()
        textbox_page.enter_name(UserData.name)
        textbox_page.enter_email(UserData.email)
        textbox_page.enter_current_address(UserData.current_address)
        textbox_page.enter_permanent_address(UserData.permanent_address)
        textbox_page.scroll_for_element(textbox_page.SUBMIT_BUTTON)
        textbox_page.click_on_submit_button()

        submitted_info = textbox_page.check_submitted_info_block()

        assert submitted_info["name"] == "Name:" + UserData.name
        assert submitted_info["email"] == "Email:" + UserData.email
        assert submitted_info["current_address"] == "Current Address :" + UserData.current_address
        assert submitted_info["permanent_address"] == "Permananet Address :" + UserData.permanent_address