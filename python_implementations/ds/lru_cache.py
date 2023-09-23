from ds.double_linked_list import DoubleLinkedList


class LRUCache:
    def __init__(self, max_size=3):
        self.max_size = max_size
        self._double_linked_list = DoubleLinkedList()
        self.lookup = {}
        self.size = 0

    def insert(self, key, value):
        if key in self.lookup:
            self._double_linked_list.delete(self.lookup[key])
            self.size -= 1
        if self.size == self.max_size:
            self._double_linked_list.delete(self._double_linked_list.head)
            self.size -= 1
        self.lookup[key] = self._double_linked_list.insert(value)
        self.size += 1

    def get(self, key):
        if key not in self.lookup:
            return
        node = self.lookup[key]
        self._double_linked_list.delete(node)
        self.size -= 1
        self.insert(key, node.item)
        return node.item
