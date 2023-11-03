import pytest

from algorithms.graph_traversals.bfs import bfs
from ds.graphs import Graph


@pytest.fixture
def graph():
    n = 10
    new_graph = Graph()

    for i in range(n):
        for j in range(i + 1, n):
            new_graph.insert_edge(i, j, j - i)
            new_graph.insert_edge(j, i, j - i)

    return new_graph


def test_bfs_returns_correct_order_visited_nodes(graph):
    nodes = list(graph.nodes)
    for node in nodes:
        expected = nodes[:]
        expected.remove(node)
        expected.insert(0, node)
        nodes_visted = bfs(node, graph)

        assert expected == nodes_visted
