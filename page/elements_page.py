import base64
import os
import random
import time

import requests
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from generator.generator import generated_person, generated_file
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioPageLocators, \
    WebTableLocators, ButtonPageLocators, LinksPageLocators, UploadAndDownloadPageLocators, \
    DynamicPropertiesPageLocators
from page.base_page import BasePage

"""Класс  TextBoxPage включает две функции для заполнения текстовых полей и получениия результатов ввода данных"""
class TextBoxPage(BasePage):
    locators = TextBoxPageLocators
    """Функция fill_all_fields заполняет текстовые поля и возвращает отправленные данные по каждому полюЮ
        Для этого: 
        1) создается генератор generated_person() и используется только одна первая итерация данных
        2) заполняется каждое поле заранее сгенерированными данными
        3) подтверждаем заполнение, нажав кнопку SUBMIT
        4) возвращаем отправленные данные по каждому полю"""
    def fill_all_fields(self):
        person_info = next(generated_person())      # next позволяет взять только 1ю итерацию при генерировании
        full_name = person_info.full_name
        email = person_info.email
        cur_addr = person_info.cur_addr
        per_addr = person_info.per_addr
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(cur_addr)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(per_addr)
        self.element_is_visible(self.locators.SUBMIT).click()
        time.sleep(4)
        return full_name, email, cur_addr, per_addr

    """Функция check_filled_form необходима для дальнейшей проверки правильности заполнения текстовых полей
        и возвращает данные, появившиеся в аутпутах по каждому полю.
            Для этого: 
            1) из каждого аутпута выбираюются текстовые данные
            2) методами python обрезаем лишнюю информацию для дальнейшего сравнения
            3) возвращаем данные, появившиеся в аутпутах по каждому полю"""
    def check_filled_form(self):
        output_full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":", maxsplit=1)[1]
        output_email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(":", maxsplit=1)[1]
        output_cur_addr = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":", maxsplit=1)[1]
        output_per_addr = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":", maxsplit=1)[1]
        return output_full_name,  output_email,  output_cur_addr,  output_per_addr


# class CheckBoxPage(BasePage):
#     locators = CheckBoxPageLocators()
#
#     def open_full_list(self):
#         self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()
#
#
#     def click_random_checkbox(self):
#         # item_list = self.elements_are_visible(self.locators.ITEM_LIST)  # все подряд чекбоксы
#         item_list = self.elements_are_visible(self.locators.ITEM_LIST_LEAF)     #только внутренние чекбоксы
#         """Если мне понадобились только внутренние чекбоксы:
#         беру их список, принтую и кликаю по каждому """
#         # for item in item_list:
#         #     self.go_to_element(item)
#         #     print(item.text)
#         #     item.click()
#         # time.sleep(10)
#         """Если нужно отметить все чекбоксы, то использую простой цикл for и
#         прохожу по всему списку (перемещаюсь к элементу, кликаю и жду)"""
#         # for item in item_list:
#         #     self.go_to_element(item)
#         #     item.click()
#         #     print(item.text)
#         #     time.sleep(0.2)
#         """Если нужно кликнуть только по одному элементу причем рандомно, то
#         использую следующее"""
#         # item = item_list[random.randint(1, 15)]
#         # self.go_to_element(item)
#         # item.click()
#         # time.sleep(2)
#
#         """Для рандомного клика нескольких чекбоксов можно использовать цикл while
#         беру количество итераций count, и пока count>0 перемещаюсь к элементу, кликаю,
#         принтую его название и затем уменьшаю count на 1; и так пока count>0; иначе выхожу из цикла"""
#         count = 5
#         while count != 0:
#             item = item_list[random.randint(0, 10)]
#             if count > 0:
#                 self.go_to_element(item)
#                 item.click()
#                 print(item.text)
#                 time.sleep(0.5)
#                 count -=1
#             else:
#                 break
#         time.sleep(1)
#
#     """Хочу получить отмеченные чекбоксы для дальнейшей их сверки с попавшими в аутпут"""
#     def get_checked_checkboxes(self):
#         checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)    #это отмеченные чекбоксы
#         data = []
#         """Каждый раз, когда я прохожусь по созданному списку, я хочу получать текст из этого чекбокса
#         НО!!!! ..... нужно понимать, что при повторном клике на тот же чекбокс выделение снимется и
#         у меня выведено будет 5 шт, а в аутпутах на сайте останется 3 выбранных
#         или же НАОБОРОТ, в моем принте будет 5 шт, а в аутпутах (и в сизуально в чекбоксах)
#         будет 6 шт, так как автоматом добавится 1 более высокого уровня """
#         by, value = self.locators.TITLE_ITEM  # распаковка нужна, чтобы элементы из массива разложить по переменным
#         for box in checked_list:
#             title_item = box.find_element(by=by, value=value)   # это распаковка, find_element принимает по чем искать и что искать
#             # print(title_item.text)
#             data.append(title_item.text)
#         # print(data)
#         return str(data).replace(' ', '').replace('.doc', '').lower()
#
#     # def a1(self, a, b, c):     # позиционные параметры
#     #     pass
#     #
#     # def a2(self, a:int=0, b:int=0, c:int=0):   # именованные параметры
#     #     a2(a, b, c)
#     #     a2(c=c, a=a, b=b)
#     #     a2()
#
#     def get_output_result(self):
#         result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
#         data = []
#         for item in result_list:
#             data.append(item.text)
#         return str(data).replace(' ', '').lower()

