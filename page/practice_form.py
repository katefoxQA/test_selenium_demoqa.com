import os
import random
import time

from selenium.webdriver import Keys

from locators.practice_form_locators import PracticeFormPageLocators
from page.base_page import BasePage
from generator.generator import generated_person_for_form, generated_date, generated_subject, generated_state, \
    generated_city1, generated_city2, generated_city3, generated_city4, generated_file_for_form
from selenium.webdriver.support.select import Select

class PracticeFormPage(BasePage):
    locators = PracticeFormPageLocators()
    """
    Функция fill_all_text_fields позволяет заполнить все текстовые поля формы в порядке расположения заранее сгенерированными 
    тестовыми данными. Возвращает данные, которые были введены в соответствующие поля формы.
    Для этого:
    1) генерируем персону (имя, фамилия, эмейл, телефон и адрес)
    2) отправялем сгенерированные данные в инпуты соответсвующих полей
    3) возвращаю отправленные данные для дальнейшего сравнения с теми, что будут получены из таблицы результатов
    """
    def fill_all_text_fields(self):
        person_info = next(generated_person_for_form())                                     # генерируем уникальную персону
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        mobile = person_info.mobile
        current_address = person_info.cur_addr
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)             # заполняем поле заранее сгенерированным first_name
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.MOBILE).send_keys(mobile)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        time.sleep(5)
        return [first_name + ' ' + last_name, email, str(mobile), current_address]
    """
    Функция choice_radiobutton позволяет выбрать конкретный пол для персоны (радио-баттон). 
    Для этого создаю словарь с ключом gender и значением локатор элемента. Выбор ключа в тесте в соответсвии с задачей тест-кейса.
    """
    def choice_radiobutton(self, choice):
        choices = {'male': self.locators.GENDER_MALE,
                   'female': self.locators.GENDER_FEMALE,
                   'other': self.locators.GENDER_OTHER}
        self.element_is_visible(choices[choice]).click()
        time.sleep(3)

    """
        Функция radio_is_checked позволяет определить какой именно радио-баттон был фактически выбран и сколько осталось невыбранных. 
        ВАЖНО: выбрать должно быть возможно только один, соответственно из 3х два должны остаться невыбранными.
        Для этого:
        1) нахожу все элементы (по инпуту) с name 'gender'
        2) прохожусь по списку циклом нахожу выбранный элемент 
        3) определяю количество радио-баттонов, которые остались невыбранными 
        4) возвращаю эти два параметра для дальнейшей проверки
        """
    def radio_is_checked(self):
        checked_radio = self.elements_are_present(self.locators.CHECKED_RADIO)          # нахожу все элементы (по инпуту) с name 'gender'
        i = []
        for radio in checked_radio:                                                     # прохлжусь по списку элементов циклом
            i.append(radio.is_selected())                                              # нахожу выбранный элемент с помощью функции is_selected()
            if radio.is_selected() == True:
                text = radio.get_attribute('value')
        n = i.count(False)                                                              # определяю количество радио-баттонов, которые остались невыбранными (False)
        return i, n, text
    """
    Функция select_date позволяет выбрать месяц, год и число месяца по календарю в соответствии с заране сгенерированной датой.
    Для этого:
    1) генерируется год, месяц и число
    2) открываем календарь с селектами 
    3) для выбора месяца используется вспомогательная функция на основе select()  (возможность заложена в верстке)
    34 затем выбирается год с использование селекта (возможность заложена в верстке)
    5) выбирается дата - циклом проходимся по списку до совпадения значения с заранее сгенерированным (в верстке нет селектов)
    6) получаем значение выбранной даты из поля input 'Date of Birth'
    7) возвращаем полученную дату
    """
    def select_date(self):
        date = next(generated_date())                                                           # генерируем дату
        input_date = self.element_is_visible(self.locators.DATE_SELECT_INPUT)                   # находим поле ввода даты
        input_date.click()                                                                      # кликаем для открытия календаря
        time.sleep(1)
        self.selecting_date(self.element_is_present(self.locators.MONTH_SELECT), date.month)    # используя вспомогательную функцию выбираем селектом желаемый месяц
        self.selecting_date(self.element_is_present(self.locators.YEAR_SELECT), date.year)      # используя вспомогательную функцию выбираем селектом желаемый год
        self.selecting_day_from_list(self.locators.DAY_SELECT_LIST, date.day)                   # используя вспомогательную функцию выбираем  желаемое число месяца (без использования селекта)
        new_date = input_date.get_attribute('value')                                            # получаем выбраннуюю дату из поля 'Date of Birth'
        return new_date

    """Вспомогательная функция для селекта месяца и года"""
    def selecting_date(self, element, text):
        select = Select(element)                                # передаю селекту элемент
        select.select_by_visible_text(text)                     # применяю функциию селекта "выбор по видимому тексту"
        time.sleep(2)
    """Вспомогательная функция для выбора числа в календаре (без селекта)"""
    def selecting_day_from_list(self, element, value):
        item_list = self.elements_are_present(element)          # Список элементов нахожу в ДОМ-дереве
        if value[0] == '0':                                     # Для сгенерированного числа месяца обрезаю 0 стоящий вначале (для вариантов 03 сгенерированного числа,т.к. в календаре числа без 0 впереди)
            value = value[1:]
        for item in item_list:                                  # прохожусь циклом по найденному списку
            # print("item.text=", item.text, item.text.__class__, value, value.__class__)                    # проверяю весь список, чтоб увидеть на каком элементе цикл прерветсяи к какому типу относится переменная
            if item.text == value:                              # момент совпадения с заранее сгенерированным значением
                item.click()                                    # выбираю элемент
                time.sleep(2)
                break                                           # прерываю цикл

    """
    Функция multicomplite_of_subject позволяет заполнить поле 'Subjects' несколькими рандомно выбранными предметами 
    в соответсвии с задачей тест-кейса.
    Для этого: 
    1) рандомно выбираю от 1 до 4х предметов из сгенерированного списка 
    2) наименование каждого отправляю в поле инпута 
    3) подтверждаю выбор ENTER
    4) возвращаю список сгенерированных предметов
    """
    def multicomplite_of_subject(self):
        any_subjects = next(generated_subject()).subject_name                           # генерирую список предметов
        subjects = random.sample(any_subjects, k=random.randint(1, 4))                  # рандомно выбираю от 1 до 4х уникальных предметов из сгенерированного списка
        for subject in subjects:
            input_multi = self.element_is_clickable(self.locators.SUBJECT_INPUT)        # нахожу поле для ввода subject
            input_multi.send_keys(subject)                                              # наименование каждого отправляю в поле инпута
            input_multi.send_keys(Keys.ENTER)                                           # подтверждаю выбор ENTER
            time.sleep(1)
        return subjects                                                                 # возвращаю список сгенерированных предметов
    """
        Функция check_subject позволяет проверить какие именно предметы были выбраны.
        Для этого: 
        1) формирую список выбранных элементов (предметов), которые отображаются в поле 'Subjects'
        2) возвращаю список наименований этих предметов
        """
    def check_subject(self):
        result_list_subjects = self.elements_are_present(self.locators.SUBJECT_LIST)        # нахожу все выбранные элементы subject
        result_subject = []
        for subject in result_list_subjects:
            result_subject.append(subject.text)                                             # формирую список наименований по этим элементам
        return result_subject

    """
    Функция click_hobbies_checkbox позволяет в рандомном порядке прокликать определёное количество чек-боксов.
    Принципиально ВАЖНО, чтобы наименование чекбоксов при выборе было разным.
    Возвращает список прокливанных наименований.
    
    Что бы избежать повторного клика по ранее выбранному чекбоксу использую:
    ВАРИАНТ 1 - random.sample 
    random.sample(population, k, counts=None), 
    где population — некоторый интервал, k — размер выборки, counts — максимальное количество повторений (по умолчанию 0)
    ВАРИАНТ 2 - наполнение сета set() при помощи random.choice() - в итоге повторений - 0
    random.choice(hobbies_list, k=1),
    где population — некоторый интервал, k — количество выбираемых случайных элементов
    """
    def click_hobbies_checkbox(self):
        """Вариант 1 - использую random.sample (повторений 0)"""
        hobbies_list = self.elements_are_visible(self.locators.HOBBIES_LIST)                # нахожу все элементы hobbies
        hobbies = random.sample(hobbies_list, k=2, counts=None)                             # рандомно выбираю два неповторяющихся hobbies
        checked_hobbies = []
        for item in hobbies:
            item.click()
            checked_hobbies.append(item.text)                                               # текст кликнутого элемента добавлю в список
            time.sleep(1)
        return checked_hobbies
        """Вариант 2 - использую сет set() обеспечивает отсутствие повторений и random.choice()"""
        # hobbies_list = self.elements_are_visible(self.locators.HOBBIES_LIST)              # нахожу все элементы hobbies
        # checked_hobbies = []                                                              # создаю пустой список выбранных hobbies
        # to_check = set()                                                                  # создаю пустой набор set для наполнения рандомно выбранными неповторяющиимися  hobbies
        # while len(to_check) < 2:                                                          # сет нужен из 2х пунктов
        # hobbies = random.choice(hobbies_list, k=1)                                        # по умолчанию k=1 (количество выбираемых случайных элементов)
        #     to_check.add(hobbies)                                                         # наполняю сет
        # for item in to_check:                                                             # прохожусь по каждому hobbies из уникального сета
        #     item.click()                                                                  # прокликиаю
        #     checked_hobbies.append(item.text)                                             # текст кликнутого элемента добавлю в список
        #     print(item.text)
        #     time.sleep(1)
        # return checked_hobbies                                                            # возвращаю список выбранных hobbies

    """Функция upload_file позволяет загрузить файл (используя путь) напрямую в поле инпута
    """
    def upload_file(self):
        file_name, path = generated_file_for_form()                                     # генерируем новый файл, его путь
        self.element_is_visible(self.locators.PICTURE_UPLOAD).send_keys(path)           # передаю путь файла напрямую в поле input 'Select picture'
        time.sleep(2)
        os.remove(path)                                                                 # почистили
        # print(file_name.split('/')[-1])
        # print(path)
        return file_name.split('/')[-1]                                                 # возвращаю наименование файла (обрезанное только до самого нащвания с расширение)

    """Функция change_state позволяет выбрать срану из выпадающего списка в соответствии 
        с заранее сгенерированным наименованием. Для этого:
        1) находим поле выбора с выпадашкой и кликаем
        2) генерируем одно название страны
        3) выбираем страну из списка, совпадающую со сгенерированной, используя вспомогательную функцию selecting_state_from_list
        6) получаем наименование  выбранной страны из поля выбора
        7) возвращаем наименование  выбранной страны"""
    def change_state(self):
        self.remove_footer()
        state_input = self.element_is_visible(self.locators.STATE_INPUT_BEFORE)         # Нахожу поле строки выбора сраны
        state_input.click()                                                             # Кликаю для открытия выпадающего списка
        time.sleep(1)
        states = next(generated_state()).state_name
        any_state = random.sample(states, k=1)[0]                                       # Рандомно выбираем один город из сгенерированного списка
        # print('Сгенерированная страна:  ', any_state)
        self.selecting_state_from_list(self.locators.STATE_LIST, any_state)             # Запускаю функцию выбора страны
        new_state = self.element_is_visible(self.locators.STATE_INPUT_AFTER).text       # Получаю наименование выбранной страны из строки выбора
        # print('Выбранная страна:  ', new_state)
        return new_state                                                                # Возвращаю наименование выбранной страны

    """Вспомогательная функция selecting_state_from_list нужна для выбора страны из списка, совпадающей со сгенерированной.
        Для этого:
        1) находим список выпадающих элементов - названий стран
        2) для каждой страны из списка проверяем на соответствие наименованию заранее сгенерированной
        3) при совпадении кликаю по этой стране и выхожу из цикла"""
    def selecting_state_from_list(self, element, any_state):
        item_list = self.elements_are_visible(element)              # Список элементов нахожу в ДОМ-дереве
        # print("item_list", item_list, item_list.__class__)
        for item in item_list:                                      # прохожусь циклом по найденному списку
            # print(f"item.text=!{item.text}! *{any_state}*")         # проверяю весь список, чтоб увидеть на каком элементе цикл прервется
            if item.text == any_state:                              # момент совпадения с заранее сгенерированным значением
                item.click()                                        # выбираю элемент
                time.sleep(2)
                break                                               # прерываю цикл

    """Функция change_city позволяет выбрать город из выпадающего списка в соответствии 
        с заранее сгенерированным наименованием. 
        ПРИМЕЧАНИЕ: каждой стране соответствует свой список городов. А само поле выбора активно только при уже выбранной стране.
        Для этого:
        1) находим поле выбора города с выпадашкой и кликаем
        2) генерируем одно название города с помощью словаря соответсвия 'страна-список городов'
        3) выбираем город из списка, совпадающий со сгенерированным, используя вспомогательную функцию selecting_city_from_list
        6) получаем наименование  выбранного города из поля выбора
        7) возвращаем наименование  выбранного города"""
    def change_city(self, state_city_num):
        city_input = self.element_is_visible(self.locators.CITY_INPUT_BEFORE)           # Нахожу поле строки выбора
        city_input.click()                                                              # Кликаю для открытия выпадающего списка
        time.sleep(2)
        """Словарь для генерирования списка городов в соответствиии со страной"""
        state_city = {
            'NCR':
                {'cities': next(generated_city1()).city_name},
            'Uttar Pradesh':
                {'cities': next(generated_city2()).city_name},
            'Haryana':
                {'cities': next(generated_city3()).city_name},
            'Rajasthan':
                {'cities': next(generated_city4()).city_name}
        }
        any_city = random.sample(state_city[state_city_num]['cities'], k=1)[0]            # Рандомно выбираем один город из сгенерированного списка
        # print('Сгенерированный город:  ', any_city)
        self.selecting_city_from_list(self.locators.CITY_LIST, any_city)                  # Запускаю функцию выбора города()
        new_city = self.element_is_visible(self.locators.CITY_INPUT_AFTER).text           # Получаю наименование выбранного города из строки выбора
        # print('Выбранный город:  ', new_city)
        return new_city                                                                   # Возвращаю наименование выбранного города

    """Вспомогательная функция selecting_city_from_list нужна для выбора города из списка, совпадающего со сгенерированным.
        Для этого:
        1) находим список выпадающих элементов - названий городов
        2) для каждого города из списка проверяем на соответствие наименованию заранее сгенерированному
        3) при совпадении кликаю по этому городу и выхожу из цикла"""
    def selecting_city_from_list(self, element, any_city):
        item_list = self.elements_are_visible(element)              # Список элементов нахожу в ДОМ-дереве
        # print("item_list", item_list, item_list.__class__)
        for item in item_list:                                      # прохожусь циклом по найденному списку
            # print(f"item.text=!{item.text}! *{any_city}*")         # проверяю весь список, чтоб увидеть на каком элементе цикл прервется
            if item.text == any_city:                              # момент совпадения с заранее сгенерированным значением
                item.click()                                        # выбираю элемент
                time.sleep(2)
                break                                               # прерываю цикл

    """Функция click_submit подтверждения заполнения всех полей формы. Становится кликабельной только при заполнении всех полей.
    """
    def click_submit(self):
        self.element_is_visible(self.locators.SUBMIT).click()

    """Функция check_result позволяющая получить результаты заполнения всех полей формы из итоговой таблицы результатов.
        Таблица появляется только после заполнения всех полей.
    """
    def check_result(self):
        result_list = self.elements_are_visible(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return data