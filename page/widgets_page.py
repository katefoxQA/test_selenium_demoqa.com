import random
import time

from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.widgets_page_locators import MenuPageLocators, ToolTipsPageLocators, AccordianPageLocators, \
    AutoCompletePageLocators, DatePickerPageLocators, SliderPageLocators, ProgresBarPageLocators, TabsPageLocators
from page.base_page import BasePage

class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {
            'first':
                {'title': self.locators.SECTION_FIRCT,
                 'content': self.locators.SECTION_FIRCT_CONTENT},
            'second':
                {'title': self.locators.SECTION_SECOND,
                 'content': self.locators.SECTION_SECOND_CONTENT},
            'third':
                {'title': self.locators.SECTION_THIRD,
                 'content': self.locators.SECTION_THIRD_CONTENT}
        }
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return section_title.text, len(section_content)


def generadet_color():
    pass


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_input_multi(self):
        any_colors = next(generated_color()).color_name
        colors = random.sample(any_colors, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
            time.sleep(1)
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    """ Как проверить удаление всех цветов одной кнопкой"""
    # def remove_all_multi(self):
    #     self.element_is_visible(self.locators.MULTI_ALL_REMOVE).click()
    #     self.find


    def check_color_multi(self):
        colors_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in colors_list:
            colors.append(color.text)
        return colors

    def fill_input_single(self):
        any_color = next(generated_color()).color_name
        color = random.sample(any_color, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        time.sleep(1)
        return color[0]

    def check_color_single(self):
        color = self.element_is_present(self.locators.SINGLE_VALUE).text
        return color

class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()
    """ Функция select_date выбирает с помощью селектора дату, состоящуюю из дня, месяца и года.
        А также возвращает старую и вновь выбранную даты. Для этого:
        1) определяется дата по умолчанию, стоящая в поле ввода даты
        2) открывается блок с селектами месяца, года и выбором даты из календаря
        3) находится селектор месяца и с помощью селекта (по видиимому тексту) выбираются сгенерированный месяц
        4) находится селектор года и с помощью селектта (по видиимому тексту) выбираются сгенерированный год
        5) находится список чисел в календаре и выбирается заранее сгенерированное число месяца
        6) определяется новая дата
        7) старая и новая даты возвращаются"""
    def select_date(self):
        input_date = self.element_is_visible(self.locators.DATE_INPUT)  # нашла вэб-элемент даты
        value_date_before = input_date.get_attribute('value')   # получила значение по умолчаниюю
        input_date.click()                                      # кликнула по полю ввода даты для получения селектов выбора месяца/года/дня
        time.sleep(1)
        date = next(generated_date())                           # сгенерированы данные для передачи селектору
        self.set_date_by_text(self.element_is_present(self.locators.DATE_SELECT_MONTH), date.month)  # выбираю селектом месяц, заранее сгенерированный
        self.set_date_by_text(self.element_is_present(self.locators.DATE_SELECT_YEAR), str(date.year))   # выбираю селектом год, заранее сгенерированный
        time.sleep(2)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)      # выбираюю день в календаре, заранее сгенерированную
        time.sleep(2)
        value_date_after = input_date.get_attribute('value')     # получила новое значение даты
        return value_date_before, value_date_after

    """ Функция select_date_and_time выбирает БЕЗ селектора месяц, год, день и время из календаря.
        А также возвращает старую и вновь выбранную даты. Для этого:
        1) определяется дата по умолчанию, стоящая в поле ввода даты
        2) открывается блок с выбором месяца, года и выбором даты из календаря
        3) находится выпадашка (это НЕ селектор в ДОМ-дереве) месяца, открывается
        4) из списка выбрирается заранее сгенерированный месяц и совершается клик
        5) находится выпадашка (это НЕ селектор в ДОМ-дереве) гоа, открывается
        6) из списка выбрирается заранее сгенерированный год и совершается клик
        7) находится список чисел в календаре и выбирается заранее сгенерированное число месяца, совершается клик по числу
        8) определяется новая дата
        9) старая и новая даты возвращаются"""
    def select_date_and_time(self):
        date = next(generated_date())                            # сгенерированы данные для передачи функции выбора из списка
        input_date = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)     # нашла вэб-элемент даты
        value_date_before = input_date.get_attribute('value')    # получила значение по умолчаниюю
        input_date.click()                                       # кликнула по полю ввода даты для получения селектов выбора месяца/года/дня
        time.sleep(1)
        self.element_is_visible(self.locators.DATE_AND_TIME_MONTH).click()       # нашла выпащку выбора месяца, кликнула, чтобы развернуть
        time.sleep(1)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)     # выбрала из списка месяцев заранее сгенерированный циклом, кликнула по нему
        print('сгенерированный месяц: ', date.month)
        self.element_is_visible(self.locators.DATE_AND_TIME_YEAR).click()        # нашла выпащку выбора года, кликнула, чтобы развернуть
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, date.year)      # выбрала из списка годов заранее сгенерированный циклом, кликнула по нему
        print('сгенерированный год: ', date.year)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_DAY_LIST, date.day)        # выбрала из списка номеров дней заранее сгенерированный циклом, кликнула по нему
        print('сгенерированный день месяца: ', date.day)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_TIME_LIST, date.time)      # выбрала из списка времени циклом 12:00, кликнула по нему
        value_date_after = input_date.get_attribute('value')                                # получила новое значение даты
        print(value_date_before)
        print(value_date_after)
        return value_date_before, value_date_after

    """ Вспомогательная функция для работы с селекторами месяца и года. Выношу для повторного использования.
        Применяю выбор по видимому тексту атрибута, но сами элементы ищу в ДОМ-дереве (is_present)"""
    def set_date_by_text(self, element, text):
        select = Select(element)    # передаю селекту элемент
        select.select_by_visible_text(text)         # применяю функциию селекта "выбор по видимому тексту"

    """ Вспомогательная функция set_date_item_from_list для работы с выбором месяца, года, дня и времени из списка. 
        Выношу для повторного использования.
        1) Список элементов нахожу в ДОМ-дереве, 
        2) прохожусь циклом до совпадения с заранее сгенерированным значением
        3) кликаю по найденному элементу"""
    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)         # Список элементов нахожу в ДОМ-дереве
        if value[0] == '0':                                     # Для сгенерированного числа месяца обрезаю 0 стоящий вначале (для вариантов 03 число, в календаре числа без 0 впереди)
            value = value[1:]
        for item in item_list:                                  # прохожусь циклом по найденному списку
            print("item.text=", item.text)                      # проверяю весь список, чтоб увидеть на каком элементе цикл прервется
            if item.text == value:                              # момент совпадения с заранее сгенерированным значением
                item.click()                                    # выбираю элемент
                time.sleep(2)
                break                                           # прерываю цикл

