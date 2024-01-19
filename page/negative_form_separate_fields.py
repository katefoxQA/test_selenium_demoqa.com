import time

from selenium.webdriver import Keys

from locators.negative_form_separate_fields_locators import NegativeFormSeparateFieldsPageLocators
from page.base_page import BasePage
from generator.generator import generated_invalid_email

"""
Негативные сценарии заполнения обязательного поля Email.
1) без @
2) без . между именем и доменом
3) нет домена
4) цыфры и спецсимволы в домене
5) в домене менее 2 разрешенных символов
6) в домене более 5 разрешенных символов

"""
class NegativeFormSeparateFieldsPage(BasePage):
    locators = NegativeFormSeparateFieldsPageLocators()

    def w(self):
        self.remove_footer()
        emails = next(generated_invalid_email()).negative_email
        invalid_input = []
        for item in emails:
            email_input = self.element_is_visible(self.locators.EMAIL)
            email_input.send_keys(item)
            self.element_is_visible(self.locators.SUBMIT).click()
            invalid_email_result = self.element_is_present(self.locators.INVALID_EMAIL)
            invalid_input.append(invalid_email_result)
            self.element_is_visible(self.locators.EMAIL).clear()
        return invalid_input, emails
