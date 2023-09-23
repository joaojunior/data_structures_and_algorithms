import pytest

from ds.lru_cache import LRUCache


@pytest.fixture
def lru_cache():
    return LRUCache(3)


def test_empty_lru_cache(lru_cache):
    assert [] == list(lru_cache._double_linked_list)


def test_insert_one_item(lru_cache):
    key = 1
    value = 10
    lru_cache.insert(key, value)

    assert [10] == list(lru_cache._double_linked_list)


def test_insert_max_items(lru_cache):
    items_to_insert = {}
    for i in range(1, lru_cache.max_size + 1):
        items_to_insert[i] = i * 10
    for key, value in items_to_insert.items():
        lru_cache.insert(key, value)

    assert list(items_to_insert.values()) == list(
        lru_cache._double_linked_list)


def test_insert_more_than_max_items_and_remove_lru(lru_cache):
    items_to_insert = {}
    for i in range(1, lru_cache.max_size + 2):
        items_to_insert[i] = i * 10
    for key, value in items_to_insert.items():
        lru_cache.insert(key, value)

    assert list(items_to_insert.values())[1:] == list(
        lru_cache._double_linked_list)


def test_get_key_update_lru(lru_cache):
    for key in range(1, lru_cache.max_size + 1):
        lru_cache = LRUCache()
        items_to_insert = {}
        for i in range(1, lru_cache.max_size + 1):
            items_to_insert[i] = i * 10
        for key, value in items_to_insert.items():
            lru_cache.insert(key, value)

        expected = list(items_to_insert.values())
        expected.remove(items_to_insert[key])
        expected.append(items_to_insert[key])
        lru_cache.get(key)

        assert expected == list(
            lru_cache._double_linked_list)


def test_get_key_not_in_lru_cache_is_no_op(lru_cache):
    items_to_insert = {}
    for i in range(1, lru_cache.max_size + 1):
        items_to_insert[i] = i * 10
    for key, value in items_to_insert.items():
        lru_cache.insert(key, value)

    assert lru_cache.get(max(items_to_insert.keys()) + 1) is None
    assert list(items_to_insert.values()) == list(
        lru_cache._double_linked_list)
