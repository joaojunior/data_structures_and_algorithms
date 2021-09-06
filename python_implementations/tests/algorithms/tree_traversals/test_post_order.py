import pytest

from algorithms.tree_traversals.post_order import post_order
from ds.binary_search_tree import BST


@pytest.fixture
def bst():
    _bst = BST()
    assert _bst.is_empty()
    return _bst


def test_post_order_sanity(bst):
    values = [3, 1, 5, 2, 4]
    expected = [2, 1, 4, 5, 3]
    for value in values:
        bst.insert(value)
    assert expected == post_order(bst.root)
