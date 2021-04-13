import pytest

from ds.max_heap import MaxHeap


@pytest.fixture()
def max_heap():
    return MaxHeap


def test_ensure_create_max_heap_with_empty_array(max_heap):
    items = []
    max_heap.build_max_heap(items)

    assert [] == items


def test_create_max_heap_with_only_one_element(max_heap):
    items = [1]
    max_heap.build_max_heap(items)

    assert [1] == items


def test_create_max_heap_with_two_elements(max_heap):
    items = [1, 2]
    max_heap.build_max_heap(items)

    assert [2, 1] == items


def test_create_max_heap_with_n_elements_that_is_already_a_max_heap(max_heap):
    n = 16
    items = list(range(n))
    items.reverse()
    max_heap.build_max_heap(items)

    expected = list(range(n))
    expected.reverse()
    assert expected == items


def test_create_max_heap_with_n_elements_that_is_not_a_max_heap(max_heap):
    n = 16
    items = list(range(n))
    max_heap.build_max_heap(items)

    expected = [15, 10, 14, 8, 9, 12, 13, 7, 1, 0, 4, 11, 5, 2, 6, 3]
    assert expected == items
