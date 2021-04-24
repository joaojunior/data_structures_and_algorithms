import random

import pytest

from ds.binary_search_tree import BST


@pytest.fixture
def bst():
    _bst = BST()
    assert _bst.is_empty()
    return _bst


def test_search_empty_tree_return_none(bst):
    assert bst.search(1) is None


def test_search_root_key(bst):
    key = 1
    node = bst.insert(key)

    assert node == bst.search(key)


def test_search_min_key(bst):
    size = 100
    min_key = 0
    sequence = list(range(size))
    random.shuffle(sequence)
    for key in sequence:
        node = bst.insert(key)
        if key == min_key:
            min_node = node
    assert min_node == bst.search(min_key)


def test_search_max_key(bst):
    size = 100
    max_key = size - 1
    sequence = list(range(size))
    random.shuffle(sequence)
    for key in sequence:
        node = bst.insert(key)
        if key == max_key:
            max_node = node
    assert max_node == bst.search(max_key)


def test_search_key_is_not_in_bst(bst):
    size = 100
    miss_key = size
    sequence = list(range(size))
    random.shuffle(sequence)
    for key in sequence:
        bst.insert(key)
    assert bst.search(miss_key) is None


def test_search_random_key_is_in_bst(bst):
    size = 100
    random_key = random.randint(0, size - 1)
    sequence = list(range(size))
    random.shuffle(sequence)
    for key in sequence:
        node = bst.insert(key)
        if key == random_key:
            _node = node
    assert _node == bst.search(random_key)


def test_insert_in_a_empty_bst(bst):
    key = 100
    assert [] == list(bst)
    node = bst.insert(key)

    assert bst.is_empty() is False
    assert key == node.key
    assert node.parent is None
    assert [key] == list(bst)


def test_insert_a_crescent_sequence_in_a_bst(bst):
    sequence = [100, 200, 300, 400, 500]
    for key in sequence:
        node = bst.insert(key)
        assert key == node.key
    assert sequence == list(bst)


def test_insert_a_decrescent_sequence_in_a_bst(bst):
    sequence = [500, 400, 300, 200, 100]
    for key in sequence:
        node = bst.insert(key)
        assert key == node.key
    assert sorted(sequence) == list(bst)


def test_insert_a_random_sequence_in_a_bst(bst):
    size = 100
    sequence = list(range(size))
    random.shuffle(sequence)
    for key in sequence:
        node = bst.insert(key)
        assert key == node.key
    assert sorted(sequence) == list(bst)


def test_delete_in_an_empty_bst(bst):
    assert bst.delete(1) is None


def test_delete_root_without_children(bst):
    key = 1
    bst.insert(key)
    bst.delete(key)
    assert bst.is_empty()


def test_delete_root_with_left_child(bst):
    root_key = 10
    left_key = 1
    bst.insert(root_key)
    node = bst.insert(left_key)
    bst.delete(root_key)
    assert bst.is_empty() is False
    assert node == bst.root


def test_delete_root_with_right_child(bst):
    root_key = 10
    right_key = 20
    bst.insert(root_key)
    node = bst.insert(right_key)
    bst.delete(root_key)
    assert bst.is_empty() is False
    assert node == bst.root


def test_delete_root_with_two_children(bst):
    root_key = 10
    left_key = 1
    right_key = 20
    bst.insert(root_key)
    bst.insert(left_key)
    node = bst.insert(right_key)
    bst.delete(root_key)
    assert bst.is_empty() is False
    assert node == bst.root
    assert [left_key, right_key] == list(bst)


def test_delete_non_root_without_children(bst):
    root_key = 100
    key = 10
    bst.insert(root_key)
    bst.insert(key)

    assert [key, root_key] == list(bst)
    bst.delete(key)
    assert [root_key] == list(bst)


def test_delete_non_root_with_left_child(bst):
    root_key = 100
    key = 10
    left_key = 1
    bst.insert(root_key)
    bst.insert(key)
    bst.insert(left_key)

    assert [left_key, key, root_key] == list(bst)
    bst.delete(key)
    assert [left_key, root_key] == list(bst)


def test_delete_non_root_with_right_child(bst):
    root_key = 100
    key = 10
    right_key = 15
    bst.insert(root_key)
    bst.insert(key)
    bst.insert(right_key)

    assert [key, right_key, root_key] == list(bst)
    bst.delete(key)
    assert [right_key, root_key] == list(bst)


def test_delete_non_root_with_two_children(bst):
    root_key = 100
    key = 10
    left_key = 5
    right_key = 15
    bst.insert(root_key)
    bst.insert(key)
    bst.insert(left_key)
    bst.insert(left_key - 1)
    bst.insert(left_key + 1)
    bst.insert(right_key)
    bst.insert(right_key - 1)
    bst.insert(right_key + 1)

    assert [
        left_key-1, left_key, left_key+1,
        key,
        right_key-1, right_key, right_key+1,
        root_key] == list(bst)
    bst.delete(key)
    assert [
        left_key-1, left_key, left_key+1,
        right_key-1, right_key, right_key+1,
        root_key] == list(bst)


def test_delete_all_keys_in_a_random_bst(bst):
    size = 1000
    sequence = list(range(size))
    random.shuffle(sequence)
    for key in sequence:
        bst.insert(key)
    assert sorted(sequence) == list(bst)

    random.shuffle(sequence)
    for key in sequence:
        bst.delete(key)
    assert [] == list(bst)
