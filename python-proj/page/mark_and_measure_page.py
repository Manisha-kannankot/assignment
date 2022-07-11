from config.config import TestData
from page.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class MarkAndMeasurePage(BasePage):
    """"By locators and Xpath"""
    measure_tool_box = (By.XPATH, '//div[@id="vertical-toolbox-menu"]')
    canvas = (By.XPATH, '//iv-main-view[@id="jquery-contextmenu-1"]//canvas')
    point = (By.XPATH, '//mat-icon[@title="Free Point"]')

    """constructor of the mark and measure class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        sleep(1)

    """Page Actions"""
    """This is used to get the page title"""

    def get_page_title(self, title):
        return self.get_title(title)

    """This is used to check if measurement tool icon is visible"""

    def is_measure_icon_exist(self):
        return self.is_visible(self.measure_icon)

    """This is used to check if measurement tool box exist"""

    def is_measure_tool_box_exist(self):
        return self.is_visible(self.measure_tool_box)

    """This is used to click on measure icon"""

    def click_on_measure_icon(self):
        self.do_click(self.measure_icon)
        WebDriverWait(self.driver, 300).until(EC.visibility_of_element_located(self.measure_tool_box))

    """This is to pick a point from tool box"""

    def pick_a_point_from_tool_box(self):
        WebDriverWait(self.driver, 300).until(EC.visibility_of_element_located(self.measure_tool_box))
        self.do_click(self.point)

    """This is to move to canvas"""

    def move_to_canvas(self):
        sleep(5)
        action = ActionChains(self.driver)
        main_canvas = WebDriverWait(self.driver, 300).until(EC.element_to_be_clickable(self.canvas))
        size = main_canvas.size
        w, h = size['width'], size['height']
        new_w = w / 2
        new_h = h / 2
        action.move_by_offset(new_h, new_h).pause(1).perform()
        WebDriverWait(self.driver, 300).until(EC.element_to_be_clickable(self.canvas)).click()
        sleep(1)
