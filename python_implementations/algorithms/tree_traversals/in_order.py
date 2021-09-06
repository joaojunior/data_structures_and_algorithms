from ds.binary_search_tree import Node


def in_order(node: Node):
    result = []

    def _in_order(node: Node):
        if node is not None:
            _in_order(node.left)
            result.append(node.key)
            _in_order(node.right)
    _in_order(node)
    return result
