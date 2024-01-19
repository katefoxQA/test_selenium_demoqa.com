import time

from page.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


class TestInteractions:
    class TestSortablePage:
        def test_sortable_page(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_sortable_items()
            grid_before, grid_after = sortable_page.change_sortable_grid()
            assert list_before != list_after
            assert grid_before != grid_after

    class TestSelectablePage:
        def test_selectable_page(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            active_element = selectable_page.select_list_item()
            active_grid_element = selectable_page.select_grid_item()
            assert len(active_element) > 0
            assert len(active_grid_element) > 0

    class TestResizablePage:
        def test_resizable_page(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_size_box, min_size_box = resizable_page.change_size_resizable_box()
            max_size, min_size = resizable_page.change_size_resizable()
            assert ('500px', '300px') == max_size_box
            assert ('150px', '150px') == min_size_box
            assert max_size != min_size

    class TestDroppablePage:
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == 'Dropped!'

        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            drop_text_not_accept, drop_text_accept = droppable_page.drop_acceptable()
            assert drop_text_not_accept == 'Drop here'
            assert drop_text_accept == 'Dropped!'

        def test_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text_not_greedly_box, text_not_greedly_inner_box, text_greedly_box, text_greedly_inner_box = droppable_page.prevent_propogation()
            assert text_not_greedly_box == 'Dropped!'
            assert text_not_greedly_inner_box == 'Dropped!'
            assert text_greedly_box == 'Outer droppable'
            assert text_greedly_inner_box == 'Dropped!'

        def test_revert_draggable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.drop_revert_draggable('will')
            not_will_after_move, not_will_after_revert = droppable_page.drop_revert_draggable('not_will')
            assert will_after_move != will_after_revert
            assert not_will_after_move == not_will_after_revert

    class TestDraggablePage:
        def test_draggable(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            before_position, after_position = draggable_page.simple_drag_box()
            assert before_position != after_position

        def test_axis_restricted(self, driver):
            draggable_page = DraggablePage(driver, 'https://demoqa.com/dragabble')
            draggable_page.open()
            top_x, left_x = draggable_page.axis_restricted_x()
            print(top_x)
            print(left_x)
            top_y, left_y = draggable_page.axis_restricted_y()
            print(top_y)
            print(left_y)
            assert top_x[0][0] == top_x[1][0] and int(top_x[1][0]) == 0
            assert left_x[0][0] != left_x[1][0] and int(left_x[1][0]) != 0
            assert top_y[0][0] != top_y[1][0] and int(top_y[1][0]) != 0
            assert left_y[0][0] == left_y[1][0] and int(left_y[1][0]) == 0












