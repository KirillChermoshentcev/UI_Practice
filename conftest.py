import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function', autouse=True)
def driver(request):
    options = Options()
    #options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get('https://demoqa.com/elements')
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()