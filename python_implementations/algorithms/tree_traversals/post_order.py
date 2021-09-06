from ds.binary_search_tree import Node


def post_order(node: Node):
    result = []

    def _post_order(node: Node):
        if node is not None:
            _post_order(node.left)
            _post_order(node.right)
            result.append(node.key)
    _post_order(node)
    return result
