from selenium.webdriver.common.by import By
import random

class NegativeFormSeparateFieldsPageLocators:
    # Necessary fields
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    GENDER = (By.CSS_SELECTOR, f'div[class*="custom-control"] label[for="gender-radio-{random.randint(1, 3)}"]')
    MOBILE = (By.CSS_SELECTOR, 'input[id="userNumber"]')

    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # Invalid necessary fields
    NOVALIDATED_FORM = (By.CSS_SELECTOR, 'form[class="was-validated"]')             # вся форма невалидна (незаполнены обязательные поля/некорректное заполнение об.полей)
    INVALID_NECESSARY_FILDS = (By.CSS_SELECTOR, 'input:invalid')                    # невалидные обязательные поля (инпуты)
    INVALID_TEXT_FILDS = (By.CSS_SELECTOR, 'input:invalid[type="text"]')            # невалидные только ТЕКСТОВЫЕ обязательные поля (инпуты)

    INVALID_RADIO_GENDER = (By.CSS_SELECTOR, 'input:invalid~.custom-control-label') # невалидные обязательные radio=buttons (текст из label)

    INVALID_EMAIL = (By.CSS_SELECTOR, '.form-control:invalid#userEmail')
    INVALID_EMAIL1 = (By.CSS_SELECTOR, '.input:invalid[id="userEmail"]')

    # Valid necessary fields
    VALID_EMAIL = (By.CSS_SELECTOR, '.form-control:valid#userEmail')
    VALID_EMAIL1 = (By.CSS_SELECTOR, 'input:valid[id="userEmail"]')