from ds.linked_list import LinkedListIterator


class Node:
    def __init__(self, item=0, previous=None, next_=None):
        self.item = item
        self.previous = previous
        self.next = next_


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def insert(self, item):
        node = Node(item)
        node.previous = self.tail
        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1
        return node

    def delete(self, node):
        if self.size == 0:
            raise ValueError('DoubleLinkedList is empty')
        if node.previous:
            node.previous.next = node.next
        if node.next:
            node.next.previous = node.previous
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.previous
        node.previous = None
        node.next = None
        self.size -= 1
        return node.item

    def __iter__(self):
        return LinkedListIterator(self.head)
