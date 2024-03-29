import time

from page.practice_form import PracticeFormPage


class TestPracticeForm:
    """
    Развернутый позитивный тест успешного заполнения формы и получения валидных результатов.
    Тест предполагает:
    1) заполнение всех текстовых полей заранее сгенерированными данными персоны и их полное совпадение с данными из таблицы результатов
    2) выбор только одного определённого радио-баттона 'gender' при остальных невыбранных и его совпадение с наименованием пола в таблице результатов
    3) выбранные в рандомном порядке несколько чекбоксов 'hobbies' и их совпадение с наименованиями хобби в таблице результатов
    4) выбранная рандомно дата, включая месяц, год и число из календаря
    5) выбранные в рандомном порядке несколько предметов subject (поле автокомплит)
    6) загрузку файла с пк пользователя
    7) выбор страны и одного из городов, соответствующих этой стране в рандомном порядке
    8) полное совпадение всех ожидаемых результатов и фактически полученных данных после заполнения формы
    """
    def test_practice_form(self, driver):
        practice_form = PracticeFormPage(driver, 'https://demoqa.com/automation-practice-form')
        practice_form.open()
        person = practice_form.fill_all_text_fields()    # запускаю функцию, заполняющую текстовые поля формы заранее сгенерированными данными  (включает first_name, last_name, email, mobile, current_addres)
        print('Ожидаемые текстовые поля: ', person)
        practice_form.choice_radiobutton('female')                                                      # запускаю функцию, которая выбирает конкретный радиобаттон (gender)
        """Запускаю функцию radio_is_checked, определяющую какой именно радио-баттон был фактически выбран и сколько осталось невыбранных. 
            Для успешной проверки 2 из 3х баттонов должны остаться невыбранными."""
        input_gender, n, text = practice_form.radio_is_checked()                                              # фактичеки выбранный радио-баттон и число непрокликанных для проверки
        print('Ожидаемый выбранный radio-button: ', text)
        new_date = practice_form.select_date()  # выбранная новая дата по календарю
        print('Ожидаемая выбранная новая дата:  ', new_date)
        checked_hobbies = practice_form.click_hobbies_checkbox()                                        # прокликанные в рандомном порядке чек-боксы
        print('Ожидаемые выбранные чек-боксы hobbies:  ', ', '.join(checked_hobbies))
        subjects = practice_form.multicomplite_of_subject()                                             # функция выбирает предметы (рандомно 1-4 из сгенерированного списка)
        result_subject = practice_form.check_subject()                                                  # фактичевки выбранные предметы
        print('Ожидаемые выбранные мультти-комплит из subjects:  ', ', '.join(result_subject))
        file_name = practice_form.upload_file()                                                                     # загружаемый файл, функция отправляет путь в инпут напрямую
        state = practice_form.change_state()                                                            # наименование выбранной страны в рандомном порядке
        time.sleep(2)
        city = practice_form.change_city(state)                                                                # наименование выбранного города в соотве свии с выбранной ранее страной
        print('Ожидаемые выбранные страна и соответсующий ей город:  ', state + ' ' + city)
        practice_form.click_submit()                                                                    # подтверждение выбора и заполнения всех полей формы
        time.sleep(3)
        result = practice_form.check_result()                                                           # результаты заполнения формы из таблицы результатов
        print('Фактически полученные результаты заполнения формы из таблицы результатов:  ', result)
        """Проверяем совпадаюют ли введенные в поля данные по персоне с фактически полученными из таблицы результатов после заполнения формы """
        assert set(person) & set(result) == set(person)
        """Проверяем дествительно ли выбран только один gender и совпадает ли выбранный пол с фактическим результатом из таблицы результатов заполнения формы"""
        assert n == 2
        assert text in result
        """Проверяю совпадают ли выбранные наименования hobbies с фактически полученными из таблицы результатов после заполнения формы"""
        assert ', '.join(checked_hobbies) in result
        """Проверяю совпадают ли выбранные наименования subjects с фактически полученными из таблицы результатов после заполнения формы"""
        assert ', '.join(result_subject) in result
        """Проверяю совпадают ли отправленный файл с фактически полученными из таблицы результатов после заполнения формы"""
        assert file_name in result
        """Проверяю совпадают ли выбранные страна и город с фактически полученными из таблицы результатов после заполнения формы"""
        assert state + ' ' + city in result



