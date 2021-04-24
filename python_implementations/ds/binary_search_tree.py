from typing import Optional


class Node:
    def __init__(self, key: int):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


class BSTInOrderIterator:
    def __init__(self, root: Optional[Node]):
        self.stack = []
        self.current = root

    def __next__(self) -> int:
        while True:
            if self.current is not None:
                self.stack.append(self.current)
                self.current = self.current.left
            elif self.stack:
                self.current = self.stack.pop()
                key = self.current.key
                self.current = self.current.right
                return key
            else:
                raise StopIteration


class BST:
    def __init__(self):
        self.root = None

    def is_empty(self) -> bool:
        return self.root is None

    def insert(self, key: int) -> Node:
        new_node = Node(key)
        p = self.root
        if p is None:
            self.root = new_node
        else:
            current = p
            while current:
                p = current
                if key < current.key:
                    current = current.left
                else:
                    current = current.right
            new_node.parent = p
            if key < p.key:
                p.left = new_node
            else:
                p.right = new_node

        return new_node

    def delete(self, key: int):
        node = self.search(key)
        if node:
            if node.left is None or node.right is None:
                child = node.left or node.right
                if child:
                    child.parent = node.parent
                if node.parent:
                    if node.parent.left == node:
                        node.parent.left = child
                    else:
                        node.parent.right = child
                else:
                    self.root = child
            else:
                sucessor = self.sucessor(node)
                if sucessor != node.right:
                    sucessor.parent.left = sucessor.right
                    if sucessor.right:
                        sucessor.right.parent = sucessor.parent
                    sucessor.right = node.right
                    node.right.parent = sucessor
                sucessor.left = node.left
                node.left.parent = sucessor
                sucessor.parent = node.parent
                if node.parent:
                    if node.parent.left == node:
                        node.parent.left = sucessor
                    else:
                        node.parent.right = sucessor
                else:
                    self.root = sucessor

    def sucessor(self, node: Node) -> Optional[Node]:
        _sucessor = None
        if node:
            current = node.right
            _sucessor = current
            while current:
                _sucessor = current
                current = current.left
        return _sucessor

    def search(self, key: int) -> Optional[Node]:
        current = self.root
        while current:
            if key == current.key:
                return current
            elif key < current.key:
                current = current.left
            else:
                current = current.right

    def __iter__(self) -> BSTInOrderIterator:
        return BSTInOrderIterator(self.root)
