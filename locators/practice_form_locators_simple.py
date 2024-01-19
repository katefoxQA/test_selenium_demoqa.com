import random
from selenium.webdriver.common.by import By

class PracticeFormPageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    GENDER = (By.CSS_SELECTOR, f'div[class*="custom-control"] label[for="gender-radio-{random.randint(1,3)}"]')
    MOBILE = (By.CSS_SELECTOR, 'input[id="userNumber"]')
    DATE_SELECT_INPUT = (By.CSS_SELECTOR, 'input[id="dateOfBirthInput"]')
    SUBJECT = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    HOBBIES = (By.CSS_SELECTOR, f'div[class*="custom-control"] label[for="hobbies-checkbox-{random.randint(1,3)}"]')
    PICTURE_UPLOAD = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    STATE_SELECT = (By.CSS_SELECTOR, 'div[id="state"]')
    STATE_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    CITY_SELECT = (By.CSS_SELECTOR, 'div[id="city"]')
    CITY_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    OUTPUT_RESULT = (By.XPATH, '//div[@class="table-responsive"]//td[2]')