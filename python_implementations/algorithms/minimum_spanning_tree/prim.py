import heapq

MAX_DISTANCE = float('inf')


def _create_distances_and_parents(root, graph):
    distances = {root: 0}
    parents = {root: None}

    for node in graph.nodes:
        if node != root:
            distances[node] = MAX_DISTANCE

    return distances, parents


def _create_mst_result(root, distances, parents):
    mst = set()
    distances.pop(root)
    for key, cost in distances.items():
        mst.add((parents[key], key, cost))
    return mst


def prim(graph):
    root = list(graph.nodes)[0]
    nodes_processed = set()
    nodes_to_process = [(0, root)]
    distances, parents = _create_distances_and_parents(root, graph)

    while nodes_to_process:
        node, _ = heapq.heappop(nodes_to_process)
        nodes_processed.add(node)

        for dest in graph.adjacents_of(node):
            cost = graph.cost(node, dest)
            if dest not in nodes_processed and cost < distances[dest]:
                distances[dest] = cost
                parents[dest] = node
                heapq.heappush(nodes_to_process, (cost, dest))

    return _create_mst_result(root, distances, parents)
