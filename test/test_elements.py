import random
import time
from page.base_page import BasePage
from page.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage


class TestElements:
    class TestTextBox:
        """Тест проверяет возможность и правильность заполнения тектстовых полей.
            Для этого:
            1) проверяется заполнение полей
            2) проверяется результаты вывода данных
            3) проверяется совпадают ли введенные и результатирующие данные отдельно для каждого поля"""
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, cur_addr, per_addr = text_box_page.fill_all_fields()
            output_full_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            assert full_name == output_full_name, 'не совпадают full_name, отправляемые драйверу, и результаты ввода в поле'
            assert email == output_email, 'не совпадают email, отправляемые драйверу, и результаты ввода в поле'
            assert cur_addr == output_cur_addr, 'не совпадают cur_addr, отправляемые драйверу, и результаты ввода в поле'
            assert per_addr == output_per_addr, 'не совпадают per_addr, отправляемые драйверу, и результаты ввода в поле'

            # time.sleep(2)
            # print(text_box_page.check_filled_form())

    # class TestCheckBox:
    #     def test_check_box(self, driver):
    #         check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
    #         check_box_page.open()
    #         check_box_page.open_full_list()   #это клик по кнопке справа, открывающей весь список чекбоксов
    #         check_box_page.click_random_checkbox()  #это перемещение к элементу и клик(для чекбокса)
    #         input_checkbox = check_box_page.get_checked_checkboxes()
    #         output_result = check_box_page.get_output_result()
    #         print(input_checkbox)
    #         print(output_result)
    #         assert input_checkbox == output_result

    class TestCheckBox:
        """Этот тест проверяет кликабельность чек-боксов. Для этого:
            1) проверяется возможность клика по отдельному чек-боксу или заданной группе
            2) проверяется соответствие полученного результата введенному названию чек-бокса
        """
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_checkbox = check_box_page.get_output_checkboxes()
            print(input_checkbox)
            print(output_checkbox)
            assert input_checkbox == output_checkbox, 'Не совпадаюют введенный и полученный чек-бокс'


    class TestRadioButton:
        """
        Эта группа тестов проверяет для каждого отдельного radio-button:
        1) возможность клика по radio-button,
        2) что при нажатии на один radio-button все остальные остаются "невыбранными" (1й и 2й assert) и
        3) что полученный результат нажатия radio-button соответствует ожидаемому (3й assert)
        """
        def test_radio_yes(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_radio_button('yes')
            input_yes, n = radio_button_page.radio_is_checked()
            print('Выбран radio-button: ', input_yes)
            print('Сколько radio-button остались невыбранными: ', n)
            output_yes = radio_button_page.get_output_result()
            assert input_yes == [True, False, False], 'Невозможно выбрать только "Yes"'
            assert n == 2, 'Невозможно выбрать "Yes" так, чтобы остальные 2 оставались невыбранными'
            assert output_yes == 'Yes', 'Невозможно выбрать Yes'

        def test_radio_impressive(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_radio_button('impressive')
            input_impressive, n = radio_button_page.radio_is_checked()
            print('Выбран radio-button: ', input_impressive)
            print('Сколько radio-button остались невыбранными: ', n)
            output_impressive = radio_button_page.get_output_result()
            assert input_impressive == [False, True, False], 'Невозможно выбрать только "Impressive"'
            assert n == 2, 'Невозможно выбрать "Impressive" так, чтобы остальные 2 оставались невыбранными'
            assert output_impressive == 'Impressive', 'Невозможно выбрать Impressive'

        def test_radio_no(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_on_radio_button('no')
            input_no, n = radio_button_page.radio_is_checked()
            print('Выбран radio-button: ', input_no)
            print('Сколько radio-button остались невыбранными: ', n)
            # output_no = radio_button_page.get_output_result()
            assert input_no == [False, False, False], 'Невозможно выбрать только "No"'
            assert n == 3, 'Невозможно выбрать "No" так, чтобы остальные 2 оставались невыбранными'
            # assert output_no == 'No', 'Невозможно выбрать No'


    """ Эта группа тестов в классе TestWebTable необходима для проверки работоспособности таблицы:
        1. Добавление нового человека 
        2. Редактирование данных о человеке
        3. Удаление данных о человеке
        4. Изменение количества строк в вэб таблице 
    """
    class TestWebTable:
        """ Тест test_add_in_web_table проверяет добавление нового человека в таблицу. Для этого:
        1) открываем страницу https://demoqa.com/webtables
        2) кликаем по кнопке добавить нового человека "ADD",
        3) заполняем все поля в выпадающем попапе,
        4) нажимаем кнопку "Submit" (Подтвердить)
        5) проверяем добавление ного человека и создаем переменную "результаты из таблицы" (список)
        6) для каждого нового человека проверяем вхожнение в список "результаты из таблицы"
        """
        def test_add_in_web_table(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            all_new_persons = web_table_page.add_new_person()       # добавление новых людей в таблице
            tabel_results = web_table_page.check_new_add_person()   # результаты добавления новых людей в таблицу
            print('Новые созданные люди', all_new_persons)
            print('Все люди из таблицы результатов', tabel_results)
            # for new_person in all_new_persons:                      # проверка есть ли новые люди в таблице (отдельно для каждого нового человека в цикле)
            assert all_new_persons in tabel_results, 'Нового человека нет в таблице'     # проверка только для 1 (есть ли новый человек в таблице)

        """ Тест test_search_by_web_table проверяет поиск человека в таблице по какому-либо критерию. Для этого:
        1) открываем страницу https://demoqa.com/webtables
        2) создаём нового человека (при создании человека получаю данные для сравнения с результами поиска)
        3) в поисковую строку вводим кулючевое слово для поиска (возьмем рандомно из списка данных созданного человека)
        4) проверяем появился ли в таблице результатов поисков искомый человек
        5) проверяем совпадают ли данные искомого человека и найденного поиском (по введённому в поисковую строку ключевому слову)
        """
        def test_search_by_web_table(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()                           # открываем страницу https://demoqa.com/webtables
            # создаём нового человека и выбранное в рандомном порядке (по индексу из списка данных созданного человека) ключевое слово ложу в переменную
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)             # в поисковую строку вводим кулючевое слово для поиска
            # проверяем появился ли в таблице результатов поисков искомый человек и ложу данные с ним в переменную (список)
            table_result_of_search = web_table_page.check_search_person()
            print('Ключевое слово для поиска: ', key_word)
            print('Результаты поиска человека по ключевому слову: ', table_result_of_search)
            # проверяю есть ли вхождение ключевого слова в результаты поиска в таблице (в виде списка)
            assert key_word in table_result_of_search, 'Среди результатов поиска нет результата, соответсвующего ключевому слову'

        """ Тест test_web_table_update_person проверяет возможность изменений данных по человеку в вэб таблице. Для этого:
        1) открываем страницу https://demoqa.com/webtables
        2) создаём нового человека (при создании человека получаю данные для сравнения с результами изменений)
        3) находим этого человека по ключевому слову (в этом тесте по lastname)
        4) нажимаем на кнопку "изменить"(карандаш)
        5) в появившемся попапе очищаем поле age, вводим новый возраст человека и подтверждаем книпкой update
        6) проверяем появился ли в таблице результатов поисков человек с обновленными данными (возрастом)
        7) проверяем совпадают ли изменённый возраст и возраст в строке результатов """
        def test_web_table_update_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()                        # открываем страницу https://demoqa.com/webtables
            lastname = web_table_page.add_new_person()[1]   # создаём нового человека и выбранное (по индексу из списка данных созданного человека) ключевое слово ложу в переменную
            web_table_page.search_some_person(lastname)  # в поисковую строку вводим кулючевое слово(lastname) для поиска определённого человека
            age = web_table_page.update_person_info()    # изменяем данные о выбранном человеке (здесь меняем возраст)
            row = web_table_page.check_search_person()   # проверяем появился ли в таблице результатов человек с изменёнными данными и ложу данные с ним в переменную (список)
            print('Новый сгенерированный возраст человека: ', age)
            print('Обновлённые данные о человеке', row)
            # проверяю есть ли вхождение возраста в результаты поиска в таблице (в виде списка)
            assert age in row, 'Данные о человеке не обновляются, новыц сегнерированный возраст не соответствует обновлённым данным о человеке'

        """ Тест test_web_table_delete_person проверяет удаление человека из вэб таблицы. Для этого:
        1) открываем страницу https://demoqa.com/webtables
        2) создаём нового человека (при создании человека получаю данные для поиска по таблице)
        3) находим этого человека по ключевому слову (в этом тесте по department)
        4) нажимаем на кнопку "удалить"(мусорка)
        5) проверяем исчез ли человек из таблицы результатов поиска и появилось ли сообщение об этом
        6) проверяем совпадает ли появляющееся сообщение с требуемым для этого случая "No rows found"(Строка не найдена) """
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()                            # открываем страницу https://demoqa.com/webtables
            department = web_table_page.add_new_person()[5]  # создаём нового человека и в переменную ложу выбранное ключевое слово   (по индексу из списка данных созданного человека)
            web_table_page.search_some_person(department)    # в поисковую строку вводим ключевое слово(department) для поиска определённого человека
            web_table_page.delete_person()                   # удаляем человека из таблицы (посредством клика на кнопку удалить)
            text = web_table_page.check_deleted()            # проверяем действительно ли удалён человек
            print('После удаления человека появляется текст:   ', text)
            print('Требуемый текст:   No rows found')
            # сравниваем появляющийся на экране текст после удаления человека с требуемым "No rows found"(Строка не найдена)
            assert text == 'No rows found', 'Появляющийся после удаления человека текст не соответсвует ожидаемому "No rows found"(Строка не найдена)'

        """ Тест test_web_table_update_count_rows проверяет возможность изменения выдаваемого количества строк 
        в вэб таблице. ДЛя этого:
         1) открываем страницу https://demoqa.com/webtables
         2) перемещаемся вниз таблицы до кнопки с селектором
         3) нажимаем на селектор
         4) в появившемся списке выбираем по порядку каждый вариант количества строк в таблице (5, 10, 20, 25, 50, 100)
         5) нажимаем на нужный вариант
         6) проверяем количество строк в таблице после выбора и соответствует ли оно требуемому набору         
        """
        """ СПОСОБ 1"""
        def test_web_table_update_count_rows(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()                            # открываем страницу https://demoqa.com/webtables
            count_rows = web_table_page.update_count_rows()        # запускаем функцию изменения количества строк в таблице (включает в себя все 1-6 шаги)
            # проверяем соответсвует ли полученный список количества строк в таблице ожидаемому набору
            assert count_rows == [5, 10, 20], 'Полученный список количества строк в таблице не соответствует ожидаемому'

        """ СПОСОБ 2"""
        def test_web_table_update_count(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()  # открываем страницу https://demoqa.com/webtables
            expecting_count_rows, actual_count_rows = web_table_page.update_count()  # запускаем функцию изменения количества строк в таблице (включает в себя все 1-6 шаги)
            print('Список ожидаемых количеств строк таблицы:  ', expecting_count_rows)
            print('Список реальных количеств строк таблицы:  ', actual_count_rows)
            # проверяем соответсвует ли полученный список количества строк в таблице ожидаемому набору
            assert expecting_count_rows == actual_count_rows, 'Полученный список количества строк в таблице не соответствует ожидаемому'


    """Эта группа тестов необходима для проверки выполнения различных видов кликов по кнопкам.
        Двойной клик. Контекстный клик (правой кнопкой). Простой клик.
    """
    class TestButtonPage:
        """ Тест test_different_clicks_on_buttons проверяет работоспособность кнопок. Для этого:
        1) открывает страницу https://demoqa.com/buttons
        2) проверяет возможность нажатия на кнопку
        3) проверяет появляется ли сообщение о подтверждениии успешности действия
        4) проверяет совпадают ли ожидаемое сообщение и получение в результате действий на странице
        """
        """ СПОСОБ 1 - один тест и 1 функция на все 3 кнопки """
        def test_different_clicks_on_buttons(self, driver):
            button_page = ButtonPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_buttons('double')
            right = button_page.click_on_different_buttons('right')
            click = button_page.click_on_different_buttons('click')
            print(double)
            print(right)
            print(click)
            assert double == 'You have done a double click', 'Двойной клик на кнопку не был совершён'
            assert right == 'You have done a right click', 'Клик правой кнопкой не был совершён'
            assert click == 'You have done a dynamic click', 'Обычный клик на кнопку не был совершён'

        """ СПОСОБ 2.1 - один тест - 1 конпка"""
        def test_click_on_double_button(self, driver):
            button_page = ButtonPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.double_click()
            print(double)
            assert double == 'You have done a double click', 'Двойной клик на кнопку не был совершён'

        """ СПОСОБ 2.2 - 3 функции (для каждой кнопки отдельно) в 1 тесте"""
        def test_different_clicks_on_buttons2(self, driver):
            button_page = ButtonPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.double_click()
            right = button_page.right_click()
            click = button_page.simple_click()
            print(double)
            print(right)
            print(click)
            assert double == 'You have done a double click', 'Двойной клик на кнопку не был совершён'
            assert right == 'You have done a right click', 'Клик правой кнопкой не был совершён'
            assert click == 'You have done a dynamic click', 'Обычный клик на кнопку не был совершён'


    """Группа позитивных и негативных тестов проверяет работоспособность ссылки, возможность перехода 
        и соответствие заданной. А также подтверждает невозможность открытия битой ссылки"""
    class TestLinksPage:
        """ Тест test_check_link проверяет работоспособность ссылки и возвращает запрашиваемую ссылку и
            ссылку, которая была реально открыта."""
        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            link_href, current_url = links_page.check_new_tab_simple_link()
            print('Запрашиваемая ссылка:  ', link_href)
            print('Ссылка, которая была реально открыта:  ', current_url)
            assert link_href == current_url, 'Открытая ссылка не соответствует запрашиваемой'

        """Негативный тест test_bad_link проверяет, что биитая ссылка НЕ открывается и 
            ожидает получить статус-код 400"""
        def test_bad_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            print('Статус код битой ссылки:  ', response_code)
            assert response_code == 400, 'Битая ссылка bad-request не может быть открыта'

    """Эта группа тестов проверяет возможность загрузки файла на сайт и 
        скачивания файла с сайта
    """
    class TestUploadDownloadPage:
        """Тест проверяет возможность загрузки сгенерированного файла на сайт."""
        def test_upload_file(self, driver):
            upload_and_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_and_download_page.open()
            file_name, result = upload_and_download_page.check_upload_file()
            print('Отправляемый файл:  ', file_name)
            print('Звгруженный файл:  ', result)
            assert file_name == result, 'Фактически загруженный файл не соответствует ожидаемому'

        """Тест проверяет возможность скачивания файла"""
        def test_download_file(self, driver):
            upload_and_download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_and_download_page.open()
            check = upload_and_download_page.check_download_file()
            assert check is True, 'Файл по заданному пути не был обнаружен'

    class TestDynamicProperties:
        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            dynamic_properties_page.check_enable_button()


















