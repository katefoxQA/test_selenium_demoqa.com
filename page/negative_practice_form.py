from locators.negative_practice_form_locators import NegativePracticeFormPageLocators
from page.base_page import BasePage

"""Работа валидации формы и обязательных полей при попытке отправки формы со всеми незаполненными полями
"""
class NegativePracticeFormPage(BasePage):
    locators = NegativePracticeFormPageLocators()
    """Функция not_fill_all_text_fields необходима для подтвержения отправки формы со всеми незаполненными полями.
    Для этого: 
    1) все поля НЕ заполняются
    2) нажимаем кнопку SUBMIT
    """
    def not_fill_all_text_fields(self):
        self.remove_footer()
        self.element_is_visible(self.locators.SUBMIT).click()

    """Функция check_novalidate_form определяет проходит ли вся форма валидацию при всех НЕ заполненных полях.
    Для этого:
    1) найти вэб элемент формы с появившемся при данных условиях классом class="was-validated"
    """
    def check_novalidate_form(self):
        return self.element_is_present(self.locators.NOVALIDATED_FORM)

    """Функция check_invalid_necessary_fields позволяет:
        1) определить все невалидные обязательные поля в форме
        2) определяет их количество
        3) найти текст подсказок в невалидных текстовых полях
        4) найти лэйблы у невалидных чекбоксов 
    """
    def check_invalid_necessary_fields(self):
        invalid_fields = self.elements_are_present(self.locators.INVALID_NECESSARY_FILDS)                # спилск невалидных обязательных полей
        count_invalid_fields = len(invalid_fields)                                                       # количество невалидных обязательных полей
        invalid_text_necessary_fields = self.elements_are_present(self.locators.INVALID_TEXT_FILDS)      # спислк невалидных вэб элементов текстовых обязательных полей
        data_text = []
        for item in invalid_text_necessary_fields:
            data_text.append(item.get_attribute('placeholder'))                                          # список текстовых подсказок в невалидных полях
        invalid_radio_necessary_fields = self.elements_are_present(self.locators.INVALID_RADIO_GENDER)
        data_radio_gender = []
        for item in invalid_radio_necessary_fields:
            data_radio_gender.append(item.text)                                                          # список текстовых подсказок для чекбоксов
        return count_invalid_fields, data_text, data_radio_gender                                        # возвращает кол-во невалидных полей, списки текстовых подсказок в текстовых полях и чек-боксах

