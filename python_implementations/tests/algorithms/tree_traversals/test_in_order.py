import pytest

from algorithms.tree_traversals.in_order import in_order
from ds.binary_search_tree import BST


@pytest.fixture
def bst():
    _bst = BST()
    assert _bst.is_empty()
    return _bst


def test_in_order_sanity(bst):
    values = [1, 2, 3, 4, 5]
    for value in values:
        bst.insert(value)
    assert values == in_order(bst.root)
