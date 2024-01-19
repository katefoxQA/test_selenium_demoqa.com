from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        element = None
        try:
            element = WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
            """ Если я хочу провести функциональные проверкии с soft assertion для локаторов. 
                Будут выполнены все шаги, до того как тест упадет на soft assertion для локаторов.
                """
            assert element is not None
        except TimeoutException:
            print(f"  Вэб-элемент отсутствует в DOM страницы {locator}")
            # pass
            """ Если я хочу сразу проверить локаторы без дальнейших функциональных проверок:
                Заваливается с AssertionError, как только не будет найден нужный вэб-элемент
                с конкретным указанием метода by и локатора."""
            # assert element is not None, f"  Вэб-элемент отсутствует в DOM страницы {locator}"
        return element



    def elements_are_present(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_context_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def action_drug_and_drop_by_offset(self, element, x_coord, y_coord):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_coord, y_coord)
        action.perform()

    def action_drag_and_drop_to_element(self, what, where):
        action = ActionChains(self.driver)
        action.drag_and_drop(what, where)
        action.perform()

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script('document.getElementById("fixedban").style.display="none"')




