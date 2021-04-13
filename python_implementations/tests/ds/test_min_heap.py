import heapq
import random

from ds.min_heap import MinHeap


def test_ensure_create_min_heap_with_empty_array():
    items = []
    MinHeap.build_min_heap(items)

    assert [] == items


def test_create_min_heap_with_only_one_element():
    items = [1]
    MinHeap.build_min_heap(items)

    assert [1] == items


def test_create_min_heap_with_two_elements():
    items = [2, 1]
    MinHeap.build_min_heap(items)

    assert [1, 2] == items


def test_create_min_heap_with_n_elements_that_is_already_a_min_heap():
    n = 16
    items = list(range(n))
    MinHeap.build_min_heap(items)

    expected = list(range(n))
    assert expected == items


def test_create_min_heap_with_n_elements_that_is_not_a_min_heap():
    n = 16
    items = list(range(n))
    items.reverse()
    MinHeap.build_min_heap(items)

    expected = list(range(n))
    expected.reverse()
    heapq.heapify(expected)
    assert expected == items


def test_create_min_heap_from_an_random_array():
    n = 1000
    items = list(range(n))
    random.shuffle(items)
    expected = items[:]
    MinHeap.build_min_heap(items)
    assert expected != items

    heapq.heapify(expected)
    assert items == expected
