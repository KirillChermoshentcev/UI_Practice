from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        self.driver.get(self.PAGE_URL)

    def find_element_with_wait(self, locator, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_visibility_of_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def send_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    def element_is_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def scroll_for_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def click_element(self, locator):
        """Кликает по элементу."""
        element = self.element_is_clickable(locator)
        element.click()
        
