import random
import time
import re

from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.interactions_page_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators, DraggablePageLocators

from page.base_page import BasePage

class SortablePage(BasePage):
    locators = SortablePageLocators()
    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_sortable_items(self):
        # self.element_is_visible(self.locators.TAB_LIST).click()
        order_before = self.get_sortable_items(self.locators.ITEM_LIST)
        item_list = random.sample(self.elements_are_visible(self.locators.ITEM_LIST), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.ITEM_LIST)
        print(order_before)
        print(order_after)
        return order_before, order_after

    def change_sortable_grid(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        order_before = self.get_sortable_items(self.locators.ITEM_GRID)
        item_list = random.sample(self.elements_are_visible(self.locators.ITEM_GRID), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.ITEM_GRID)
        print(order_before)
        print(order_after)
        return order_before, order_after

class SelectablePage(BasePage):
    locators = SelectablePageLocators()
    def click_selectable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=1)[0].click()

    def select_list_item(self):
        # self.element_is_visible(self.locators.TAB_LIST).click()
        self.click_selectable_item(self.locators.ITEM_LIST)
        active_element = self.element_is_visible(self.locators.ITEM_LIST_ACTIVE)
        print(active_element.text)
        time.sleep(2)
        return active_element.text

    def select_grid_item(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        self.click_selectable_item(self.locators.ITEM_GRID)
        active_grid_element = self.element_is_visible(self.locators.GRID_LIST_ACTIVE)
        print(active_grid_element.text)
        time.sleep(2)
        return active_grid_element.text

class ResizablePage(BasePage):
    locators = ResizablePageLocators()
    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_size_resizable_box(self):
        self.action_drug_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        time.sleep(1)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        print(max_size)
        self.action_drug_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_BOX_HANDLE), -500, -300)
        time.sleep(1)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        print(min_size)
        return max_size, min_size

    def change_size_resizable(self):
        self.action_drug_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_HANDLE), random.randint(1, 300), random.randint(1, 100))
        time.sleep(1)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        print(max_size)
        self.action_drug_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_HANDLE), random.randint(-200, -1), random.randint(-200, -1))
        time.sleep(2)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        print(min_size)
        return max_size, min_size

class DroppablePage(BasePage):
    locators = DroppablePageLocators()
    def drop_simple(self):
        drag_div = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        print(drop_div.text)
        return drop_div.text

    def drop_acceptable(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()
        time.sleep(1)
        acceptable_div = self.element_is_visible(self.locators.ACCETABLE)
        not_acceptable_div = self.element_is_visible(self.locators.NOT_ACCETABLE)
        drop_here_div = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)
        self.action_drag_and_drop_to_element(not_acceptable_div, drop_here_div)
        drop_text_not_accept = drop_here_div.text
        print(drop_text_not_accept)
        self.action_drag_and_drop_to_element(acceptable_div, drop_here_div)
        drop_text_accept = drop_here_div.text
        print(drop_text_accept)
        return drop_text_not_accept, drop_text_accept

    def prevent_propogation(self):
        self.element_is_visible(self.locators.PREVENT_PROPOGATION_TAB).click()
        time.sleep(1)
        drag_div = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        not_greedly_inner_box = self.element_is_visible(self.locators.NOT_GREEDLY_INNER_BOX)
        self.action_drag_and_drop_to_element(drag_div, not_greedly_inner_box)
        text_not_greedly_box = self.element_is_visible(self.locators.NOT_GREEDLY_DROP_BOX_TEXT).text
        text_not_greedly_inner_box = not_greedly_inner_box.text
        time.sleep(1)
        print(text_not_greedly_box)
        print(text_not_greedly_inner_box)
        greedly_box = self.element_is_visible(self.locators.GREEDLY_INNER_BOX)
        self.action_drag_and_drop_to_element(drag_div, greedly_box)
        time.sleep(1)
        text_greedly_box = self.element_is_visible(self.locators.GREEDLY_DROP_BOX_TEXT).text
        text_greedly_inner_box = greedly_box.text
        print(text_greedly_box)
        print(text_greedly_inner_box)
        return text_not_greedly_box, text_not_greedly_inner_box, text_greedly_box, text_greedly_inner_box

    # def drop_revert_draggable(self):
    #     self.element_is_visible(self.locators.REVERT_DRAGGABLE_TAB).click()
    #     time.sleep(1)
    #     will_revert = self.element_is_visible(self.locators.WILL_REVERT)
    #     drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
    #     self.action_drag_and_drop_to_element(will_revert, drop_div)
    #     position_after_move = will_revert.get_attribute('style')
    #     time.sleep(2)
    #     position_after_revert = will_revert.get_attribute('style')
    #     print(position_after_move)
    #     print(position_after_revert)
    #     return position_after_move, position_after_revert

    def drop_revert_draggable(self, type_drag):
        drags = {
            'will':
                {'revert': self.locators.WILL_REVERT},
            'not_will':
                {'revert': self.locators.NOT_REVERT}
        }
        self.element_is_visible(self.locators.REVERT_DRAGGABLE_TAB).click()
        time.sleep(1)
        revert = self.element_is_visible(drags[type_drag]['revert'])
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVERT)
        self.action_drag_and_drop_to_element(revert, drop_div)
        position_after_move = revert.get_attribute('style')
        time.sleep(2)
        position_after_revert = revert.get_attribute('style')
        print(position_after_move)
        print(position_after_revert)
        return position_after_move, position_after_revert

class DraggablePage(BasePage):
    locators = DraggablePageLocators()
    def get_after_and_before_position(self, drag_element):
        self.action_drug_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 60))
        before_position = drag_element.get_attribute('style')
        time.sleep(1)
        # print(before_position)
        self.action_drug_and_drop_by_offset(drag_element, random.randint(0, 50), random.randint(0, 60))
        after_position = drag_element.get_attribute('style')
        # print(after_position)
        time.sleep(1)
        return before_position, after_position

    def simple_drag_box(self):
        drag_div = self.element_is_visible(self.locators.DRAG_ME)
        before_position, after_position = self.get_after_and_before_position(drag_div)
        return before_position, after_position

    def get_top_position(self, positions):
        return re.findall(r"\d[0-9]|\d", positions.split(';')[2])

    def get_left_position(self, positions):
        return re.findall(r'\d[0-9]|\d', positions.split(';')[1])

    def axis_restricted_x(self):
        self.element_is_visible(self.locators.AXIS_RESTRICTED_TAB).click()
        only_x = self.element_is_visible(self.locators.ONLY_X)
        position_x = self.get_after_and_before_position(only_x)
        print(position_x)
        top_x_before = self.get_top_position(position_x[0])
        top_x_after = self.get_top_position(position_x[1])
        left_x_before = self.get_left_position(position_x[0])
        left_x_after = self.get_left_position(position_x[1])
        print(top_x_before)
        print(top_x_after)
        print(left_x_before)
        print(left_x_after)
        return [top_x_before, top_x_after], [left_x_before, left_x_after]

    def axis_restricted_y(self):
        self.element_is_visible(self.locators.AXIS_RESTRICTED_TAB).click()
        only_y = self.element_is_visible(self.locators.ONLY_Y)
        position_y = self.get_after_and_before_position(only_y)
        # print(position_y)
        top_y_before = self.get_top_position(position_y[0])
        top_y_after = self.get_top_position(position_y[1])
        left_y_before = self.get_left_position(position_y[0])
        left_y_after = self.get_left_position(position_y[1])
        # print(top_y_before)
        # print(top_y_after)
        # print(left_y_before)
        # print(left_y_after)
        return [top_y_before, top_y_after], [left_y_before, left_y_after]















