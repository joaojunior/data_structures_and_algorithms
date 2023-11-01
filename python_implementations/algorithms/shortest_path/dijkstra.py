import heapq

MAX_DISTANCE = float('inf')


def dijkstra(src, graph):
    nodes_to_process = [(0, src)]
    parents, distances = {src: None}, {src: 0}

    for node in graph.nodes:
        if node != src:
            nodes_to_process.append((MAX_DISTANCE, node))
            distances[node] = MAX_DISTANCE

    while nodes_to_process:
        distance, node = heapq.heappop(nodes_to_process)
        for adjacent in graph.adjacents_of(node):
            cost = distances[node] + graph.cost(node, adjacent)
            if cost < distances[adjacent]:
                distances[adjacent] = cost
                parents[adjacent] = node
                heapq.heappush(nodes_to_process, (cost, adjacent))
    return parents, distances
