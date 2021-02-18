from typing import Any

from ds.linked_list import LinkedList, LinkedListIterator


class Stack:
    def __init__(self) -> None:
        self.__linked_list = LinkedList()

    def is_empty(self) -> bool:
        return self.__linked_list.is_empty()

    def push(self, item: Any) -> None:
        self.__linked_list.insert(item)

    def pop(self) -> Any:
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self.__linked_list.delete(self.__linked_list.head.item)

    def __iter__(self) -> LinkedListIterator:
        return LinkedListIterator(self.__linked_list.head)
