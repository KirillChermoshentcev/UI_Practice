from pages.base_page import BasePage
from links import ElementsTabLinks
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data import UserData


class TextBoxPage(BasePage):

    PAGE_URL = ElementsTabLinks.TEXTBOX_PAGE
    FULL_NAME_FIELD = ("xpath", '//input[@id="userName"]')
    EMAIL_FIELD = ("xpath", '//input[@id="userEmail"]')
    ADDRESS_FIELD = ("xpath", '//textarea[@id="currentAddress"]')
    PERMANENT_ADDRESS_FIELD = ("xpath", '//textarea[@id="permanentAddress"]')
    SUBMIT_BUTTON = ("xpath", '//button[@id="submit"]')

    SUBMITTED_NAME = ("xpath", '//p[@id="name"]')
    SUBMITTED_EMAIL = ("xpath", '//p[@id="email"]')
    SUBMITTED_ADDRESS = ("xpath", '//p[@id="currentAddress"]')
    SUBMITTED_PERMANENT_ADDRESS = ("xpath", '//p[@id="permanentAddress"]')

    def enter_name(self, name):
        self.wait.until(EC.element_to_be_clickable(self.FULL_NAME_FIELD)).send_keys(name)

    def enter_email(self, email):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).send_keys(email)

    def enter_current_address(self, current_address):
        self.wait.until(EC.element_to_be_clickable(self.ADDRESS_FIELD)).send_keys(current_address)

    def enter_permanent_address(self, permanent_address):
        self.wait.until(EC.element_to_be_clickable(self.PERMANENT_ADDRESS_FIELD)).send_keys(permanent_address)

    def click_on_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def check_submitted_info_block(self):
        self.wait_visibility_of_element(self.SUBMITTED_NAME)
        self.wait_visibility_of_element(self.SUBMITTED_EMAIL)
        self.wait_visibility_of_element(self.SUBMITTED_ADDRESS)
        self.wait_visibility_of_element(self.SUBMITTED_PERMANENT_ADDRESS)

        submitted_name = self.driver.find_element(*self.SUBMITTED_NAME).text
        submitted_email = self.driver.find_element(*self.SUBMITTED_EMAIL).text
        submitted_current_address = self.driver.find_element(*self.SUBMITTED_ADDRESS).text
        submitted_permanent_address = self.driver.find_element(*self.SUBMITTED_PERMANENT_ADDRESS).text

        return {
            "name": submitted_name,
            "email": submitted_email,
            "current_address": submitted_current_address,
            "permanent_address": submitted_permanent_address
        }