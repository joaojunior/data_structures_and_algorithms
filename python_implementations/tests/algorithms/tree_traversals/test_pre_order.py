import pytest

from algorithms.tree_traversals.pre_order import pre_order
from ds.binary_search_tree import BST


@pytest.fixture
def bst():
    _bst = BST()
    assert _bst.is_empty()
    return _bst


def test_pre_order_sanity(bst):
    values = [3, 1, 5, 2, 4]
    expected = [3, 1, 2, 5, 4]
    for value in values:
        bst.insert(value)
    assert expected == pre_order(bst.root)
