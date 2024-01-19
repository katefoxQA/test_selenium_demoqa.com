from selenium.webdriver.common.by import By

class AccordianPageLocators:
    SECTION_FIRCT = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    SECTION_FIRCT_CONTENT = (By.CSS_SELECTOR, 'div[id="section1Content"] p')
    SECTION_SECOND = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECTION_SECOND_CONTENT = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    SECTION_THIRD = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    SECTION_THIRD_CONTENT = (By.CSS_SELECTOR, 'div[id="section3Content"] p')

class AutoCompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_VALUE = (By.CSS_SELECTOR, 'div[class="css-12jo7m5 auto-complete__multi-value__label"]')
    MULTI_REMOVE = (By.CSS_SELECTOR, 'svg[class="css-19bqh2r"]')
    SINGLE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')


    MULTI_ALL_REMOVE = (By.CSS_SELECTOR, 'div[aria-hidden="true"]')

class DatePickerPageLocators:
    DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
    DATE_AND_TIME_DAY_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day--"]')
    DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]')
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-option"]')

class SliderPageLocators:
    SLIDER_INPUT = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')

class ProgresBarPageLocators:
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, 'div[id="progressBar"] div[class="progress-bar bg-info"]')
    PROGRESS_BAR_BUTTON = (By.CSS_SELECTOR, 'button[id="startStopButton"]')

class TabsPageLocators:
    WHAT_BUTTON = (By.CSS_SELECTOR, 'a[id="demo-tab-what"]')
    WHAT_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-what"]')
    ORIGIN_BUTTON = (By.CSS_SELECTOR, 'a[id="demo-tab-origin"]')
    ORIGIN_CONTENT = (By.CSS_SELECTOR, 'div[class="fade tab-pane active show"]')
    USE_BUTTON = (By.CSS_SELECTOR, 'a[id="demo-tab-use"]')
    USE_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-use"]')



class ToolTipsPageLocators:
    """
    1. нахожу сам объект
    2. объект при появлении подсказки (класс появляется только при наведении и удерживании курсора)
    3. текст подсказок
    """
    BUTTON = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    # TOOL_TIP_BUTTON = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')
    FIELD = (By.XPATH, '//input[@id="toolTipTextField-----"]')
    # TOOL_TIP_FIELD = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')
    CONTRARY_LINK = (By.XPATH, '//a[text()="Contrary----"]')
    # TOOL_TIP_CONTRARY_LINK = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')
    LINK = (By.XPATH, '//a[text()="1.10.32"]')
    # TOOL_TIP_LINK = (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')

    # текст подсказок
    TOOL_TIP_INNERS = (By.XPATH, '//div[@class="tooltip-inner"]')

class MenuPageLocators:
    MENU_ITEM_LIST = (By.CSS_SELECTOR, 'ul[id="nav"] li a')

