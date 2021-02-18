import pytest

from ds.stack import Stack


@pytest.fixture()
def stack():
    return Stack()


def test_ensure_empty_stack_when_create_an_instance(stack):
    assert stack.is_empty()
    assert [] == list(stack)


def test_insert_one_item_in_an_empty_stack(stack):
    stack.push(1)
    assert [1] == list(stack)


def test_insert_n_items(stack):
    items_to_insert = [1, 2, 3, 4, 5]
    for item in items_to_insert:
        stack.push(item)

    items_to_insert.reverse()
    assert items_to_insert == list(stack)


def test_remove_unique_item(stack):
    stack.push(1)

    assert 1 == stack.pop()
    assert stack.is_empty()
    assert [] == list(stack)


def test_remove_all_items(stack):
    items_to_delete = [1, 2, 3, 4, 5]
    for item in items_to_delete:
        stack.push(item)

    items_to_delete.reverse()
    for item in items_to_delete:
        assert item == stack.pop()

    assert stack.is_empty()
    assert [] == list(stack)


def test_try_to_remove_in_empty_stack_raises_exception(stack):
    with pytest.raises(ValueError, match="Stack is empty"):
        stack.pop()
