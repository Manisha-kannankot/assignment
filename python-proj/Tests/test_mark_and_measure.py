import pytest

from config.config import TestData
from page.mark_and_measure_page import MarkAndMeasurePage


@pytest.mark.usefixtures("init_driver")
class TestMarkAndMeasure:

    def test_home_page_title(self):
        self.mark_and_measure = MarkAndMeasurePage(self.driver)
        title = self.mark_and_measure.get_page_title(TestData.TITLE)
        assert title == TestData.TITLE

    def test_mark_and_measure_icon_visible(self):
        self.mark_and_measure = MarkAndMeasurePage(self.driver)
        self.mark_and_measure.accept_cookies()
        flag = self.mark_and_measure.is_measure_icon_exist()
        assert flag

    def test_navigating_to_mark_and_measure_tool(self):
        self.mark_and_measure = MarkAndMeasurePage(self.driver)
        self.mark_and_measure.accept_cookies()
        self.mark_and_measure.click_on_measure_icon()
        tool_box_exist = self.mark_and_measure.is_measure_tool_box_exist()
        assert tool_box_exist

    # '''This test is commented as it does not satisfy the functionality'''
    # def test_user_can_mark_point_on_2d_view(self):
    #     self.mark_and_measure = MarkAndMeasurePage(self.driver)
    #     self.mark_and_measure.accept_cookies()
    #     self.mark_and_measure.click_on_measure_icon()
    #     self.mark_and_measure.pick_a_point_from_tool_box()
    #     self.mark_and_measure.move_to_canvas()













