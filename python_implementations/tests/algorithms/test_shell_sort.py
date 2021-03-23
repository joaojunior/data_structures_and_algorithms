import random

import pytest

from algorithms.sorting.shell_sort import ShellSort


@pytest.fixture
def shell_sort():
    return ShellSort()


def test_array_already_sorted_asc(shell_sort):
    items = [0, 1, 2, 3, 4]

    shell_sort.sort(items)
    assert list(range(5)) == items


def test_array_sorted_desc(shell_sort):
    items = [4, 3, 2, 1, 0]

    shell_sort.sort(items)
    assert list(range(5)) == items


def test_array_sorted_random(shell_sort):
    items = [0, 4, 2, 3, 1]
    random.shuffle(items)

    shell_sort.sort(items)
    assert list(range(5)) == items
