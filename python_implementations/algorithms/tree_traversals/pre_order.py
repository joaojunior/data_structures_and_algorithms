from ds.binary_search_tree import Node


def pre_order(node: Node):
    result = []

    def _pre_order(node: Node):
        if node is not None:
            result.append(node.key)
            _pre_order(node.left)
            _pre_order(node.right)
    _pre_order(node)
    return result
