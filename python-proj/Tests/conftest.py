import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--window-size=1680,1080")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])


@pytest.fixture(scope='class')
def init_driver(request):
    """Set up"""
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
    request.cls.driver = driver

    """tear down"""
    yield
    driver.close()

