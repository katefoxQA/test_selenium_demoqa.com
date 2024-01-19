from selenium.webdriver.common.by import By

class TextBoxPageLocators:

    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')

# class CheckBoxPageLocators:
#     EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
#     # ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
#     ITEM_LIST_LEAF = (By.XPATH, '//*[@class="rct-node rct-node-leaf"]//span[@class="rct-title"]')
#     CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
#     TITLE_ITEM = (By.XPATH, "../../span[@class='rct-title']")
#     OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')

class CheckBoxPageLocators:
    OPEN_LIST = (By.CSS_SELECTOR, "button[title='Expand all']")

    """ Шаг 1 - находим нужные чекбоксы для клика по ним"""
    ITEM_CHECKBOX = (By.CSS_SELECTOR, 'span[class="rct-title"]')          # можно так  'span.rct-title'
    # ITEM_LIST_LEAF = (By.XPATH, '//*[@class="rct-node rct-node-leaf"]//span[@class="rct-title"]')   # только по внутренним чекбоксам
    # ITEM_CHECKBOX1 = (By.CSS_SELECTOR, 'label[for="tree-node-{}"]')      # нужно определить чем отличаются локаторы и использовать гнезда
    # ITEM_CHECKBOX2 = (By.CSS_SELECTOR, 'label[for="tree-node-private"]')
    # ITEM_CHECKBOX3 = (By.CSS_SELECTOR, 'label[for="tree-node-wordFile"]')

    """ Шаг 2. СПОСОБ 1 - находим отмеченные чекбоксы и в этом списке далее ищем названия чекбоксов"""
    # CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")         # выделенные чекбоксы   'svg.rct-icon.rct-icon-check'
    CHECKED_ITEMS = (By.XPATH, '//*[local-name()="svg" and contains(@class, "rct-icon-check")]')
    """ находим текст элементов по ПРЕДВАРИТЕЛЬНО НАЙДЕННЫМ выделенным чекбоксам"""
    # TITLE_CHECKBOXES1 = (By.XPATH, '../../span[@class="rct-title"]')
    # TITLE_CHECKBOXES1 = (By.XPATH, 'ancestor::*[contains(@for, "tree-node-")]/descendant::*[@class="rct-title"]')
    TITLE_CHECKBOXES1 = (By.XPATH, 'following::*[@class="rct-title"]')
    # TITLE_CHECKBOXES1 = (By.XPATH, './/ancestor::span[@class="rct-text"]')     # использовалось в видео

    """ СПОСОБ 2 - Когда сразу ищу текст выделенных чекбоксов, минуя предварительный поиск самих галочек на чекбоксах"""
    TITLE_CHECKBOXES2 = (By.XPATH, '//*[local-name()="svg" and contains(@class, "rct-icon-check")]/../../span[@class="rct-title"]')
    # это поиск через предков текущего узла (по условию) и потом от него уже через уго потомков по нужному классу
    # TITLE_CHECKBOXES2 = (By.XPATH, '//*[local-name()="svg" and contains(@class, "rct-icon-check")]/ancestor::*[contains(@for, "tree-node-")]/descendant::*[@class="rct-title"]')
    # это следующий узел за текущим и внутри него по искомому классу
    # TITLE_CHECKBOXES2 = (By.XPATH, '//*[local-name()="svg" and contains(@class, "rct-icon-check")]/following::*[@class="rct-title"]')

    """ Шаг 3 - находим результаты вводимых данных в ДОМ дереве (в аутпутах)"""
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span.text-success')         # 'span[class="text-success"]' можно так


class RadioPageLocators:
    # ITEM_RADIO_BUTTONS = (By.CSS_SELECTOR, 'label[class*="custom-control-label"]')     # для простого варианта с циклом

    YES_RADIO = (By.CSS_SELECTOR, 'label[class*="custom-control-label"][for="yesRadio"]')
    IMPRESSIVE_RADIO = (By.CSS_SELECTOR, 'label[class*="custom-control-label"][for="impressiveRadio"]')
    NO_RADIO = (By.CSS_SELECTOR, 'label[class*="custom-control-label"][for="noRadio"]')

    CHECKED_RADIO = (By.CSS_SELECTOR, "div input[name='like']")

    OUTPUT_RADIO = (By.CSS_SELECTOR, 'p span[class="text-success"]')

class WebTableLocators:
    # add person
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # table
    FULL_PERSON_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')                #  полный список всех людей в таблице (вместе с пустыми строками)
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')                       # поле поиска человека в таблице
    DELETE_BUTTON = (By.XPATH, '//span[@title="Delete"]')                           # нахожу кнопку delete, которая есть у строки с данными результатов поиска
    PARENT_ROW = (By.XPATH, 'ancestor::div[@class="rt-tr -odd"]')                   # нахожду строку предка со всеми данными результатов поиска (использую затем для find_element в функции)
    ROW_SEARCH_RESULT = (By.XPATH, '//span[@title="Delete"]/ancestor::div[@class="rt-tr -odd"]')       # сразу строка результатов поиска (полный путь по Xpath)
    NO_PERSON = (By.XPATH, '//div[@class="rt-noData"]')                             # сообщение об отсутствии искомого человека "No rows found"
    SELECT_COUNT_ROW = (By.XPATH, '//select[@aria-label="rows per page"]')

    # update
    UPDATE_BUTTON = (By.XPATH, '//span[@title="Edit"]')                             # кнопка update (карандаш) для внесения изменений в даннные по человеку
    SELECTING_COUNT_ROWS = (By.XPATH, "//option[contains(text(), ' rows')]")

class ButtonPageLocators:
    # buttons
    DOUBLE_CLICK = (By.XPATH, '//button[text() ="Double Click Me"]')
    RIGHT_CLICK = (By.XPATH, '//button[text()="Right Click Me"]')
    CLICK_ME = (By.XPATH, '//button[text()="Click Me"]')

    # result
    RESULT_DOUBLE_CLICK = (By.XPATH, '//p[@id="doubleClickMessage"]')
    RESULT_RIGHT_CLICK = (By.XPATH, '//p[@id="rightClickMessage"]')
    RESULT_CLICK_ME = (By.XPATH, '//p[@id="dynamicClickMessage"]')

class LinksPageLocators:
    SIMPLE_LINK = (By.XPATH, '//a[@id="simpleLink"]')
    BAD_REQUEST = (By.XPATH, '//a[@id="bad-request"]')
    RESPONCE = (By.XPATH, '//b[text()="Bad Request"]')


class UploadAndDownloadPageLocators:
    UPLOAD_FILE = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    UPLOAD_RESULT = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')

    DOWNLOAD_FILE = (By.CSS_SELECTOR, 'a[id="downloadButton"]')

class DynamicPropertiesPageLocators:
    ENABLE_AFTER_BUTTON = (By.CSS_SELECTOR, 'button[id="enableAfter"]')

