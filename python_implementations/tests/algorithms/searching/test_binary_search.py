from algorithms.searching.binary_search import (binary_search,
                                                binary_search_less_than)


class TestBinarySearch:
    def test_found_all_elements_in_sorted_array(self):
        items = list(range(10))

        for idx, item in enumerate(items):
            assert idx == binary_search(item, items)

    def test_return_flag_when_item_is_not_found(self):
        items = list(range(10))
        flag = - 1
        less_than_min = min(items) - 1
        bigger_than_max = max(items) + 1

        assert flag == binary_search(less_than_min, items)
        assert flag == binary_search(bigger_than_max, items)


class TestBinarySearchLessThan:
    def test_found_bigger_item_less_than_given_item(self):
        items = list(range(10))

        for idx in range(1, len(items)):
            item = items[idx]
            assert idx - 1 == binary_search_less_than(item - 0.1, items)
            assert idx - 1 == binary_search_less_than(item, items)
            assert idx == binary_search_less_than(item + 0.1, items)

    def test_return_flag_when_given_element_is_min_or_less(self):
        items = list(range(10))
        item = min(items)
        flag = -1

        assert flag == binary_search_less_than(item - 0.1, items)
        assert flag == binary_search_less_than(item, items)
