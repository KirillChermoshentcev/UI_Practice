import random

from pages.base_page import BasePage
from links import ElementsTabLinks
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CheckBoxPage(BasePage):

    PAGE_URL = ElementsTabLinks.CHECKBOX_PAGE
    EXPAND_ALL_LIST_BUTTON = ("xpath", '//button[@title="Expand all"]')
    ITEM_LIST = ("xpath", '//span[@class="rct-title"]')
    CHECKED_ITEMS = ("css selector", 'svg[class="rct-icon rct-icon-check"]')
    TITLE_ITEM = ("xpath", './/ancestor::span[@class="rct-text"]')
    OUTPUT_RESULT = ("css selector", 'span[class="text-success"]')

    def open_full_list(self):
        self.wait.until(EC.visibility_of_element_located(self.EXPAND_ALL_LIST_BUTTON)).click()

    def click_on_random_checkbox(self):
        item_list = self.wait_visibility_of_elements(self.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_items = box.find_elements(*self.TITLE_ITEM)
            for item in title_items:
                data.append(item.text)
        return str(data).replace(' ', '').replace('doc','').replace('.','').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()



