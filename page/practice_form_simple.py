import os
import time

from selenium.webdriver import Keys

from generator.generator import generated_person_for_form, generated_file_for_form
from locators.practice_form_locators_simple import PracticeFormPageLocators
from page.base_page import BasePage

class PracticeFormPage(BasePage):
    locators = PracticeFormPageLocators()
    """
        Функция fill_all_fields позволяет убедиться в том что форма рабочая при помощи наиболее простого способа заполнения 
        без учета выбора каких-то конкретных данных или опций.
        А именно все текстовые поля возможно заполнить, чекбоксы и радио-баттоны можно выбрать (чек-бокс хотя бы 1), 
        файл загрузить, селекты выбора страны и города прокликиваются)
        Для этого:
        1) все текстовые поля заполняются через генератор
        2) радио-баттон выбирается рандомно (локаторы идентичны)
        3) чек-бокс выбирается рандомно и только 1 (локаторы идентичны)
        4) автозаполнение (поле subject) отправляем 1 заранее выбранный - полный текст
        5) файл загружается напрямую в инпут (его путь)
        6) страна и город выбираются простым кликом по пункту, на котором выбор стоит по умолчанию
        """
    def fill_all_fields(self):
        person_info = next(generated_person_for_form())                             # генерируем уникальную персону
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        mobile = person_info.mobile
        current_address = person_info.cur_addr
        file_name, path = generated_file_for_form()                                 # генерируем уникальный файл и его путь
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)     # заполняем поле заранее сгенерированным first_name
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.GENDER).click()                       # кликаем по рандомному радио-баттону (локаторы у них идентичны за исключением номера)
        self.element_is_visible(self.locators.MOBILE).send_keys(mobile)
        self.element_is_visible(self.locators.SUBJECT).send_keys('Economics')       # в поле с автозаполнение просто отправляем полное название одного из предметов, чтобы не формировать словарь и более сложный выбор
        self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES).click()                      # кликаем по рандомному чекбоксу, причем только по одному (локаторы у них идентичны за исключением номера)
        self.element_is_present(self.locators.PICTURE_UPLOAD).send_keys(path)       # отправляем путь созданного файла сразу в инпут поля UPLOAD
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.STATE_SELECT).click()                 # кликом открываем выпадашку выбора страны
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)   # кнопкой RETURN кликаем по выбранному по умолчанию пункту из выпадашки (без создания генератора всех стран и выбора какого-то конкретного пункта)
        time.sleep(1)
        self.element_is_visible(self.locators.CITY_SELECT).click()                  # кликом открываем выпадашку выбора города
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)    # кнопкой RETURN кликаем по выбранному по умолчанию пункту из выпадашки (без создания словаря всех городов, соответсвующих стране и выбора какого-то конкретного пункта)
        time.sleep(1)
        self.remove_footer()                                                        # убираем футер, мешающий нажатиию кнопки
        self.element_is_visible(self.locators.SUBMIT).click()                       # подтверждаем заполнение всех полей формы
        time.sleep(3)
        return [person_info.first_name + ' ' + person_info.last_name, person_info.email, str(person_info.mobile), person_info.cur_addr]
    """
    Функция result_form позволяет выбрать текстовые данные из таблица результатов заполнения формы. Таблица появляется после 
    заполнения и нажатия кнопки "SUBMIT" и должна содержать 10 заполненных полей в столбце "VALUE".
    """
    def result_form(self):
        results = self.elements_are_present(self.locators.OUTPUT_RESULT)
        result_form = []
        for item in results:
            result_form.append(item.text)
        return result_form


