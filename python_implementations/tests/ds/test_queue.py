import pytest

from ds.queue import Queue


@pytest.fixture()
def queue():
    return Queue()


def test_ensure_empty_queue_when_create_an_instance(queue):
    assert queue.is_empty()
    assert [] == list(queue)


def test_insert_one_item_in_an_empty_queue(queue):
    queue.enqueue(1)
    assert [1] == list(queue)


def test_insert_n_items(queue):
    items_to_insert = [1, 2, 3, 4, 5]
    for item in items_to_insert:
        queue.enqueue(item)

    assert items_to_insert == list(queue)


def test_remove_unique_item(queue):
    queue.enqueue(1)

    assert 1 == queue.dequeue()
    assert queue.is_empty()
    assert [] == list(queue)


def test_remove_all_items(queue):
    items_to_delete = [1, 2, 3, 4, 5]
    for item in items_to_delete:
        queue.enqueue(item)

    for item in items_to_delete:
        assert item == queue.dequeue()

    assert queue.is_empty()
    assert [] == list(queue)


def test_try_to_remove_in_empty_queue_raises_exception(queue):
    with pytest.raises(ValueError, match="Queue is empty"):
        queue.dequeue()
