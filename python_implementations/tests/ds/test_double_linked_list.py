import pytest

from ds.double_linked_list import DoubleLinkedList


@pytest.fixture
def double_linked_list():
    return DoubleLinkedList()


def test_ensure_empty_double_linked_list_when_create_one(double_linked_list):
    assert double_linked_list.is_empty()


def test_insert_one_item_in_an_empty_double_linked_list(double_linked_list):
    double_linked_list.insert(1)

    assert [1] == list(double_linked_list)


def test_insert_n_items(double_linked_list):
    items_to_insert = [1, 2, 3, 4, 5]
    for item in items_to_insert:
        double_linked_list.insert(item)

    assert items_to_insert == list(double_linked_list)


def test_remove_unique_item(double_linked_list):
    node1 = double_linked_list.insert(1)

    assert 1 == double_linked_list.delete(node1)
    assert double_linked_list.is_empty()
    assert [] == list(double_linked_list)


def test_remove_all_items(double_linked_list):
    items_to_delete = [1, 2, 3, 4, 5]
    nodes_to_delete = []
    for item in items_to_delete:
        nodes_to_delete.append(double_linked_list.insert(item))

    for node in nodes_to_delete:
        assert node.item == double_linked_list.delete(node)

    assert double_linked_list.is_empty()
    assert [] == list(double_linked_list)


def test_remove_tail(double_linked_list):
    items_to_insert = [1, 2, 3, 4]
    item_to_delete = 5
    for item in items_to_insert:
        double_linked_list.insert(item)
    node = double_linked_list.insert(item_to_delete)

    assert node.item == double_linked_list.delete(node)
    assert items_to_insert == list(double_linked_list)


def test_remove_head(double_linked_list):
    items = [2, 3, 4, 5]
    node = double_linked_list.insert(1)
    for item in items:
        double_linked_list.insert(item)
    assert node.item == double_linked_list.delete(node)
    assert items == list(double_linked_list)


def test_try_to_remove_in_empty_double_linked_list_raises_exception(
        double_linked_list):
    with pytest.raises(ValueError, match="DoubleLinkedList is empty"):
        double_linked_list.delete(1)
