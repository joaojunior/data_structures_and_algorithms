import pytest

from ds.linked_list import LinkedList


@pytest.fixture
def linked_list():
    return LinkedList()


def test_ensure_empty_list_when_create_an_instance(linked_list):
    assert linked_list.is_empty()
    assert [] == list(linked_list)


def test_insert_one_item_in_an_empty_linked_list(linked_list):
    linked_list.insert(1)
    assert [1] == list(linked_list)


def test_insert_n_items(linked_list):
    items_to_insert = [1, 2, 3, 4, 5]
    for item in items_to_insert:
        linked_list.insert(item)

    items_to_insert.reverse()
    assert items_to_insert == list(linked_list)


def test_remove_unique_item(linked_list):
    linked_list.insert(1)

    assert 1 == linked_list.delete(1)
    assert linked_list.is_empty()
    assert [] == list(linked_list)


def test_remove_all_items(linked_list):
    items_to_delete = [1, 2, 3, 4, 5]
    for item in items_to_delete:
        linked_list.insert(item)

    for item in items_to_delete:
        linked_list.delete(item)

    assert linked_list.is_empty()
    assert [] == list(linked_list)


def test_remove_last_item(linked_list):
    items_to_insert = [1, 2, 3, 4]
    item_to_delete = 5
    for item in items_to_insert:
        linked_list.insert(item)
    linked_list.insert(item_to_delete)

    assert item_to_delete == linked_list.delete(item_to_delete)
    items_to_insert.reverse()
    assert items_to_insert == list(linked_list)


def test_remove_first_item(linked_list):
    items = [1, 2, 3, 4, 5]
    for item in items:
        linked_list.insert(item)

    assert 1 == linked_list.delete(items.pop(0))
    items.reverse()
    assert items == list(linked_list)


def test_try_to_remove_in_empty_linked_list_raises_exception(linked_list):
    with pytest.raises(ValueError, match="Item 1 is not in the LinkedList"):
        linked_list.delete(1)


def test_try_to_remove_item_not_in_the_linked_list_raises_exception(
        linked_list):
    items = [1, 2, 3, 4, 5]
    for item in items:
        linked_list.insert(item)

    with pytest.raises(ValueError, match="Item 6 is not in the LinkedList"):
        linked_list.delete(6)
