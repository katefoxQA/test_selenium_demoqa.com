from selenium.webdriver.common.by import By

class PracticeFormPageLocators:
    # text fields
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    MOBILE = (By.CSS_SELECTOR, 'input[id="userNumber"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')

    # gender radio-button
    GENDER_MALE = (By.CSS_SELECTOR, 'label[class="custom-control-label"][for="gender-radio-1"]')
    GENDER_FEMALE = (By.CSS_SELECTOR, 'label[class="custom-control-label"][for="gender-radio-2"]')
    GENDER_OTHER = (By.CSS_SELECTOR, 'label[class="custom-control-label"][for="gender-radio-3"]')
    GENDER_LIST = (By.CSS_SELECTOR, 'label[class="custom-control-label"][for*="gender-radio"]')
    CHECKED_RADIO = (By.CSS_SELECTOR, 'div input[name="gender"]')

    # date select
    DATE_SELECT_INPUT = (By.CSS_SELECTOR, 'input[id="dateOfBirthInput"]')
    MONTH_SELECT = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    MONTH_LIST = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"] option')
    YEAR_SELECT = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    YEAR_LIST = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"] option')
    DAY_SELECT_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month"] div[class*="react-datepicker__day"] ')

    # subject multicomplite
    SUBJECT_INPUT = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    SUBJECT_LIST = (By.CSS_SELECTOR, 'div[class="css-12jo7m5 subjects-auto-complete__multi-value__label"]')

    # hobbies check-box
    HOBBIES_LIST = (By.CSS_SELECTOR, 'div[id="hobbiesWrapper"] label[class="custom-control-label"]')


    # upload file
    PICTURE_UPLOAD = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')

    #
    STATE_INPUT_BEFORE = (By.CSS_SELECTOR, 'div[id="state"]')
    STATE_LIST = (By.CSS_SELECTOR, 'div[class =" css-26l3qy-menu"] div[id*="-option-"]')
    STATE_INPUT_AFTER = (By.XPATH, '//div[@class=" css-1uccc91-singleValue"]')

    # < div class =" css-26l3qy-menu" >
    #     < div class =" css-11unzgr" >
    #         < div class =" css-yt9ioa-option" id="react-select-17-option-0" tabindex="-1" > NCR < /div >
    #         < div class =" css-9gakcf-option" id="react-select-17-option-1" tabindex="-1" > Uttar Pradesh < /div >
    #         < div class =" css-yt9ioa-option" id="react-select-17-option-2" tabindex="-1" > Haryana < /div >
    #         < div class =" css-yt9ioa-option" id="react-select-17-option-3" tabindex="-1" > Rajasthan < /div >

    CITY_INPUT_BEFORE = (By.CSS_SELECTOR, 'div[id="city"]')
    CITY_LIST = (By.CSS_SELECTOR, 'div[class =" css-26l3qy-menu"] div[id*="-option-"]')
    CITY_INPUT_AFTER = (By.XPATH, '//div[@id="city"]//div[@class=" css-1uccc91-singleValue"]')

# <div class=" css-26l3qy-menu">
#     <div class=" css-11unzgr">
#         <div class=" css-1n7v3ny-option" id="react-select-18-option-0" tabindex="-1">Agra</div>
#         <div class=" css-yt9ioa-option" id="react-select-18-option-1" tabindex="-1">Lucknow</div>
#         <div class=" css-yt9ioa-option" id="react-select-18-option-2" tabindex="-1">Merrut</div>

    # button
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # output
    OUTPUT_RESULT = (By.XPATH, '//div[@class="table-responsive"]//td[2]')