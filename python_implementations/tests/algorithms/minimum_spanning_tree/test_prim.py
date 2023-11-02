import pytest

from algorithms.minimum_spanning_tree.prim import prim
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


def test_bellmanford_return_correct_shortest_path(graph):
    mst = prim(graph)

    expected = set()
    for i in range(graph.number_of_nodes - 1):
        expected.add((i, i + 1, 1))

    assert expected == mst
