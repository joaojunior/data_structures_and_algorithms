MAX_DISTANCE = float('inf')


def bellmanford(source, graph):
    distances = {}
    parents = {}

    for node in graph.nodes:
        distances[node] = MAX_DISTANCE
        parents[node] = None
    distances[source] = 0

    for _ in range(graph.number_of_nodes - 1):
        for edge in graph.edges:
            cost = distances[edge.source] + edge.cost
            if cost < distances[edge.dest]:
                distances[edge.dest] = cost
                parents[edge.dest] = edge.source

    return parents, distances
