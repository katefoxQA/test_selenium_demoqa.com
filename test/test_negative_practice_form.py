import time
from page.negative_practice_form import NegativePracticeFormPage

class TestNegativePracticeForm:
    """
    Простой негативный тест проверяет невозможность отправки формы без заполнения всех обязательных полей.
    Тест предполагает:
    1) что проверяем только 6 обязательных полей (3 текстовых и выбор пола - 3шт) на невалидность при их НЕ заполнении
    2) при попытке отправить незаполненную форму нажав на кнопку SUBMIT, форма станет невалидной
    3) также при незаполненных всех (в т.ч. обязательных) полях и клику по кнопке SUBMIT количество невалидных полей будет составлять 6 шт
    4) также при этих условиях наименование невалидных полей совпадёт с перечнем обязательных полей для валидации по ТЗ
    """
    def test_negative_practice_form(self, driver):
        negative_practice_form = NegativePracticeFormPage(driver, 'https://demoqa.com/automation-practice-form')
        negative_practice_form.open()
        negative_practice_form.not_fill_all_text_fields()                       # нажимаем на кнопку SUBMIT при НЕ заполненных всех полях формы (в т.ч. обязательных)
        time.sleep(2)
        novalidate_form = negative_practice_form.check_novalidate_form()        # находим элемент - у невалидной формы появляется class="was-validated"
        # нахожу невалидные обязательные поля формы (их количество, placeholder текстовых полей, label чекбоксов пола)
        count_invalid_fields, invalid_text_necessary_fields, invalid_radio_necessary_fields = negative_practice_form.check_invalid_necessary_fields()
        # Проверка 1 - становится ли вся форма невалидной (есть ли элемент форма с классом class="was-validated")
        assert novalidate_form is not None, 'Валидация формы не сработала, у элемента form не появился класс class="was-validated"'
        # Проверка 2 - соответствует ли фактическое количество полей, не прошедших валидацию, требуемому по ТЗ (6 полей)
        assert count_invalid_fields == 6, 'Не совпадает количество ожидаемых и фактически не прошедших валидацию полей формы'
        # Проверка 3 - совпадают ли фактические полученные тексты подсказок в незаполненных обязатедьных полях с требуемыми по ТЗ
        assert invalid_text_necessary_fields + invalid_text_necessary_fields == ['First Name', 'Last Name', 'Mobile Number', 'Male', 'Female', 'Other'], 'Текст полученных подсказок в незаполненных полях формы не совпадает с требуемыми текстами по ТЗ'


