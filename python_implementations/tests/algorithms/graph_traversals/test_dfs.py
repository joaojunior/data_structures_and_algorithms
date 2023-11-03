import pytest

from algorithms.graph_traversals.dfs import dfs
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


def test_dfs_returns_correct_order_visited_nodes(graph):
    expected = list(graph.nodes)
    nodes_visted = dfs(graph)

    assert expected == nodes_visted