class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()
    """Функция open_full_list открывает полный список всех возможных чек-боксов для последующего выбора"""
    def open_full_list(self):
        self.element_is_visible(self.locators.OPEN_LIST).click()
        time.sleep(1)
    """Функция  click_checkbox осуществляет клик по заданному списку чек-боксов или одному конкретному"""
    def click_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_CHECKBOX)       # кликать по нескольким рандомным чек-боксам из полного списка
        # item_list = self.elements_are_visible(self.locators.ITEM_LIST_LEAF)    # только внутренние чекбоксы
        count = 5                                                                # рандомно по нескольким элементам
        while count != 0:
            i = item_list[random.randint(1, 16)]
            if count > 0:
                self.go_to_element(i)
                i.click()
                # print(i.text)
                count -= 1
                # time.sleep(1)
            else:
                break
        # time.sleep(0.5)
        """Кликать по конкретному чек-боксу"""
        # i = item_list[5]
        # i.click()   # кликнула только по конкретному чекбоксу (напр, по 3му в по порядку)
        # print(i.text)
        # time.sleep(2)
        """Прокликать по всем чек-боксам из списка"""
        # for i in item_list:   # кликаем по всем из списка, проходясь по списку
        #     self.go_to_element(i)
        #     i.click()
        #     time.sleep(0.5)
        #     print(i.text)
        """Кликать по одному чек-боксу рандомно"""
        # i = item_list[random.randint(1, 16)]     # кликаю по одному рандомно
        # self.go_to_element(i)
        # i.click()
        # time.sleep(1)
        # print(i.text)
        """Кликать по нескольким конкретным чек-боксам с укразанным локатором """
        # by, value = self.locators.ITEM_CHECKBOX1                     # если нужны по определенным локаторам
        # for selector in ["angular", "private", "wordFile"]:
        #     el = self.element_is_visible(by, value.format(selector))  # (используя форматирование) подставляем в гнезда конкретные отличия в локаторах
        #     self.go_to_element(el)
        #     time.sleep(1)
        #     el.click()
        #     print(el.text)
        #     time.sleep(1)

        # i1 = self.element_is_visible(self.locators.ITEM_CHECKBOX1)   # если нужны по определенным локаторам
        # i2 = self.element_is_visible(self.locators.ITEM_CHECKBOX2)
        # i3 = self.element_is_visible(self.locators.ITEM_CHECKBOX3)
        # item_list1 = [i1, i2, i3]
        # for i in item_list1:
        #     self.go_to_element(i)
        #     time.sleep(0.5)
        #     i.click()
        #     print(i.text)
        #     time.sleep(0.2)

    """Функция get_checked_checkboxes позволяет получить список выбранных чек-боксов. 
        Для этого можно использовать два способа: сразу получить текст выбранного бокса или сначала список отмеченных боксов,
        а затем текст.
        Функция возвращает текст отмеченных чек-боксов"""
    def get_checked_checkboxes(self):
        """ СПОСОБ 1 - если нужно выбрать текст элементов xpath-ом из предварительно найденных выбранных чекбоксов"""
        # checked_checkboxes = self.elements_are_present(self.locators.CHECKED_ITEMS)    # нахожу выделенные чекбоксы, ложу в массив
        # data1 = []                                                         # выбираю текст элементов по ПРЕДВАРИТЕЛЬНО НАЙДЕННЫМ выделенным чекбоксам
        # by, value = self.locators.TITLE_CHECKBOXES1
        # for checkbox in checked_checkboxes:
        #     title_checkbox = checkbox.find_element(by=by, value=value)
        #     data1.append(title_checkbox.text)
        #     print(title_checkbox.text)
        #     time.sleep(0.3)
        # return data1
        # print("----------------------")

        """ СПОСОБ 2 - Если сразу искать xpath-ом текст выбранных чекбоксов (без предварительного поиска выбранных чекбоксов)"""
        title_checkbox1 = self.elements_are_present(self.locators.TITLE_CHECKBOXES2)   # получаю список вэб элементов названий выделенных чекбоксов
        # data2 = []
        # for title in title_checkbox1:          # прохожу по каждому элементу списка, вытаскивая текст из вэб элементов
        #     print(title.text)
        #     data2.append(title.text)
        #     time.sleep(0.3)
        # return data2
        data3 = [el.text for el in title_checkbox1]      # создает массив путём перебора другого массива, (елси еще нужно проверить по условию, то добавить  if)
        # print(data3)
        return str(data3).replace(' ', '').replace('.doc', '').lower()
    """Функция get_output_checkboxes позволяет получить текст чек-боксов, которые фактически оказались выбранными.
        Возвращает текст наименований чекбоксов из аутпутов."""
    def get_output_checkboxes(self):
        output_titles = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data4 = []
        for output in output_titles:
            data4.append(output.text)
        # print(data4)
        return str(data4).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioPageLocators()

    # def click_on_radio_button(self):                # простой вариант, циклом переберу все варианты выбора
    #     item_radio_buttons = self.elements_are_visible(self.locators.ITEM_RADIO_BUTTONS)
    #     for item in item_radio_buttons:
    #         self.go_to_element(item)
    #         time.sleep(1)
    #         item.click()
    #         print(item.text)
    #         time.sleep(1)

    """Функция click_on_radio_button позволяет проклткать заданные кнопки radio_button.
        Для удобства используется словарь с локаторами."""
    def click_on_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADIO,
                   'impressive': self.locators.IMPRESSIVE_RADIO,
                   'no': self.locators.NO_RADIO}
        self.element_is_visible(choices[choice]).click()
        time.sleep(1)

    """Функция radio_is_checked позволяет проверить, что выбран только один radio_button, а остальные остались невыбранными.
    Для этого: 
    1) формирует список radio_button-ов, в котором выбранный выражен True, а остальные - False.
    2) определяется количество невыбранных radio_button-ов после клика
    3) эти данные возвращаюются для дальнейшей проверки в тесте"""
    def radio_is_checked(self):
        checked_radio = self.elements_are_present(self.locators.CHECKED_RADIO)
        i = []
        for radio in checked_radio:
            i.append(radio.is_selected())
        # print(i)
        n = i.count(False)
        return i, n

    """Функция get_output_result позволяет получить текст из выбранных radio_button-ов для дальнейшей проверки в тесте"""
    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RADIO).text


