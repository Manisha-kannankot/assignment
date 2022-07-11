from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

''' This class is the parent of all pages'''
'''This contains all the generic methods and utilities for all the pages'''


class BasePage:
    """"By locators and Xpath"""
    cookie_accept = (By.XPATH, '//button[text()="Accept"]')
    measure_icon = (By.XPATH, '//span[@id="tooltip-8"]')

    def __init__(self, driver):
        self.driver = driver

    """All common page actions goes here"""

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).click()
        sleep(1)

    def send_keys(self, by_locator,text):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 20).until(EC.title_is(title))
        return self.driver.title

    """Generic method to accept cookie"""
    def accept_cookies(self):
        self.do_click(self.cookie_accept)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.measure_icon))
