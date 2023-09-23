from algorithms.searching.binary_search import (
    binary_search, binary_search_bigger_than, binary_search_less_than,
    binary_search_rotate_array_index_min)


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


class TestBinarySearchBiggerThan:
    def test_found_smallest_item_bigger_than_given_item(self):
        items = list(range(10))

        for idx in range(0, len(items) - 1):
            item = items[idx]
            assert idx == binary_search_bigger_than(item - 0.1, items)
            assert idx + 1 == binary_search_bigger_than(item, items)
            assert idx + 1 == binary_search_bigger_than(item + 0.1, items)

    def test_return_flag_when_given_element_is_max_or_bigger(self):
        items = list(range(10))
        item = max(items)
        flag = -1

        assert flag == binary_search_bigger_than(item, items)
        assert flag == binary_search_bigger_than(item + 0.1, items)


class TestBinarySearchRotateArrayIndexMin:
    def test_return_index_min_in_rotate_array(self):
        n = 10
        for i in range(n):
            items = list(range(n))
            items = items[i:] + items[:i]
            idx = items.index(min(items))
            assert idx == binary_search_rotate_array_index_min(items)

    def test_return_0_when_array_contains_only_one_element(self):
        items = [42]
        assert 0 == binary_search_rotate_array_index_min(items)

    def test_return_flag_when_array_is_empty(self):
        items = []
        flag = -1
        assert flag == binary_search_rotate_array_index_min(items)
