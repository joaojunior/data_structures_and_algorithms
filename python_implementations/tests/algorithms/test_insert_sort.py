import random

import pytest

from algorithms.sorting.insert_sort import InsertSort


@pytest.fixture
def insert_sort():
    return InsertSort()


def test_array_already_sorted_asc(insert_sort):
    items = [0, 1, 2, 3, 4]

    insert_sort.sort(items)
    assert list(range(5)) == items


def test_array_sorted_desc(insert_sort):
    items = [4, 3, 2, 1, 0]

    insert_sort.sort(items)
    assert list(range(5)) == items


def test_array_sorted_random(insert_sort):
    items = [0, 4, 2, 3, 1]
    random.shuffle(items)

    insert_sort.sort(items)
    assert list(range(5)) == items
