from typing import Any

from ds.linked_list import LinkedList, LinkedListIterator, Node


class LinkedListInsertInLast(LinkedList):
    def __init__(self):
        super().__init__()
        self.last = None

    def insert(self, item: Any) -> None:
        self._size += 1
        new_node = Node(item)
        if self.last is None:
            self.head = new_node
        else:
            self.last.next = new_node
        self.last = new_node

    def delete_first_element(self) -> Any:
        if self.head is not None:
            self._size -= 1
            item = self.head.item
            self.head = self.head.next
            if super().is_empty():
                self.last = None
            return item
        else:
            raise ValueError('Queue is empty')


class Queue:
    def __init__(self) -> None:
        self.__linked_list = LinkedListInsertInLast()

    def is_empty(self) -> bool:
        return self.__linked_list.is_empty()

    def enqueue(self, item: Any) -> None:
        self.__linked_list.insert(item)

    def dequeue(self) -> Any:
        return self.__linked_list.delete_first_element()

    def __iter__(self) -> LinkedListIterator:
        return LinkedListIterator(self.__linked_list.head)
