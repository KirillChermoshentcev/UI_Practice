from conftest import driver
from pages.checkbox_page import CheckBoxPage


class TestCheckBoxPage:

    def test_check_box(self, driver):
        checkbox_page = CheckBoxPage(driver)
        checkbox_page.open()
        checkbox_page.open_full_list()
        checkbox_page.click_on_random_checkbox()
        input_checkbox = checkbox_page.get_checked_checkboxes()
        output_result = checkbox_page.get_output_result()
        print(input_checkbox)
        print(output_result)
        assert input_checkbox == output_result
        