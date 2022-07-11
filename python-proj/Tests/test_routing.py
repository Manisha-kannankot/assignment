import pytest

from config.config import TestData
from page.home_page import HomePage


@pytest.mark.usefixtures("init_driver")
class TestRouting:

    def test_end_to_end_routing(self):
        self.routing = HomePage(self.driver)
        self.routing.accept_cookies()
        # searching for kitchen
        self.routing.search_a_place(TestData.FIFTH_FLOOR)
        self.routing.click_on_search_result(TestData.KITCHEN_TEXT)
        current_floor_number = self.routing.verify_floor_number()
        assert current_floor_number == '5'
        self.routing.do_click(self.routing.close_icon)
        # navigating for printer in 4th floor
        self.routing.search_a_place(TestData.FOURTH_FLOOR)
        self.routing.click_on_search_result(TestData.PRINTER_TEXT)
        self.routing.click_on_route_icon()
        self.routing.send_keys(self.routing.route_start_input, TestData.FIFTH_FLOOR)
        self.routing.click_on_search_result(TestData.KITCHEN_TEXT)
        # verifying floors
        self.routing.click_on_start()
        current_floor_number = self.routing.verify_floor_number()
        assert current_floor_number == '5'
        self.routing.click_on_destination_icon()
        current_floor_number = self.routing.verify_floor_number()
        assert current_floor_number == '4'
        # verifying the time and distance estimated
        time_estimated = self.routing.get_element_text(self.routing.time_estimate)
        distance_estimated = self.routing.get_element_text(self.routing.route_distance)
        assert time_estimated + distance_estimated == '1 min(154 ft)'