class WebTablePage(BasePage):
    locators = WebTableLocators()

    """ Функция добавляет нового человека в таблицу, а именно:
    1) кликнуть по кнопке "ADD", 
    2) заполнить все поля в выпадающем попапе,
    3) нажать кнопку "Submit"
    И возвращает текстовые данные по добавленному человеку для дальнейшего сравнения """
    def add_new_person(self):              # добавляем только 1 человека или нескольких
        count = 1
        # people = []
        while count != 0:
            person_info = next(generated_person())    # с помощьюю метода next() берем данные по человеку из сгенерированного generated_person()
            first_name = person_info.first_name       # генерирую данные для полей ввода
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            # Далее заполняю все поля
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            time.sleep(1)
            self.element_is_visible(self.locators.SUBMIT).click()           # жму кнопку подтвердить и отправить
            # people.append([first_name, last_name, str(age), email, str(salary), department])
            count -= 1
            time.sleep(2)
            return [first_name, last_name, str(age), email, str(salary), department]       # возвращаю данные по человеку для дальнейшего сравнения с результатами в таблице
        # return people                                     # возвращаю данные по человеку для дальнейшего сравнения с результатами в таблице

    """ Функция формирует список данных по всем людям в таблице, включая вновь созданных.
        Возвращаемый текстовый список данных по всем людям в таблице (нужен для сравнения с данными вновь добавленного человека)"""
    def check_new_add_person(self):
        persons_list = self.elements_are_present(self.locators.FULL_PERSON_LIST)     # список вэб элементов по таблице после добавления новых людей
        tabel_results = []                                             # преобразую список вэб элементов в список с текстовыми данными по каждому человеку в таблице
        for person in persons_list:
            tabel_results.append(person.text.splitlines())
            time.sleep(2)
        return tabel_results

    """ Функция находит человека по ключевому слову, которое вводится в строку поиска
     (берём по индексу из списка данных созданного человека)"""
    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    """ Функция проверяет появился ли в таблице результатов поисков искомый человек и 
    возвращает текст строки с данными по найденному человеку"""
    def check_search_person(self):
        """ СПОСОБ 1 - длинный: найти кнопку delete у строки результатов поиска, а затем по этому элементу найти средствами python
        find_element() строку предка, содержащую все данные об искомом человеке.
        Вернуть текст найденной строки"""
        # delete_button = self.element_is_visible(self.locators.DELETE_BUTTON)
        # by, value = self.locators.PARENT_ROW
        # row = delete_button.find_element(by=by, value=value)
        # time.sleep(3)
        # return row.text.splitlines()
        """ СПОСОБ 2 - короткий: сразу средствами Xpath найти строку с данными результатов поиска и передать текст строки"""
        row = self.element_is_present(self.locators.ROW_SEARCH_RESULT)
        time.sleep(3)
        return row.text.splitlines()

    """ Функция update_person_info производит изменение данных по человеку и возвращает изменённые данные в виде строки. Для этого:
    1) генерирует новый возраст человека с помощью метода next() и генератора данных человека
    2) нажимает на кнопку изменить (карандаш)
    3) очищает необходимое поле ввода age 
    4) вводит в поле новый сгенерированный возраст
    5) нажимает кнопку подтвердить  """
    def update_person_info(self):
        person_info = next(generated_person())                          # с помощьюю метода next() берем данные по человеку из сгенерированного generated_person()
        age = person_info.age                                           # генерирую новый возраст для внесения изменений в конкретного человека
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()    # нажимаем на кнопку изменить (карандаш)
        time.sleep(1)
        self.element_is_visible(self.locators.AGE_INPUT).clear()         # очищаем поле age методом clear()
        time.sleep(1)
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)  # отправляем новый возраст в поле age появившегося попапа с данными человека
        time.sleep(1)
        self.element_is_visible(self.locators.SUBMIT).click()            # кликаем на submit
        return str(age)


    """ Функция производит удаление человека из таблицы. Для этого:
    1) кликаю на кнопку "удалить" (мусорка) """
    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()
        time.sleep(2)

    """ Функция проверяет удаление человека из таблицы. Для этого:
        1) нахожу сообщение, появляющееся на экране после удаления человека
        2) возвращаюю этот текст для дальнейшего сравнения с требуемым """
    def check_deleted(self):
        return self.element_is_present(self.locators.NO_PERSON).text

    """ Функция update_count_rows проверяет изменение строк в таблице. Для этого:
    1) нахожу селектор для выбора количества строк на странице
    2) перемещаюсь к селектору (в поле видимости)
    3) нажимаю на селектор
    4) нахожу каждый вариант выдачи количества строк в таблице
    5) нажимаю на соответствующий
    6) формирую список из значений количества строк, используя вложенную функцию update_count_rows
    7) возвращаю список 
    """
    """ СПОСОБ 1"""
    def update_count_rows(self):
        count = [5, 10, 20]                                                      # ожидаемое количество строк в таблице
        data = []                                                                             # создаем список количества строк
        for x in count:                                                                       # проходим по каждому значению count и выбираем соответсвующий варииант в выпадающих вариантах селекта
            select_count_button = self.element_is_visible(self.locators.SELECT_COUNT_ROW)     # находим на странице кнопу-селектор для выбора количества отображаемых строк таблицы
            self.go_to_element(select_count_button)                                           # перемещаемся вниз таблицы до кнопки с селектором
            select_count_button.click()                                                       # нажимаем на кнопку select
            time.sleep(2)
            locator1 = (By.CSS_SELECTOR, f'option[value="{x}"]')
            selecting_count = self.element_is_visible(locator1)    # выбираем вариант количества строк в таблице
            selecting_count.click()                                                               # нажимаем на него
            time.sleep(2)
            data.append(self.check_count_rows())                                              # ложим в список количество строк из вложенной функции def check_count_rows
        return data                                                                           # возвращаем количество строк в таблице

    """ Функция check_count_rows проверяет количество строк в таблице и 
    испольлзуется как вложенная для функции update_count_rows """
    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PERSON_LIST)
        return len(list_rows)


    """ СПОСОБ 2, используя find_element(), и динамически создавая список ожидаемого кол-ва строк в таблице"""
    """ Функция update_count_rows проверяет изменение строк в таблице. Для этого:
       1) нахожу селектор для выбора количества строк на странице
       2) перемещаюсь к селектору (в поле видимости)
       3) нажимаю на селектор
       4) нахожу каждый вариант выдачи количества строк в таблице
       5) нажимаю на соответствующий
       6) формирую список из значений количества строк, используя вложенную функцию update_count_rows
       7) возвращаю список 
       """
    def update_count(self):
        select_count_button = self.element_is_present(self.locators.SELECT_COUNT_ROW)     # нахожу на странице кнопу-селектор для выбора количества отображаемых строк таблицы
        self.go_to_element(select_count_button)                                           # перемещаюсь вниз таблицы к селектору
        select_count_button.click()                                                       # нажимаю на кнопку селектора
        excepting_data = []                                                               # создаю список ожидаемых количеств строк таблицы
        real_data = []                                                                    # создаю список реальных количеств строк таблицы
        options = select_count_button.find_elements(By.CSS_SELECTOR, "option")          # используя метод find_elements(), нахожу все элементы с тэгом option
        for option in options:
            try:
                val = int(option.get_attribute("value"))                                # для каждого option методом get_attribute() получаю значение атрибута value и преобразуюю его сразу в число
            except:                                                                     # потребуется, если выбор из (10, 20, 50, все)
                continue
            option.click()                                                              # кликаю по выбранной позиции
            excepting_data.append(val)                                                  # добавляю полученное число в список ожидаемого количества строк
            real_data.append(self.check_count_rows())                                   # ложу в список количество строк из вложенной функции def check_count_rows
        return excepting_data, real_data                                                # возвращаю ожидаемый список и актуальный


