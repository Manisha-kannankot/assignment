from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from config.config import TestData
from page.base_page import BasePage


class HomePage(BasePage):
    """"By locators and Xpath"""
    search_input = (By.NAME, "searchInput")
    search_result_span = (By.XPATH, '//div[@class="site-model-entity-name"]')
    search_icon = (By.XPATH, '//mat-icon[text()="search"]')
    route_icon = (By.XPATH, '//span[text()="Route"]')
    close_icon = (By.XPATH, '//mat-icon[text()="close"]')
    reverse_button = (By.XPATH, '//img[@alt="Reverse route"]')
    time_estimate = (By.XPATH, '//div//strong')
    route_distance = (By.XPATH, '//span[contains(@class,"route-distance")]')
    floor_number = (By.XPATH, '//button[@id="floor-changer-button" and contains(@class,"active")]')
    route_start_input = (By.NAME, 'routeStartInput')
    start_here_icon = (By.XPATH, '//div[contains(text()," Start here ")]')
    destination_icon = (By.XPATH, '//img[@ng-src="img/poi_navvis/generic_poi.png"]')

    """constructor of the mark and measure class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        sleep(1)

    """Page Actions"""

    """To search a place"""
    def search_a_place(self, text):
        self.do_click(self.search_input)
        self.send_keys(self.search_input, text)
        self.do_click(self.search_icon)

    """To click on search result"""
    def click_on_search_result(self, text):
        search_results = self.driver.find_elements(By.XPATH, '//div[contains(@class,"mat-caption")]')
        for result in search_results:
            if result.text == text:
                result.click()
                sleep(3)
                break

    """To click on route icon"""
    def click_on_route_icon(self):
        self.do_click(self.route_icon)

    """To click on reverse route button"""
    def click_on_reverse_button(self):
        self.do_click(self.reverse_button)

    """Gets the number of floor"""
    def verify_floor_number(self):
        return self.get_element_text(self.floor_number)

    """To click on start button"""
    def click_on_start(self):
        self.do_click(self.start_here_icon)

    """To click on destination icon"""
    def click_on_destination_icon(self):
        self.do_click(self.destination_icon)





