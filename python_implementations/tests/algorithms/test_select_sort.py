import random

import pytest

from algorithms.sorting.select_sort import SelectSort


@pytest.fixture
def select_sort():
    return SelectSort()


def test_array_already_sorted_asc(select_sort):
    items = [0, 1, 2, 3, 4]

    select_sort.sort(items)
    assert list(range(5)) == items


def test_array_sorted_desc(select_sort):
    items = [4, 3, 2, 1, 0]

    select_sort.sort(items)
    assert list(range(5)) == items


def test_array_sorted_random(select_sort):
    items = [0, 4, 2, 3, 1]
    random.shuffle(items)

    select_sort.sort(items)
    assert list(range(5)) == items