class ButtonPage(BasePage):
    locators = ButtonPageLocators()

    """ СПОСОБ 1 - все действия с кнопками происводятся в одной функции"""
    """ Функция click_on_different_buttons проверяет кликабельность трёх кнопок по порядку.
        Для этого:
        1) в зависимости от типа клика(двойной, правой кнопкой и просто клик) получает элемент (локатор кнопки), 
        находящийся в поле видимости, и используя метод ActioChains совершает сооответвующий клик по кнопке
        2) возвращает текст появляющегося сообщения (после успешного нажатия), используя вложенную функцию check_clicked_on_button
    """
    def click_on_different_buttons(self, type_click):
        if type_click == "double":                                          # выбираем тип клика по кнопке
            element = self.element_is_visible(self.locators.DOUBLE_CLICK)   # получаем элемент кнопки
            self.action_double_click(element)                               # делаем двойной клик по кнопке
            result_message = self.element_is_present(self.locators.RESULT_DOUBLE_CLICK)     # получаем вэб элемент сообщения после успешного нажатия на кнопку
            time.sleep(1)
            return result_message.text                                      # возвращаем текст успешного сообщения

        if type_click == "right":                                           # выбираем тип клика по кнопке
            element = self.element_is_visible(self.locators.RIGHT_CLICK)    # получаем элемент кнопки
            self.action_context_click(element)                              # делаем клик правой клавишей мыши по кнопке
            time.sleep(1)
            return self.check_clicked_on_button(self.locators.RESULT_RIGHT_CLICK).text  # возвращаем текст сообщения после успешного нажатиия на кнопку

        if type_click == "click":                                           # выбираем тип клика по кнопке
            self.element_is_visible(self.locators.CLICK_ME).click()          # получаем элемент кнопки и просто кликаем по нему
            time.sleep(1)
            return self.check_clicked_on_button(self.locators.RESULT_CLICK_ME).text     # возвращаем текст сообщения после успешного нажатиия на кнопку

    """ Функция check_clicked_on_button получает элемент в ДОМ дереве. 
        Служит вложенной функцией для поиска вэб элемента результатируещего сообщения в функции click_on_different_buttons
    """
    def check_clicked_on_button(self, element):
        return self.element_is_present(element)

    """ СПОСОБ 2"""
    def double_click(self):
        element = self.element_is_visible(self.locators.DOUBLE_CLICK)       # получаем элемент кнопки
        self.action_double_click(element)                                   # делаем двойной клик по кнопке
        time.sleep(1)
        return self.element_is_present(self.locators.RESULT_DOUBLE_CLICK).text       # возвращаем текст сообщения после успешного нажатия на кнопку

    def right_click(self):
        element = self.element_is_visible(self.locators.RIGHT_CLICK)        # получаем элемент кнопки
        self.action_context_click(element)                                  # делаем клик правой кнопкой
        time.sleep(1)
        return self.element_is_present(self.locators.RESULT_RIGHT_CLICK).text       # возвращаем текст сообщения после успешного нажатия на кнопку

    def simple_click(self):
        element = self.element_is_visible(self.locators.CLICK_ME).click()       # получаем элемент кнопки и кликаем по кнопке
        time.sleep(1)
        return self.element_is_present(self.locators.RESULT_CLICK_ME).text       # возвращаем текст сообщения после успешного нажатия на кнопку