class SliderPage(BasePage):
    locators = SliderPageLocators()

    def check_slider(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        print(value_before)
        slider_input = self.element_is_visible(self.locators.SLIDER_INPUT)
        self.action_drug_and_drop_by_offset(slider_input, random.randint(0, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        print(value_after)
        return value_before, value_after

class ProgresBarPage(BasePage):
    locators = ProgresBarPageLocators()
    def check_progress_bar(self):
        self.element_is_visible(self.locators.PROGRESS_BAR_BUTTON).click()
        time.sleep(random.randint(1, 6))
        self.element_is_visible(self.locators.PROGRESS_BAR_BUTTON).click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        print(value_after)
        return value_after

class TabsPage(BasePage):
    locators = TabsPageLocators()
    def check_tabs(self):
        what_tab = self.element_is_clickable(self.locators.WHAT_BUTTON)
        what_content = self.element_is_visible(self.locators.WHAT_CONTENT).text
        print('Содержание вкладки: ', what_content)
        time.sleep(1)
        origin_tab = self.element_is_clickable(self.locators.ORIGIN_BUTTON)
        origin_tab.click()
        time.sleep(1)
        origin_content = self.element_is_present(self.locators.ORIGIN_CONTENT).text
        print('Содержание вкладки: ', origin_content)
        use_tab = self.element_is_visible(self.locators.USE_BUTTON)
        use_tab.click()
        time.sleep(1)
        use_content = self.element_is_present(self.locators.USE_CONTENT).text
        print('Содержание вкладки: ', use_content)
        return what_tab.text, len(what_content), origin_tab.text, len(origin_content), use_tab.text, len(use_content)




class MenuPage(BasePage):
    locators = MenuPageLocators()

    def check_menu(self):
        menu_item_list = self.elements_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data
class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()
    def get_text_from_tool_tips(self, hover_elem):
        element = self.element_is_present(hover_elem)
        self.action_move_to_element(element)
        time.sleep(0.5)
        # self.element_is_visible(wait_elem)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIP_INNERS).text
        return tool_tip_text

    def check_tool_tips(self):
        tool_tips_text_button = self.get_text_from_tool_tips(self.locators.BUTTON)
        tool_tips_text_field = self.get_text_from_tool_tips(self.locators.FIELD)
        tool_tips_text_contrary = self.get_text_from_tool_tips(self.locators.CONTRARY_LINK)
        tool_tips_text_link = self.get_text_from_tool_tips(self.locators.LINK)
        return tool_tips_text_button, tool_tips_text_field, tool_tips_text_contrary, tool_tips_text_link

    def check(self):
        locators = [self.locators.BUTTON,
                    self.locators.FIELD,
                    self.locators.CONTRARY_LINK,
                    self.locators.LINK]
        text_data = []
        for locator in locators:
            element = self.element_is_present(locator)
            # assert element is not None, f"Не найден элемент {locator}"
            if element:
                self.action_move_to_element(element)
                time.sleep(0.5)
                tool_tip_text = self.element_is_visible(self.locators.TOOL_TIP_INNERS).text
                text_data.append(tool_tip_text)
        return text_data





