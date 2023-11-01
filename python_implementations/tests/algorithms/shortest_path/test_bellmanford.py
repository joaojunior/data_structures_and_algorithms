import pytest

from algorithms.shortest_path.bellmanford import bellmanford
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
    for i in graph.nodes:
        parents, distances = bellmanford(i, graph)
        for j in graph.nodes:
            expected_distance = abs(j - i)
            expected_parent = i if i != j else None

            assert expected_distance == distances[j]
            assert expected_parent == parents[j]