class LinksPage(BasePage):
    locators = LinksPageLocators()

    """ Функция check_new_tab_simple_link проверяет работоспособность ссылки и возвращает запрашиваемую ссылку и 
        ссылку, которая была реально открыта. Буду использовать библиотеку Request, чтобы отправлять запрос к ссылкам и 
        получать статус-код. ДЛя этого:
        1) нахожу ссылку на странице и получаю её атрибут href
        2) посылаю запрос к ссылке посредствам метода библиотеки requests
        3) получаю в ответ статус-код. 
        4) в случае статуса 200 нажимаю на ссылку и переключаюсь на новое окно (метод switch_to.window())
        5) получаю url открытой ссылки (метод current_url)
        6) возвращаю запрашиваемую ссылку и ссылку, которая была реально открыта.
           В ином случае возвращаю запрашиваемую ссылку и статус код
    """
    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)        # нахожу ссылку
        link_href = simple_link.get_attribute('href')           # получаю её атрибут href
        # посылаю запрос к ссылке посредствам метода библиотеки requests и получаю в ответ статус-код
        request = requests.get(link_href)                       # если нужно сломать тест, то ставлю link_href "поломанной" (f"{link_href}bad-request") и получаю else (ссылку и статус-код 400)
        if request.status_code == 200:                          # в случае статуса 200 нажимаю на ссылку
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])     # переключаюсь на новое окно (метод switch_to.window())
            url = self.driver.current_url                       # получаю url открытой ссылки (метод current_url)
            return link_href, url                               # возвращаю запрашиваемую ссылку и ссылку, которая была реально открыта
        else:
            return link_href, request.status_code               # В ином случае возвращаю запрашиваемую ссылку и статус код

    """ Функция check_broken_link проверяет неработоспособную ссылку и возвращает статус-код ссылки (негативный тест - 
        ссылка не должна открываться). 
        Буду использовать библиотеку Request, чтобы отправлять запрос к ссылкам и получать статус-код. 
        ДЛя этого:
        1) посылаю запрос к ссылке посредствам метода библиотеки requests
        2) получаю в ответ статус-код
        3) если статус 200, открываю рабочую ссылку - тест будет провален; 
        4) в ином случае возвращаю статус-код - основной сценария теста"""
    def check_broken_link(self, url):
        request = requests.get(url)                             # посылаю запрос к ссылке посредствам метода библиотеки requests и получаю в ответ статус-код
        if request.status_code == 200:                          # если статус 200
            self.element_is_present(self.locators.BAD_REQUEST).click()  # открываю рабочую ссылку - тест будет провален
        else:
            return request.status_code                          # в ином случае возвращаю статус-код - основной сценария теста

class UploadAndDownloadPage(BasePage):
    locators = UploadAndDownloadPageLocators()

    def check_upload_file(self):
        file_name, path = generated_file()
        self.element_is_visible(self.locators.UPLOAD_FILE).send_keys(path)
        time.sleep(2)
        os.remove(path)
        text = self.element_is_present(self.locators.UPLOAD_RESULT).text
        # print(file_name)
        # print(text)
        return file_name.split('/')[-1], text.split('\\')[-1]

    def check_download_file(self):
        link = self.element_is_present(self.locators.DOWNLOAD_FILE).get_attribute('href')
        # print(link)
        link_b = base64.b64decode(link)
        path_name_file = rf'/Users/kateryna/PycharmProjects/QA_example3/filetest{random.randint(0, 999)}.jpg'
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            os.remove(path_name_file)
        return check_file

class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()
    """ Функция check_enable_button позволяет проверить, что кнопка действительно становится доступной/кликабельной
        только через 5 секунд. Для этого:
    """
    def check_enable_button(self):
        try:
            self.element_is_clickable(self.locators.ENABLE_AFTER_BUTTON, 1)
        except TimeoutException:
            return False
        return True



































