from collections import deque

NOT_STARTED, STARTED, FINISHED = 0, 1, 2


def bfs(src, graph):
    order_nodes_visited = []
    status = {}
    for node in graph.nodes:
        status[node] = NOT_STARTED
    status[src] = STARTED

    nodes_to_process = deque([src])
    while nodes_to_process:
        node = nodes_to_process.popleft()
        order_nodes_visited.append(node)
        for adjacent in graph.adjacents_of(node):
            if status[adjacent] == NOT_STARTED:
                status[adjacent] = STARTED
                nodes_to_process.append(adjacent)
        status[node] = FINISHED
    return order_nodes_visited
