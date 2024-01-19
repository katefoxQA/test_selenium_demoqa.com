from page.negative_form_separate_fields import NegativeFormSeparateFieldsPage


class TestNegativePracticeForm:
    """
    Развёрнутый негативный тест проверяет невозможность отправки формы .
    Тест предполагает:
    1)
    """
    def test_negative_practice_form(self, driver):
        negative_form_separate_fields = NegativeFormSeparateFieldsPage(driver, 'https://demoqa.com/automation-practice-form')
        negative_form_separate_fields.open()
        invalid_input_email, negative_email = negative_form_separate_fields.w()
        print(negative_email)
        print(invalid_input_email)
        assert invalid_input_email[0] is not None
        assert invalid_input_email[1] is not None
        assert invalid_input_email[2] is not None
