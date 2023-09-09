from algorithms.searching.binary_search import binary_search


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
