from typing import Any


class Node:
    def __init__(self, item: Any) -> None:
        self.item = item
        self.next = None


class LinkedListIterator:
    def __init__(self, head: Node) -> None:
        self.__node = head

    def __next__(self) -> Any:
        if self.__node is not None:
            item = self.__node.item
            self.__node = self.__node.next

            return item
        else:
            raise StopIteration


class LinkedList:
    def __init__(self):
        self.__size = 0
        self.head = None

    def is_empty(self) -> bool:
        return self.__size == 0

    def insert(self, item: Any) -> None:
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.__size += 1

    def delete(self, item: Any) -> Any:
        previous = None
        current = self.head
        while current is not None and current.item != item:
            previous = current
            current = current.next

        if current is not None and current.item == item:
            self.__size -= 1
            if current == self.head:
                self.head = self.head.next
            else:
                previous.next = current.next
        else:
            raise ValueError(f'Item {item} is not in the LinkedList')
        return item

    def __iter__(self) -> LinkedListIterator:
        return LinkedListIterator(self.head)
