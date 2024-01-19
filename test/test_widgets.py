import time

from page.widgets_page import MenuPage, ToolTipsPage, AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, \
    ProgresBarPage, TabsPage


class TestWidgets:
    class TestAccordian:
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            title_first, content_first = accordian_page.check_accordian('first')
            title_second, content_second = accordian_page.check_accordian('second')
            title_third, content_third = accordian_page.check_accordian('third')
            assert title_first == 'What is Lorem Ipsum?' and content_first > 0
            assert title_second == 'Where does it come from?' and content_second > 0
            assert title_third == 'Why do we use it?' and content_third > 0

    class TestAutoCompletePage:
        def test_fill_multi_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            colors = auto_complete_page.fill_input_multi()
            colors_result = auto_complete_page.check_color_multi()
            assert colors ==colors_result

        def test_remove_multi_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            auto_complete_page.fill_input_multi()
            count_before, count_after = auto_complete_page.remove_value_from_multi()
            time.sleep(2)
            assert count_before != count_after

        def test_fill_single_complete(self, driver):
            auto_complete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete_page.open()
            color = auto_complete_page.fill_input_single()
            color_result = auto_complete_page.check_color_single()
            assert color == color_result

    class TestDatePickerPage:
        def test_date_picker_page(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            date_before, date_after = date_picker_page.select_date()
            assert date_before != date_after

        def test_date_and_time_picker(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            date_before, date_after = date_picker_page.select_date_and_time()
            assert date_before != date_after

    class TestSliderPage:
        def test_slider_page(selfself, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            value_before, value_after = slider_page.check_slider()
            assert value_before != value_after

        def test_progress_bar_page(selfself, driver):
            progress_bar_page = ProgresBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            value_after = progress_bar_page.check_progress_bar()
            assert '0%' != value_after

    class TestTabsPage:
        def test_tabs_page(self, driver):
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            what_tab, what_content, origin_tab, origin_content, use_tab, use_content = tabs_page.check_tabs()
            assert what_tab == 'What' and what_content > 100
            assert origin_tab == 'Origin' and origin_content > 100
            assert use_tab == 'Use' and use_content > 100



    class TestMenuPage:
        def test_menu_items(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu')
            menu_page.open()
            item_menu = menu_page.check_menu()
            # print(item_menu)
            assert item_menu == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3']

    class TestToolTipsPage:
        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            text = tool_tips_page.check()
            expected_text = ['You hovered over the Button', 'You hovered over the text field', 'You hovered over the Contrary', 'You hovered over the 1.10.32']
            assert text == expected_text
